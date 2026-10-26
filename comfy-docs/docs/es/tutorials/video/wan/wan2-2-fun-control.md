---
url: https://docs.comfy.org/es/tutorials/video/wan/wan2-2-fun-control/
title: Wan2.2 Fun Control en ComfyUI: generaci\u00f3n de video con control - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:01.620283+00:00
---

# Wan2.2 Fun Control en ComfyUI: generación de video con control - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/wan2-2-fun-control/

## En esta página

Volver arriba

  * Repetición de la transmisión en vivo de Wan2.2 Fun InP y Control de ComfyOrg en YouTube
  * Ejemplo de flujo de trabajo de generación de video con Wan2.2 Fun Control
    * 1\. Descarga el flujo de trabajo y los materiales
    * 2\. Modelos
    * 3\. Guía del flujo de trabajo
    * Notas adicionales



Wan Video

# Wan2.2 Fun Control en ComfyUI: generación de video con control

Copiar páginaCopiar página

Ejecuta el flujo de trabajo Wan2.2 Fun Control 14B en ComfyUI para generar video guiado por un video de control, con modelos de alto y bajo ruido y LoRAs de 4 pasos.

Copiar páginaCopiar página

**Wan2.2-Fun-Control** es un modelo de generación y control de video de nueva generación lanzado por el equipo de Alibaba PAI. Mediante un innovador mecanismo de Control Codes combinado con aprendizaje profundo y entradas condicionales multimodales, puede generar videos de alta calidad que cumplen con condiciones de control predefinidas. El modelo se publica bajo la **licencia Apache 2.0** y admite uso comercial. **Características principales** :

  * **Control multimodal** : admite varias condiciones de control, como **Canny (arte lineal)** , **Profundidad** , **OpenPose (pose humana)** , **MLSD (bordes geométricos)** y **control de trayectoria**
  * **Generación de video de alta calidad** : basado en la arquitectura Wan2.2, produce videos con calidad cinematográfica
  * **Compatibilidad con varios idiomas** : admite prompts en varios idiomas, incluidos el chino y el inglés

