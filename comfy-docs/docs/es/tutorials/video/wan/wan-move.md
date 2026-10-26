---
url: https://docs.comfy.org/es/tutorials/video/wan/wan-move/
title: Ejemplo de flujo de trabajo Wan-Move en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:01.422960+00:00
---

# Ejemplo de flujo de trabajo Wan-Move en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/wan-move/

## En esta página

Volver arriba

  * Flujo de trabajo de imagen a video Wan-Move
  * Enlaces de modelos



Wan2.1

# Ejemplo de flujo de trabajo Wan-Move en ComfyUI

Copiar páginaCopiar página

Genera video con movimiento controlable usando Wan-Move en ComfyUI: guía el movimiento de objetos con trayectorias de puntos para imagen a video.

Copiar páginaCopiar página

**Wan-Move** es un framework de generación de video con control de movimiento desarrollado por Tongyi Lab de Alibaba. Permite controlar el movimiento de los objetos en los videos generados especificando trayectorias de puntos sobre la imagen de entrada, lo que hace que la generación de imagen a video sea más precisa y controlable. **Características principales** :

  * **Control de movimiento en 480p y 5 s de alta calidad** : genera videos de 5 segundos en 480p con una controlabilidad de movimiento de grano fino
  * **Orientación por trayectorias latent** : representa las condiciones de movimiento propagando las características del primer fotograma a lo largo de las trayectorias
  * **Control de grano fino a nivel puntual** : los movimientos de los objetos se representan con trayectorias de puntos densas, lo que permite un control preciso a nivel de región
  * **Sin cambios en la arquitectura** : se integra sin problemas en Wan-I2V-14B sin módulos de movimiento adicionales

**Enlaces relacionados** :

  * [GitHub](https://github.com/ali-vilab/Wan-Move)
  * [Hugging Face](https://huggingface.co/Ruihang/Wan-Move-14B-480P)
  * [Paper](https://arxiv.org/abs/2512.08765)



## 

​

Flujo de trabajo de imagen a video Wan-Move

Vista previa del resultado del flujo de trabajo: ![Vista previa de Wan-Move](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wanmove_480p-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan-Move Motion-Control” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## snowboard_rush.png

Nodo `LoadImage` · `snowboard_rush.png`

![snowboard_rush.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/snowboard_rush.png)

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

Enlaces de modelos

## Checkpoint: Wan21-WanMove

Colócalo en `ComfyUI/models/diffusion_models/`

## LoRA: LightX2V Distilled

Colócalo en `ComfyUI/models/loras/`

## Text Encoder: umt5

Colócalo en `ComfyUI/models/text_encoders/`

## CLIP Vision: clip_vision_h

Colócalo en `ComfyUI/models/clip_vision/`

## VAE: wan_2.1_vae

Colócalo en `ComfyUI/models/vae/`

**Ubicación de almacenamiento de modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 text_encoders/
    │   │      └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── 📂 clip_vision/
    │   │      └── clip_vision_h.safetensors
    │   ├── 📂 loras/
    │   │      └── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
    │   ├── 📂 diffusion_models/
    │   │      └── Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors
    │   └── 📂 vae/
    │          └── wan_2.1_vae.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/wan-move.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/wan-move)

[Wan2.1 VACE](https://docs.comfy.org/es/tutorials/video/wan/vace)[Wan-Alpha](https://docs.comfy.org/es/tutorials/video/wan/wan-alpha)
