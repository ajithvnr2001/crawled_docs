---
url: https://docs.comfy.org/es/tutorials/video/hunyuan/hunyuan-video-1-5/
title: HunyuanVideo 1.5 en ComfyUI: T2V e I2V en GPUs de consumo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:58.709640+00:00
---

# HunyuanVideo 1.5 en ComfyUI: T2V e I2V en GPUs de consumo - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/hunyuan/hunyuan-video-1-5/

## En esta página

Volver arriba

  * Aspectos destacados del modelo
  * Modelos comunes para todos los flujos de trabajo
    * Almacenamiento
  * Flujo de trabajo de texto a video de Hunyuan Video 1.5
    * Descargas de modelos
    * Almacenamiento de modelos
    * Pasos para ejecutar el flujo de trabajo
  * Flujo de trabajo de imagen a video con Hunyuan Video 1.5
    * Descargas de modelos
    * Almacenamiento de modelos
    * Pasos para ejecutar el flujo de trabajo
  * Ampliador de superresolución



Hunyuan

# HunyuanVideo 1.5 en ComfyUI: T2V e I2V en GPUs de consumo

Copiar páginaCopiar página

Ejecuta HunyuanVideo 1.5 en ComfyUI con una GPU de 24 GB: texto a video e imagen a video de 8.3B en 720p, más un upscaler de superresolución para 1080p.

Copiar páginaCopiar página

