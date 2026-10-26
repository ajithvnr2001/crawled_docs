---
url: https://docs.comfy.org/es/manager/install/
title: Instalaci\u00f3n de ComfyUI-Manager - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:03.888564+00:00
---

# Instalación de ComfyUI-Manager - ComfyUI

> Source: https://docs.comfy.org/es/manager/install/

## En esta página

Volver arriba

  * Usuarios de escritorio
  * Usuarios de Portable
  * Usuarios de instalación manual
    * Opciones de línea de comandos
    * Cambiar entre la UI nueva y la clásica
  * Actualizar ComfyUI-Manager
  * Métodos de instalación clásicos



ComfyUI-Manager

# Instalación de ComfyUI-Manager

Copiar páginaCopiar página

Instala ComfyUI-Manager en ComfyUI Desktop, Portable o manual para buscar, instalar y actualizar nodos personalizados desde la aplicación.

Copiar páginaCopiar página

## 

​

Usuarios de escritorio

Comfy Desktop incluye ComfyUI-Manager en cada instalación de ComfyUI y lo arranca con `--enable-manager`, así que no tienes que instalar nada aparte. Configuras el Manager por instalación desde la propia app:

1

Abre el panel **Manage** para la instalación

En Comfy Desktop, abre la instalación y ve al panel **Manage** , luego cambia a la pestaña **Startup Args**.

2

Configura las opciones ComfyUI Manager

  * **Manager Security Level** (nivel de seguridad ComfyUI Manager) decide qué paquetes de nodos puede instalar ComfyUI Manager: **Strict** , **Standard** (recomendado), **Relaxed** o **Permissive**. Los niveles más estrictos son especialmente importantes cuando ComfyUI está expuesto a tu red con `--listen`
  * **Manager Network Mode** (modo de red ComfyUI Manager) decide cómo llega ComfyUI Manager al registro de nodos: **Public** (predeterminado), **Private** , **Offline** o **Personal cloud** (solo para una máquina que controles)

Ambas opciones se aplican la próxima vez que inicies esa instalación.

3

Cambia los flags con los que se inicia ComfyUI Manager (opcional)

**Startup Arguments** en la misma pestaña controla los flags con los que se inicia la instalación. Elimina `--enable-manager` para ejecutar ComfyUI sin ComfyUI Manager, o mantenlo y agrega `--disable-manager-ui` para ocultar la interfaz ComfyUI Manager mientras sus tareas en segundo plano continúan.

