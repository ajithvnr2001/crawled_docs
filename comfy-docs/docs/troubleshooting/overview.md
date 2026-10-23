---
url: https://docs.comfy.org/troubleshooting/overview/
title: How to Troubleshoot and Solve ComfyUI Issues - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:15.667038+00:00
---

# How to Troubleshoot and Solve ComfyUI Issues - ComfyUI

> Source: https://docs.comfy.org/troubleshooting/overview/

## On this page

  * Common Issues & Quick Fixes
    * ComfyUI Won’t Start
    * Generation Fails or Produces Errors
    * Slow Performance
  * Installation-Specific Issues
    * Desktop App Issues
    * Manual Installation Issues
    * Linux-Specific Issues
  * Model-Related Issues
  * Network & API Issues
    * Partner Nodes Not Working
    * Connection Issues
    * Frontend Issues
  * Hardware-Specific Issues
    * NVIDIA GPU Issues
    * AMD GPU Issues
    * Apple Silicon (M1/M2/M3) Issues
    * Intel GPU Issues
  * Frequently Asked Questions
    * How do I run ComfyUI with Docker?
  * Getting Help & Reporting Bugs
    * Before Reporting a Bug
    * How to Report Bugs Effectively
    * For ComfyUI Core Issues
    * For Desktop App Issues
    * For Frontend Issues
    * For Custom Node Issues
    * Required Information
  * Community Resources



Troubleshooting

# How to Troubleshoot and Solve ComfyUI Issues

Copy pageCopy page

ComfyUI troubleshooting guide: rule out custom nodes first, fix common core issues, and file a bug report with the right details.

Copy pageCopy page

