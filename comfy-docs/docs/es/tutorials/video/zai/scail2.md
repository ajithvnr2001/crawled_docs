---
url: https://docs.comfy.org/es/tutorials/video/zai/scail2/
title: Tutorial del flujo de trabajo de reemplazo de personaje con SCAIL-2 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:02.033566+00:00
---

# Tutorial del flujo de trabajo de reemplazo de personaje con SCAIL-2 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/zai/scail2/

## En esta página

Volver arriba

  * Flujo de trabajo de reemplazo de personaje con SCAIL-2
    * Reemplazo de personaje con SCAIL-2
  * Cómo funciona el flujo de trabajo
    * Videos largos
  * Dos modos
  * Entradas y parámetros
    * Parámetros compartidos (Base y Extend)
    * Seguimiento con SAM3 (dos entradas)
  * Instalación de modelos
    * Modelos necesarios
    * Ubicaciones de almacenamiento de archivos



ZAI

# Tutorial del flujo de trabajo de reemplazo de personaje con SCAIL-2 en ComfyUI

Copiar páginaCopiar página

Anima una imagen de personaje de referencia con un video guía o reemplaza al personaje del video usando SCAIL-2.

Copiar páginaCopiar página

**SCAIL-2** es un modelo de animación de personajes de extremo a extremo construido sobre Wan2.1. Impulsa una imagen de referencia de un personaje con un video de conducción, lo que permite tanto la animación de personajes (hacer que un personaje ejecute el movimiento) como el reemplazo de personajes dentro del video (sustituir a una persona rastreada en un video por el personaje de referencia). **Características principales** :

  * **Animación de personajes de extremo a extremo** : Impulsa una imagen fija de un personaje con el movimiento de un video de conducción
  * **Dos modos** : Modo Animación (el personaje ejecuta el movimiento) y Modo Reemplazo (sustituye la persona rastreada por el personaje de referencia)
  * **Soporte para video largo** : Generación extendida basada en fragmentos con superposición de fotogramas entre segmentos
  * **Nodos integrados de ComfyUI** : Usa `WanSCAILToVideo`, `SCAIL2ColoredMask` y el seguimiento `SAM3` nativos. No se requieren nodos personalizados más allá de las descargas de modelos estándar.

