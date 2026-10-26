---
url: https://docs.comfy.org/es/tutorials/image/z-image/z-image-turbo/
title: Ejemplo de flujo de trabajo de Z-Image-Turbo en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:45.185066+00:00
---

# Ejemplo de flujo de trabajo de Z-Image-Turbo en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/z-image/z-image-turbo/

## En esta página

Volver arriba

  * Flujo de trabajo de texto a imagen de Z-Image-Turbo
    * Z-Image-Turbo: Text to Image
    * Descargas de modelos de Z-Image-Turbo
  * Flujo de trabajo de ControlNet Fun Union de Z-Image-Turbo
    * Z-Image-Turbo Fun Union ControlNet
    * Modelo adicional para ControlNet



Z-Image

# Ejemplo de flujo de trabajo de Z-Image-Turbo en ComfyUI

Copiar páginaCopiar página

Z-Image-Turbo es un modelo destilado y eficiente de 6B parámetros con latencia de inferencia inferior a un segundo.

Copiar páginaCopiar página

**Z-Image (造相)** es un modelo de generación de imágenes potente y muy eficiente con **6B** parámetros, desarrollado por Tongyi Lab de Alibaba. Utiliza una arquitectura **Scalable Single-Stream DiT** (S3-DiT) en la que los tokens de texto, los tokens semánticos visuales y los tokens del VAE de imagen se concatenan a nivel de secuencia para formar un único flujo de entrada, maximizando la eficiencia de los parámetros. **Variantes del modelo** :

  * 🚀 **Z-Image-Turbo** : una versión destilada que iguala o supera a los principales competidores con solo **8 NFE** (Number of Function Evaluations). Ofrece una **latencia de inferencia inferior a un segundo** en GPUs H800 de clase empresarial y cabe en **dispositivos de consumo con 16 GB de VRAM**.
  * 🧱 **Z-Image-Base** : el modelo base sin destilar, pensado para el ajuste fino impulsado por la comunidad y el desarrollo personalizado.
  * ✍️ **Z-Image-Edit** : una variante ajustada para tareas de edición de imágenes, con una capacidad notable para seguir instrucciones.

**Aspectos destacados del modelo** :

  * **Calidad fotorrealista** : ofrece una sólida generación de imágenes fotorrealistas sin perder una excelente calidad estética
  * **Renderizado bilingüe preciso de texto** : sobresale al renderizar con precisión texto complejo en chino e inglés
  * **Mejora de prompts y razonamiento** : el Prompt Enhancer dota al modelo de capacidades de razonamiento
  * **Inferencia inferior a un segundo** : alcanza una velocidad de generación rápida en el hardware compatible

**Enlaces relacionados** :

  * [GitHub](https://github.com/Tongyi-MAI/Z-Image)
  * [Hugging Face](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)



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

Flujo de trabajo de texto a imagen de Z-Image-Turbo

### 

​

Z-Image-Turbo: Text to Image

Un modelo fundacional eficiente de generación de imágenes con Single-Stream Diffusion Transformer; admite inglés y chino. ![Vista previa del flujo de trabajo de texto a imagen de Z-Image-Turbo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image_turbo-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo directamente en Comfy Cloud

## Descargar flujo de trabajo

Descarga el archivo JSON del flujo de trabajo de texto a imagen de Z-Image-Turbo

**Ejemplo de salida** ![Ejemplo de salida de Z-Image-Turbo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_z_image_turbo.png)

### 

​

Descargas de modelos de Z-Image-Turbo

## qwen_3_4b.safetensors

Codificador de texto para Z-Image-Turbo.

## z_image_turbo_bf16.safetensors

Modelo de difusión para Z-Image-Turbo.

## ae.safetensors

VAE para Z-Image-Turbo.

**Ubicación de almacenamiento de los modelos de Z-Image-Turbo**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_3_4b.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── z_image_turbo_bf16.safetensors
    │   └── 📂 vae/
    │          └── ae.safetensors
    

## 

​

Flujo de trabajo de ControlNet Fun Union de Z-Image-Turbo

### 

​

Z-Image-Turbo Fun Union ControlNet

ControlNet multi-control compatible con Canny, HED, Depth, Pose y MLSD para Z-Image-Turbo. ![Vista previa del flujo de trabajo de ControlNet Fun Union de Z-Image-Turbo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image_turbo_fun_union_controlnet-1.webp)

## Ejecutar en Comfy Cloud

Ejecuta este flujo de trabajo directamente en Comfy Cloud

## Descargar flujo de trabajo

Descarga el archivo JSON del flujo de trabajo de ControlNet Fun Union de Z-Image-Turbo

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## image_z_image_turbo_fun_union_controlnet_input_image.png

Nodo `LoadImage` 58 · `image_z_image_turbo_fun_union_controlnet_input_image.png`

![image_z_image_turbo_fun_union_controlnet_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_z_image_turbo_fun_union_controlnet_input_image.png)

### 

​

Modelo adicional para ControlNet

## Z-Image-Turbo-Fun-Controlnet-Union.safetensors

Parche de modelo ControlNet para Z-Image-Turbo.

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── qwen_3_4b.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── z_image_turbo_bf16.safetensors
    │   ├── 📂 vae/
    │   │      └── ae.safetensors
    │   └── 📂 model_patches/
    │          └── Z-Image-Turbo-Fun-Controlnet-Union.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/z-image/z-image-turbo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/z-image/z-image-turbo)

[Z-Image](https://docs.comfy.org/es/tutorials/image/z-image/z-image)[Boogu-Image-0.1](https://docs.comfy.org/es/tutorials/image/boogu/boogu-image-0.1)
