---
url: https://docs.comfy.org/es/installation/manual_install/
title: Instalar ComfyUI manualmente (Windows, macOS, Linux) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:48.903908+00:00
---

# Instalar ComfyUI manualmente (Windows, macOS, Linux) - ComfyUI

> Source: https://docs.comfy.org/es/installation/manual_install/

## En esta página

  * Crear un entorno virtual
  * Clona el repositorio de código de ComfyUI
  * Instala las dependencias de GPU y de ComfyUI
  * Cómo actualizar ComfyUI
  * Agregar rutas de modelos adicionales
    * Abrir el archivo de configuración
    * Estructura de ejemplo
    * Agregar rutas de nodos personalizados adicionales
  * Preguntas frecuentes
    * Cómo detener o salir de ComfyUI



Local (autoalojado)

# Instalar ComfyUI manualmente (Windows, macOS, Linux)

Copiar páginaCopiar página

Instala ComfyUI manualmente en Windows, macOS o Linux: crea un entorno virtual, clona el repositorio, instala las dependencias de la GPU e inicia la aplicación.

Copiar páginaCopiar página

La instalación de ComfyUI se divide principalmente en varios pasos:

  1. Crear un entorno virtual (para evitar contaminar el entorno de Python del sistema)
  2. Clonar el repositorio de código de ComfyUI
  3. Instalar las dependencias
  4. Iniciar ComfyUI

