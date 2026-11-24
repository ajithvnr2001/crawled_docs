---
url: https://docs.comfy.org/installation/system_requirements/
title: ComfyUI System Requirements: OS, Python, and GPU - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:35.226263+00:00
---

# ComfyUI System Requirements: OS, Python, and GPU - ComfyUI

> Source: https://docs.comfy.org/installation/system_requirements/

## On this page

Back to top

  * Supported Operating Systems
  * Python Version
  * Browser Requirements
  * Supported Hardware
  * Dependencies
  * FAQ



Portable (Self-Hosted)

# ComfyUI System Requirements: OS, Python, and GPU

Copy pageCopy page

What ComfyUI needs to run: supported operating systems, the recommended Python 3.13 build, browser version, and GPU backends per vendor.

Copy pageCopy page

In this guide, we will introduce the system requirements for installing ComfyUI. Due to frequent updates of ComfyUI, this document may not be updated in a timely manner. Please refer to the relevant instructions in [ComfyUI](https://github.com/Comfy-Org/ComfyUI). Regardless of which version of ComfyUI you use, it runs in a separate Python environment.

### Supported Operating Systems

Currently, we support the following operating systems:

  * Windows
  * Linux
  * macOS (supports Apple Silicon, such as the M series)

See the links below for installation instructions specific to your OS and setup.

Comfy Desktop

Comfy Desktop supports standalone installation on **Windows** , **macOS (Apple Silicon)** , and **Linux** (AppImage and `.deb`).

  * Source is on [GitHub](https://github.com/Comfy-Org/Comfy-Desktop)



Desktop installs track the **stable** ComfyUI release by default. If you want every latest commit, use the portable version or a manual git install, or switch a build’s update channel to **Latest on GitHub**.

## Comfy Desktop Installation Guide

Windows 10 or later, macOS on Apple silicon, or Linux. The guide has a tab for each system.

ComfyUI Portable (Windows)

Portable version is a ComfyUI version that integrates an independent embedded Python environment, using the portable version you can experience the latest features, currently only supports **Windows** system

## ComfyUI Portable (Windows) Installation Guide

Supports **Windows** ComfyUI version running on **Nvidia GPUs** or **CPU-only** , always use the latest commits and completely portable.

Manual Installation

## ComfyUI Manual Installation Guide

Supports all system types and GPU types (Nvidia, AMD, Intel, Apple Silicon, Ascend NPU, Cambricon MLU)

### Python Version

  * **Python 3.13** is very well supported and recommended
  * Python 3.14 works but some custom nodes may have issues. The free threaded variant works but some dependencies will enable the GIL so it’s not fully supported
  * Python 3.12 is a good fallback if you have trouble with some custom node dependencies on 3.13



### Browser Requirements

For the best experience, use **Google Chrome version 143 or later**. Earlier versions of Chrome (142 and below) have known issues that can cause visual glitches and performance problems in ComfyUI.

### Supported Hardware

  * **NVIDIA GPU** \- Install stable pytorch with CUDA 13.0: `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130`
  * **AMD GPU (Linux)** \- ROCm 7.2 stable or nightly
  * **AMD GPU (Windows)** \- ROCm 10.0 via AMD multi-architecture PyTorch packages. Supports RDNA 2, RDNA 3, RDNA 3.5, and RDNA 4; no separate HIP SDK installation needed
  * **Intel GPU** \- Arc series with native PyTorch torch.xpu support
  * **Apple Silicon** \- M1/M2/M3/M4 series with Metal acceleration
  * **Ascend NPU** \- Via torch_npu extension
  * **Cambricon MLU** \- Via torch_mlu extension
  * **Iluvatar Corex** \- Via Iluvatar Extension for PyTorch
  * **CPU** \- Use the `--cpu` parameter (slower)

Please refer to the [ComfyUI Windows and Linux manual installation section](https://github.com/Comfy-Org/ComfyUI?tab=readme-ov-file#manual-install-windows-linux) for detailed installation steps.

PyTorch 2.7 and above is supported, but using a newer version is strongly recommended. A cu130 or above version of PyTorch is required on Nvidia 20 series and above. Some features and optimizations might only work on newer versions. We generally recommend using the latest major version of PyTorch with the latest CUDA version unless it is less than 2 weeks old.The Windows portable build currently comes with Python 3.13 and PyTorch CUDA 13.0. Update your Nvidia drivers if it doesn’t start.

### Dependencies

  * Install PyTorch (version specific to your hardware)
  * Install all dependencies in the requirements.txt of ComfyUI: `pip install -r requirements.txt`



## Manual Installation

Please refer to the manual installation section for detailed installation steps.

## FAQ

Does ComfyUI support MLX (Apple's machine learning framework)?

ComfyUI does not use MLX directly. On Apple Silicon (M1/M2/M3/M4) Macs, ComfyUI uses PyTorch with the **MPS (Metal Performance Shaders)** backend, which leverages Apple’s Metal graphics framework for GPU acceleration.MLX is a separate machine-learning array framework designed for Apple Silicon. ComfyUI’s PyTorch-based architecture uses MPS instead.To verify MPS is working on your Mac:
    
    
    python -c "import torch; print(torch.backends.mps.is_available())"
    

**Docker:** ComfyUI does not provide an official Docker image. If you want to run ComfyUI in a container, you can use community-maintained images from [Docker Hub](https://hub.docker.com/search?q=comfyui). These images are **not officially maintained by Comfy-Org** and are not supported by the ComfyUI team. Use them at your own risk.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/system_requirements.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/system_requirements)

[Portable (Local)](https://docs.comfy.org/installation/comfyui_portable_windows)[Manual (Local)](https://docs.comfy.org/installation/manual_install)
