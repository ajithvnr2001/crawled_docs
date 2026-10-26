---
url: https://docs.comfy.org/es/tutorials/image/pixeldit/pixeldit/
title: Ejemplo de flujo de trabajo de PixelDiT en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:44.719347+00:00
---

# Ejemplo de flujo de trabajo de PixelDiT en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/pixeldit/pixeldit/

## En esta página

Volver arriba

  * Flujo de trabajo de texto a imagen con PixelDiT
    * Controles del flujo de trabajo
  * Descargas de modelos
    * Ubicación de almacenamiento de los modelos



PixelDiT

# Ejemplo de flujo de trabajo de PixelDiT en ComfyUI

Copiar páginaCopiar página

PixelDiT es el transformer de difusión en espacio de píxeles de NVIDIA para generar imágenes de 1024px a partir de texto, sin codificación VAE.

Copiar páginaCopiar página

**PixelDiT** es el transformer de difusión en espacio de píxeles de NVIDIA para la generación de texto a imagen a 1024px. A diferencia de los modelos de difusión tradicionales que operan en el espacio latente, PixelDiT genera imágenes directamente en el espacio de píxeles mediante una arquitectura DiT de dos niveles: un DiT a nivel de parche combinado con un DiT a nivel de píxel, con fusión MM-DiT para la atención conjunta entre tokens de texto e imagen. **Aspectos destacados del modelo** :

  * **Sin VAE** : genera directamente en el espacio de píxeles, sin codificación ni decodificación VAE tradicional
  * **DiT de dos niveles** : DiT a nivel de parche + DiT a nivel de píxel para una generación de alta calidad
  * **Múltiples relaciones de aspecto** : resolución base de 1024px con soporte para varias relaciones de aspecto
  * **~1.3B parámetros** : lo bastante eficiente para GPUs de consumo
  * **Licencia** : NSCLv1 (solo para investigación y evaluación no comercial)

**Enlaces relacionados** :

  * [Modelo oficial en Hugging Face](https://huggingface.co/nvidia/PixelDiT-1300M-1024px)
  * [Comfy-Org/PixelDiT](https://huggingface.co/Comfy-Org/PixelDiT)



## 

​

Flujo de trabajo de texto a imagen con PixelDiT

![Flujo de trabajo de texto a imagen con PixelDiT](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_pixeldit_t2i-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “PixelDiT” en la Biblioteca de plantillas

## Ejecutar en Comfy Cloud

Abrir en la nube

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

El flujo de trabajo consta de tres nodos principales:

  1. **ResolutionSelector** : elige la resolución de salida deseada
  2. **Subgrafo Text to Image (PixelDiT)** : el nodo de generación principal con controles expuestos para el prompt, la semilla, la selección del modelo y la resolución
  3. **SaveImage** : guarda la imagen generada



## Acerca de los subgrafos

Este flujo de trabajo usa nodos de subgrafo para el procesamiento modular. Consulta la documentación de subgrafos para aprender a personalizar y ampliar el flujo de trabajo.

### 

​

Controles del flujo de trabajo

Los controles expuestos en el nodo de subgrafo **Text to Image (PixelDiT)** incluyen:

Control| Descripción  
---|---  
**Positive Prompt**|  El prompt de texto que describe la imagen que quieres generar  
**Negative Prompt**|  Texto que describe lo que quieres evitar en la imagen generada  
**Seed**|  Semilla aleatoria para la reproducibilidad  
**UNet Model**|  Selección del checkpoint del modelo PixelDiT  
**CLIP Model**|  Selección del modelo codificador de texto  
  
## 

​

Descargas de modelos

PixelDiT usa dos archivos de modelo: un codificador de texto y el modelo de difusión.

## Codificador de texto

gemma_2_2b_it_elm_bf16.safetensors: codificador de texto Gemma-2-2B-IT

## Modelo de difusión

pixeldit_1300m_1024px_bf16.safetensors: modelo de difusión PixelDiT 1300M 1024px

### 

​

Ubicación de almacenamiento de los modelos
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── gemma_2_2b_it_elm_bf16.safetensors
    │   └── 📂 diffusion_models/
    │          └── pixeldit_1300m_1024px_bf16.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/pixeldit/pixeldit.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/pixeldit/pixeldit)

[Lens](https://docs.comfy.org/es/tutorials/image/lens/lens)[PiD Latent Upscale](https://docs.comfy.org/es/tutorials/image/nvidia/pid-latent-upscale)
