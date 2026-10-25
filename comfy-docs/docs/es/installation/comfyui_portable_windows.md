---
url: https://docs.comfy.org/es/installation/comfyui_portable_windows/
title: ComfyUI Portable para Windows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:47.920039+00:00
---

# ComfyUI Portable para Windows - ComfyUI

> Source: https://docs.comfy.org/es/installation/comfyui_portable_windows/

## En esta página

  * Descargar ComfyUI Portable
  * Agregar rutas de modelos adicionales
    * Abrir el archivo de configuración
    * Estructura de ejemplo
    * Agregar rutas de nodos personalizados adicionales
  * Primera generación de imágenes
  * Instrucciones adicionales de ComfyUI Portable
    * 1\. Actualizar ComfyUI Portable
    * 2\. Configurar el acceso a la red local para ComfyUI Portable
    * 3\. Instalar paquetes adicionales de Python



Local (autoalojado)

# ComfyUI Portable para Windows

Copiar páginaCopiar página

Descarga y ejecuta ComfyUI Portable en Windows: un paquete independiente con Python integrado y compilaciones CUDA para GPU NVIDIA. Extrae el archivo comprimido y luego ejecuta ComfyUI.

Copiar páginaCopiar página

**ComfyUI Portable** es una versión completa, autónoma y empaquetada de ComfyUI para Windows que integra un **Python (python_embeded)** independiente, requerido para que ComfyUI funcione. Solo necesitas extraerlo para usarlo. Esta sección de la guía te mostrará cómo instalar ComfyUI Portable.

## 

​

Descargar ComfyUI Portable

Elige el paquete de descarga que coincida con tu tipo de GPU. ComfyUI Portable ofrece paquetes separados para los distintos tipos de hardware de GPU.

  * GPU Nvidia

  * GPU AMD

  * GPU Intel




### 

​

Portable estándar para GPU Nvidia

## GPU Nvidia (CUDA 13.0, Python 3.13)

Para GPU Nvidia modernas (serie RTX)

## GPU Nvidia (CUDA 12.6, Python 3.12)

Para GPU Nvidia serie 10 y anteriores

## GPU Nvidia en Windows ARM64 (Python 3.14)

Para dispositivos Windows on ARM con una GPU Nvidia

