---
url: https://docs.comfy.org/es/tutorials/video/ltxv/
title: LTX-Video 0.9.5 en ComfyUI: T2V, I2V, control de m\u00faltiples fotogramas - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:59.794991+00:00
---

# LTX-Video 0.9.5 en ComfyUI: T2V, I2V, control de múltiples fotogramas - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/ltxv/

## En esta página

Volver arriba

  * Control de múltiples fotogramas
  * Imagen a video
    * LTXV Image to Video
  * Texto a video
    * LTXV Text to Video
  * Requisitos



LTX

# LTX-Video 0.9.5 en ComfyUI: T2V, I2V, control de múltiples fotogramas

Copiar páginaCopiar página

Ejecuta LTX-Video 0.9.5 en ComfyUI para texto a video, imagen a video y control multifotograma desde imágenes inicial y final, con descarga y configuración.

Copiar páginaCopiar página

[LTX-Video](https://huggingface.co/Lightricks/LTX-Video) es un modelo de video muy eficiente de Lightricks. Lo importante con este modelo es darle prompts largos y descriptivos.

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

Control de múltiples fotogramas

Te permite controlar el video con una serie de imágenes. Puedes descargar las imágenes de entrada: [fotograma inicial](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/house1.png) y [fotograma final](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/house2.png). ![Control de múltiples fotogramas de LTX-Video](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/ltxv/multi-frame/workflow.webp)

Arrastra el video directamente a ComfyUI para ejecutar el flujo de trabajo.

## 

​

Imagen a video

### 

​

LTXV Image to Video

Genera videos a partir de imágenes fijas. ![Vista previa del flujo de trabajo LTXV Image to Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/ltxv_image_to_video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “LTXV Image to Video” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## ltxv_image_to_video_input_image.jpg

Nodo `LoadImage` 78 · `ltxv_image_to_video_input_image.jpg`

![ltxv_image_to_video_input_image.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/ltxv_image_to_video_input_image.jpg)

Arrastra el video directamente a ComfyUI para ejecutar el flujo de trabajo.

## 

​

Texto a video

### 

​

LTXV Text to Video

Genera videos a partir de prompts de texto. ![Vista previa del flujo de trabajo LTXV Text to Video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/ltxv_text_to_video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descargar JSON o buscar “LTXV Text to Video” en la Biblioteca de plantillas

Arrastra el video directamente a ComfyUI para ejecutar el flujo de trabajo.

## 

​

Requisitos

Descarga los siguientes modelos y colócalos en las ubicaciones que se indican a continuación:

## ltx-video-2b-v0.9.5.safetensors

Descarga y guárdalo en ComfyUI/models/checkpoints/

## t5xxl_fp16.safetensors

Descarga y guárdalo en ComfyUI/models/text_encoders/
    
    
    ├── checkpoints/
    │   └── ltx-video-2b-v0.9.5.safetensors
    └── text_encoders/
        └── t5xxl_fp16.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/ltxv.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/ltxv)

[LTX-2.0](https://docs.comfy.org/es/tutorials/video/ltx/ltx-2)[Wan Animate 2](https://docs.comfy.org/es/tutorials/video/wan/wan-animate-2)
