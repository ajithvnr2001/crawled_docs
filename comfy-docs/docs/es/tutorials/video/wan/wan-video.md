---
url: https://docs.comfy.org/es/tutorials/video/wan/wan-video/
title: Wan2.1 en ComfyUI: flujos de trabajo de texto a video e imagen a video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:01.778359+00:00
---

# Wan2.1 en ComfyUI: flujos de trabajo de texto a video e imagen a video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/wan-video/

## En esta página

Volver arriba

  * Ejemplos de flujos de trabajo nativos de Wan2.1 en ComfyUI
  * Instalación de modelos
  * Flujo de trabajo de texto a video Wan2.1 (1.3B)
    * Wan 2.1 de texto a video
    * Descargas de modelos
    * Pasos para ejecutar
  * Flujo de trabajo de imagen a video con Wan2.1 (14B)
    * Versión 480P
    * Wan 2.1 imagen a video
    * Descargas de modelos
    * Pasos para ejecutar
    * Versión 720P
    * Descargas de modelos
    * Pasos para ejecutar



Wan2.1

# Wan2.1 en ComfyUI: flujos de trabajo de texto a video e imagen a video

Copiar páginaCopiar página

Ejecuta el modelo texto a video 1.3B y el imagen a video 14B, con instalación de archivos de modelo y los flujos de trabajo nativos de ComfyUI.

Copiar páginaCopiar página

