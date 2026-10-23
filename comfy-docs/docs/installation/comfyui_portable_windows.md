---
url: https://docs.comfy.org/installation/comfyui_portable_windows/
title: ComfyUI Portable for Windows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:56.809981+00:00
---

# ComfyUI Portable for Windows - ComfyUI

> Source: https://docs.comfy.org/installation/comfyui_portable_windows/

## On this page

  * Download ComfyUI Portable
  * Adding Extra Model Paths
    * Open Config File
    * Example Structure
    * Add Extra Custom Nodes Path
  * First Image Generation
  * Additional ComfyUI Portable Instructions
    * 1\. Upgrading ComfyUI Portable
    * 2\. Setting Up LAN Access for ComfyUI Portable
    * 3\. Installing Additional Python Packages



Local (Self-Hosted)

# ComfyUI Portable for Windows

Copy pageCopy page

Download and run ComfyUI Portable on Windows: a standalone package with embedded Python and CUDA builds for NVIDIA GPUs. Extract the archive, then run ComfyUI.

Copy pageCopy page

**ComfyUI Portable** is a standalone packaged complete ComfyUI Windows version that has integrated an independent **Python (python_embeded)** required for ComfyUI to run. You only need to extract it to use it. This guide section will walk you through installing ComfyUI Portable.

## 

​

Download ComfyUI Portable

Choose the download package that matches your GPU type. ComfyUI Portable provides separate packages for different GPU hardware.

  * Nvidia GPU

  * AMD GPU

  * Intel GPU




### 

​

Standard portable for Nvidia GPUs

## Nvidia GPU (CUDA 13.0, Python 3.13)

For modern Nvidia GPUs (RTX series)

## Nvidia GPU (CUDA 12.6, Python 3.12)

For Nvidia 10 series and older GPUs

## Nvidia GPU on Windows ARM64 (Python 3.14)

For Windows on ARM devices with an Nvidia GPU