We receive a lot of feedback issues, and we find that most of the issues submitted are related to custom nodes. So please ensure that you have read the [custom node troubleshooting guide](https://docs.comfy.org/troubleshooting/custom-node-issues) before submitting an error report to ensure that the issue is not caused by ComfyUI core issues.

## Custom Node Troubleshooting Guide

Check how to troubleshoot issues caused by custom nodes.

## 

​

Common Issues & Quick Fixes

Before diving into detailed troubleshooting, try these common solutions:

### 

​

ComfyUI Won’t Start

**Symptoms:** Application crashes on startup, black screen, or fails to load **Quick fixes:**

  1. **Check system requirements** \- Ensure your system meets the [minimum requirements](https://docs.comfy.org/installation/system_requirements)
  2. **Update GPU drivers** \- Download latest drivers from NVIDIA/AMD/Intel



### 

​

Generation Fails or Produces Errors

**Symptoms:** “Prompt execution failed” dialog with “Show report” button, workflow stops executing **Quick fixes:**

  1. **Click “Show report”** \- Read the detailed error message to identify the specific issue
  2. **Check if it’s a custom node issue** \- [Follow our custom node troubleshooting guide](https://docs.comfy.org/troubleshooting/custom-node-issues)
  3. **Verify model files** \- See [Models documentation](https://docs.comfy.org/basic-concepts/models) for model setup
  4. **Check VRAM usage** \- Close other applications using GPU memory



### 

​

Slow Performance

**Symptoms:** Very slow generation times, system freezing, out of memory errors **Quick fixes:**

  1. **Lower resolution/batch size** \- Reduce image size or number of images
  2. **Use memory optimization flags** \- See performance optimization section below
  3. **Close unnecessary applications** \- Free up RAM and VRAM
  4. **Check CPU/GPU usage** \- Use Task Manager to identify bottlenecks

**Performance Optimization Commands:** For low VRAM systems:
    
    
    # Low VRAM mode (uses cpu for text encoder)
    python main.py --lowvram
    
    # CPU mode (very slow but works with any hardware, only use as absolute last resort)
    python main.py --cpu
    

For better performance:
    
    
    # Disable previews (saves VRAM and processing)
    python main.py --preview-method none
    
    # Use optimized attention mechanisms
    python main.py --use-pytorch-cross-attention
    python main.py --use-flash-attention
    
    # Async weight offloading
    python main.py --async-offload
    

For memory management:
    
    
    # Reserve specific VRAM amount for OS (in GB)
    python main.py --reserve-vram 2
    
    # Disable smart memory management
    python main.py --disable-smart-memory
    
    # Use different caching strategies
    python main.py --cache-none      # Less RAM usage, but slower
    python main.py --cache-lru 10    # Cache 10 results, faster
    python main.py --cache-classic   # Use the old style (aggressive) caching. 
    

## 

​

Installation-Specific Issues

### 

​

Desktop App Issues

For comprehensive desktop installation troubleshooting, see the [Desktop Installation Guide](https://docs.comfy.org/installation/desktop/windows).

  * Windows

  * macOS

  * Linux




  * **Unsupported device** : Comfy Desktop Windows only supports NVIDIA GPUs with CUDA. Use [ComfyUI Portable](https://docs.comfy.org/installation/comfyui_portable_windows) or [manual installation](https://docs.comfy.org/installation/manual_install) for other GPUs
  * **Installation fails** : Run installer as administrator, ensure at least 15GB disk space
  * **Maintenance page** : Check [mirror settings](https://docs.comfy.org/installation/desktop/usage/settings#advanced) if downloads fail
  * **Missing models** : Models are not copied during migration, only linked. Verify model paths



  * **“App is damaged”** : Allow app in Security & Privacy settings
  * **Performance issues** : Grant Full Disk Access in Privacy settings
  * **Crashes** : Check Console app for crash reports



  * **Missing libraries** : Install dependencies with package manager
  * **LD_LIBRARY_PATH errors** : PyTorch library path issues (see below)



### 

​

Manual Installation Issues

The documentation may be slightly out of date. If an issue occurs, please manually verify whether a newer stable version of pytorch or any of the listed libraries exists. Refer to resources like the [pytorch installation matrix](https://pytorch.org/get-started/locally/) or the [ROCm website](https://rocm.docs.amd.com/projects/install-on-linux/en/develop/install/3rd-party/pytorch-install.html#using-a-wheels-package).

**Python version conflicts:**
    
    
    # Check Python version (3.9+ required, 3.12 recommended)
    python --version
    
    # Use virtual environment (recommended)
    python -m venv comfyui_env
    source comfyui_env/bin/activate  # Linux/Mac
    comfyui_env\Scripts\activate     # Windows
    

**Package installation failures:**
    
    
    # Update pip first
    python -m pip install --upgrade pip
    
    # Install dependencies
    pip install -r requirements.txt
    
    # For NVIDIA GPUs (CUDA 13.0)
    pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130
    
    # For AMD GPUs (Linux only - ROCm 7.2)
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm7.2
    

### 

​

Linux-Specific Issues

**LD_LIBRARY_PATH errors:** Common symptoms:

  * “libcuda.so.1: cannot open shared object file”
  * “libnccl.so: cannot open shared object file”
  * “ImportError: libnvinfer.so.X: cannot open shared object file”

**Solutions:**

  1. **Modern PyTorch installations (most common):**


    
    
    # For virtual environments with NVIDIA packages
    export LD_LIBRARY_PATH=$VIRTUAL_ENV/lib/python3.12/site-packages/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH
    
    # For conda environments
    export LD_LIBRARY_PATH=$CONDA_PREFIX/lib/python3.12/site-packages/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH
    
    # Or find your Python site-packages automatically
    PYTHON_PATH=$(python -c "import site; print(site.getsitepackages()[0])")
    export LD_LIBRARY_PATH=$PYTHON_PATH/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH
    
    # You may also need other NVIDIA libraries
    export LD_LIBRARY_PATH=$PYTHON_PATH/nvidia/cuda_runtime/lib:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=$PYTHON_PATH/nvidia/cublas/lib:$LD_LIBRARY_PATH
    

  2. **Find what libraries you have:**


    
    
    # Check installed NVIDIA packages
    python -c "import site; import os; nvidia_path=os.path.join(site.getsitepackages()[0], 'nvidia'); print('NVIDIA libs:', [d for d in os.listdir(nvidia_path) if os.path.isdir(os.path.join(nvidia_path, d))] if os.path.exists(nvidia_path) else 'Not found')"
    
    # Find missing libraries that PyTorch needs
    python -c "import torch; print(torch.__file__)"
    ldd $(python -c "import torch; print(torch.__file__.replace('__init__.py', 'lib/libtorch_cuda.so'))")
    

  3. **Set permanently for your environment:**


    
    
    # For virtual environments, add to activation script
    echo 'export LD_LIBRARY_PATH=$VIRTUAL_ENV/lib/python*/site-packages/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH' >> $VIRTUAL_ENV/bin/activate
    
    # For conda environments
    conda env config vars set LD_LIBRARY_PATH=$CONDA_PREFIX/lib/python*/site-packages/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH
    
    # For global bashrc (adjust Python version as needed)
    echo 'export LD_LIBRARY_PATH=$(python -c "import site; print(site.getsitepackages()[0])")/nvidia/nvjitlink/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
    

  4. **Alternative: Use ldconfig:**


    
    
    # Check current library cache
    ldconfig -p | grep cuda
    ldconfig -p | grep nccl
    
    # If missing, add library paths (requires root)
    sudo echo "/usr/local/cuda/lib64" > /etc/ld.so.conf.d/cuda.conf
    sudo ldconfig
    

  5. **Debug library loading:**


    
    
    # Verbose library loading to see what's missing
    LD_DEBUG=libs python main.py 2>&1 | grep "looking for"
    
    # Check PyTorch CUDA availability
    python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('CUDA version:', torch.version.cuda)"
    

## 

​

Model-Related Issues

For comprehensive model troubleshooting including architecture mismatches, missing models, and loading errors, see the dedicated [Model Issues](https://docs.comfy.org/troubleshooting/model-issues) page.

## 

​

Network & API Issues

### 

​

Partner Nodes Not Working

**Symptoms:** API calls fail, timeout errors, quota exceeded **Solutions:**

  1. **Check API key validity** \- Verify keys in [user settings](https://docs.comfy.org/interface/user)
  2. **Check account credits** \- Ensure sufficient [API credits](https://docs.comfy.org/interface/credits)
  3. **Verify internet connection** \- Test with other online services
  4. **Check service status** \- Provider may be experiencing downtime



### 

​

Connection Issues

**Symptoms:** “Failed to connect to server”, timeout errors **Solutions:**

  1. **Check firewall settings** \- Allow ComfyUI through firewall
  2. **Try different port** \- Default is 8188, try 8189 or 8190
  3. **Disable VPN temporarily** \- VPN may be blocking connections
  4. **Check proxy settings** \- Disable proxy if not required



### 

​

Frontend Issues

**“Frontend or Templates Package Not Updated”:**
    
    
    # After updating ComfyUI via Git, update frontend dependencies
    pip install -r requirements.txt
    

**“Can’t Find Custom Node”:**

  * Disable node validation in ComfyUI settings

**“Error Toast About Workflow Failing Validation”:**

  * Disable workflow validation in settings temporarily
  * Report the issue to the ComfyUI team

**Login Issues When Not on Localhost:**

  * Normal login only works when accessing from localhost
  * For LAN/remote access: Generate API key at [platform.comfy.org/login](https://platform.comfy.org/login)
  * Use API key in login dialog or with `--api-key` command line argument



## 

​

Hardware-Specific Issues

### 

​

NVIDIA GPU Issues

**“Torch not compiled with CUDA enabled” error:**
    
    
    # First uninstall torch
    pip uninstall torch
    
    # Install stable PyTorch with CUDA 13.0
    pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130
    
    # For nightly builds (might have performance improvements)
    pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu132
    
    # Verify CUDA support
    python -c "import torch; print(torch.cuda.is_available())"
    

**GPU not detected:**
    
    
    # Check if GPU is visible
    nvidia-smi
    
    # Check driver version and CUDA compatibility
    nvidia-smi --query-gpu=driver_version --format=csv
    

**Blackwell GPUs (`sm_103`): generation fails at the first attention layer:** On Blackwell-generation NVIDIA GPUs, PyTorch’s default scaled dot-product attention (SDPA) can select the cuDNN backend, which has no valid plan for this architecture:
    
    
    cuDNN Frontend error: No valid execution plans built
    

With FLUX this hits the very first attention block in the UNet, so no image is ever produced.
    
    
    # Use a hand-written attention implementation that bypasses SDPA and cuDNN
    python main.py --use-split-cross-attention
    
    # Blackwell also requires a CUDA 12.8 or newer PyTorch build;
    # builds compiled against cu121 will not run on these cards at all
    

Disabling the cuDNN SDPA backend programmatically before startup — for example calling `torch.backends.cuda.enable_cudnn_sdp(False)` from a `sitecustomize.py` — does not work, because the flag is not retained through CUDA initialization. The launch flag is the reliable fix.

_This entry was added in[PR #1491](https://github.com/Comfy-Org/docs/pull/1491)._

### 

​

AMD GPU Issues

**ROCm support (Linux only):**
    
    
    # Install stable ROCm PyTorch (7.2 at the time of writing)
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm7.2
    
    # For nightly builds (ROCm 7.2 at the time of writing, which might have performance improvements)
    pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm7.2
    

**Unsupported AMD GPUs:**
    
    
    # For RDNA2 or older (6700, 6600)
    HSA_OVERRIDE_GFX_VERSION=10.3.0 python main.py
    
    # For RDNA3 cards (7600)
    HSA_OVERRIDE_GFX_VERSION=11.0.0 python main.py
    

**Performance optimization:**
    
    
    # Enable experimental memory efficient attention (no longer necessary with PyTorch 2.4)
    TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1 python main.py --use-pytorch-cross-attention
    
    # Enable tunable operations (slow first run, but faster subsequent runs)
    PYTORCH_TUNABLEOP_ENABLED=1 python main.py
    

### 

​

Apple Silicon (M1/M2/M3) Issues

The steps in this section apply to a manual or source install, where ComfyUI runs in a Python environment you set up yourself. See [System Requirements](https://docs.comfy.org/installation/system_requirements) for the supported Python versions and [Manual Installation](https://docs.comfy.org/installation/manual_install) for the setup steps.**Comfy Desktop** on Apple silicon does not need a separate Python install: the app manages its own Python environment for each instance. See [Comfy Desktop for macOS](https://docs.comfy.org/installation/desktop/macos).

**MPS backend setup:**
    
    
    # Install PyTorch nightly for Apple Silicon
    # Follow Apple's guide: https://developer.apple.com/metal/pytorch/
    
    # Check MPS availability
    python -c "import torch; print(torch.backends.mps.is_available())"
    
    # Launch ComfyUI
    python main.py
    

**If MPS causes issues:**
    
    
    # Force CPU mode
    python main.py --cpu
    
    # With memory optimization
    python main.py --force-fp16 --cpu
    

### 

​

Intel GPU Issues

**“Torch not compiled with CUDA enabled” error:** On Intel GPUs this error means ComfyUI tried to use CUDA because the XPU backend was not available. Do not follow the NVIDIA CUDA reinstallation steps above. Intel GPUs use XPU, not CUDA. Check whether PyTorch can see the Intel GPU:
    
    
    python -c "import torch; print('XPU available:', hasattr(torch, 'xpu') and torch.xpu.is_available())"
    

If this prints `True`, ComfyUI uses the XPU backend automatically. If it prints `False`:

  1. Confirm you have a supported Intel Arc GPU (Arc A-Series, Arc B-Series, or a Core Ultra processor with Arc Graphics).
  2. Install or update the [Intel GPU driver](https://www.intel.com/content/www/us/en/developer/articles/tool/pytorch-prerequisites-for-intel-gpu.html).
  3. Install an XPU-enabled PyTorch build using one of the options below. Do not install a CUDA wheel.

**Option 1: Native PyTorch XPU support (Windows/Linux):**
    
    
    # Stable XPU wheels (recommended)
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu
    
    # Nightly XPU wheels (may include performance improvements)
    pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/xpu
    
    # Launch ComfyUI
    python main.py
    

**Option 2: Intel Extension for PyTorch (IPEX):**
    
    
    # For Intel Arc A-Series Graphics
    conda install libuv
    pip install torch==2.3.1.post0+cxx11.abi torchvision==0.18.1.post0+cxx11.abi torchaudio==2.3.1.post0+cxx11.abi intel-extension-for-pytorch==2.3.110.post0+xpu --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/
    

## 

​

Frequently Asked Questions

### 

​

How do I run ComfyUI with Docker?

**Docker:** ComfyUI does not provide an official Docker image. If you want to run ComfyUI in a container, you can use community-maintained images from [Docker Hub](https://hub.docker.com/search?q=comfyui). These images are **not officially maintained by Comfy-Org** and are not supported by the ComfyUI team. Use them at your own risk.

For local installation on Linux, follow the [Manual Installation Guide](https://docs.comfy.org/installation/manual_install). For cloud usage, see [Comfy Cloud](https://docs.comfy.org/get_started/cloud).

## 

​

Getting Help & Reporting Bugs

### 

​

Before Reporting a Bug

  1. **Check if it’s a known issue:**
     * Search [GitHub Issues](https://github.com/Comfy-Org/ComfyUI/issues)
     * Check [ComfyUI Forum](https://forum.comfy.org/)
     * Review [Discord discussions](https://discord.com/invite/comfyorg)
  2. **Try basic troubleshooting:**
     * Test with [default workflow](https://docs.comfy.org/get_started/first_generation)
     * Disable all custom nodes (see [custom node troubleshooting](https://docs.comfy.org/troubleshooting/custom-node-issues))
     * Check console/terminal for error messages
     * If using comfy-cli, try updating: `comfy node update all`



### 

​

How to Report Bugs Effectively

#### 

​

For ComfyUI Core Issues

**Where to report:** [GitHub Issues](https://github.com/Comfy-Org/ComfyUI/issues)

#### 

​

For Desktop App Issues

**Where to report:** [Desktop GitHub Issues](https://github.com/Comfy-Org/Comfy-Desktop/issues)

#### 

​

For Frontend Issues

**Where to report:** [Frontend GitHub Issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)

#### 

​

For Custom Node Issues

**Where to report:** Contact the specific custom node developer

### 

​

Required Information

When reporting any issue, include:

1

System Information

  * From ComfyUI Interface

  * From Command Line




**System Information (can be found in the About page in settings):**

  * Operating System (Windows 11, macOS 14.1, Ubuntu 22.04, etc.)
  * ComfyUI version (check About page in settings)
  * Python version: `python --version`
  * PyTorch version: `python -c "import torch; print(torch.__version__)"`
  * GPU model and driver version
  * Installation method (Desktop, Portable, Manual, comfy-cli) ![About page in settings](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/menu-about.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=c5bbb54ba0d54a908d76ea3e863680d8)



  * Windows

  * macOS/Linux



    
    
    # System info
    systeminfo | findstr /C:"OS Name" /C:"OS Version"
    
    # GPU info
    wmic path win32_VideoController get name
    
    # Python & PyTorch info
    python --version
    python -c "import torch; print(f'PyTorch: {torch.__version__}')"
    python -c "import torch; print(f'CUDA Available: {torch.cuda.is_available()}')"
    
    
    
    # System info
    uname -a
    
    # GPU info (Linux)
    lspci | grep VGA
    
    # Python & PyTorch info
    python --version
    python -c "import torch; print(f'PyTorch: {torch.__version__}')"
    python -c "import torch; print(f'CUDA Available: {torch.cuda.is_available()}')"
    

2

Desktop App issues

**For Desktop App issues, also include:**

  * Log files from: `C:\Users\<username>\AppData\Roaming\ComfyUI\logs` (Windows)
  * Config files from: `C:\Users\<username>\AppData\Roaming\ComfyUI` (Windows)



3

Problem Details

**Problem Details:**

  * Clear description of the issue
  * Steps to reproduce the problem
  * Expected vs actual behavior
  * Screenshots or videos if applicable

**Error Messages:**

  * Full error text from console/terminal
  * Browser console errors (F12 → Console tab)
  * Any crash logs or error dialogs



4

Additional Context

**Additional Context:**

  * List of installed custom nodes
  * Workflow file (.json) that reproduces the issue
  * Recent changes (new installations, updates, etc.)



## 

​

Community Resources

  * **Official Forum:** [forum.comfy.org](https://forum.comfy.org/)
  * **Discord:** [ComfyUI Discord Server](https://discord.com/invite/comfyorg)
  * **Reddit:** [r/comfyui](https://reddit.com/r/comfyui)
  * **YouTube:** [ComfyUI Tutorials](https://www.youtube.com/@comfyorg)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/troubleshooting/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/troubleshooting/overview)

[Comfy Cloud invoice informationPrevious](https://docs.comfy.org/support/payment/invoice-information)[How to Troubleshoot and Solve ComfyUI Model IssuesNext](https://docs.comfy.org/troubleshooting/model-issues)

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
