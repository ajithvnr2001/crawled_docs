---
url: https://docs.comfy.org/es/tutorials/video/wan/fun-camera/
title: Ejemplos oficiales de ComfyUI Wan2.1 Fun Camera - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:00.144050+00:00
---

# Ejemplos oficiales de ComfyUI Wan2.1 Fun Camera - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/fun-camera/

## En esta página

Volver arriba

  * Acerca de Wan2.1 Fun Camera
  * Instalación de modelos
    * Modelos de difusión
    * Codificadores de texto
    * VAE
    * CLIP Vision
  * Flujo de trabajo ComfyUI Wan2.1 Fun Camera 1.3B
    * Wan 2.1 Fun Camera 1.3B
    * 3\. Completar el flujo de trabajo paso a paso
  * Flujo de trabajo ComfyUI Wan2.1 Fun Camera 14B
    * Wan 2.1 Fun Camera 14B
  * Referencia de rendimiento



Wan2.1

# Ejemplos oficiales de ComfyUI Wan2.1 Fun Camera

Copiar páginaCopiar página

Esta guía muestra cómo usar Wan2.1 Fun Camera en ComfyUI para generar video

Copiar páginaCopiar página

Wan2.1 Fun Camera es un modelo de generación de video con movimiento de cámara del proyecto VideoX-Fun de Alibaba, con soporte nativo en ComfyUI. Genera videos cuyo movimiento de cámara sigue tus condiciones de control, así puedes dirigir cómo se mueve la cámara en el resultado en lugar de describir cada plano en el prompt. El modelo forma parte de la familia Wan2.1-Fun y se distribuye en dos tamaños: la versión 1.3B (unos 19 GB) para ejecuciones locales ligeras y la versión 14B (unos 47 GB) para un resultado de mayor fidelidad. Ambas admiten predicción de video multirresolución a 512, 768 y 1024 píxeles, están entrenadas a 16 fotogramas por segundo para hasta 81 fotogramas (unos 5 segundos) y aceptan prompts en varios idiomas. Los pesos se publican bajo la licencia Apache-2.0.

## 

​

Acerca de Wan2.1 Fun Camera

