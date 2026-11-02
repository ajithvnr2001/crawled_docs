---
url: https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-edit-2511/
title: Qwen-Image-Edit-2511 en ComfyUI: edici\u00f3n de im\u00e1genes coherente - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:34.859819+00:00
---

# Qwen-Image-Edit-2511 en ComfyUI: edición de imágenes coherente - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-edit-2511/

## En esta página

Volver arriba

  * Ejemplo de flujo de trabajo nativo de ComfyUI para Qwen-Image-Edit-2511
    * Qwen Image Edit 2511: reemplazo de materiales
    * 1\. Archivo del flujo de trabajo
    * 2\. Descarga del modelo



Qwen

# Qwen-Image-Edit-2511 en ComfyUI: edición de imágenes coherente

Copiar páginaCopiar página

Edita imágenes con Qwen-Image-Edit-2511 en ComfyUI: mayor coherencia de personajes y de varias personas, LoRA integradas y sustitución de materiales.

Copiar páginaCopiar página

**Qwen-Image-Edit-2511** es una versión mejorada de Qwen-Image-Edit-2509 que incluye varias mejoras, entre ellas una consistencia notablemente mejor. Este modelo extiende las capacidades únicas de renderizado de texto de Qwen-Image a las tareas de edición, lo que permite una edición precisa del texto junto con capacidades de edición semántica y de apariencia. **Mejoras clave en Qwen-Image-Edit-2511** :

  * **Reducción de la deriva de imagen** : mayor estabilidad durante las operaciones de edición
  * **Mejor consistencia de personajes** : mejor conservación de la identidad y de las características visuales durante las ediciones creativas
  * **Consistencia entre varias personas** : fusión de alta fidelidad de varias imágenes de personas en tomas grupales coherentes
  * **Capacidades de LoRA integradas** : LoRAs populares de la comunidad incorporadas directamente en el modelo base
  * **Mejor generación de diseño industrial** : mejor soporte para el diseño por lotes de productos industriales y el reemplazo de materiales
  * **Razonamiento geométrico reforzado** : generación directa de líneas auxiliares de construcción para diseño o anotación

**Enlaces oficiales** :

  * [Repositorio de GitHub](https://github.com/QwenLM/Qwen-Image)
  * [Hugging Face](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)
  * [ModelScope](https://modelscope.cn/models/Qwen/Qwen-Image-Edit-2511)
  * [Informe técnico](https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen-Image/Qwen_Image.pdf)
  * [Blog](https://qwen.ai/blog?id=qwen-image-edit-2511)



## 

​

Ejemplo de flujo de trabajo nativo de ComfyUI para Qwen-Image-Edit-2511

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

Qwen Image Edit 2511: reemplazo de materiales

Reemplaza los materiales de objetos (por ejemplo, muebles) combinando imágenes de referencia con Qwen-Image-Edit-2511. ![Vista previa del flujo de trabajo de Qwen-Image-Edit-2511](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit_2511-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Qwen-Image-Edit-2511” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` correspondientes:

## leather_sofa.png

Nodo `LoadImage` 41 · `leather_sofa.png`

## texture_fur.png

Nodo `LoadImage` 83 · `texture_fur.png`

![leather_sofa.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/leather_sofa.png)![texture_fur.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/texture_fur.png)

**Ejemplo de salida**

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/leather_sofa.png)![Ejemplo de salida de Qwen-Image-Edit-2511](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_qwen_image_edit_2511.png)

### 

​

1\. Archivo del flujo de trabajo

Después de actualizar ComfyUI, puedes encontrar el archivo del flujo de trabajo en las plantillas, o arrastrar la vista previa del flujo de trabajo de arriba a ComfyUI para cargarlo.

### 

​

2\. Descarga del modelo

**Codificadores de texto**

  * [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)

**LoRA (opcional, para la aceleración Lightning de 4 pasos)**

  * [Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/blob/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors)

**Modelos de difusión**

  * [qwen_image_edit_2511_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors)

**VAE**

  * [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors)

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   ├── 📂 loras/
    │   │      └── Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── qwen_image_edit_2511_bf16.safetensors
    │   └── 📂 vae/
    │          └── qwen_image_vae.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/qwen/qwen-image-edit-2511.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/qwen/qwen-image-edit-2511)

[Qwen-Image-Edit](https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-edit)[Qwen-Image-Layered](https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-layered)
