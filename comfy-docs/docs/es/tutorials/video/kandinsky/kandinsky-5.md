---
url: https://docs.comfy.org/es/tutorials/video/kandinsky/kandinsky-5/
title: Kandinsky 5.0 en ComfyUI: texto a video e imagen a video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:59.187247+00:00
---

# Kandinsky 5.0 en ComfyUI: texto a video e imagen a video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/kandinsky/kandinsky-5/

## En esta página

Volver arriba

  * Descripción general
  * Variantes del modelo
  * Flujo de trabajo de texto a video
    * Kandinsky 5.0 Video Lite Text to Video
    * 2\. Descargar los modelos manualmente
  * Flujo de trabajo de imagen a video
    * Kandinsky 5.0 Video Lite Image to Video
    * 2\. Descargar los modelos manualmente
  * Recursos



Kandinsky

# Kandinsky 5.0 en ComfyUI: texto a video e imagen a video

Copiar páginaCopiar página

Usa Kandinsky 5.0 Video Lite en ComfyUI: texto a video de hasta 10 segundos e imagen a video de 5 segundos, con variantes SFT de 2B, no-CFG y destilada.

Copiar páginaCopiar página

[Kandinsky 5.0](https://huggingface.co/kandinskylab/Kandinsky-5.0-I2V-Lite-5s) es una familia de modelos de difusión para la generación de video e imágenes desarrollada por [Kandinsky Lab](https://huggingface.co/kandinskylab). Kandinsky 5.0 T2V Lite es un modelo ligero de 2B parámetros que se ubica entre los mejores modelos de generación de video de código abierto, capaz de generar videos de hasta 10 segundos de duración.

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

Descripción general

Kandinsky 5.0 usa un pipeline de difusión latent con Flow Matching e incluye:

  * **Diffusion Transformer (DiT):** Arquitectura generativa principal con atención cruzada a los embeddings de texto
  * **Qwen2.5-VL y CLIP:** Proporciona embeddings de texto de alta calidad
  * **HunyuanVideo 3D VAE:** Codifica y decodifica el video en un espacio latent

La familia de modelos incluye varias variantes optimizadas para diferentes casos de uso:

  * **Modelo SFT:** Máxima calidad de generación
  * **CFG-distilled:** Inferencia 2× más rápida
  * **Diffusion-distilled:** 6× más rápida con una pérdida mínima de calidad (16 pasos)
  * **Modelo preentrenado:** Diseñado para fine-tuning

Todos los modelos están disponibles en versiones de generación de video de 5 y 10 segundos.

## 

​

Variantes del modelo

Modelo| Duración del video| NFE| Latencia (H100)  
---|---|---|---  
Kandinsky 5.0 T2V Lite SFT| 5s / 10s| 100| 139s / 224s  
Kandinsky 5.0 T2V Lite no-CFG| 5s / 10s| 50| 77s / 124s  
Kandinsky 5.0 T2V Lite distill| 5s / 10s| 16| 35s / 61s  
Kandinsky 5.0 I2V Lite| 5s| 100| 673s  
  
## 

​

Flujo de trabajo de texto a video

### 

​

Kandinsky 5.0 Video Lite Text to Video

Un modelo ligero de 2B que genera videos a partir de prompts en inglés y ruso con alta calidad visual. ![Vista previa del flujo de trabajo Kandinsky 5.0 Video Lite de texto a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_kandinsky5_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kandinsky 5.0 Video Lite Text to Video” en la Biblioteca de plantillas

### 

​

2\. Descargar los modelos manualmente

**Codificadores de texto**

## Text Encoder: qwen_2.5_vl_7b_fp8_scaled.safetensors

Codificador de texto Qwen2.5-VL 7B (FP8). Colócalo en `ComfyUI/models/text_encoders/`

## Text Encoder: clip_l.safetensors

Codificador de texto CLIP-L. Colócalo en `ComfyUI/models/text_encoders/`

**Modelo de difusión**

## Diffusion Model: kandinsky5lite_t2v_sft_5s.safetensors

Modelo de difusión Kandinsky 5.0 T2V Lite SFT (5 s). Colócalo en `ComfyUI/models/diffusion_models/`

**VAE**

## VAE: hunyuan_video_vae_bf16.safetensors

VAE 3D de HunyuanVideo. Colócalo en `ComfyUI/models/vae/`
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   │      └── clip_l.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── kandinsky5lite_t2v_sft_5s.safetensors
    │   └── 📂 vae/
    │          └── hunyuan_video_vae_bf16.safetensors
    

## 

​

Flujo de trabajo de imagen a video

### 

​

Kandinsky 5.0 Video Lite Image to Video

Un modelo ligero de 2B que genera videos a partir de prompts en inglés y ruso con alta calidad visual. ![Vista previa del flujo de trabajo Kandinsky 5.0 Video Lite de imagen a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_kandinsky5_i2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kandinsky 5.0 Video Lite Image to Video” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## crystal_flower.png

Nodo `LoadImage` 11 · `crystal_flower.png`

![crystal_flower.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/crystal_flower.png)

### 

​

2\. Descargar los modelos manualmente

**Codificadores de texto**

## Text Encoder: qwen_2.5_vl_7b_fp8_scaled.safetensors

Codificador de texto Qwen2.5-VL 7B (FP8). Colócalo en `ComfyUI/models/text_encoders/`

## Text Encoder: clip_l.safetensors

Codificador de texto CLIP-L. Colócalo en `ComfyUI/models/text_encoders/`

**Modelo de difusión**

## Diffusion Model: kandinsky5lite_i2v_5s.safetensors

Modelo de difusión Kandinsky 5.0 I2V Lite (5 s). Colócalo en `ComfyUI/models/diffusion_models/`

**VAE**

## VAE: hunyuan_video_vae_bf16.safetensors

VAE 3D de HunyuanVideo. Colócalo en `ComfyUI/models/vae/`
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   │      └── clip_l.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── kandinsky5lite_i2v_5s.safetensors
    │   └── 📂 vae/
    │          └── hunyuan_video_vae_bf16.safetensors
    

## 

​

Recursos

  * [Colección de modelos de Hugging Face](https://huggingface.co/collections/kandinskylab/kandinsky-50-video-lite)
  * [Repositorio de GitHub](https://github.com/ai-forever/Kandinsky-5)
  * [Integración con ComfyUI](https://github.com/ai-forever/Kandinsky-5/blob/main/comfyui/README.md)
  * [Página del proyecto](https://kandinskylab.github.io/kandinsky-5/)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/kandinsky/kandinsky-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/kandinsky/kandinsky-5)

[Cosmos-Predict2](https://docs.comfy.org/es/tutorials/video/cosmos/cosmos-predict2-video2world)[SCAIL-2](https://docs.comfy.org/es/tutorials/video/zai/scail2)