**Wan2.1 Fun Camera** es un proyecto de generación de video lanzado por el equipo de Alibaba, centrado en controlar los efectos de generación de video mediante el movimiento de cámara. **Descargar los pesos del modelo** :

  * [Versión 14B](https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-14B-Control-Camera)
  * [Versión 1.3B](https://huggingface.co/alibaba-pai/Wan2.1-Fun-V1.1-1.3B-Control-Camera)

**Repositorio de código** : [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun) **ComfyUI ahora es compatible de forma nativa con el modelo Wan2.1 Fun Camera**.

  * Usuarios locales

  * Usuarios de Cloud




Asegúrate de que tu ComfyUI esté actualizado.

  * [Descargar ComfyUI](https://www.comfy.org/download)
  * [Guía de actualización](https://docs.comfy.org/es/installation/update_comfyui)

Los flujos de trabajo de esta guía se encuentran en las [Plantillas de flujos de trabajo](https://docs.comfy.org/es/interface/features/template). Si no los encuentras en las plantillas, es posible que tu ComfyUI esté desactualizado.Si faltan nodos al cargar un flujo de trabajo, estas son las posibles razones:

  1. No estás usando la última versión de ComfyUI (versión nocturna)
  2. Algunos nodos fallaron al importarse durante el inicio



  * [Cloud](https://cloud.comfy.org) se actualizará después del lanzamiento estable de ComfyUI.

Por lo tanto, si notas que falta algún nodo central en este documento, puede deberse a que los nuevos nodos centrales aún no se han publicado en la última versión estable. Espera al próximo lanzamiento estable.

## 

​

Instalación de modelos

Estos modelos solo hay que instalarlos una vez. Además, la información de descarga de los modelos está incluida en las imágenes de los flujos de trabajo correspondientes, así que puedes elegir la forma de descarga que prefieras. Todos los modelos siguientes están disponibles en [Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### 

​

Modelos de difusión

Elige entre 1.3B o 14B:

## wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors

Modelo de difusión Wan2.1 Fun Camera 1.3B

## wan2.1_fun_camera_v1.1_14B_bf16.safetensors

Modelo de difusión Wan2.1 Fun Camera 14B

Si ya has usado modelos de Wan2.1, deberías tener ya los siguientes modelos. Si no es así, descárgalos:

### 

​

Codificadores de texto

Elige uno de los siguientes:

## umt5_xxl_fp16.safetensors

Codificador de texto de precisión completa

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

Codificador de texto cuantizado FP8 (recomendado para menos VRAM)

### 

​

VAE

## wan_2.1_vae.safetensors

Modelo VAE de Wan2.1

### 

​

CLIP Vision

## clip_vision_h.safetensors

Codificador CLIP Vision

Ubicación de almacenamiento de archivos:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │ ├── 📂 diffusion_models/
    │ │   ├── wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors # 1.3B version
    │ │   └── wan2.1_fun_camera_v1.1_14B_bf16.safetensors # 14B version
    │ ├── 📂 text_encoders/
    │ │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │ ├── 📂 vae/
    │ │   └── wan_2.1_vae.safetensors
    │ └── 📂 clip_vision/
    │     └── clip_vision_h.safetensors
    

## 

​

Flujo de trabajo ComfyUI Wan2.1 Fun Camera 1.3B

### 

​

Wan 2.1 Fun Camera 1.3B

Genera videos dinámicos con movimientos de cámara cinematográficos usando el modelo Wan 2.1 Fun Camera 1.3B. ![Vista previa del flujo de trabajo Wan 2.1 Fun Camera 1.3B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2.1_fun_camera_v1.1_1.3B-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan 2.1 Fun Camera 1.3B” en la biblioteca de plantillas

Descarga el video de abajo y arrástralo a ComfyUI para cargar el flujo de trabajo correspondiente:

Si quieres usar la versión 14B, solo reemplaza el archivo del modelo por la versión 14B, pero ten en cuenta los requisitos de VRAM.

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## video_wan2.1_fun_camera_v1.1_1.3B_start_image.jpg

Nodo `LoadImage` 52 · `video_wan2.1_fun_camera_v1.1_1.3B_start_image.jpg`

![video_wan2.1_fun_camera_v1.1_1.3B_start_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/video_wan2.1_fun_camera_v1.1_1.3B_start_image.jpg)

### 

​

3\. Completar el flujo de trabajo paso a paso

![Pasos del flujo de trabajo Wan2.1 Fun Camera](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2-1-fun-camera-1-3b-step-guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=f6fb10f8a36cb9036a66e1e99986c641)

  1. Verifica que se haya cargado la versión correcta del archivo del modelo: 
     * Versión 1.3B: `wan2.1_fun_camera_v1.1_1.3B_bf16.safetensors`
     * Versión 14B: `wan2.1_fun_camera_v1.1_14B_bf16.safetensors`
  2. Verifica que el nodo `Load CLIP` tenga cargado `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Verifica que el nodo `Load VAE` tenga cargado `wan_2.1_vae.safetensors`
  4. Verifica que el nodo `Load CLIP Vision` tenga cargado `clip_vision_h.safetensors`
  5. Sube el fotograma inicial al nodo `Load Image`
  6. Modifica el prompt si vas a usar tu propia imagen de entrada
  7. Configura el movimiento de cámara en el nodo `WanCameraEmbedding`
  8. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación



## 

​

Flujo de trabajo ComfyUI Wan2.1 Fun Camera 14B

### 

​

Wan 2.1 Fun Camera 14B

Genera videos de alta calidad con control de cámara avanzado usando el modelo completo de 14B. ![Vista previa del flujo de trabajo Wan 2.1 Fun Camera 14B](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2.1_fun_camera_v1.1_14B-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan 2.1 Fun Camera 14B” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## video_wan2.1_fun_camera_v1.1_14B_start_image.jpg

nodo `LoadImage` 52 · `video_wan2.1_fun_camera_v1.1_14B_start_image.jpg`

![video_wan2.1_fun_camera_v1.1_14B_start_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/video_wan2.1_fun_camera_v1.1_14B_start_image.jpg)

## 

​

Referencia de rendimiento

**Versión 1.3B** :

  * A 512x512 de resolución, una RTX 4090 tarda unos 72 segundos en generar 81 frames

**Versión 14B** :

  * Una RTX 4090 de 24 GB de VRAM puede quedarse sin memoria al generar a 512x512 de resolución, y también han aparecido problemas de memoria en una A100 al usar tamaños mayores



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/fun-camera.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/fun-camera)

[Wan2.1 Fun Control](https://docs.comfy.org/es/tutorials/video/wan/fun-control)[Wan2.1 Fun InP](https://docs.comfy.org/es/tutorials/video/wan/fun-inp)