A continuación se muestran los pesos del modelo y los repositorios de código relevantes:

  * [🤗Wan2.2-Fun-A14B-Control](https://huggingface.co/alibaba-pai/Wan2.2-Fun-A14B-Control)
  * Repositorio de código: [VideoX-Fun](https://github.com/aigc-apps/VideoX-Fun)



## 

​

Repetición de la transmisión en vivo de Wan2.2 Fun InP y Control de ComfyOrg en YouTube

## 

​

Ejemplo de flujo de trabajo de generación de video con Wan2.2 Fun Control

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

Este flujo de trabajo ofrece dos versiones:

  1. Una versión con el LoRA de 4 pasos [Wan2.2-Lightning](https://huggingface.co/lightx2v/Wan2.2-Lightning) de lightx2v: puede provocar cierta pérdida de dinamismo en el video, pero ofrece mayor velocidad
  2. Una versión fp8_scaled sin LoRA de aceleración

A continuación se muestran los resultados de las pruebas con una GPU RTX4090D de 24 GB de VRAM a una resolución de 640×640 con 81 fotogramas

Tipo de modelo| Uso de VRAM| Tiempo de la primera generación| Tiempo de la segunda generación  
---|---|---|---  
fp8_scaled| 83%| ≈ 524s| ≈ 520s  
fp8_scaled + 4-step LoRA| 89%| ≈ 138s| ≈ 79s  
  
Como el LoRA de 4 pasos ofrece una mejor experiencia a quienes usan el flujo de trabajo por primera vez, aunque puede provocar cierta pérdida de dinamismo en el video, hemos activado por defecto la versión con LoRA de aceleración. Si quieres activar el otro flujo de trabajo, selecciónalo y usa **Ctrl+B** para habilitarlo.

### 

​

1\. Descarga el flujo de trabajo y los materiales

Actualiza tu ComfyUI a la última versión, luego descarga el archivo del flujo de trabajo y arrástralo a ComfyUI, o busca “Wan2.2 Fun Control” en la Biblioteca de plantillas en `Workflow` → `Browse Templates` → `Video`. ![Wan2.2 Fun Control workflow](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_fun_control-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan2.2 Fun Control” en la Biblioteca de plantillas

Descarga las siguientes imágenes y videos como materiales de entrada. **Materiales de entrada**

## video_wan2_2_14B_fun_control_start_image.jpg

Fotograma inicial para la generación del video. Descarga y usa esta imagen, o reemplázala por la tuya.

## video_wan2_2_14B_fun_control_start_image_control_video.mp4

Video de control de pose ya preprocesado. Descarga y usa este video, o reemplázalo por el tuyo.

> Aquí usamos un video ya preprocesado.

### 

​

2\. Modelos

Todos los modelos que se usan en esta guía están [aquí](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files). **Modelos de difusión**

## Wan2.2 Fun Control High Noise 14B FP8

wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors: Modelo de difusión de alto ruido

## Wan2.2 Fun Control Low Noise 14B FP8

wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors: Modelo de difusión de bajo ruido

**LoRA Wan2.2-Lightning (opcional, para acelerar)**

## High Noise 4-Step LoRA

wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors: LoRA de aceleración de 4 pasos para alto ruido

## Low Noise 4-Step LoRA

wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors: LoRA de aceleración de 4 pasos para bajo ruido

**VAE**

## Wan2.1 VAE

wan_2.1_vae.safetensors: VAE de Wan2.1 para codificar y decodificar

**Codificador de texto**

## UMT5 XXL FP8 Scaled

umt5_xxl_fp8_e4m3fn_scaled.safetensors: Codificador de texto FP8 escalado
    
    
    ComfyUI/
    ├───📂 models/
    │   ├───📂 diffusion_models/
    │   │   ├─── wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors
    │   │   └─── wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors
    │   ├───📂 loras/
    │   │   ├─── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
    │   │   └─── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
    │   ├───📂 text_encoders/
    │   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
    │   └───📂 vae/
    │       └── wan_2.1_vae.safetensors
    

### 

​

3\. Guía del flujo de trabajo

![Wan2.2 Fun Control Workflow Steps](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan2_2/wan_2.2_14b_fun_control.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=1c5d26bea52f7f790ac6059e7a195c8d)

Este flujo de trabajo usa LoRA. Asegúrate de que el modelo de difusión y el LoRA correspondientes estén emparejados: los modelos y LoRA de alto ruido y de bajo ruido deben usarse de forma correspondiente.

  1. Carga del modelo de **alto ruido** y del **LoRA**
     * Asegúrate de que el nodo `Load Diffusion Model` cargue el modelo `wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors`
     * Asegúrate de que el nodo `LoraLoaderModelOnly` cargue el `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors`
  2. Carga del modelo de **bajo ruido** y del **LoRA**
     * Asegúrate de que el nodo `Load Diffusion Model` cargue el modelo `wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors`
     * Asegúrate de que el nodo `LoraLoaderModelOnly` cargue el `wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors`
  3. Asegúrate de que el nodo `Load CLIP` cargue el modelo `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  4. Asegúrate de que el nodo `Load VAE` cargue el modelo `wan_2.1_vae.safetensors`
  5. Sube el fotograma inicial en el nodo `Load Image`
  6. En el segundo nodo `Load video`, carga el video de control de pose. El video que se proporciona ya está preprocesado y puedes usarlo directamente
  7. Como proporcionamos un video de pose ya preprocesado, hay que desactivar el nodo de preprocesamiento de imagen de video correspondiente. Puedes seleccionarlo y usar `Ctrl + B` para desactivarlo
  8. Modifica el prompt: puedes usar tanto chino como inglés
  9. En `Wan22FunControlToVideo`, modifica las dimensiones del video. Por defecto se usa una resolución de 640×640 para evitar tiempos de procesamiento excesivos en equipos con poca VRAM
  10. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter`, para ejecutar la generación del video



### 

​

Notas adicionales

Como los nodos integrados de ComfyUI solo incluyen el preprocesador Canny, puedes usar herramientas como [ComfyUI-comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux) para aplicar otros tipos de preprocesamiento de imagen

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/wan2-2-fun-control.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/wan2-2-fun-control)

[Wan2.2 Fun Inp](https://docs.comfy.org/es/tutorials/video/wan/wan2-2-fun-inp)[Wan2.2 Fun Camera](https://docs.comfy.org/es/tutorials/video/wan/wan2-2-fun-camera)
