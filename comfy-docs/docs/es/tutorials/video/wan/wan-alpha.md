---
url: https://docs.comfy.org/es/tutorials/video/wan/wan-alpha/
title: Tutorial de Wan-Alpha - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:00.699451+00:00
---

# Tutorial de Wan-Alpha - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/wan-alpha/

## En esta página

Volver arriba

  * Tutorial en video
  * Recursos
  * Flujo de trabajo de texto a video Wan-Alpha (14B)
    * 1\. Descargar el flujo de trabajo
    * 2\. Instalar los modelos
    * 3\. Completar el flujo de trabajo paso a paso



Wan2.1

# Tutorial de Wan-Alpha

Copiar páginaCopiar página

Aprende a generar videos con transparencia de canal alfa usando Wan-Alpha en ComfyUI

Copiar páginaCopiar página

Wan-Alpha es un modelo especializado de texto a video que genera videos de alta calidad con transparencia de canal alfa. Basado en el modelo base Wan2.1-14B-T2V, crea videos con fondos transparentes y objetos semitransparentes, ideal para flujos de trabajo de composición. El modelo destaca en la generación de fondos transparentes, objetos semitransparentes (burbujas, vidrio, agua), efectos de brillo y detalles finos con canales alfa adecuados (cabello, humo, partículas).

# 

​

Tutorial en video

## 

​

Recursos

  * [Wan-Alpha en GitHub](https://github.com/WeChatCV/Wan-Alpha)
  * [Modelo en Hugging Face](https://huggingface.co/htdong/Wan-Alpha)
  * [Versión de ComfyUI](https://huggingface.co/htdong/Wan-Alpha_ComfyUI)
  * [Artículo de investigación](https://arxiv.org/pdf/2509.24979)



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

Flujo de trabajo de texto a video Wan-Alpha (14B)

### 

​

1\. Descargar el flujo de trabajo

Actualiza tu ComfyUI a la última versión, luego descarga el archivo del flujo de trabajo y arrástralo a ComfyUI, o busca “Wan 2.1 Alpha T2V 14B” en la Biblioteca de plantillas en `Workflow` → `Browse Templates` → `Video`. ![Vista previa del flujo de trabajo T2V de Wan-Alpha](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2.1_alpha_t2v_14B-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan 2.1 Alpha T2V 14B” en la Biblioteca de plantillas

### 

​

2\. Instalar los modelos

Todos los modelos mencionados se encuentran en [Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged). **Modelos de difusión** : elige una versión:

## wan2.1_t2v_14B_fp8_scaled.safetensors

Modelo de difusión FP8 scaled. Colócalo en `ComfyUI/models/diffusion_models/`

## wan2.1_t2v_14B_bf16.safetensors

Modelo de difusión BF16. Colócalo en `ComfyUI/models/diffusion_models/`

**Codificador de texto**

## umt5_xxl_fp8_e4m3fn_scaled.safetensors

Codificador de texto FP8. Colócalo en `ComfyUI/models/text_encoders/`

**Modelos VAE**

## wan_alpha_2.1_vae_rgb_channel.safetensors

VAE de canal RGB. Colócalo en `ComfyUI/models/vae/`

## wan_alpha_2.1_vae_alpha_channel.safetensors

VAE de canal alfa. Colócalo en `ComfyUI/models/vae/`

**Modelos LoRA**

## wan_alpha_2.1_rgba_lora.safetensors

LoRA para generar alfa. Colócala en `ComfyUI/models/loras/`

## lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors

LoRA Lightning para inferencia rápida. Colócala en `ComfyUI/models/loras/`

Ubicaciones de almacenamiento de archivos:
    
    
    ComfyUI/
    ├── models/
    │   ├── diffusion_models/
    │   │   ├── wan2.1_t2v_14B_fp8_scaled.safetensors
    │   │   └── wan2.1_t2v_14B_bf16.safetensors
    │   ├── text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── vae/
    │   │   ├── wan_alpha_2.1_vae_rgb_channel.safetensors
    │   │   └── wan_alpha_2.1_vae_alpha_channel.safetensors
    │   └── loras/
    │       ├── wan_alpha_2.1_rgba_lora.safetensors
    │       └── lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors
    

### 

​

3\. Completar el flujo de trabajo paso a paso

  1. Asegúrate de que el modelo de difusión correcto esté cargado en el nodo `Load Diffusion Model`
  2. Asegúrate de que el nodo `Load CLIP` tenga cargado `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Asegúrate de que el nodo `Load VAE` para RGB tenga cargado `wan_alpha_2.1_vae_rgb_channel.safetensors`
  4. Asegúrate de que el segundo nodo `Load VAE` para Alpha tenga cargado `wan_alpha_2.1_vae_alpha_channel.safetensors`
  5. Asegúrate de que el nodo `LoRA Loader` tenga cargado `wan_alpha_2.1_rgba_lora.safetensors`
  6. (Opcional) Carga `lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors` en el nodo LoRA Lightning para una generación más rápida
  7. Define tu prompt positivo en el nodo `CLIP Text Encode (Positive Prompt)`
  8. (Opcional) Modifica las dimensiones del video en el nodo `EmptyHunyuanLatentVideo`
  9. Haz clic en el botón `Run` o usa `Ctrl(Cmd) + Enter` para ejecutar la generación



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/wan-alpha.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/wan-alpha)

[Wan-Move](https://docs.comfy.org/es/tutorials/video/wan/wan-move)[WAN2l1 ATI](https://docs.comfy.org/es/tutorials/video/wan/wan-ati)