**Enlaces relacionados** :

  * [Hugging Face: SCAIL-2](https://huggingface.co/zai-org/SCAIL-2)
  * [Modelo de difusión SCAIL-2](https://huggingface.co/Comfy-Org/SCAIL-2)



## 

​

Flujo de trabajo de reemplazo de personaje con SCAIL-2

### 

​

Reemplazo de personaje con SCAIL-2

Reemplaza a un personaje en un video conservando el movimiento y el contexto de la escena. ![Vista previa del flujo de trabajo de reemplazo de personaje con SCAIL-2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan21_scail2_character_replacement-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “SCAIL-2 Character Replacement” en la Biblioteca de plantillas

**Materiales de entrada**

## Imagen de referencia

Descarga la imagen de referencia predeterminada del personaje o usa la tuya.

## Video conductor

Descarga el video conductor predeterminado o usa el tuyo.

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

Cómo funciona el flujo de trabajo

Este flujo de trabajo usa dos nodos de subgrafo: un subgrafo **Base** (primer segmento) y un subgrafo **Extend** (segmentos posteriores). Esto permite animar personajes tanto en videos cortos como largos.

  1. **Carga** un video guía (`pose_video`) y una imagen de referencia del personaje
  2. El **subgrafo Base** procesa el primer segmento (81 fotogramas por defecto)
  3. El **subgrafo Extend** procesa los segmentos adicionales, del 2 en adelante, encadenando `previous_frames` del segmento anterior
  4. Previsualiza el resultado y guárdalo



## Acerca de Subgraph

Este flujo de trabajo usa nodos Subgraph para un procesamiento modular. Consulta la documentación de Subgraph para aprender a personalizar y extender el flujo de trabajo.

### 

​

Videos largos

Para videos más largos, calcula el número de segmentos: `ceil(total_frames / 76)`. Todos los segmentos excepto el primero usan el subgrafo Extend. Duplica el nodo Extend para más segmentos, encadena la salida `previous_frames` e incrementa `segment_index`.

> **Nota:** `WanSCAILToVideo` no puede poner en cola todos los segmentos automáticamente. Ejecuta cada segmento manualmente.

## 

​

Dos modos

Modo| `replace_mode`| Fondo de la máscara de conducción| Resumen  
---|---|---|---  
**Reemplazo**| `true` (predeterminado)| Blanco| Intercambia la persona rastreada en el video de conducción por el personaje de referencia  
**Animación**| `false`| Negro| El personaje de referencia realiza el movimiento del video de conducción  
  
Establece el parámetro `replace_mode` en ambos nodos del subgrafo.

## 

​

Entradas y parámetros

### 

​

Parámetros compartidos (Base y Extend)

Parámetro| Descripción  
---|---  
`pose_video`| El video de conducción que contiene el movimiento que se va a transferir  
`reference_image`| La imagen del personaje que se va a animar o insertar  
`prompt`| Descripción del video de salida  
`replace_mode`| `true` = Reemplazo, `false` = Animación  
`segment_index`| `1` para el primer fragmento, `2+` para la continuación. Desplazamiento de pose = `76 × (index − 1)`  
`width` / `height`| Resolución de salida, por ejemplo `896×512`. Debe ser divisible entre 16  
`frame_count`| Fotogramas por segmento (predeterminado: 81)  
`previous_frame_count`| Fotogramas de superposición entre segmentos (predeterminado: 5)  
`pose_strength` / `pose_start` / `pose_end`| Intensidad y sincronización del conditioning de pose  
  
### 

​

Seguimiento con SAM3 (dos entradas)

Las entradas `sam3_video_object` y `sam3_image_object` controlan el seguimiento de máscaras de SAM3, **no** el prompt de salida de SCAIL-2. Estas determinan qué objetos se rastrean para las máscaras de color:

Entrada| Objetivo| Salida  
---|---|---  
`sam3_video_object`| Video de conducción| `pose_video_mask`  
`sam3_image_object`| Imagen de referencia| `reference_image_mask`  
  
  * Usa texto de vocabulario abierto (predeterminado: `human`)
  * Usa el mismo término cuando el sujeto sea el mismo en el video y en la referencia
  * Usa términos distintos si el video y la referencia necesitan un enfoque diferente (por ejemplo, escenas concurridas)



## 

​

Instalación de modelos

Actualiza ComfyUI a la última versión para tener los nodos integrados WanSCAILToVideo y SCAIL2ColoredMask.

### 

​

Modelos necesarios

**diffusion_models**

  * [wan2.1_14B_SCAIL_2_fp16.safetensors](https://huggingface.co/Comfy-Org/SCAIL-2/blob/main/diffusion_models/wan2.1_14B_SCAIL_2_fp16.safetensors)

**text_encoders** (elige uno)

  * [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors)

**clip_vision**

  * [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/blob/main/split_files/clip_vision/clip_vision_h.safetensors)

**vae**

  * [Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_bf16.safetensors)

**loras**

  * [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors)
  * [wan2.1_SCAIL_2_DPO_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/SCAIL-2/blob/main/loras/wan2.1_SCAIL_2_DPO_lora_bf16.safetensors)

**checkpoints**

  * [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/blob/main/checkpoints/sam3.1_multiplex_fp16.safetensors)



### 

​

Ubicaciones de almacenamiento de archivos
    
    
    ComfyUI/
    ├── models/
    │   ├── diffusion_models/
    │   │   └── wan2.1_14B_SCAIL_2_fp16.safetensors
    │   ├── text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
    │   ├── clip_vision/
    │   │   └── clip_vision_h.safetensors
    │   ├── vae/
    │   │   └── Wan2_1_VAE_bf16.safetensors
    │   ├── loras/
    │   │   ├── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
    │   │   └── wan2.1_SCAIL_2_DPO_lora_bf16.safetensors
    │   └── checkpoints/
    │       └── sam3.1_multiplex_fp16.safetensors
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/zai/scail2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/zai/scail2)

[Kandinsky 5.0](https://docs.comfy.org/es/tutorials/video/kandinsky/kandinsky-5)[YuE2](https://docs.comfy.org/es/tutorials/audio/yue2/yue2)