Descarga el archivo y extráelo con [7-ZIP](https://7-zip.org/). La estructura de carpetas extraída:
    
    
    ComfyUI_windows_portable
    ├── 📂ComfyUI                   // Programa principal de ComfyUI
    ├── 📂python_embeded            // Entorno Python independiente
    ├── 📂update                    // Scripts por lotes para actualizar la versión portable
    ├── README_VERY_IMPORTANT.txt   // Instrucciones de uso de ComfyUI Portable en inglés
    ├── run_cpu.bat                 // Haz doble clic para iniciar ComfyUI (solo CPU)
    └── run_nvidia_gpu.bat          // Haz doble clic para iniciar ComfyUI (GPU Nvidia)
    

Haz doble clic en `run_nvidia_gpu.bat` para iniciar ComfyUI.

### 

​

Portable para GPU AMD

## GPU AMD

Descarga para GPU AMD (ROCm)

Descarga el archivo y extráelo con [7-ZIP](https://7-zip.org/). La estructura de carpetas extraída:
    
    
    ComfyUI_windows_portable_amd
    ├── 📂ComfyUI                   // Programa principal de ComfyUI
    ├── 📂python_embeded            // Entorno Python independiente
    ├── 📂update                    // Scripts por lotes para actualizar la versión portable
    ├── README_VERY_IMPORTANT.txt   // Instrucciones de uso de ComfyUI Portable en inglés
    ├── run_cpu.bat                 // Haz doble clic para iniciar ComfyUI (solo CPU)
    └── run_amd_gpu.bat             // Haz doble clic para iniciar ComfyUI (GPU AMD)
    

Haz doble clic en `run_amd_gpu.bat` para iniciar ComfyUI.

### 

​

Portable para GPU Intel

## GPU Intel

Descarga para GPU Intel

Descarga el archivo y extráelo con [7-ZIP](https://7-zip.org/). La estructura de carpetas extraída:
    
    
    ComfyUI_windows_portable_intel
    ├── 📂ComfyUI                   // Programa principal de ComfyUI
    ├── 📂python_embeded            // Entorno Python independiente
    ├── 📂update                    // Scripts por lotes para actualizar la versión portable
    ├── README_VERY_IMPORTANT.txt   // Instrucciones de uso de ComfyUI Portable en inglés
    ├── run_cpu.bat                 // Haz doble clic para iniciar ComfyUI (solo CPU)
    └── run_intel_gpu.bat           // Haz doble clic para iniciar ComfyUI (GPU Intel)
    

Haz doble clic en `run_intel_gpu.bat` para iniciar ComfyUI.

Después de descargar y extraer, verás el comando ejecutándose como se muestra en la imagen a continuación ![ComfyUI Portable Command Prompt](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyui-portable-cmd.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=27ead27f4bf5f09cabffc238e5a5890a) Cuando veas algo similar a la imagen
    
    
    To see the GUI go to: http://127.0.0.1:8188
    

En este punto, tu servicio de ComfyUI ya está iniciado. Normalmente, ComfyUI abrirá automáticamente tu navegador predeterminado y navegará a `http://127.0.0.1:8188`. Si no se abre automáticamente, abre tu navegador manualmente y visita esta dirección.

Durante el uso, no cierres la ventana de la línea de comandos correspondiente, de lo contrario ComfyUI detendrá su ejecución.

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

Primera generación de imágenes

Después de una instalación exitosa, puedes consultar la sección a continuación para comenzar tu recorrido con ComfyUI~

## Primera generación de imágenes

Este tutorial te guiará en la instalación de tu primer modelo y en la generación de imagen a partir de texto

## 

​

Instrucciones adicionales de ComfyUI Portable

### 

​

1\. Actualizar ComfyUI Portable

Puedes usar los comandos por lotes en la carpeta update para actualizar tu versión de ComfyUI Portable
    
    
    ComfyUI_windows_portable
    └─ 📂update
       ├── update.py
       ├── update_comfyui.bat                          // Actualiza ComfyUI a la última versión del commit
       ├── update_comfyui_and_python_dependencies.bat  // Úsalo solo cuando tengas problemas con tu entorno de ejecución
       └── update_comfyui_stable.bat                   // Actualiza ComfyUI a la última versión estable
    

### 

​

2\. Configurar el acceso a la red local para ComfyUI Portable

Si tu ComfyUI se ejecuta en una red local y quieres que otros dispositivos accedan a ComfyUI, puedes modificar el archivo `.bat` correspondiente (por ejemplo, `run_nvidia_gpu.bat`, `run_amd_gpu.bat` o `run_cpu.bat`) con el Bloc de notas para completar la configuración. Esto se hace principalmente agregando `--listen` para especificar la dirección de escucha. A continuación tienes un ejemplo del comando del archivo `run_nvidia_gpu.bat` con el parámetro `--listen` agregado
    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build
    pause
    

Después de habilitar ComfyUI, notarás que la dirección de ejecución final será
    
    
    Starting server
    
    To see the GUI go to: http://0.0.0.0:8188
    To see the GUI go to: http://[::]:8188
    

Puedes presionar `WIN + R` y escribir `cmd` para abrir el símbolo del sistema, luego ingresar `ipconfig` para ver tu dirección IP local. Otros dispositivos podrán acceder a ComfyUI ingresando `http://tu-IP-local:8188` en su navegador.

### 

​

3\. Instalar paquetes adicionales de Python

La versión portable incluye un entorno de Python Integrado (`python_embeded`). Para instalar paquetes adicionales de Python (como optimizaciones de atención, dependencias de nodos personalizados u otras herramientas), usa el pip del Python Integrado desde la línea de comandos:
    
    
    # Primero navega a tu carpeta de ComfyUI portable
    cd ComfyUI_windows_portable
    
    # Instala un paquete usando el Python Integrado
    .\python_embeded\python.exe -m pip install <package-name>
    

Después de instalar un paquete que requiere un indicador de inicio, agrega el indicador correspondiente a tu archivo `.bat` (por ejemplo, `run_nvidia_gpu.bat`):
    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --<startup-flag> --windows-standalone-build
    

Para obtener orientación detallada sobre cómo instalar las dependencias de nodos personalizados, consulta la [guía de dependencias de nodos personalizados](https://docs.comfy.org/basic-concepts/custom-nodes).

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/installation/comfyui_portable_windows.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/installation/comfyui_portable_windows)

[FAQ](https://docs.comfy.org/es/installation/desktop/faq)[Manual (local)](https://docs.comfy.org/es/installation/manual_install)
