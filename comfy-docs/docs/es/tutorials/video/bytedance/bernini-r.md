---
url: https://docs.comfy.org/es/tutorials/video/bytedance/bernini-r/
title: Bernini-R en ComfyUI: edici\u00f3n de im\u00e1genes y video en contexto - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:58.792385+00:00
---

# Bernini-R en ComfyUI: edición de imágenes y video en contexto - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/bytedance/bernini-r/

## En esta página

Volver arriba

  * Introducción a ComfyUI Bernini-R
  * Instalación de modelos
  * Flujos de trabajo de ejemplo
  * 1\. Edición de imagen
    * Pasos para ejecutar
  * 2\. Edición de video
    * Pasos para ejecutar
  * Recursos de la comunidad



ByteDance

# Bernini-R en ComfyUI: edición de imágenes y video en contexto

Copiar páginaCopiar página

Edita imágenes y video en ComfyUI con ByteDance Bernini-R, un modelo Wan 2.2 solo de renderizado que usa imágenes o video de referencia sin entrenamiento LoRA.

Copiar páginaCopiar página

# 

​

Introducción a ComfyUI Bernini-R

[Bernini-R](https://github.com/bytedance/Bernini) es el modelo Wan 2.2 **solo de renderizado** de ByteDance para el conditioning de imágenes y video en contexto. Utiliza un conjunto de flujos de conditioning (video fuente, imágenes de referencia, video de referencia) para guiar la generación. No requiere entrenamiento de LoRA ni ajuste fino. Capacidades principales:

  * **Varios tipos de tarea en un solo modelo** : generación de imagen y video, edición, cambio de iluminación, cambio de estilo, inserción de sujetos
  * **Acondicionamiento en contexto** : las imágenes y videos de referencia actúan como prompts visuales, inyectados como tokens
  * **Ligero** : modelo solo de renderizado. Sin backbone de difusión de texto a video.
  * **Soporte flexible de entradas** : referencias de una o varias imágenes, video a video, edición guiada por referencia

Bernini-R admite estos tipos de tarea:

Tarea| Entradas| Descripción  
---|---|---  
**t2v**|  Prompt de texto| Generación de texto a video  
**v2v**|  Video fuente| Cambio de estilo de video a video  
**rv2v**|  Video fuente + imagen(es) de referencia| Edición de video guiada por referencia (cambio de iluminación, inserción de sujetos)  
**r2v**|  Solo imagen(es) de referencia| Generación de referencia a video  
**img**|  Imagen fuente + prompt de texto| Edición de imagen (cambio de iluminación, cambio de estilo, inserción de sujetos)  
**ads2v**|  Video fuente + video de referencia| Insertar contenido de imagen o video en el video fuente  
  
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

ComfyUI ahora admite de forma nativa los nodos de Bernini-R. Asegúrate de haber actualizado a la última versión de [ComfyUI](https://github.com/Comfy-Org/ComfyUI) antes de empezar.

## 

​

Instalación de modelos

Descarga los pesos de modelo necesarios y guárdalos en las carpetas correspondientes de ComfyUI: **text_encoders:**

  * [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true)

**vae:**

  * [Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_bf16.safetensors?download=true)

**loras:**

  * [lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors?download=true)

**diffusion_models:**

  * [wan2.2_bernini_r_fp16.safetensors](https://huggingface.co/Comfy-Org/Bernini-R/blob/main/wan2.2_bernini_r_fp16.safetensors)


    
    
    ComfyUI/
    ├── models/
    │   ├── text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── vae/
    │   │   └── Wan2_1_VAE_bf16.safetensors
    │   ├── loras/
    │   │   └── lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors
    │   ├── diffusion_models/
    │   │   └── wan2.2_bernini_r_fp16.safetensors
    

## 

​

Flujos de trabajo de ejemplo

* * *

## 

​

1\. Edición de imagen

**Qué hace:** genera una imagen editada con iluminación coincidente y consulta una comparación en paralelo de antes y después. Es ideal para cambiar la iluminación de retratos y productos, mantener una iluminación coherente en conjuntos de fotos y para fotografía de catálogo de comercio electrónico. ![Vista previa del flujo de trabajo de edición de imagen con Bernini-R](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_bernini_r_image_editing-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bernini-R” en la biblioteca de plantillas

**Materiales de entrada**

## Imagen de entrada

Descarga la imagen de entrada predeterminada o usa la tuya.

## Imagen de referencia

Descarga la imagen de referencia predeterminada o usa la tuya.

### 

​

Pasos para ejecutar

  1. **Selecciona el tipo de tarea** : elige tu tarea (Image Editing, Subject to Image, etc.)
  2. **Conecta las entradas** : carga la imagen de origen y las imágenes de referencia opcionales
  3. **Escribe el prompt** : describe la edición que deseas
  4. **Ejecuta** : haz clic en Queue o usa `Cmd+Enter`

**Entrada de imagen de referencia:** úsala para **Subject to Image** cuando necesites una o más imágenes de referencia (sujeto, vestuario, escena, accesorios). En el prompt, usa `image0`, `image1`, … para hacer referencia a cada imagen. No es necesaria para **Image Editing** : esa tarea usa `source_image` en su lugar.

## Acerca de Subgraph

Este flujo de trabajo usa nodos Subgraph para el procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y extender el flujo de trabajo.

* * *

## 

​

2\. Edición de video

**Qué hace:** Genera un video editado con una nueva iluminación consistente usando Bernini-R. Conecta un video de origen, una o varias imágenes de referencia opcionales o un video de referencia, elige el tipo de tarea, escribe un prompt y ejecuta. ![Vista previa del flujo de trabajo de edición de video con Bernini-R](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_bernini_r_video_editing-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Bernini-R” en Biblioteca de plantillas

**Materiales de entrada**

## Video de entrada

Descarga el video de entrada predeterminado o usa el tuyo.

## Imagen de referencia

Descarga la imagen de referencia predeterminada o usa la tuya.

### 

​

Pasos para ejecutar

  1. **Carga el video de origen** : conecta tu video de entrada
  2. **(Opcional) Carga las referencias** : una o varias imágenes de referencia o un video de referencia
  3. **Selecciona el tipo de tarea** : v2v, rv2v, r2v o ads2v
  4. **Escribe el prompt** : describe la edición que quieres
  5. **Ejecuta** : haz clic en Queue o usa `Cmd+Enter`

**Entrada de imagen de referencia:** úsala cuando una tarea necesite una o más imágenes de referencia (rv2v, r2v, conjuntos de varias prendas). Cada imagen del lote se convierte en su propio token en contexto. Menciona `image0`, `image1`, … en el prompt si las referencias cumplen funciones distintas.

## Acerca de Subgraph

Este flujo de trabajo usa nodos Subgraph para un procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y ampliar el flujo de trabajo.

* * *

## 

​

Recursos de la comunidad

  * [Bernini GitHub (bytedance/Bernini)](https://github.com/bytedance/Bernini): Documentación del artículo de investigación y de las tareas
  * [Comfy-Org/Bernini-R](https://huggingface.co/Comfy-Org/Bernini-R): Pesos oficiales del modelo para ComfyUI
  * [Bernini: Latent Semantic Planning for Video Diffusion](https://arxiv.org/abs/2605.22344): Artículo de investigación



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/bytedance/bernini-r.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/bytedance/bernini-r)

[Wan2.1 FLF2V](https://docs.comfy.org/es/tutorials/video/wan/wan-flf)[Hunyuan Video](https://docs.comfy.org/es/tutorials/video/hunyuan/hunyuan-video)