Download the file and extract it with [7-ZIP](https://7-zip.org/). The extracted folder structure:
    
    
    ComfyUI_windows_portable
    ├── 📂ComfyUI                   // ComfyUI main program
    ├── 📂python_embeded            // Independent Python environment
    ├── 📂update                    // Batch scripts for upgrading portable version
    ├── README_VERY_IMPORTANT.txt   // ComfyUI Portable usage instructions in English
    ├── run_cpu.bat                 // Double click to start ComfyUI (CPU only)
    └── run_nvidia_gpu.bat          // Double click to start ComfyUI (Nvidia GPU)
    

Double click `run_nvidia_gpu.bat` to launch ComfyUI.

### 

​

Portable for AMD GPUs

## AMD GPU

Download for AMD GPUs (ROCm)

Download the file and extract it with [7-ZIP](https://7-zip.org/). The extracted folder structure:
    
    
    ComfyUI_windows_portable_amd
    ├── 📂ComfyUI                   // ComfyUI main program
    ├── 📂python_embeded            // Independent Python environment
    ├── 📂update                    // Batch scripts for upgrading portable version
    ├── README_VERY_IMPORTANT.txt   // ComfyUI Portable usage instructions in English
    ├── run_cpu.bat                 // Double click to start ComfyUI (CPU only)
    └── run_amd_gpu.bat             // Double click to start ComfyUI (AMD GPU)
    

Double click `run_amd_gpu.bat` to launch ComfyUI.

### 

​

Portable for Intel GPUs

## Intel GPU

Download for Intel GPUs

Download the file and extract it with [7-ZIP](https://7-zip.org/). The extracted folder structure:
    
    
    ComfyUI_windows_portable_intel
    ├── 📂ComfyUI                   // ComfyUI main program
    ├── 📂python_embeded            // Independent Python environment
    ├── 📂update                    // Batch scripts for upgrading portable version
    ├── README_VERY_IMPORTANT.txt   // ComfyUI Portable usage instructions in English
    ├── run_cpu.bat                 // Double click to start ComfyUI (CPU only)
    └── run_intel_gpu.bat           // Double click to start ComfyUI (Intel GPU)
    

Double click `run_intel_gpu.bat` to launch ComfyUI.

After downloading and extracting, you will see the command running as shown in the image below ![ComfyUI Portable Command Prompt](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyui-portable-cmd.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=27ead27f4bf5f09cabffc238e5a5890a) When you see something similar to the image
    
    
    To see the GUI go to: http://127.0.0.1:8188
    

At this point, your ComfyUI service has started. Normally, ComfyUI will automatically open your default browser and navigate to `http://127.0.0.1:8188`. If it doesn’t open automatically, please manually open your browser and visit this address.

During use, please do not close the corresponding command line window, otherwise ComfyUI will stop running

## 

​

Adding Extra Model Paths

If you want to manage your model files outside of `ComfyUI/models`, you may have the following reasons:

  * You have multiple ComfyUI instances and want them to share model files to save disk space
  * You have different types of GUI programs (such as WebUI) and want them to use the same model files
  * Model files cannot be recognized or found

We provide a way to add extra model search paths via the `extra_model_paths.yaml` configuration file

### 

​

Open Config File

  * Portable/Manual Install

  * Comfy Desktop




For the ComfyUI version such as [portable](https://docs.comfy.org/installation/comfyui_portable_windows) and [manual](https://docs.comfy.org/installation/manual_install), you can find an example file named `extra_model_paths.yaml.example` in the root directory of ComfyUI:
    
    
    ComfyUI/extra_model_paths.yaml.example
    

Copy and rename it to `extra_model_paths.yaml` for use. Keep it in ComfyUI’s root directory at `ComfyUI/extra_model_paths.yaml`. You can also find the config example file [here](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example)

If you are using the [Comfy Desktop](https://docs.comfy.org/installation/desktop/windows) application, click the capsule menu at the top of the desktop app, then open the **Storage** tab and add your model directories there. The capsule only exists in the desktop app, not when ComfyUI runs in a browser.![Comfy Desktop capsule menu: Storage tab showing model directory settings](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)Or open it directly at:

  * Windows

  * macOS



    
    
    C:\Users\YourUsername\AppData\Roaming\ComfyUI\extra_models_config.yaml
    
    
    
    ~/Library/Application Support/ComfyUI/extra_models_config.yaml
    

You should keep the file in the same directory, should not move these files to other places.

If the file does not exist, you can create it yourself with any text editor.

### 

​

Example Structure

Suppose you want to add the following model paths to ComfyUI:
    
    
    📁 YOUR_PATH/
      ├── 📁models/
      |   ├── 📁 loras/
      |   │   └── xxxxx.safetensors
      |   ├── 📁 checkpoints/
      |   │   └── xxxxx.safetensors
      |   ├── 📁 vae/
      |   │   └── xxxxx.safetensors
      |   └── 📁 controlnet/
      |       └── xxxxx.safetensors
    

Then you can configure the `extra_model_paths.yaml` file like below to let ComfyUI recognize the model paths on your device:
    
    
    my_custom_config:
        base_path: YOUR_PATH
        loras: models/loras/
        checkpoints: models/checkpoints/
        vae: models/vae/
        controlnet: models/controlnet/
    

or
    
    
    my_custom_config:
        base_path: YOUR_PATH/models/
        loras: loras
        checkpoints: checkpoints
        vae: vae
        controlnet: controlnet
    

For the desktop version, please add the configuration to the existing configuration path without overwriting the path configuration generated during installation. Please back up the corresponding file before modification, so that you can restore it when you make a mistake.

Or you can refer to the default [extra_model_paths.yaml.example](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example) for more configuration options. After saving, you need to **restart ComfyUI** for the changes to take effect. Below is the original config example:
    
    
    #Rename this to extra_model_paths.yaml and ComfyUI will load it
    
    
    #config for a1111 ui
    #all you have to do is change the base_path to where yours is installed
    a111:
        base_path: path/to/stable-diffusion-webui/
    
        checkpoints: models/Stable-diffusion
        configs: models/Stable-diffusion
        vae: models/VAE
        loras: |
             models/Lora
             models/LyCORIS
        upscale_models: |
                      models/ESRGAN
                      models/RealESRGAN
                      models/SwinIR
        embeddings: embeddings
        hypernetworks: models/hypernetworks
        controlnet: models/ControlNet
    
    #config for comfyui
    #your base path should be either an existing comfy install or a central folder where you store all of your models, loras, etc.
    
    #comfyui:
    #     base_path: path/to/comfyui/
    #     # You can use is_default to mark that these folders should be listed first, and used as the default dirs for eg downloads
    #     #is_default: true
    #     checkpoints: models/checkpoints/
    #     clip: models/clip/
    #     clip_vision: models/clip_vision/
    #     configs: models/configs/
    #     controlnet: models/controlnet/
    #     diffusion_models: |
    #                  models/diffusion_models
    #                  models/unet
    #     embeddings: models/embeddings/
    #     loras: models/loras/
    #     upscale_models: models/upscale_models/
    #     vae: models/vae/
    
    #other_ui:
    #    base_path: path/to/ui
    #    checkpoints: models/checkpoints
    #    gligen: models/gligen
    #    custom_nodes: path/custom_nodes
    
    

For example, if your WebUI is located at `D:\stable-diffusion-webui\`, you can modify the corresponding configuration to
    
    
    a111:
        base_path: D:\stable-diffusion-webui\
        checkpoints: models/Stable-diffusion
        configs: models/Stable-diffusion
        vae: models/VAE
        loras: |
             models/Lora
             models/LyCORIS
        upscale_models: |
                      models/ESRGAN
                      models/RealESRGAN
                      models/SwinIR
        embeddings: embeddings
        hypernetworks: models/hypernetworks
        controlnet: models/ControlNet
    

### 

​

Add Extra Custom Nodes Path

Besides adding external models, you can also add custom nodes paths that are not in the default path of ComfyUI

Please note that this will not change the default installation path of custom nodes, but will add an extra path search when starting ComfyUI. You still need to complete the installation of custom node dependencies in the corresponding environment to ensure the integrity of the running environment.

Below is a simple configuration example (MacOS), please modify it according to your actual situation and add it to the corresponding configuration file, save it and restart ComfyUI for the changes to take effect:
    
    
    my_custom_nodes:
      custom_nodes: /Users/your_username/Documents/extra_custom_nodes
    

## 

​

First Image Generation

After successful installation, you can refer to the section below to start your ComfyUI journey~

## First Image Generation

This tutorial will guide you through your first model installation and text-to-image generation

## 

​

Additional ComfyUI Portable Instructions

### 

​

1\. Upgrading ComfyUI Portable

You can use the batch commands in the update folder to upgrade your ComfyUI Portable version
    
    
    ComfyUI_windows_portable
    └─ 📂update
       ├── update.py
       ├── update_comfyui.bat                          // Update ComfyUI to the latest commit version
       ├── update_comfyui_and_python_dependencies.bat  // Only use when you have issues with your runtime environment
       └── update_comfyui_stable.bat                   // Update ComfyUI to the latest stable version
    

### 

​

2\. Setting Up LAN Access for ComfyUI Portable

If your ComfyUI is running on a local network and you want other devices to access ComfyUI, you can modify the corresponding `.bat` file (e.g. `run_nvidia_gpu.bat`, `run_amd_gpu.bat`, or `run_cpu.bat`) using Notepad to complete the configuration. This is mainly done by adding `--listen` to specify the listening address. Below is an example of the `run_nvidia_gpu.bat` file command with the `--listen` parameter added
    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build
    pause
    

After enabling ComfyUI, you will notice the final running address will become
    
    
    Starting server
    
    To see the GUI go to: http://0.0.0.0:8188
    To see the GUI go to: http://[::]:8188
    

You can press `WIN + R` and type `cmd` to open the command prompt, then enter `ipconfig` to view your local IP address. Other devices can then access ComfyUI by entering `http://your-local-IP:8188` in their browser.

### 

​

3\. Installing Additional Python Packages

The portable version ships with an embedded Python environment (`python_embeded`). To install additional Python packages (such as attention optimizations, custom node dependencies, or other tools), use the embedded Python’s pip from the command line:
    
    
    # Navigate to your ComfyUI portable folder first
    cd ComfyUI_windows_portable
    
    # Install a package using the embedded Python
    .\python_embeded\python.exe -m pip install <package-name>
    

After installing a package that requires a startup flag, add the corresponding flag to your `.bat` file (e.g. `run_nvidia_gpu.bat`):
    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --<startup-flag> --windows-standalone-build
    

For detailed guidance on installing custom node dependencies, see the [custom nodes dependency guide](https://docs.comfy.org/basic-concepts/custom-nodes).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/comfyui_portable_windows.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/comfyui_portable_windows)

[Comfy Desktop FAQPrevious](https://docs.comfy.org/installation/desktop/faq)[Install ComfyUI Manually (Windows, macOS, Linux)Next](https://docs.comfy.org/installation/manual_install)

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