[HunyuanVideo 1.5](https://github.com/Tencent/HunyuanVideo) es un modelo ligero de 8.3B parámetros desarrollado por el equipo Hunyuan de Tencent. Ofrece generación de video con calidad de primer nivel en GPUs de consumo (24 GB de VRAM), lo que reduce enormemente la barrera de entrada sin sacrificar la calidad.

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

Aspectos destacados del modelo

  * **Potencia compacta** : Ofrece un rendimiento SOTA comparable al de modelos más grandes mientras se ejecuta en hardware de consumo.
  * **Generación versátil** : Admite generación de texto a video e imagen a video (5-10s) de alta calidad con una consistencia excepcional.
  * **Control preciso** : Sigue instrucciones con solidez para movimientos de cámara, física y expresiones emocionales.
  * **Calidad cinematográfica** : Salida nativa en 720p (ampliable a 1080p) con una estética profesional.
  * **Funciones completas** : Admite diversos estilos (realista, anime, 3D) y renderizado de texto en el video (chino/inglés).



## 

​

Modelos comunes para todos los flujos de trabajo

Los siguientes modelos se usan tanto en los flujos de trabajo de texto a video como en los de imagen a video. Descárgalos y guárdalos en los directorios indicados:

## Descargar Qwen2.5 VL 7B

qwen_2.5_vl_7b_fp8_scaled.safetensors — guárdalo en `ComfyUI/models/text_encoders/`

## Descargar ByT5 Small

byt5_small_glyphxl_fp16.safetensors — guárdalo en `ComfyUI/models/text_encoders/`

## Descargar el VAE de HunyuanVideo 1.5

hunyuanvideo15_vae_fp16.safetensors — guárdalo en `ComfyUI/models/vae/`

#### 

​

Almacenamiento
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │   ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   │   └── byt5_small_glyphxl_fp16.safetensors
    │   └── 📂 vae/
    │       └── hunyuanvideo15_vae_fp16.safetensors
    

## 

​

Flujo de trabajo de texto a video de Hunyuan Video 1.5

HunyuanVideo 1.5 Text-to-Video genera videos de 5 a 10 segundos a partir de descripciones en lenguaje natural, con mejor calidad y menores requisitos de VRAM. ![Flujo de trabajo de ComfyUI - Hunyuan Video 1.5 T2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_hunyuan_video_1.5_720p_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Hunyuan Video 1.5 T2V” en la Biblioteca de plantillas

### 

​

Descargas de modelos

## Descargar modelo de difusión T2V

hunyuanvideo1.5_720p_t2v_fp16.safetensors: guárdalo en `ComfyUI/models/diffusion_models/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │   ├── qwen_2.5_vl_7b_fp8_scaled.safetensors       // Modelo compartido
    │   │   └── byt5_small_glyphxl_fp16.safetensors           // Modelo compartido
    │   ├── 📂 vae/
    │   │   └── hunyuanvideo15_vae_fp16.safetensors           // Modelo compartido
    │   └── 📂 diffusion_models/
    │       └── hunyuanvideo1.5_720p_t2v_fp16.safetensors     // Modelo T2V
    

### 

​

Pasos para ejecutar el flujo de trabajo

  1. Asegúrate de que el nodo `DualCLIPLoader` tenga cargados estos modelos: 
     * clip_name1: `qwen_2.5_vl_7b_fp8_scaled.safetensors`
     * clip_name2: `byt5_small_glyphxl_fp16.safetensors`
  2. Asegúrate de que el nodo `Load Diffusion Model` tenga cargado `hunyuanvideo1.5_720p_t2v_fp16.safetensors`
  3. Asegúrate de que el nodo `Load VAE` tenga cargado `hunyuanvideo15_vae_fp16.safetensors`
  4. Haz clic en el botón `Queue` o usa el atajo `Ctrl(Cmd) + Enter` para ejecutar el flujo de trabajo



El flujo de trabajo incluye un nodo de superresolución. Cuando está habilitado, usa `hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors` para aumentar la resolución de la salida a 1080p.

## 

​

Flujo de trabajo de imagen a video con Hunyuan Video 1.5

HunyuanVideo 1.5 imagen a video transforma imágenes estáticas en videos suaves y de alta calidad, con mejor consistencia y dinámica de movimiento. ![Flujo de trabajo de ComfyUI - Hunyuan Video 1.5 I2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_hunyuan_video_1.5_720p_i2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Hunyuan Video 1.5 I2V” en la Biblioteca de plantillas

**Materiales de entrada**

## Imagen de entrada

Descarga la imagen de entrada predeterminada o usa tu propia imagen como fotograma inicial.

### 

​

Descargas de modelos

## Descargar CLIP Vision

sigclip_vision_patch14_384.safetensors: guardar en `ComfyUI/models/clip_vision/`

## Descargar modelo de difusión I2V

hunyuanvideo1.5_720p_i2v_fp16.safetensors: guardar en `ComfyUI/models/diffusion_models/`

#### 

​

Almacenamiento de modelos
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 clip_vision/
    │   │   └── sigclip_vision_patch14_384.safetensors          // Codificador de visión I2V
    │   ├── 📂 text_encoders/
    │   │   ├── qwen_2.5_vl_7b_fp8_scaled.safetensors           // Modelo compartido
    │   │   └── byt5_small_glyphxl_fp16.safetensors             // Modelo compartido
    │   ├── 📂 vae/
    │   │   └── hunyuanvideo15_vae_fp16.safetensors             // Modelo compartido
    │   └── 📂 diffusion_models/
    │       └── hunyuanvideo1.5_720p_i2v_fp16.safetensors       // Modelo I2V
    

### 

​

Pasos para ejecutar el flujo de trabajo

  1. Asegúrate de que el nodo `DualCLIPLoader` haya cargado estos modelos: 
     * clip_name1: `qwen_2.5_vl_7b_fp8_scaled.safetensors`
     * clip_name2: `byt5_small_glyphxl_fp16.safetensors`
  2. Asegúrate de que el nodo `CLIPVisionLoader` haya cargado `sigclip_vision_patch14_384.safetensors`
  3. Asegúrate de que el nodo `Load Diffusion Model` haya cargado `hunyuanvideo1.5_720p_i2v_fp16.safetensors`
  4. Asegúrate de que el nodo `Load VAE` haya cargado `hunyuanvideo15_vae_fp16.safetensors`
  5. Haz clic en el botón `Queue` o usa el atajo `Ctrl(Cmd) + Enter` para ejecutar el flujo de trabajo



## 

​

Ampliador de superresolución

Ambos flujos de trabajo incluyen un nodo de superresolución que puede hacer upscale del video de salida de 720p a 1080p. Este ampliador opcional usa un modelo destilado para obtener una salida de alta resolución de forma eficiente.

## Descargar el ampliador a 1080p

hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors — guárdalo en `ComfyUI/models/diffusion_models/`

Todos los modelos compartidos y específicos de cada flujo de trabajo, en conjunto:
    
    
    ComfyUI/
    ├── 📂 models/
    │   ├── 📂 clip_vision/
    │   │   └── sigclip_vision_patch14_384.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
    │   │   └── byt5_small_glyphxl_fp16.safetensors
    │   ├── 📂 vae/
    │   │   └── hunyuanvideo15_vae_fp16.safetensors
    │   └── 📂 diffusion_models/
    │       ├── hunyuanvideo1.5_720p_t2v_fp16.safetensors        // T2V model
    │       ├── hunyuanvideo1.5_720p_i2v_fp16.safetensors        // I2V model
    │       └── hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors  // Upscaler
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/hunyuan/hunyuan-video-1-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/hunyuan/hunyuan-video-1-5)

[Hunyuan Video](https://docs.comfy.org/es/tutorials/video/hunyuan/hunyuan-video)[Cosmos-Predict2](https://docs.comfy.org/es/tutorials/video/cosmos/cosmos-predict2-video2world)
