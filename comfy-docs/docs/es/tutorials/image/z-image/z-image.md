---
url: https://docs.comfy.org/es/tutorials/image/z-image/z-image/
title: Ejemplo de flujo de trabajo de ComfyUI con Z-Image - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:45.475535+00:00
---

# Ejemplo de flujo de trabajo de ComfyUI con Z-Image - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/z-image/z-image/

## En esta página

Volver arriba

  * Flujo de trabajo de texto a imagen con Z-Image
    * Z-Image: Texto a imagen
  * Descargas de modelos de Z-Image



Z-Image

# Ejemplo de flujo de trabajo de ComfyUI con Z-Image

Copiar páginaCopiar página

Z-Image es un modelo base de generación de imágenes eficiente de 6B de Alibaba Tongyi Lab. Su DiT de flujo único busca ajuste fino y desarrollo personalizado.

Copiar páginaCopiar página

**Z-Image (造相)** es un modelo de generación de imágenes potente y altamente eficiente con **6B** parámetros, desarrollado por Tongyi Lab de Alibaba. Utiliza una arquitectura **Scalable Single-Stream DiT** (S3-DiT), en la que los tokens de texto, los tokens semánticos visuales y los tokens VAE de imagen se concatenan a nivel de secuencia para formar un flujo de entrada unificado, lo que maximiza la eficiencia de los parámetros. Z-Image (Base) es el modelo base no destilado diseñado para el ajuste fino impulsado por la comunidad y el desarrollo personalizado. **Puntos destacados del modelo** :

  * **Calidad fotorrealista** : ofrece una potente generación de imágenes fotorrealistas y mantiene una excelente calidad estética.
  * **Renderizado de texto bilingüe preciso** : destaca por renderizar con precisión texto complejo en chino e inglés.
  * **Mejora de prompt y razonamiento** : Prompt Enhancer dota al modelo de capacidades de razonamiento.
  * **Listo para ajuste fino** : modelo base ideal para entrenamiento personalizado y adaptación.

**Enlaces relacionados** :

  * [GitHub](https://github.com/Tongyi-MAI/Z-Image)
  * [Hugging Face](https://huggingface.co/Tongyi-MAI/Z-Image)
  * [ModelScope](https://modelscope.cn/models/Tongyi-MAI/Z-Image)



## 

​

Flujo de trabajo de texto a imagen con Z-Image

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

Z-Image: Texto a imagen

La base para la libertad creativa. Estética diversa con una calidad fotorrealista excepcional; ideal para fine-tuning; responde a los prompts negativos; alta diversidad de generación. ![Vista previa del flujo de trabajo de texto a imagen con Z-Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo directamente en Comfy Cloud

## Descargar flujo de trabajo

Descarga el archivo JSON del flujo de trabajo de texto a imagen con Z-Image

**Salida de ejemplo** ![Salida de ejemplo de Z-Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_z_image.png)

## 

​

Descargas de modelos de Z-Image

## qwen_3_4b.safetensors

Codificador de texto para Z-Image.

## z_image_bf16.safetensors

Modelo de difusión para Z-Image.

## ae.safetensors

VAE para Z-Image.

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_3_4b.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── z_image_bf16.safetensors
    │   └── 📂 vae/
    │          └── ae.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/z-image/z-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/z-image/z-image)

[Qwen-Image-Layered](https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-layered)[Z-Image-Turbo](https://docs.comfy.org/es/tutorials/image/z-image/z-image-turbo)