Consulta la [pestaña Startup Args](https://docs.comfy.org/es/installation/desktop/usage/manage#pesta%C3%B1a-argumentos-de-inicio) para el resto de las configuraciones por instalación y la [referencia de flags de inicio](https://docs.comfy.org/es/development/comfyui-server/startup-flags) para los flags ComfyUI Manager.

## 

​

Usuarios de Portable

Si usas [Windows Portable](https://docs.comfy.org/es/installation/comfyui_portable_windows), el nuevo ComfyUI-Manager ya viene en el núcleo de ComfyUI, pero hay que habilitarlo.

  1. Instala las dependencias ComfyUI Manager:
         
         .\python_embeded\python.exe -m pip install -r ComfyUI\manager_requirements.txt
         

  2. Inicia ComfyUI con ComfyUI Manager habilitado:
         
         .\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --enable-manager
         pause
         




## 

​

Usuarios de instalación manual

Si tienes una [instalación manual](https://docs.comfy.org/es/installation/manual_install), el nuevo ComfyUI-Manager ya viene en el núcleo de ComfyUI, pero hay que habilitarlo.

  1. Activa tu entorno virtual:
         
         # Windows
         venv\Scripts\activate
         
         # Linux/macOS
         source venv/bin/activate
         

  2. Instala las dependencias ComfyUI Manager:
         
         pip install -r manager_requirements.txt
         

  3. Habilita ComfyUI Manager con el flag `--enable-manager` al ejecutar ComfyUI:
         
         python main.py --enable-manager
         




### 

​

Opciones de línea de comandos

Opción (flag)| Descripción  
---|---  
`--enable-manager`| Habilita ComfyUI-Manager  
`--enable-manager-legacy-ui`| Usa la interfaz clásica ComfyUI Manager en lugar de la nueva UI (requiere `--enable-manager`)  
`--disable-manager-ui`| Deshabilita la UI y los endpoints ComfyUI Manager mientras mantiene las funciones en segundo plano (requiere `--enable-manager`)  
  
### 

​

Cambiar entre la UI nueva y la clásica

Las siguientes actualizaciones de versión solo son compatibles con instalaciones mediante pip. Las versiones instaladas a través de nodos personalizados no permiten cambiar a la nueva UI.

  * Usuarios que no usan Desktop

  * Usuarios de Desktop




Para usar la nueva UI:
    
    
    python main.py --enable-manager
    

Para usar la interfaz clásica:
    
    
    python main.py --enable-manager --enable-manager-legacy-ui
    

Los usuarios de Desktop pueden cambiar a la interfaz clásica en **Server Settings → UI Settings → Use legacy manager interface**![Cambiar a la interfaz clásica](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_use_legacy_manager_ui.png?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=5a47648f9d602868c022a17b01c4d2df)

## 

​

Actualizar ComfyUI-Manager

ComfyUI-Manager se distribuye como su propio paquete de Python, y el núcleo de ComfyUI fija la versión con la que funciona en `manager_requirements.txt`. La forma de actualizar ComfyUI Manager depende de cómo esté instalado ComfyUI:

  * Desktop

  * Instalaciones portable y manual

  * Clonación de Git




Desktop incluye ComfyUI Manager y lo mantiene al día con las actualizaciones de Comfy Desktop. Actualiza el motor de ComfyUI desde el [panel Manage](https://docs.comfy.org/es/installation/desktop/usage/manage#pesta%C3%B1a-actualizar).

Actualizar ComfyUI puede dejar sin cambios el paquete ComfyUI Manager que ya está instalado. Instala los requisitos ComfyUI Manager en el entorno desde el que inicias ComfyUI y luego reinicia ComfyUI con `--enable-manager`:
    
    
    # Portable (Windows)
    .\python_embeded\python.exe -m pip install -r ComfyUI\manager_requirements.txt
    .\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --enable-manager
    
    # Instalación manual
    pip install -r manager_requirements.txt
    python main.py --enable-manager
    

Si clonaste ComfyUI Manager dentro de `custom_nodes` por tu cuenta:
    
    
    cd ComfyUI/custom_nodes/comfyui-manager
    git pull
    

Luego reinicia ComfyUI.

## 

​

Métodos de instalación clásicos

Método 1: Clonar con Git (instalación general)

Para instalar ComfyUI-Manager además de una instalación existente de ComfyUI:

  1. Ve al directorio `ComfyUI/custom_nodes` en la terminal
  2. Clona el repositorio: 
         
         git clone https://github.com/Comfy-Org/ComfyUI-Manager comfyui-manager
         

  3. Instala las dependencias ComfyUI Manager: 
         
         cd comfyui-manager
         pip install -r requirements.txt
         

  4. Reinicia ComfyUI



Método 2: Versión portable (Windows)

  1. Instala [Git for Windows](https://git-scm.com/download/win) (versión independiente, selecciona “use windows default console window”)
  2. Descarga [install-manager-for-portable-version.bat](https://github.com/Comfy-Org/ComfyUI-Manager/raw/main/scripts/install-manager-for-portable-version.bat) en tu directorio `ComfyUI_windows_portable`
  3. Haz doble clic en el archivo de lote para instalar



Método 3: comfy-cli (RECOMENDADO para instalaciones nuevas)

comfy-cli ofrece varias funciones para administrar ComfyUI desde la CLI.**Requisitos** : Python 3, Git**Windows:**
    
    
     python -m venv venv
    venv\Scripts\activate
    pip install comfy-cli
    comfy install
    

**Linux/macOS:**
    
    
     python -m venv venv
    . venv/bin/activate
    pip install comfy-cli
    comfy install
    

Consulta también: [documentación de comfy-cli](https://docs.comfy.org/es/comfy-cli/getting-started)

Método 4: Linux + venv

**Requisitos** : python-is-python3, python3-venv, git

  1. Descarga [install-comfyui-venv-linux.sh](https://github.com/comfy-org/ComfyUI-Manager/raw/main/scripts/install-comfyui-venv-linux.sh) en un directorio de instalación vacío
  2. Ejecuta: 
         
         chmod +x install-comfyui-venv-linux.sh
         ./install-comfyui-venv-linux.sh
         

  3. Ejecuta ComfyUI con `./run_gpu.sh` o `./run_cpu.sh`



**Precauciones de instalación:**

  * Los archivos de ComfyUI-Manager deben estar ubicados exactamente en la ruta `ComfyUI/custom_nodes/comfyui-manager`
  * No descomprimas directamente en `ComfyUI/custom_nodes` (archivos como `__init__.py` no deben estar en ese directorio)
  * No instales en rutas como `ComfyUI/custom_nodes/ComfyUI-Manager/ComfyUI-Manager` o `ComfyUI/custom_nodes/ComfyUI-Manager-main`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/manager/install.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/manager/install)

[Descripción general](https://docs.comfy.org/es/manager/overview)[Nueva interfaz](https://docs.comfy.org/es/manager/pack-management)
