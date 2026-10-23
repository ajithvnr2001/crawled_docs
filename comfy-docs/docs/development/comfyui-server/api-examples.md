---
url: https://docs.comfy.org/development/comfyui-server/api-examples/
title: API Examples - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:54.635615+00:00
---

# API Examples - ComfyUI

> Source: https://docs.comfy.org/development/comfyui-server/api-examples/

## On this page

  * Method 1: Submit and Forget (HTTP only)
  * Method 2: WebSocket + History (Monitor Completion)
  * Method 3: WebSocket with SaveImageWebsocket (Real-time Images)
  * Which Method Should I Use?



Self-Hosted Server API

# API Examples

Copy pageCopy page

Three common patterns for calling the ComfyUI Server API

Copy pageCopy page

This page demonstrates three ways to interact with the ComfyUI Server API, from a simple HTTP submission to a full WebSocket integration with real-time image output. All examples use the [default SD1.5 workflow](https://github.com/Comfy-Org/ComfyUI/blob/master/script_examples) for illustration. Before using the API, you need to export your workflow in [API format](https://docs.comfy.org/development/api-development/workflow-api-format).

These examples use Python with the standard library and the `websocket-client` package (`pip install websocket-client`). The underlying API protocol is the same regardless of language. See the [Cloud API Reference](https://docs.comfy.org/development/cloud/api-reference) for TypeScript and curl equivalents.

* * *

## 

​

Method 1: Submit and Forget (HTTP only)

Source: [`basic_api_example.py`](https://github.com/Comfy-Org/ComfyUI/blob/master/script_examples/basic_api_example.py) The simplest approach: submit a workflow and don’t wait for results. Useful for fire-and-forget jobs where you check outputs later.
    
    
    """basic_api_example.py — Submit a workflow via HTTP only."""
    
    import json
    from urllib import request
    
    SERVER_ADDRESS = "127.0.0.1:8188"
    
    
    def queue_prompt(prompt):
        p = {"prompt": prompt}
        data = json.dumps(p).encode("utf-8")
        req = request.Request(
            f"http://{SERVER_ADDRESS}/prompt", data=data
        )
        request.urlopen(req)
    
    
    if __name__ == "__main__":
        # Load a workflow exported in API format
        prompt_text = """{
            "3": {
                "class_type": "KSampler",
                "inputs": {
                    "cfg": 8, "denoise": 1,
                    "latent_image": ["5", 0],
                    "model": ["4", 0],
                    "negative": ["7", 0],
                    "positive": ["6", 0],
                    "sampler_name": "euler",
                    "scheduler": "normal",
                    "seed": 8566257, "steps": 20
                }
            },
            "4": {
                "class_type": "CheckpointLoaderSimple",
                "inputs": {"ckpt_name": "v1-5-pruned-emaonly.safetensors"}
            },
            "5": {
                "class_type": "EmptyLatentImage",
                "inputs": {"batch_size": 1, "height": 512, "width": 512}
            },
            "6": {
                "class_type": "CLIPTextEncode",
                "inputs": {"clip": ["4", 1], "text": "masterpiece best quality man"}
            },
            "7": {
                "class_type": "CLIPTextEncode",
                "inputs": {"clip": ["4", 1], "text": "bad hands"}
            },
            "8": {
                "class_type": "VAEDecode",
                "inputs": {"samples": ["3", 0], "vae": ["4", 2]}
            },
            "9": {
                "class_type": "SaveImage",
                "inputs": {"filename_prefix": "ComfyUI", "images": ["8", 0]}
            }
        }"""
    
        prompt = json.loads(prompt_text)
        # Modify inputs before submitting
        prompt["3"]["inputs"]["seed"] = 5
        prompt["6"]["inputs"]["text"] = "masterpiece best quality man"
    
        queue_prompt(prompt)
        print("Prompt submitted successfully.")
    

This method uses the `SaveImage` node, which saves images to disk on the server. To retrieve them, you’d need to follow up with a call to `GET /view?filename=...`.

* * *

## 

​

Method 2: WebSocket + History (Monitor Completion)

Source: [`websockets_api_example.py`](https://github.com/Comfy-Org/ComfyUI/blob/master/script_examples/websockets_api_example.py) Use WebSocket to wait for execution to finish, then retrieve outputs via the `/history` endpoint. This is the recommended pattern for most use cases.
    
    
    """websockets_api_example.py — Monitor execution via WebSocket, download via /history."""
    
    import websocket  # pip install websocket-client
    import uuid
    import json
    import urllib.request
    import urllib.parse
    
    SERVER_ADDRESS = "127.0.0.1:8188"
    client_id = str(uuid.uuid4())
    
    
    def queue_prompt(prompt, prompt_id):
        p = {"prompt": prompt, "client_id": client_id, "prompt_id": prompt_id}
        data = json.dumps(p).encode("utf-8")
        req = urllib.request.Request(
            f"http://{SERVER_ADDRESS}/prompt", data=data
        )
        urllib.request.urlopen(req)
    
    
    def get_image(filename, subfolder, folder_type):
        params = urllib.parse.urlencode({
            "filename": filename,
            "subfolder": subfolder,
            "type": folder_type,
        })
        with urllib.request.urlopen(
            f"http://{SERVER_ADDRESS}/view?{params}"
        ) as response:
            return response.read()
    
    
    def get_history(prompt_id):
        with urllib.request.urlopen(
            f"http://{SERVER_ADDRESS}/history/{prompt_id}"
        ) as response:
            return json.loads(response.read())
    
    
    def get_images(ws, prompt):
        prompt_id = str(uuid.uuid4())
        queue_prompt(prompt, prompt_id)
    
        while True:
            out = ws.recv()
            if isinstance(out, str):
                message = json.loads(out)
                if message["type"] == "executing":
                    data = message["data"]
                    if data["node"] is None and data["prompt_id"] == prompt_id:
                        break  # Execution done
            # Binary frames are preview images — skip them here
            continue
    
        history = get_history(prompt_id)[prompt_id]
        output_images = {}
        for node_id in history["outputs"]:
            node_output = history["outputs"][node_id]
            images_output = []
            if "images" in node_output:
                for image in node_output["images"]:
                    image_data = get_image(
                        image["filename"], image["subfolder"], image["type"]
                    )
                    images_output.append(image_data)
            output_images[node_id] = images_output
        return output_images
    
    
    if __name__ == "__main__":
        prompt_text = """{
            "3": { ... }, "4": { ... }, "5": { ... },
            "6": { ... }, "7": { ... }, "8": { ... },
            "9": { "class_type": "SaveImage", "inputs": { ... } }
        }"""
        prompt = json.loads(prompt_text)
        prompt["3"]["inputs"]["seed"] = 5
        prompt["6"]["inputs"]["text"] = "masterpiece best quality man"
    
        ws = websocket.WebSocket()
        ws.connect(f"ws://{SERVER_ADDRESS}/ws?clientId={client_id}")
        images = get_images(ws, prompt)
        ws.close()
    
        print(f"Got {len(images)} output node(s) with images.")
    
        # Display the images (requires Pillow):
        # for node_id in images:
        #     for image_data in images[node_id]:
        #         from PIL import Image
        #         import io
        #         img = Image.open(io.BytesIO(image_data))
        #         img.show()
    

The WebSocket binary frames contain in-progress preview images during generation. You can decode them for live previews (see the [Server Messages](https://docs.comfy.org/development/comfyui-server/comms_messages) page for the binary format).

* * *

## 

​

Method 3: WebSocket with SaveImageWebsocket (Real-time Images)

Source: [`websockets_api_example_ws_images.py`](https://github.com/Comfy-Org/ComfyUI/blob/master/script_examples/websockets_api_example_ws_images.py) For scenarios where you don’t want images saved to disk, use the `SaveImageWebsocket` node. Images are delivered directly via WebSocket binary frames.
    
    
    """websockets_api_example_ws_images.py — Receive images directly via WebSocket."""
    
    import websocket  # pip install websocket-client
    import uuid
    import json
    import urllib.request
    import urllib.parse
    
    SERVER_ADDRESS = "127.0.0.1:8188"
    client_id = str(uuid.uuid4())
    
    
    def queue_prompt(prompt):
        p = {"prompt": prompt, "client_id": client_id}
        data = json.dumps(p).encode("utf-8")
        req = urllib.request.Request(
            f"http://{SERVER_ADDRESS}/prompt", data=data
        )
        return json.loads(urllib.request.urlopen(req).read())
    
    
    def get_images(ws, prompt):
        prompt_id = queue_prompt(prompt)["prompt_id"]
        output_images = {}
        current_node = ""
    
        while True:
            out = ws.recv()
            if isinstance(out, str):
                message = json.loads(out)
                if message["type"] == "executing":
                    data = message["data"]
                    if data["prompt_id"] == prompt_id:
                        if data["node"] is None:
                            break  # Execution done
                        current_node = data["node"]
            else:
                # Binary frame — image data from SaveImageWebsocket
                if current_node == "save_image_websocket_node":
                    images_output = output_images.get(current_node, [])
                    # The first 8 bytes are type/meta, rest is image data
                    images_output.append(out[8:])
                    output_images[current_node] = images_output
    
        return output_images
    
    
    if __name__ == "__main__":
        prompt_text = """{
            "3": { "class_type": "KSampler", "inputs": { ... } },
            ...
            "save_image_websocket_node": {
                "class_type": "SaveImageWebsocket",
                "inputs": {"images": ["8", 0]}
            }
        }"""
        prompt = json.loads(prompt_text)
        prompt["3"]["inputs"]["seed"] = 5
    
        ws = websocket.WebSocket()
        ws.connect(f"ws://{SERVER_ADDRESS}/ws?clientId={client_id}")
        images = get_images(ws, prompt)
        ws.close()
    
        print(f"Received {len(images)} image(s) via WebSocket.")
    
        # Display (requires Pillow):
        # for image_data in images.get("save_image_websocket_node", []):
        #     from PIL import Image
        #     import io
        #     img = Image.open(io.BytesIO(image_data))
        #     img.show()
    

The workflow must use a node with `class_type: "SaveImageWebsocket"` (a built-in node) instead of the regular `SaveImage` node.

* * *

## 

​

Which Method Should I Use?

## Method 1: HTTP Only

**Fire and forget.** Use when you don’t need immediate output, or when retrieving results later is acceptable.

## Method 2: WebSocket + History

**Recommended.** Wait for completion, then download outputs. Best balance of simplicity and reliability.

## Method 3: SaveImageWebsocket

**Real-time images.** Best for interactive apps where you want images delivered without disk writes.

For the full API reference (endpoints, payload formats, error handling), see the [Server Routes](https://docs.comfy.org/development/comfyui-server/comms_routes) and [Server Messages](https://docs.comfy.org/development/comfyui-server/comms_messages) pages.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/comfyui-server/api-examples.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/comfyui-server/api-examples)

[Server OverviewPrevious](https://docs.comfy.org/development/comfyui-server/comms_overview)[ComfyUI Server Routes (HTTP and WebSocket API)Next](https://docs.comfy.org/development/comfyui-server/comms_routes)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)
