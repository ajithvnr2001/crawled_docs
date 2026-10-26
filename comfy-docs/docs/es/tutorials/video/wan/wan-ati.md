---
url: https://docs.comfy.org/es/tutorials/video/wan/wan-ati/
title: Flujo de trabajo nativo de Wan ATI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:01.268297+00:00
---

# Flujo de trabajo nativo de Wan ATI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/wan/wan-ati/

## En esta página

Volver arriba

  * Funciones clave
  * Ejemplo del flujo de trabajo de control de trayectoria WAN ATI
    * 1\. Descargar el flujo de trabajo
    * 2\. Instalar los modelos manualmente
    * 3\. Completar la ejecución del flujo de trabajo paso a paso



Wan2.1

# Flujo de trabajo nativo de Wan ATI

Copiar páginaCopiar página

Control de trayectorias Wan ATI en ComfyUI: dibuja trayectorias para dirigir el movimiento de objetos, regiones y cámara en el video generado, sobre Wan2.1.

Copiar páginaCopiar página

**ATI (Any Trajectory Instruction)** es un framework de generación de video controlable propuesto por el equipo de ByteDance. ATI se implementa sobre Wan2.1 y admite el control unificado de objetos, regiones locales y movimiento de cámara en videos mediante instrucciones de trayectoria arbitrarias.

## Repositorio del proyecto

Código fuente y documentación de ATI en GitHub

## Herramienta de edición de trayectorias en línea

Herramienta visual para dibujar y editar trayectorias de movimiento sobre imágenes

## 

​

Funciones clave

  * **Control de movimiento unificado** : Admite control de trayectoria para varios tipos de movimiento, incluidos objetos, regiones locales y movimientos de cámara.
  * **Editor de trayectorias interactivo** : Herramienta visual que permite dibujar y editar libremente trayectorias de movimiento sobre las imágenes.
  * **Compatible con Wan2.1** : Basado en la implementación oficial de Wan2.1, compatible con entornos y estructuras de modelo.
  * **Herramientas de visualización completas** : Admite la visualización de trayectorias de entrada, videos de salida y superposiciones de trayectorias.



## 

​

Ejemplo del flujo de trabajo de control de trayectoria WAN ATI

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

1\. Descargar el flujo de trabajo

Actualiza ComfyUI a la última versión y luego descarga el archivo del flujo de trabajo y arrástralo a ComfyUI, o busca “Wan2.1 ATI” en la Biblioteca de plantillas en `Workflow` → `Browse Templates` → `Video`. ![Vista previa del flujo de trabajo Wan2.1 ATI](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_ati-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar el flujo de trabajo

Descarga el JSON o busca “Wan2.1 ATI” en la Biblioteca de plantillas

Usaremos la siguiente imagen como entrada:

## Imagen de entrada: video_wan_ati_input_image.jpg

Descarga la imagen de entrada predeterminada o usa tu propia imagen como fotograma inicial.

### 

​

2\. Instalar los modelos manualmente

Todos los modelos que se usan en esta guía están disponibles [aquí](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files). **Modelo de difusión** : elige una versión:

## Modelo de difusión: Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors

Modelo de difusión Wan2.1 I2V ATI 14B (precisión fp8). Colócalo en `ComfyUI/models/diffusion_models/`

**Codificadores de texto** : elige una versión:

## Codificador de texto: umt5_xxl_fp16.safetensors

Codificador de texto de precisión completa (mayor calidad, mayor tamaño). Colócalo en `ComfyUI/models/text_encoders/`

## Codificador de texto: umt5_xxl_fp8_e4m3fn_scaled.safetensors

Codificador de texto FP8 (menor uso de VRAM). Colócalo en `ComfyUI/models/text_encoders/`

**VAE**

## VAE: wan_2.1_vae.safetensors

Modelo VAE de Wan2.1. Colócalo en `ComfyUI/models/vae/`

**CLIP Vision**

## CLIP Vision: clip_vision_h.safetensors

Modelo CLIP Vision para procesar imágenes de referencia. Colócalo en `ComfyUI/models/clip_vision/`

**Ubicación de almacenamiento de archivos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors
    │   ├── 📂 text_encoders/
    │   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors  # o la versión que elijas
    │   ├── 📂 clip_vision/
    │   │   └── clip_vision_h.safetensors
    │   └── 📂 vae/
    │       └── wan_2.1_vae.safetensors
    

### 

​

3\. Completar la ejecución del flujo de trabajo paso a paso

![Diagrama de pasos del flujo de trabajo](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/tutorial/video/wan/wan_ati_guide.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=300a2b5bd7002d944e1224e22ed4cd92) Sigue los pasos numerados de la imagen para asegurar una ejecución fluida del flujo de trabajo correspondiente.

  1. Verifica que el nodo `Load Diffusion Model` tenga cargado el modelo `Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors`
  2. Verifica que el nodo `Load CLIP` tenga cargado el modelo `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
  3. Verifica que el nodo `Load VAE` tenga cargado el modelo `wan_2.1_vae.safetensors`
  4. Verifica que el nodo `Load CLIP Vision` tenga cargado el modelo `clip_vision_h.safetensors`
  5. Sube la imagen de entrada proporcionada en el nodo `Load Image`
  6. Edición de trayectoria: actualmente ComfyUI todavía no cuenta con un editor de trayectoria. Puedes usar el siguiente enlace para completar la edición de la trayectoria. 
     * [Herramienta de anotación de trayectoria en línea](https://comfyui-wiki.github.io/Trajectory-Annotation-Tool/)
  7. Si necesitas modificar los prompts (positivo y negativo), haz los cambios en el nodo `CLIP Text Encoder` con el número `5`
  8. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación de video



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/wan/wan-ati.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/wan/wan-ati)

[Wan-Alpha](https://docs.comfy.org/es/tutorials/video/wan/wan-alpha)[Wan2.1 Fun Control](https://docs.comfy.org/es/tutorials/video/wan/fun-control)