Wan2.1 Video series es una serie de modelos de generación de video de código abierto publicada por Alibaba en febrero de 2025 bajo la [licencia Apache 2.0](https://github.com/Wan-Video/Wan2.1?tab=Apache-2.0-1-ov-file). Ofrece dos versiones:

  * 14B (14 mil millones de parámetros)
  * 1.3B (1.3 mil millones de parámetros) Cubre varias tareas, incluidas texto a video (T2V) e imagen a video (I2V). El modelo no solo supera en rendimiento a los modelos de código abierto existentes, sino que, más importante aún, su versión ligera solo necesita 8GB de VRAM para ejecutarse, lo que reduce significativamente la barrera de entrada.



  * [Repositorio de código de Wan2.1](https://github.com/Wan-Video/Wan2.1)
  * [Repositorio de modelos de Wan2.1](https://huggingface.co/Wan-AI)



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

Ejemplos de flujos de trabajo nativos de Wan2.1 en ComfyUI

Actualiza ComfyUI a la última versión antes de comenzar con los ejemplos para asegurarte de tener soporte nativo para Wan Video.

## 

​

Instalación de modelos

Todos los modelos mencionados en esta guía los puedes encontrar [aquí](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files). Abajo tienes los modelos comunes que necesitarás para los ejemplos de esta guía, y que puedes descargar con anticipación: Elige una versión de **Codificadores de texto** para descargar:

## umt5_xxl_fp16.safetensors

Codificador de texto con precisión FP16. Colócalo en `ComfyUI/models/text_encoders/`

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

Codificador de texto escalado FP8. Colócalo en `ComfyUI/models/text_encoders/`

**VAE**

## wan_2.1_vae.safetensors

Modelo VAE de Wan2.1. Colócalo en `ComfyUI/models/vae/`

**CLIP Vision**

## clip_vision_h.safetensors

Modelo CLIP Vision para el acondicionamiento de imágenes. Colócalo en `ComfyUI/models/clip_vision/`

Ubicaciones de almacenamiento de archivos:
    
    
    ComfyUI/
    ├── models/
    │   ├── diffusion_models/
    │   │   └── ... (download per workflow below)
    │   ├── text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── vae/
    │   │   └── wan_2.1_vae.safetensors
    │   └── clip_vision/
    │       └── clip_vision_h.safetensors
    

Para los modelos diffusion, en esta guía usaremos los modelos con precisión fp16 porque hemos comprobado que funcionan mejor que las versiones bf16. Si necesitas otras versiones de precisión, visita [aquí](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models) para descargarlas.

## 

​

Flujo de trabajo de texto a video Wan2.1 (1.3B)

### 

​

Wan 2.1 de texto a video

Genera videos a partir de prompts de texto con Wan 2.1. ![Vista previa del flujo de trabajo de texto a video de Wan 2.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/text_to_video_wan-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan 2.1 Text to Video” en la Biblioteca de plantillas

### 

​

Descargas de modelos

## wan2.1_t2v_1.3B_fp16.safetensors

Modelo de difusión para Wan2.1 de texto a video. Colócalo en `ComfyUI/models/diffusion_models/`

> Si necesitas otras versiones de precisión de t2v, visita [este enlace](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/diffusion_models) para descargarlas.

### 

​

Pasos para ejecutar

![Pasos del flujo de trabajo de Wan2.1 en ComfyUI](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_t2v_1.3b_flow_diagram.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=db6d32906ab2db132e6b92fdb0823419)

  1. Asegúrate de que el nodo `Load Diffusion Model` tenga cargado el modelo `wan2.1_t2v_1.3B_fp16.safetensors`
  2. Asegúrate de que el nodo `Load CLIP` tenga cargado el modelo `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Asegúrate de que el nodo `Load VAE` tenga cargado el modelo `wan_2.1_vae.safetensors`
  4. (Opcional) Puedes modificar las dimensiones del video en el nodo `EmptyHunyuanLatentVideo` si es necesario
  5. (Opcional) Si necesitas modificar los prompts (positivo y negativo), haz los cambios en el nodo `CLIP Text Encoder` en el número `5`
  6. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación del video



## 

​

Flujo de trabajo de imagen a video con Wan2.1 (14B)

**Como Wan Video separa los modelos de 480P y 720P** , en esta guía debemos incluir ejemplos para ambas resoluciones. Además de usar modelos distintos, también tienen ligeras diferencias en los parámetros.

### 

​

Versión 480P

### 

​

Wan 2.1 imagen a video

Genera videos a partir de imágenes con Wan 2.1. ![Vista previa del flujo de trabajo Wan 2.1 imagen a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_to_video_wan-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan 2.1 Image to Video” en la biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## image_to_video_wan_start_image.png

Nodo `LoadImage` 52 · `image_to_video_wan_start_image.png`

![image_to_video_wan_start_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/image_to_video_wan_start_image.png)

#### 

​

Descargas de modelos

## wan2.1_i2v_480p_14B_fp16.safetensors

Modelo de difusión para Wan2.1 I2V 480P. Colócalo en `ComfyUI/models/diffusion_models/`

#### 

​

Pasos para ejecutar

![Pasos del flujo de trabajo de Wan2.1 en ComfyUI](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_480p_flow_diagram.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=91de28e61a2633cf39b3a52afc2a6459)

  1. Asegúrate de que el nodo `Load Diffusion Model` tenga cargado el modelo `wan2.1_i2v_480p_14B_fp16.safetensors`
  2. Asegúrate de que el nodo `Load CLIP` tenga cargado el modelo `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Asegúrate de que el nodo `Load VAE` tenga cargado el modelo `wan_2.1_vae.safetensors`
  4. Asegúrate de que el nodo `Load CLIP Vision` tenga cargado el modelo `clip_vision_h.safetensors`
  5. Sube la imagen de entrada proporcionada en el nodo `Load Image`
  6. (Opcional) Introduce la descripción del video que quieres generar en el nodo `CLIP Text Encoder`
  7. (Opcional) Puedes modificar las dimensiones del video en el nodo `WanImageToVideo` si es necesario
  8. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación del video



### 

​

Versión 720P

![Flujo de trabajo Wan2.1 imagen a video 14B 720P](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/wan2.1/wan2.1_i2v_14b_720P.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga la imagen del flujo de trabajo y arrástrala a ComfyUI para cargar el flujo de trabajo

## Imagen de entrada

Descarga la imagen de entrada predeterminada o usa tu propia imagen.

#### 

​

Descargas de modelos

## wan2.1_i2v_720p_14B_fp16.safetensors

Modelo de difusión para Wan2.1 I2V 720P. Colócalo en `ComfyUI/models/diffusion_models/`

#### 

​

Pasos para ejecutar

![Pasos del flujo de trabajo de Wan2.1 en ComfyUI](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2.1_i2v_14b_720p_flow_diagram.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=c99af487f3164515ac1ffaf94f0add71)

  1. Asegúrate de que el nodo `Load Diffusion Model` tenga cargado el modelo `wan2.1_i2v_720p_14B_fp16.safetensors`
  2. Asegúrate de que el nodo `Load CLIP` tenga cargado el modelo `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Asegúrate de que el nodo `Load VAE` tenga cargado el modelo `wan_2.1_vae.safetensors`
  4. Asegúrate de que el nodo `Load CLIP Vision` tenga cargado el modelo `clip_vision_h.safetensors`
  5. Sube la imagen de entrada proporcionada en el nodo `Load Image`
  6. (Opcional) Introduce la descripción del video que quieres generar en el nodo `CLIP Text Encoder`
  7. (Opcional) Puedes modificar las dimensiones del video en el nodo `WanImageToVideo` si es necesario
  8. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación del video



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/wan-video.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/wan-video)

[Wan2.2 Fun Camera](https://docs.comfy.org/es/tutorials/video/wan/wan2-2-fun-camera)[InfiniteTalk](https://docs.comfy.org/es/tutorials/video/wan/wan-infinitetalk)
