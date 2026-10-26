---
url: https://docs.comfy.org/es/tutorials/image/boogu/boogu-image-0.1
title: Ejemplo de flujo de trabajo de Boogu-Image-0.1 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:43.315152+00:00
---

# Ejemplo de flujo de trabajo de Boogu-Image-0.1 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/boogu/boogu-image-0.1

## En esta página

Volver arriba

  * Flujo de trabajo de texto a imagen de Boogu-Image-0.1-Turbo
    * Boogu Turbo: Text to Image
    * Descargas de modelos de Boogu-Image-0.1-Turbo
  * Flujo de trabajo de edición de imágenes de Boogu-Image-0.1-Edit
    * Boogu image 0.1 Edit
    * Descargas de modelos de Boogu-Image-0.1-Edit



Boogu

# Ejemplo de flujo de trabajo de Boogu-Image-0.1 en ComfyUI

Copiar páginaCopiar página

Boogu-Image-0.1 es una familia de modelos de generación y edición de imágenes de 10B parámetros con licencia Apache-2.0, con variantes de texto a imagen y edición guiada por instrucciones.

Copiar páginaCopiar página

**Boogu-Image-0.1** es una familia de modelos unificados de código abierto con licencia Apache-2.0 para la generación y edición de imágenes. Utiliza un sistema que integra comprensión y generación para ofrecer un rendimiento competitivo en fotografía, renderizado de texto, estilización y tareas de edición de imágenes. **Variantes del modelo** :

  * **Boogu-Image-0.1-Turbo** : una variante destilada de texto a imagen de cuatro pasos, enfocada en la generación de alta calidad y el fotorrealismo, equipada con un módulo LoRA de rango 128. Solo requiere 3-4 pasos de muestreo. Se recomienda como opción predeterminada para la mayoría de los casos de uso de texto a imagen.
  * **Boogu-Image-0.1-Base** : el modelo base, con gran diversidad y controlabilidad, ideal para el ajuste fino y el renderizado de texto ultradenso en resolución 2K.
  * **Boogu-Image-0.1-Edit** : una variante ajustada para tareas de edición y transformación de imágenes con control guiado por instrucciones.

**Aspectos destacados del modelo** :

  * **10B de parámetros** con una inferencia eficiente en GPUs de consumo
  * **Licencia Apache-2.0** para uso libre y desarrollo derivado
  * **Renderizado de texto bilingüe** (chino e inglés) con tipografía confiable
  * **Capacidades versátiles** : fotografía realista, estilización, diseño de pósteres y renderizado de texto preciso

**Enlaces relacionados** :

  * [Página del proyecto](https://boogu.org/)
  * [GitHub](https://github.com/boogu-project/Boogu-Image)
  * [Hugging Face (ComfyUI)](https://huggingface.co/Comfy-Org/Boogu-Image)
  * [Hugging Face (Turbo)](https://huggingface.co/Boogu/Boogu-Image-0.1-Turbo-fp8)
  * [Hugging Face (Edit)](https://huggingface.co/Boogu/Boogu-Image-0.1-Edit-fp8)



## 

​

Flujo de trabajo de texto a imagen de Boogu-Image-0.1-Turbo

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

### 

​

Boogu Turbo: Text to Image

Genera imágenes de alta calidad a partir de prompts de texto con el modelo Boogu Turbo, un pipeline de texto a imagen destilado de 10B de parámetros que produce resultados fotorrealistas en solo 4 pasos. ![Vista previa del flujo de trabajo de texto a imagen de Boogu Turbo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_boogu_image_0_1_turbo_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Boogu Turbo” en la Biblioteca de plantillas

El flujo de trabajo de Boogu-Image-0.1-Turbo usa un subgrafo que encapsula el pipeline de difusión, de codificación de texto y de decodificación del VAE. Tú proporcionas un prompt de texto y los ajustes de resolución, y el subgrafo se encarga del resto.

### 

​

Descargas de modelos de Boogu-Image-0.1-Turbo

## boogu_image_turbo_fp8_scaled.safetensors

Modelo de difusión para Boogu-Image-0.1-Turbo.

## qwen3vl_8b_fp8_scaled.safetensors

Codificador de texto para Boogu-Image-0.1-Turbo.

## ae.safetensors

VAE para Boogu-Image-0.1-Turbo.

## boogu_image_turbo_lora_rank_128_bf16.safetensors

Módulo LoRA (rank-128) para Boogu-Image-0.1-Turbo.

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── boogu_image_turbo_fp8_scaled.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_8b_fp8_scaled.safetensors
    │   ├── 📂 vae/
    │   │   └── ae.safetensors
    │   └── 📂 loras/
    │       └── boogu_image_turbo_lora_rank_128_bf16.safetensors
    

## 

​

Flujo de trabajo de edición de imágenes de Boogu-Image-0.1-Edit

### 

​

Boogu image 0.1 Edit

Edita imágenes con el modelo guiado por instrucciones de Boogu: toma una imagen de entrada y genera una salida editada junto con una vista de comparación lado a lado. ![Vista previa del flujo de trabajo de Boogu image 0.1 Edit](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_boogu_image_0_1_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Boogu image 0.1 Edit” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## tech_cowboy.png

Nodo `LoadImage` 32 · `tech_cowboy.png`

![tech_cowboy.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/tech_cowboy.png)

### 

​

Descargas de modelos de Boogu-Image-0.1-Edit

## boogu_image_edit_fp8_scaled.safetensors

Modelo de difusión para Boogu-Image-0.1-Edit.

## qwen3vl_8b_fp8_scaled.safetensors

Codificador de texto para Boogu-Image-0.1-Edit.

## ae.safetensors

VAE para Boogu-Image-0.1-Edit.

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── boogu_image_edit_fp8_scaled.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── qwen3vl_8b_fp8_scaled.safetensors
    │   └── 📂 vae/
    │       └── ae.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/boogu/boogu-image-0.1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/boogu/boogu-image-0.1)

[Z-Image-Turbo](https://docs.comfy.org/es/tutorials/image/z-image/z-image-turbo)[HiDream-I1](https://docs.comfy.org/es/tutorials/image/hidream/hidream-i1)
