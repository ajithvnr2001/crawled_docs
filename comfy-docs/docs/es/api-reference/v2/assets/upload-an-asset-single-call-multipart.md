---
url: https://docs.comfy.org/es/api-reference/v2/assets/upload-an-asset-single-call-multipart/
title: Upload an asset (single-call multipart) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:28.694708+00:00
---

# Upload an asset (single-call multipart) - ComfyUI

> Source: https://docs.comfy.org/es/api-reference/v2/assets/upload-an-asset-single-call-multipart/

Upload an asset (single-call multipart)

cURL
    
    
    curl --request POST \
      --url http://127.0.0.1:8189/api/v2/assets \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: multipart/form-data' \
      --form file=@example-file \
      --form content_type=image/png \
      --form file_path=photo.png \
      --form expected_hash=blake3:9f8a1c0d... \
      --form 'tags=<string>' \
      --form expires_in=86400
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/assets"
    
    files = { "file": ("example-file", open("example-file", "rb")) }
    payload = {
        "content_type": "image/png",
        "file_path": "photo.png",
        "expected_hash": "blake3:9f8a1c0d...",
        "tags": "<string>",
        "expires_in": "86400"
    }
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.post(url, data=payload, files=files, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('file', '<string>');
    form.append('content_type', 'image/png');
    form.append('file_path', 'photo.png');
    form.append('expected_hash', 'blake3:9f8a1c0d...');
    form.append('tags', '<string>');
    form.append('expires_in', '86400');
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    options.body = form;
    
    fetch('http://127.0.0.1:8189/api/v2/assets', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/assets",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: multipart/form-data"
      ],
    ]);
    
    $response = curl_exec($curl);
    $err = curl_error($curl);
    
    curl_close($curl);
    
    if ($err) {
      echo "cURL Error #:" . $err;
    } else {
      echo $response;
    }
    
    
    package main
    
    import (
    	"fmt"
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "http://127.0.0.1:8189/api/v2/assets"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("http://127.0.0.1:8189/api/v2/assets")
      .header("Authorization", "Bearer <token>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/assets")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

201

401

403

409

422

429

500

503
    
    
    {
      "id": "9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b",
      "hash": "blake3:9f8a1c0d...",
      "size_bytes": 4816293,
      "content_type": "image/png",
      "created_at": "2023-11-07T05:31:56Z",
      "url": "<string>",
      "url_expires_at": "2023-11-07T05:31:56Z",
      "file_path": "photo.png",
      "created_new": true,
      "expires_at": "2023-11-07T05:31:56Z",
      "job_id": "<string>",
      "job_metadata": {
        "client": "acme"
      }
    }
    
    
    {
      "id": "9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b",
      "hash": "blake3:9f8a1c0d...",
      "size_bytes": 4816293,
      "content_type": "image/png",
      "created_at": "2023-11-07T05:31:56Z",
      "url": "<string>",
      "url_expires_at": "2023-11-07T05:31:56Z",
      "file_path": "photo.png",
      "created_new": true,
      "expires_at": "2023-11-07T05:31:56Z",
      "job_id": "<string>",
      "job_metadata": {
        "client": "acme"
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }

assets

# Upload an asset (single-call multipart)

Copiar páginaCopiar página

Single-call `multipart/form-data` upload. The platform streams the bytes through its trusted byte-path, dedups by the server-computed hash, and mints the asset record.

The blake3 hash is always computed server-side from the received bytes — a client-declared `expected_hash` is verified, never trusted. If location metadata (GPS, XMP, IPTC) is removed from an image before it is stored, the asset’s `hash` is the hash of the stored bytes and can differ from `expected_hash`. On Comfy Cloud, an upload whose bytes open as a JPEG, PNG, WebP or classic TIFF (including TIFF-based camera RAW such as DNG, NEF, ARW and CR2, but not BigTIFF) and that is over 50 MiB is refused with 422 `validation_error`, whatever its `content_type` and whether or not it carries location metadata. A request that declares a `Content-Length` over Comfy Cloud’s 200 MB (200,000,000-byte) body limit is refused before that check with a plain 413 that does not use the `ErrorEnvelope` shape. A body sent without a declared length is cut off when it passes that limit, and no 413 is sent: a cut-off while the fields before `file` are read fails with 422 `invalid_body`, and a cut-off inside the file usually fails with 500 `upstream_error`. Nothing after the `file` field is read, so a body that only passes the limit there is uploaded normally. Deployment-scoped surfaces neither strip location metadata nor apply the 50 MiB image cap; they limit the request body to 110 MB (110,000,000 bytes). A request that declares a `Content-Length` over that limit is refused with the same plain 413; a body sent without a declared length is cut off when it passes the limit, and the upload then fails with an error response that is not guaranteed to be a 413. The uploaded asset is referenceable immediately; any content scanning runs in the background and does not block the response.

An upload is a single request. v1 expects files of up to ~100 MB; the hard cap is the body limit of the surface it is sent to (above). Chunked/resumable large uploads are a deliberate open question.

On Comfy Cloud an upload fails with 422 `upload_timed_out` when no request bytes arrive for 30 seconds, or when the whole request takes longer than 10 minutes, however steadily bytes keep arriving. On Comfy Cloud an upload can also be refused with 503 `upload_busy` and `Retry-After` when the server is busy with other uploads: nothing was stored, so the same upload can be sent again after `Retry-After`. On a Developer Platform deployment the same 422 `upload_timed_out` applies when no request bytes arrive for 30 seconds, or when the whole request takes longer than 20 minutes.

Copiar páginaCopiar página

POST

http://127.0.0.1:8189https://cloud.comfy.orghttps://{deployment}.run.comfy.app

/

api

/

v2

/

assets

Pruébalo

Upload an asset (single-call multipart)

cURL
    
    
    curl --request POST \
      --url http://127.0.0.1:8189/api/v2/assets \
      --header 'Authorization: Bearer <token>' \
      --header 'Content-Type: multipart/form-data' \
      --form file=@example-file \
      --form content_type=image/png \
      --form file_path=photo.png \
      --form expected_hash=blake3:9f8a1c0d... \
      --form 'tags=<string>' \
      --form expires_in=86400
    
    
    import requests
    
    url = "http://127.0.0.1:8189/api/v2/assets"
    
    files = { "file": ("example-file", open("example-file", "rb")) }
    payload = {
        "content_type": "image/png",
        "file_path": "photo.png",
        "expected_hash": "blake3:9f8a1c0d...",
        "tags": "<string>",
        "expires_in": "86400"
    }
    headers = {"Authorization": "Bearer <token>"}
    
    response = requests.post(url, data=payload, files=files, headers=headers)
    
    print(response.text)
    
    
    const form = new FormData();
    form.append('file', '<string>');
    form.append('content_type', 'image/png');
    form.append('file_path', 'photo.png');
    form.append('expected_hash', 'blake3:9f8a1c0d...');
    form.append('tags', '<string>');
    form.append('expires_in', '86400');
    
    const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};
    
    options.body = form;
    
    fetch('http://127.0.0.1:8189/api/v2/assets', options)
      .then(res => res.json())
      .then(res => console.log(res))
      .catch(err => console.error(err));
    
    
    <?php
    
    $curl = curl_init();
    
    curl_setopt_array($curl, [
      CURLOPT_PORT => "8189",
      CURLOPT_URL => "http://127.0.0.1:8189/api/v2/assets",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--",
      CURLOPT_HTTPHEADER => [
        "Authorization: Bearer <token>",
        "Content-Type: multipart/form-data"
      ],
    ]);
    
    $response = curl_exec($curl);
    $err = curl_error($curl);
    
    curl_close($curl);
    
    if ($err) {
      echo "cURL Error #:" . $err;
    } else {
      echo $response;
    }
    
    
    package main
    
    import (
    	"fmt"
    	"strings"
    	"net/http"
    	"io"
    )
    
    func main() {
    
    	url := "http://127.0.0.1:8189/api/v2/assets"
    
    	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--")
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer <token>")
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }
    
    
    HttpResponse<String> response = Unirest.post("http://127.0.0.1:8189/api/v2/assets")
      .header("Authorization", "Bearer <token>")
      .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--")
      .asString();
    
    
    require 'uri'
    require 'net/http'
    
    url = URI("http://127.0.0.1:8189/api/v2/assets")
    
    http = Net::HTTP.new(url.host, url.port)
    
    request = Net::HTTP::Post.new(url)
    request["Authorization"] = 'Bearer <token>'
    request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"; filename=\"example-file\"\r\nContent-Type: application/octet-stream\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"content_type\"\r\n\r\nimage/png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file_path\"\r\n\r\nphoto.png\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expected_hash\"\r\n\r\nblake3:9f8a1c0d...\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tags\"\r\n\r\n<string>\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"expires_in\"\r\n\r\n86400\r\n-----011000010111000001101001--"
    
    response = http.request(request)
    puts response.read_body

200

201

401

403

409

422

429

500

503
    
    
    {
      "id": "9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b",
      "hash": "blake3:9f8a1c0d...",
      "size_bytes": 4816293,
      "content_type": "image/png",
      "created_at": "2023-11-07T05:31:56Z",
      "url": "<string>",
      "url_expires_at": "2023-11-07T05:31:56Z",
      "file_path": "photo.png",
      "created_new": true,
      "expires_at": "2023-11-07T05:31:56Z",
      "job_id": "<string>",
      "job_metadata": {
        "client": "acme"
      }
    }
    
    
    {
      "id": "9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b",
      "hash": "blake3:9f8a1c0d...",
      "size_bytes": 4816293,
      "content_type": "image/png",
      "created_at": "2023-11-07T05:31:56Z",
      "url": "<string>",
      "url_expires_at": "2023-11-07T05:31:56Z",
      "file_path": "photo.png",
      "created_new": true,
      "expires_at": "2023-11-07T05:31:56Z",
      "job_id": "<string>",
      "job_metadata": {
        "client": "acme"
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }
    
    
    {
      "error": {
        "code": "invalid_workflow",
        "message": "Node 12 (KSampler): required input 'model' is not connected",
        "organization_id": "org_01HXYZEXAMPLE",
        "details": {
          "node_errors": {
            "12": {
              "class_type": "SomeCustomNode",
              "errors": [
                {
                  "type": "unknown_node_class",
                  "message": "this deployment's build does not contain the node class SomeCustomNode."
                }
              ]
            }
          },
          "unknown_node_classes": [
            "SomeCustomNode"
          ]
        }
      }
    }

#### Autorizaciones

​

Authorization

string

header

requerido

`Authorization: Bearer <credential>`. The credential is one of: an account-scoped API key (`comfyui-…`), accepted on Cloud and serverless; a Comfy Cloud session JWT; or an OAuth access token issued for the Comfy Cloud resource. Which kinds a given deployment accepts is deployment configuration — an API key always works on Cloud and serverless, and a deployment that does not accept JWT bearers answers `401` with a message saying so. Self-hosted accepts unauthenticated requests by default and can be configured with a static bearer token.

#### Encabezados

​

Idempotency-Key

string

Client-generated UUID (recommended). Single-use: the first request to present a key is processed; any later request with the same key is rejected `422` `idempotency_key_reuse` (reject-on-duplicate, no response replay). Keys expire after 24h.

#### Cuerpo

multipart/form-data

​

file

file

requerido

The raw bytes.

​

content_type

string

requerido

Ejemplo:

`"image/png"`

​

file_path

string

requerido

Placement path / filename (global-namespace-root form, e.g. `photo.png` or `models/checkpoints/x.safetensors`). On Comfy Cloud the last segment becomes the asset name, so it must be valid UTF-8, at most 255 bytes, must not start with `.`, and must not contain control characters (C0, DEL, C1, U+2028, U+2029) or invisible format and default-ignorable characters (Unicode general category Cf, which includes the bidi embedding, override and isolate controls, soft hyphen, zero-width space, word joiner, BOM and tag characters, plus the other default-ignorable code points such as U+034F, U+2065 and the Hangul fillers); otherwise the request is refused with 422 `invalid_body` before anything is stored. ZWNJ/ZWJ (U+200C, U+200D) and the direction marks U+200E, U+200F and U+061C are allowed, for right-to-left and emoji names, and so are the visible Arabic number signs (prepended concatenation marks such as U+0600) and variation selectors; the direction marks can still change how a name is displayed.

Ejemplo:

`"photo.png"`

​

expected_hash

string

Optional client-computed blake3 (`blake3:<hex>`) of the bytes sent. Verified against the server-computed blake3 of the received bytes, not of the stored bytes; mismatch is rejected with 409 `hash_mismatch`. On serverless deployments no asset is minted and no existing asset's retention is changed; elsewhere the upload is stored before the check, so the 409 returns no asset and a retry with the corrected expectation dedups onto it.

Ejemplo:

`"blake3:9f8a1c0d..."`

​

tags

string[]

Category tags (e.g. `input`). A create carries at most 64 tags, each a non-empty UTF-8 string of at most 256 bytes (surrounding whitespace included) with no NUL byte. A deployment adds `input` to every asset and counts it, so it takes at most 63 of the caller's own; the `model_type:` tags derived for a model asset are not counted. A tag set breaking a limit is refused with 422. Cloud's hosted API also caps this encoded JSON field at 8 KiB, so a long tag set can be refused (422 `invalid_body`) below these limits. Invalid UTF-8 or a lone surrogate escape (e.g. `\ud800`) inside a JSON-encoded tag is not refused: JSON decoding replaces it with U+FFFD (3 bytes each), and the 256-byte limit applies to the replaced value.

​

expires_in

integer

Optional retention override in seconds (60s–7d): the asset's `expires_at` becomes now + `expires_in`, replacing the platform's default retention. Implementations without configurable retention ignore it. The bounds apply to this override only — the platform default is operator-configured and may lie outside them.

Rango requerido: `60 <= x <= 604800`

Ejemplo:

`86400`

#### Respuesta

200

application/json

Bytes deduped to an existing blob; asset minted over it.

A user-owned record identified by a server-assigned UUID, backing an immutable blob whose content carries a server-computed blake3 hash. `hash` may be computed lazily: an asset record (and its retrievable bytes) can exist before its hash is filled in. On an output, `job_metadata` carries the labels its producing job was submitted with, so code holding only the asset knows which run it came from. It is absent for assets no job produced, for outputs of a job sent without labels, where the serving surface keeps no job labels, and when the labels could not be read: so `job_id` without `job_metadata` does not prove the job had no labels. A create whose file path and bytes match an existing output answers with that output, so its `job_id` and `job_metadata` are the output's.

​

id

string

requerido

Ejemplo:

`"9f8a1c0d-2b3e-4f56-8a7b-1c2d3e4f5a6b"`

​

hash

string | null

requerido

`blake3:<hex>`; null while lazily computed.

Ejemplo:

`"blake3:9f8a1c0d..."`

​

size_bytes

integer<int64>

requerido

Ejemplo:

`4816293`

​

content_type

string

requerido

Ejemplo:

`"image/png"`

​

created_at

string<date-time>

requerido

​

url

string<uri>

requerido

Short-lived content URL (signed, or proxy-served).

​

url_expires_at

string<date-time>

requerido

​

file_path

string | null

Ejemplo:

`"photo.png"`

​

created_new

boolean

On create responses: distinguishes a brand-new blob (true) from a dedup hit against bytes the platform already had (false).

​

expires_at

string<date-time> | null

Retention deadline for the asset itself (distinct from `url_expires_at`, the signed URL's validity). Null or absent means the asset is non-expiring. On a dedup-hit create response the deadline may be later than now + the requested/default retention: re-referencing content extends its retention, never shortens it.

​

job_id

string | null

ID of the job that produced this asset. Absent for assets no job produced, such as a fresh upload.

​

job_metadata

object

The labels the producing job was submitted with, read through `job_id` on each read. Absent for assets no job produced, for outputs of a job sent without labels, where the serving surface keeps no job labels, when the job is gone, and when the labels could not be read: so `job_id` without `job_metadata` does not prove the job had no labels.

Show child attributes

Ejemplo:
    
    
    { "client": "acme" }

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/api-reference/v2/assets/upload-an-asset-single-call-multipart.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/api-reference/v2/assets/upload-an-asset-single-call-multipart)

[Notas de diseño](https://docs.comfy.org/es/development/api-development/sdks-design)[Mint an asset over existing bytes (dedup fast-path)](https://docs.comfy.org/es/api-reference/v2/assets/mint-an-asset-over-existing-bytes-dedup-fast-path)
