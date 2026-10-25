---
url: https://docs.comfy.org/es/installation/system_requirements/
title: Requisitos del sistema - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:49.109468+00:00
---

# Requisitos del sistema - ComfyUI

> Source: https://docs.comfy.org/es/installation/system_requirements/

## En esta página

  * Sistemas operativos compatibles
  * Versión de Python
  * Requisitos del navegador
  * Hardware compatible
  * Dependencias
  * Preguntas frecuentes



Local (autoalojado)

# Requisitos del sistema

Copiar páginaCopiar página

Requisitos de hardware y software para instalar y ejecutar ComfyUI.

Copiar páginaCopiar página

En esta guía presentaremos los requisitos del sistema para instalar ComfyUI. Debido a las frecuentes actualizaciones de ComfyUI, es posible que este documento no se actualice de forma oportuna. Consulta las instrucciones correspondientes en [ComfyUI](https://github.com/Comfy-Org/ComfyUI). Independientemente de la versión de ComfyUI que uses, se ejecuta en un entorno Python separado.

### 

​

Sistemas operativos compatibles

Actualmente, admitimos los siguientes sistemas operativos:

  * Windows
  * Linux
  * macOS (compatible con Apple Silicon, como la serie M)

Consulta los enlaces a continuación para ver las instrucciones de instalación específicas de tu sistema operativo y configuración.

Comfy Desktop

Comfy Desktop permite la instalación independiente en **Windows** , **macOS (Apple Silicon)** y **Linux** (AppImage y `.deb`).

  * El código fuente está en [GitHub](https://github.com/Comfy-Org/Comfy-Desktop)



Las instalaciones de Desktop siguen por defecto la versión **estable** de ComfyUI. Si quieres cada última confirmación (commit), usa la versión portable o una instalación manual con git, o cambia el canal de actualización de la instancia a **Latest on GitHub**.

A continuación puedes elegir la instalación adecuada para tu sistema y hardware

  * Windows

  * macOS (Apple Silicon)

  * Linux




## Guía de instalación de Comfy Desktop (Windows)

Adecuada para **Windows** 10 o posterior. Se recomienda GPU NVIDIA o AMD.

## Guía de instalación de Comfy Desktop (macOS)

Adecuada para macOS con **Apple Silicon**

## Guía de instalación de Comfy Desktop (Linux)

Instala el AppImage o el `.deb`, o compila y ejecuta desde el código fuente.

ComfyUI Portable (Windows)

La versión portable es una versión de ComfyUI que integra un entorno Python integrado independiente; con la versión portable puedes probar las últimas funciones, actualmente solo es compatible con el sistema **Windows**

## Guía de instalación de ComfyUI Portable (Windows)

Compatible con la versión de ComfyUI para **Windows** que se ejecuta en **GPU Nvidia** o **solo con CPU** , siempre usa las últimas confirmaciones (commits) y es completamente portable.

Instalación manual

## Guía de instalación manual de ComfyUI

Compatible con todos los tipos de sistema y de GPU (Nvidia, AMD, Intel, Apple Silicon, Ascend NPU, Cambricon MLU)

### 

​

Versión de Python

  * **Python 3.13** tiene muy buen soporte y es la versión recomendada
  * Python 3.14 funciona, pero algunos nodos personalizados pueden tener problemas. La variante free threaded funciona, pero algunas dependencias habilitarán el GIL, por lo que no tiene soporte completo
  * Python 3.12 es una buena alternativa si tienes problemas con las dependencias de algunos nodos personalizados en 3.13



### 

​

Requisitos del navegador

Para obtener la mejor experiencia, usa **Google Chrome versión 143 o posterior**. Las versiones anteriores de Chrome (142 y anteriores) tienen problemas conocidos que pueden causar fallos visuales y problemas de rendimiento en ComfyUI.

### 

​

Hardware compatible

  * **GPU NVIDIA** \- Instala pytorch estable con CUDA 13.0: `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130`
  * **GPU AMD (Linux)** \- ROCm 7.2 estable o nocturna
  * **GPU AMD (Windows)** \- ROCm 10.0 mediante los paquetes PyTorch multiarquitectura de AMD. Compatible con RDNA 2, RDNA 3, RDNA 3.5 y RDNA 4; no se necesita instalar el SDK de HIP por separado
  * **GPU Intel** \- Serie Arc con soporte nativo de PyTorch torch.xpu
  * **Apple Silicon** \- Serie M1/M2/M3/M4 con aceleración Metal
  * **NPU Ascend** \- Mediante la extensión torch_npu
  * **MLU Cambricon** \- Mediante la extensión torch_mlu
  * **Iluvatar Corex** \- Mediante Iluvatar Extension for PyTorch
  * **CPU** \- Usa el parámetro `--cpu` (más lento)

Consulta la [sección de instalación manual de ComfyUI para Windows y Linux](https://github.com/Comfy-Org/ComfyUI?tab=readme-ov-file#manual-install-windows-linux) para ver los pasos de instalación detallados.

Se admite PyTorch 2.7 y versiones posteriores, pero se recomienda encarecidamente usar una versión más reciente. En las tarjetas Nvidia de la serie 20 y posteriores se requiere una versión de PyTorch con cu130 o superior. Algunas funciones y optimizaciones podrían funcionar solo en versiones más recientes. Por lo general, recomendamos usar la última versión principal de PyTorch con la última versión de CUDA, a menos que tenga menos de 2 semanas de antigüedad.La compilación portable para Windows actualmente incluye Python 3.13 y PyTorch CUDA 13.0. Actualiza tus controladores de Nvidia si no se inicia.

### 

​

Dependencias

  * Instala PyTorch (la versión específica para tu hardware)
  * Instala todas las dependencias del archivo requirements.txt de ComfyUI: `pip install -r requirements.txt`



## Instalación manual

Consulta la sección de instalación manual para ver los pasos de instalación detallados.

## 

​

Preguntas frecuentes

¿ComfyUI es compatible con MLX (el framework de aprendizaje automático de Apple)?

ComfyUI no usa MLX directamente. En los Mac con Apple Silicon (M1/M2/M3/M4), ComfyUI usa PyTorch con el backend **MPS (Metal Performance Shaders)** , que aprovecha el framework gráfico Metal de Apple para la aceleración por GPU.MLX es un framework de arrays para aprendizaje automático independiente, diseñado para Apple Silicon. La arquitectura de ComfyUI, basada en PyTorch, usa MPS en su lugar.Para verificar que MPS funciona en tu Mac:
    
    
    python -c "import torch; print(torch.backends.mps.is_available())"
    

**Docker:** ComfyUI no proporciona una imagen oficial de Docker. Si quieres ejecutar ComfyUI en un contenedor, puedes usar las imágenes mantenidas por la comunidad en [Docker Hub](https://hub.docker.com/search?q=comfyui). Estas imágenes **no están mantenidas oficialmente por Comfy-Org** y no cuentan con el soporte del equipo de ComfyUI. Úsalas bajo tu propio riesgo.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/installation/system_requirements.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/installation/system_requirements)

[Comfy Cloud](https://docs.comfy.org/es/get_started/cloud)[Descripción general](https://docs.comfy.org/es/installation/desktop/overview)