También puedes consultar [ComfyUI CLI](https://docs.comfy.org/comfy-cli/getting-started) para instalar ComfyUI. Es una herramienta de línea de comandos que permite instalar ComfyUI y administrar sus dependencias fácilmente.

## 

​

Crear un entorno virtual

Los entornos virtuales independientes son necesarios porque las dependencias de ComfyUI pueden entrar en conflicto con otras dependencias del sistema, y también permiten evitar contaminar el entorno de Python a nivel de sistema.

[Instala Miniconda](https://docs.anaconda.com/free/miniconda/index.html#latest-miniconda-installer-links). Esto te ayuda a instalar las versiones correctas de Python y de las demás bibliotecas que necesita ComfyUI. Crea un entorno con Conda.
    
    
    conda create -n comfyenv
    conda activate comfyenv
    

## 

​

Clona el repositorio de código de ComfyUI

Asegúrate de tener [Git](https://git-scm.com/downloads) instalado en tu sistema. Primero abre la terminal (línea de comandos) y luego clona el repositorio.

  * Windows

  * Linux

  * MacOS




Si no has instalado Microsoft Visual C++ Redistributable, instálalo [aquí.](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

Abre la aplicación Terminal.

Abre la [aplicación Terminal](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac).
    
    
    git clone https://github.com/Comfy-Org/ComfyUI.git
    

## 

​

Instala las dependencias de GPU y de ComfyUI

1

Instala las dependencias de GPU

Instalar dependencias de GPU

Nvidia
    
    
    pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130
    

También puedes instalar la versión nightly de PyTorch.

Instalar la versión nightly

Instalar la versión nightly (puede ser más arriesgado)
    
    
    pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu132
    

AMD

En Linux, instala la versión ROCm 7.2 de PyTorch:
    
    
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm7.2
    

También puedes instalar la versión nightly de PyTorch (ROCm 7.2).

Instalar la versión nightly

Instalar la versión nightly (puede ser más riesgoso)
    
    
    pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm7.2
    

En Windows, usa los [paquetes PyTorch multiarquitectura](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/frameworks/pytorch/install.html) de AMD con ROCm 10.0. Los extras `device-*` instalan los kernels de tu GPU y el entorno de ejecución de ROCm correspondiente de forma automática; no necesitas instalar el SDK de HIP por separado. Usa Windows 11, un [controlador de gráficos AMD](https://www.amd.com/en/support/download/drivers.html) actual y Python 3.13 de 64 bits.El comando de instalación siguiente usa `device-all` para instalar los kernels de todas las GPU compatibles. Para reducir el tamaño de la descarga y el uso de disco, puedes reemplazar **ambas** apariciones de `device-all` por el destino de tu GPU:

GPU| Extra de dispositivo  
---|---  
RX 9070 / XT, Radeon AI PRO R9700| `device-gfx1201`  
RX 9060 / XT| `device-gfx1200`  
RX 7900 XT / XTX| `device-gfx1100`  
RX 7700 XT / 7800 XT| `device-gfx1101`  
RX 7600 / XT| `device-gfx1102`  
Ryzen AI Max / Max+ (Strix Halo)| `device-gfx1151`  
  
Esta tabla solo contiene ejemplos. Una GPU que no aparezca aquí puede seguir siendo compatible: las arquitecturas compatibles incluyen RDNA 2, RDNA 3, RDNA 3.5 y RDNA 4. Mantén `device-all` para instalar los kernels de todos los destinos compatibles. Para otros modelos, consulta la [tabla de destinos de GPU](https://github.com/ROCm/TheRock/blob/main/RELEASES.md#gfx-target-lookup-table) de AMD y la [matriz de compatibilidad de ROCm](https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html).
    
    
    pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-all]==2.13.0+rocm10.0.0" "torchvision[device-all]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"
    

Mac con silicio ARM
    
    
    conda install pytorch-nightly::pytorch torchvision torchaudio -c pytorch-nightly
    

Intel

Las GPU Intel Arc (Arc serie A, Arc serie B y procesadores Core Ultra con Arc Graphics) son compatibles a través del backend XPU nativo de PyTorch. Las GPU Intel usan XPU, no CUDA.
    
    
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/xpu
    

Asegúrate de que tu [controlador de GPU Intel](https://www.intel.com/content/www/us/en/developer/articles/tool/pytorch-prerequisites-for-intel-gpu.html) esté instalado y actualizado. No instales los wheels de CUDA. Si ComfyUI sigue sin detectar la GPU, consulta [solución de problemas de GPU Intel](https://docs.comfy.org/troubleshooting/overview#intel-gpu-issues).

2

Instala las dependencias de ComfyUI
    
    
    cd ComfyUI
    pip install -r requirements.txt
    

3

Inicia ComfyUI

Inicia la aplicación
    
    
    cd ComfyUI
    python main.py
    

Ejecuta `python main.py --help` para ver la ayuda integrada, o consulta la [Referencia de indicadores de inicio](https://docs.comfy.org/development/comfyui-server/startup-flags) para obtener una lista completa de las opciones de línea de comandos.

Para la configuración avanzada del servidor (puerto personalizado, acceso a la LAN, modos de VRAM y más), consulta la [referencia de indicadores de inicio](https://docs.comfy.org/development/comfyui-server/startup-flags).

## 

​

Cómo actualizar ComfyUI

1

Obtener el último código

Usa la línea de comandos para entrar a la ruta de instalación de ComfyUI y luego obtén el último código.
    
    
    cd <installation path>/ComfyUI
    git pull
    

2

Instalar las dependencias

Usa la línea de comandos para entrar a la ruta de instalación de ComfyUI y luego instala las dependencias.

Debes asegurarte de que el entorno de Python actual sea el entorno virtual de ComfyUI; de lo contrario, las dependencias se instalarán en el entorno de Python del sistema, contaminándolo.
    
    
        pip install -r requirements.txt
    

## 

​

Agregar rutas de modelos adicionales

Si quieres gestionar tus archivos de modelo fuera de `ComfyUI/models`, puede que tengas alguno de estos motivos:

  * Tienes varias instancias de ComfyUI y quieres que compartan los archivos de modelo para ahorrar espacio en disco
  * Tienes distintos programas con interfaz gráfica (como WebUI) y quieres que usen los mismos archivos de modelo
  * Los archivos de modelo no se reconocen o no se encuentran

Ofrecemos una forma de agregar rutas de búsqueda de modelos adicionales mediante el archivo de configuración `extra_model_paths.yaml`.

### 

​

Abrir el archivo de configuración

  * Instalación portable/manual

  * Comfy Desktop




En el caso de las versiones de ComfyUI como la [portable](https://docs.comfy.org/es/installation/comfyui_portable_windows) y la [manual](https://docs.comfy.org/es/installation/manual_install), puedes encontrar un archivo de ejemplo llamado `extra_model_paths.yaml.example` en el directorio raíz de ComfyUI:
    
    
    ComfyUI/extra_model_paths.yaml.example
    

Cópialo y cámbiale el nombre a `extra_model_paths.yaml` para usarlo. Déjalo en el directorio raíz de ComfyUI, en `ComfyUI/extra_model_paths.yaml`. También puedes encontrar el archivo de ejemplo de configuración [aquí](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example)

Si usas la aplicación [Comfy Desktop](https://docs.comfy.org/es/installation/desktop/windows), haz clic en el menú de la cápsula en la parte superior de la aplicación de escritorio, luego abre la pestaña **Almacenamiento** y agrega allí tus directorios de modelos. La cápsula solo existe en la aplicación de escritorio, no cuando ComfyUI se ejecuta en el navegador.![Menú de la cápsula de Comfy Desktop: pestaña Almacenamiento con la configuración de directorios de modelos](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)O ábrelo directamente en:

  * Windows

  * macOS



    
    
    C:\Users\YourUsername\AppData\Roaming\ComfyUI\extra_models_config.yaml
    
    
    
    ~/Library/Application Support/ComfyUI/extra_models_config.yaml
    

Debes mantener el archivo en el mismo directorio, no muevas estos archivos a otros lugares.

Si el archivo no existe, puedes crearlo tú mismo con cualquier editor de texto.

### 

​

Estructura de ejemplo

Supongamos que quieres agregar las siguientes rutas de modelos a ComfyUI:
    
    
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
    

Después puedes configurar el archivo `extra_model_paths.yaml` como se muestra abajo para que ComfyUI reconozca las rutas de modelos en tu dispositivo:
    
    
    my_custom_config:
        base_path: YOUR_PATH
        loras: models/loras/
        checkpoints: models/checkpoints/
        vae: models/vae/
        controlnet: models/controlnet/
    

o
    
    
    my_custom_config:
        base_path: YOUR_PATH/models/
        loras: loras
        checkpoints: checkpoints
        vae: vae
        controlnet: controlnet
    

Para la versión de escritorio, agrega la configuración a la ruta de configuración existente sin sobrescribir la configuración de rutas generada durante la instalación. Haz una copia de seguridad del archivo correspondiente antes de modificarlo, para que puedas restaurarlo si te equivocas.

O puedes consultar el [extra_model_paths.yaml.example](https://github.com/Comfy-Org/ComfyUI/blob/master/extra_model_paths.yaml.example) predeterminado para ver más opciones de configuración. Después de guardar, debes **reiniciar ComfyUI** para que los cambios tengan efecto. Abajo está el ejemplo de configuración original:
    
    
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
    
    

Por ejemplo, si tu WebUI está en `D:\stable-diffusion-webui\`, puedes modificar la configuración correspondiente a
    
    
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

Agregar rutas de nodos personalizados adicionales

Además de agregar modelos externos, también puedes agregar rutas de nodos personalizados que no estén en la ruta predeterminada de ComfyUI.

Ten en cuenta que esto no cambiará la ruta de instalación predeterminada de los nodos personalizados, sino que agregará una búsqueda de rutas adicional al iniciar ComfyUI. Aún necesitas completar la instalación de las dependencias de los nodos personalizados en el entorno correspondiente para garantizar la integridad del entorno de ejecución.

Abajo hay un ejemplo de configuración simple (MacOS); modifícalo según tu situación real y agrégalo al archivo de configuración correspondiente, guárdalo y reinicia ComfyUI para que los cambios tengan efecto:
    
    
    my_custom_nodes:
      custom_nodes: /Users/your_username/Documents/extra_custom_nodes
    

## 

​

Preguntas frecuentes

**Docker:** ComfyUI no proporciona una imagen oficial de Docker. Si quieres ejecutar ComfyUI en un contenedor, puedes usar las imágenes mantenidas por la comunidad en [Docker Hub](https://hub.docker.com/search?q=comfyui). Estas imágenes **no están mantenidas oficialmente por Comfy-Org** y no cuentan con el soporte del equipo de ComfyUI. Úsalas bajo tu propio riesgo.

### 

​

Cómo detener o salir de ComfyUI

Presiona **Ctrl+C** en la ventana de terminal donde se está ejecutando ComfyUI, o simplemente cierra la ventana de terminal.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/installation/manual_install.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/installation/manual_install)

[Portátil (Local)](https://docs.comfy.org/es/installation/comfyui_portable_windows)[Actualizar ComfyUI](https://docs.comfy.org/es/installation/update_comfyui)
