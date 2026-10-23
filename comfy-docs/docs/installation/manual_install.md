---
url: https://docs.comfy.org/installation/manual_install/
title: Install ComfyUI Manually (Windows, macOS, Linux) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:59.240380+00:00
---

# Install ComfyUI Manually (Windows, macOS, Linux) - ComfyUI

> Source: https://docs.comfy.org/installation/manual_install/

## On this page

  * Create a virtual environment
  * Clone the ComfyUI code repository
  * Install GPU and ComfyUI dependencies
  * How to update ComfyUI
  * Adding Extra Model Paths
    * Open Config File
    * Example Structure
    * Add Extra Custom Nodes Path
  * FAQ
    * How to Stop/Exit ComfyUI



Local (Self-Hosted)

# Install ComfyUI Manually (Windows, macOS, Linux)

Copy pageCopy page

Install ComfyUI manually on Windows, macOS, or Linux: create a virtual environment, clone the repository, install GPU dependencies, and start the app.

Copy pageCopy page

For the installation of ComfyUI, it is mainly divided into several steps:

  1. Create a virtual environment(avoid polluting the system-level Python environment)
  2. Clone the ComfyUI code repository
  3. Install dependencies
  4. Start ComfyUI

You can also refer to [ComfyUI CLI](https://docs.comfy.org/comfy-cli/getting-started) to install ComfyUI, it is a command line tool that can easily install ComfyUI and manage its dependencies.

## 

​

Create a virtual environment

Independent virtual environments are necessary because ComfyUI’s dependencies may conflict with other dependencies on the system, and it can also avoid polluting the system-level Python environment.

[Install Miniconda](https://docs.anaconda.com/free/miniconda/index.html#latest-miniconda-installer-links). This will help you install the correct versions of Python and other libraries needed by ComfyUI. Create an environment with Conda.
    
    
    conda create -n comfyenv
    conda activate comfyenv
    

## 

​

Clone the ComfyUI code repository

You need to ensure that you have installed [Git](https://git-scm.com/downloads) on your system. First, you need to open the terminal (command line), then clone the code repository.

  * Windows

  * Linux

  * MacOS




If you have not installed Microsoft Visual C++ Redistributable, please install it [here.](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

Open Terminal application.

Open [Terminal application](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac).
    
    
    git clone https://github.com/Comfy-Org/ComfyUI.git
    

## 

​

Install GPU and ComfyUI dependencies

1

Install GPU dependencies

Install GPU Dependencies

Nvidia
    
    
    pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130
    

Alternatively, you can install the nightly version of PyTorch.

Install Nightly

Install Nightly version (might be more risky)
    
    
    pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu132
    

AMD

For Linux, install the ROCm 7.2 version of PyTorch:
    
    
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm7.2
    

Alternatively, you can install the nightly version of PyTorch (ROCm 7.2).

Install Nightly

Install Nightly version (might be more risky)
    
    
    pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm7.2
    

For Windows, use AMD’s [multi-architecture PyTorch packages](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/frameworks/pytorch/install.html) with ROCm 10.0. The `device-*` extras install your GPU’s kernels and the matching ROCm runtime automatically; a separate HIP SDK installation is not needed. Use Windows 11, a current [AMD graphics driver](https://www.amd.com/en/support/download/drivers.html), and 64-bit Python 3.13.The install command below uses `device-all` to install kernels for all supported GPUs. To reduce download size and disk usage, optionally replace **both** occurrences of `device-all` with the target for your GPU:

GPU| Device extra  
---|---  
RX 9070 / XT, Radeon AI PRO R9700| `device-gfx1201`  
RX 9060 / XT| `device-gfx1200`  
RX 7900 XT / XTX| `device-gfx1100`  
RX 7700 XT / 7800 XT| `device-gfx1101`  
RX 7600 / XT| `device-gfx1102`  
Ryzen AI Max / Max+ (Strix Halo)| `device-gfx1151`  
  
This table only lists examples. A GPU missing from it may still be supported: supported architectures include RDNA 2, RDNA 3, RDNA 3.5, and RDNA 4. Keep `device-all` to install kernels for all supported targets. For other models, see AMD’s [GPU target table](https://github.com/ROCm/TheRock/blob/main/RELEASES.md#gfx-target-lookup-table) and [ROCm compatibility matrix](https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html).
    
    
    pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-all]==2.13.0+rocm10.0.0" "torchvision[device-all]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"
    

Mac ARM Silicon
    
    
    conda install pytorch-nightly::pytorch torchvision torchaudio -c pytorch-nightly
    

Intel

Intel Arc GPUs (Arc A-Series, Arc B-Series, and Core Ultra processors with Arc Graphics) are supported through PyTorch’s native XPU backend. Intel GPUs use XPU, not CUDA.
    
    
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu
    

Make sure your [Intel GPU driver](https://www.intel.com/content/www/us/en/developer/articles/tool/pytorch-prerequisites-for-intel-gpu.html) is installed and up to date. Do not install CUDA wheels. If ComfyUI still does not detect the GPU, see [Intel GPU troubleshooting](https://docs.comfy.org/troubleshooting/overview#intel-gpu-issues).

2

Install ComfyUI dependencies
    
    
    cd ComfyUI
    pip install -r requirements.txt
    

3

Start ComfyUI

Start the application
    
    
    cd ComfyUI
    python main.py
    

Run `python main.py --help` for built-in help, or see the [Startup Flags reference](https://docs.comfy.org/development/comfyui-server/startup-flags) for a complete list of command-line options.

For advanced server configuration (custom port, LAN access, VRAM modes, and more), see the [Startup Flags reference](https://docs.comfy.org/development/comfyui-server/startup-flags).

## 

​

How to update ComfyUI

1

pull the latest code

Use the command line to enter the installation path of ComfyUI, then pull the latest code.
    
    
    cd <installation path>/ComfyUI
    git pull
    

2

install the dependencies

Use the command line to enter the installation path of ComfyUI, then install the dependencies.

You need to ensure that the current Python environment is the ComfyUI virtual environment, otherwise the dependencies will be installed to the system-level Python environment, polluting the system-level Python environment.
    
    
        pip install -r requirements.txt
    

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

FAQ

**Docker:** ComfyUI does not provide an official Docker image. If you want to run ComfyUI in a container, you can use community-maintained images from [Docker Hub](https://hub.docker.com/search?q=comfyui). These images are **not officially maintained by Comfy-Org** and are not supported by the ComfyUI team. Use them at your own risk.

### 

​

How to Stop/Exit ComfyUI

Press **Ctrl+C** in the terminal window where ComfyUI is running, or simply close the terminal window.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/manual_install.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/manual_install)

[ComfyUI Portable for WindowsPrevious](https://docs.comfy.org/installation/comfyui_portable_windows)[How to Update ComfyUINext](https://docs.comfy.org/installation/update_comfyui)

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
