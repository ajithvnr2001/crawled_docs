---
url: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/save-svg/
title: Save SVG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:38.396754+00:00
---

# Save SVG - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/save-svg/

## On this page

Back to top

  * Node Function
  * Parameters
    * Basic Parameters
    * Output
  * Usage Example
  * Source Code



Recraft

# Save SVG - ComfyUI Built-in Node Documentation

Copy pageCopy page

A utility node for saving SVG vector graphics to files

Copy pageCopy page

![ComfyUI Built-in Save SVG Node](https://mintcdn.com/dripart/5003JSxULDwNImme/images/built-in-nodes/api_nodes/recraft/save-svg.jpg?fit=max&auto=format&n=5003JSxULDwNImme&q=85&s=f9f08f55c06ee2d300d66cd2e82194f0) The Save SVG node allows you to save SVG data from Recraft vector generation nodes as usable files in the filesystem. This is an essential component for handling and exporting vector graphics.

## Node Function

This node receives SVG vector data and saves it as standard SVG files in the filesystem. It supports automatic file naming and save path specification, allowing vector graphics to be opened and edited in other software.

## Parameters

### Basic Parameters

Parameter| Type| Default| Description  
---|---|---|---  
svg| SVG| -| SVG vector data to save  
filename_prefix| string| ”recraft”| Prefix for the filename  
output_dir| string| -| Output directory, defaults to ComfyUI output folder at `ComfyUI/output/svg/`  
index| integer| -1| Save index, -1 means save all generated SVGs  
  
### Output

Output| Type| Description  
---|---|---  
SVG| SVG| Passes through the input SVG data  
  
## Usage Example

## Recraft Text to Image Workflow Example

Recraft Text to Image Workflow Example

## Source Code

[Node Source Code (Updated 2025-05-03)]
    
    
    class SaveSVGNode:
        """
        Save SVG files on disk.
        """
    
        def __init__(self):
            self.output_dir = folder_paths.get_output_directory()
            self.type = "output"
            self.prefix_append = ""
    
        RETURN_TYPES = ()
        DESCRIPTION = cleandoc(__doc__ or "")  # Handle potential None value
        FUNCTION = "save_svg"
        CATEGORY = "api node/image/Recraft"
        OUTPUT_NODE = True
    
        @classmethod
        def INPUT_TYPES(s):
            return {
                "required": {
                    "svg": (RecraftIO.SVG,),
                    "filename_prefix": ("STRING", {"default": "svg/ComfyUI", "tooltip": "The prefix for the file to save. This may include formatting information such as %date:yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes."})
                },
                "hidden": {
                    "prompt": "PROMPT",
                    "extra_pnginfo": "EXTRA_PNGINFO"
                }
            }
    
        def save_svg(self, svg: SVG, filename_prefix="svg/ComfyUI", prompt=None, extra_pnginfo=None):
            filename_prefix += self.prefix_append
            full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, self.output_dir)
            results = list()
    
            # Prepare metadata JSON
            metadata_dict = {}
            if prompt is not None:
                metadata_dict["prompt"] = prompt
            if extra_pnginfo is not None:
                metadata_dict.update(extra_pnginfo)
    
            # Convert metadata to JSON string
            metadata_json = json.dumps(metadata_dict, indent=2) if metadata_dict else None
    
            for batch_number, svg_bytes in enumerate(svg.data):
                filename_with_batch_num = filename.replace("%batch_num%", str(batch_number))
                file = f"{filename_with_batch_num}_{counter:05}_.svg"
    
                # Read SVG content
                svg_bytes.seek(0)
                svg_content = svg_bytes.read().decode('utf-8')
    
                # Inject metadata if available
                if metadata_json:
                    # Create metadata element with CDATA section
                    metadata_element = f"""  <metadata>
        <![CDATA[
    {metadata_json}
        ]]>
      </metadata>
    """
                    # Insert metadata after opening svg tag using regex
                    import re
                    svg_content = re.sub(r'(<svg[^>]*>)', r'\1\n' + metadata_element, svg_content)
    
                # Write the modified SVG to file
                with open(os.path.join(full_output_folder, file), 'wb') as svg_file:
                    svg_file.write(svg_content.encode('utf-8'))
    
                results.append({
                    "filename": file,
                    "subfolder": subfolder,
                    "type": self.type
                })
                counter += 1
            return { "ui": { "images": results } }
    
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/partner-node/image/recraft/save-svg.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/partner-node/image/recraft/save-svg)

[Recraft Vectorize Image](https://docs.comfy.org/built-in-nodes/partner-node/image/recraft/recraft-vectorize-image)[Google Veo2 Video](https://docs.comfy.org/built-in-nodes/partner-node/video/google/google-veo2-video)
