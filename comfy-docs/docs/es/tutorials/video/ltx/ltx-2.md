---
url: https://docs.comfy.org/es/tutorials/video/ltx/ltx-2/
title: LTX-2 en ComfyUI: flujos de trabajo de audio y video sincronizados - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:59.722072+00:00
---

# LTX-2 en ComfyUI: flujos de trabajo de audio y video sincronizados - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/video/ltx/ltx-2/

## En esta página

Volver arriba

  * Características clave
  * Checkpoints de modelo
  * Primeros pasos
  * Flujos de trabajo
    * Texto a video
    * Imagen a video
    * Control a video
  * Consejos para escribir prompts
  * Recursos



LTX

# LTX-2 en ComfyUI: flujos de trabajo de audio y video sincronizados

Copiar páginaCopiar página

Genera video y audio sincronizados en ComfyUI con LTX-2: texto a video, imagen a video, control video a video, interpolación de keyframes y upscalers 2x.

Copiar páginaCopiar página

[LTX-2](https://huggingface.co/Lightricks/LTX-2) es un modelo fundacional de audio y video basado en DiT, con 19B de parámetros, creado por Lightricks. Genera video y audio sincronizados en una sola pasada, creando experiencias cohesionadas en las que el movimiento, el diálogo, el ruido de fondo y la música surgen juntos.

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

Características clave

  * **Generación sincronizada de audio y video** : Genera movimiento, diálogo, SFX y música juntos en una sola pasada
  * **Múltiples modos de generación** : Texto a video, imagen a video y video a video
  * **Opciones de control** : Control de video a video con Canny, Depth y Pose mediante IC-LoRAs
  * **Generación guiada por keyframes** : Interpola entre imágenes de keyframe
  * **Upscale nativo** : Ampliadores espaciales (2x) y temporales (2x) para mayor resolución y FPS
  * **Mejora de prompt** : Soporte para mejora automática del prompt



## 

​

Checkpoints de modelo

Nombre| Descripción  
---|---  
ltx-2-19b-dev| Modelo completo en bf16, flexible y entrenable  
ltx-2-19b-dev-fp8| Modelo completo en cuantización fp8  
ltx-2-19b-distilled| Versión destilada, 8 pasos, CFG=1  
ltx-2-spatial-upscaler-x2-1.0| Upscaler espacial 2x para obtener mayor resolución  
ltx-2-temporal-upscaler-x2-1.0| Upscaler temporal 2x para obtener más FPS  
  
## 

​

Primeros pasos

LTX-2 es compatible de forma nativa con ComfyUI. Para empezar:

  1. Actualiza ComfyUI a la última versión
  2. Ve a **Biblioteca de plantillas** > **Video** > elige cualquier flujo de trabajo de LTX-2
  3. Sigue la ventana emergente para descargar los modelos y ejecutar el flujo de trabajo



## 

​

Flujos de trabajo

### 

​

Texto a video

Genera videos a partir de prompts de texto. ![Flujo de trabajo de ComfyUI - LTX-2 T2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_t2v-1.webp)

## Texto a video

Descargar flujo de trabajo

## Ejecutar en Comfy Cloud

Ejecutar en Comfy Cloud

**Versión destilada** (más rápida, 8 pasos): ![Flujo de trabajo de ComfyUI - LTX-2 T2V destilado](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_t2v_distilled-1.webp)

## Texto a video destilado

Descargar flujo de trabajo

## Ejecutar en Comfy Cloud

Ejecutar en Comfy Cloud

### 

​

Imagen a video

Genera videos a partir de una imagen de entrada. ![Flujo de trabajo de ComfyUI - LTX-2 I2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_i2v-1.webp)

## Imagen a video

Descargar flujo de trabajo

## Ejecutar en Comfy Cloud

Ejecutar en Comfy Cloud

**Materiales de entrada**

## Imagen de entrada

Descarga la imagen de entrada predeterminada o usa tu propia imagen.

**Versión destilada** (más rápida, 8 pasos): ![Flujo de trabajo de ComfyUI - LTX-2 I2V destilado](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_i2v_distilled-1.webp)

## Imagen a video destilado

Descargar flujo de trabajo

## Ejecutar en Comfy Cloud

Ejecutar en Comfy Cloud

**Materiales de entrada**

## Imagen de entrada

Descarga la imagen de entrada predeterminada o usa tu propia imagen.

### 

​

Control a video

Genera videos con control estructural usando IC-LoRAs. **Control de profundidad:** ![Flujo de trabajo de ComfyUI - LTX-2 de profundidad a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_depth_to_video-1.webp)

## Profundidad a video

Descargar flujo de trabajo

## Ejecutar en Comfy Cloud

Ejecutar en Comfy Cloud

**Materiales de entrada**

## Imagen de entrada

Descarga la imagen de entrada de profundidad predeterminada, o usa la tuya.

## Video de entrada

Descarga el video de entrada predeterminado, o usa el tuyo.

**Control de Canny:** ![Flujo de trabajo de ComfyUI - LTX-2 de Canny a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_canny_to_video-1.webp)

## Canny a video

Descargar flujo de trabajo

## Ejecutar en Comfy Cloud

Ejecutar en Comfy Cloud

**Materiales de entrada**

## Imagen de entrada

Descarga la imagen de entrada de Canny predeterminada, o usa la tuya.

## Video de entrada

Descarga el video de entrada predeterminado, o usa el tuyo.

**Control de postura:** ![Flujo de trabajo de ComfyUI - LTX-2 de postura a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_pose_to_video-1.webp)

## Postura a video

Descargar flujo de trabajo

## Ejecutar en Comfy Cloud

Ejecutar en Comfy Cloud

**Materiales de entrada**

## Imagen de entrada

Descarga la imagen de postura de entrada predeterminada, o usa la tuya.

## Video de entrada

Descarga el video de entrada predeterminado, o usa el tuyo.

## 

​

Consejos para escribir prompts

Al escribir prompts para LTX-2, céntrate en descripciones detalladas y cronológicas de acciones y escenas. Incluye movimientos, apariencias, ángulos de cámara y detalles del entorno específicos en un solo párrafo fluido. Comienza directamente con la acción y mantén las descripciones literales y precisas. Estructura tus prompts con:

  * Acción principal en una sola frase
  * Detalles específicos sobre movimientos y gestos
  * Apariencia de personajes y objetos
  * Detalles del fondo y del entorno
  * Ángulos y movimientos de cámara
  * Iluminación y colores
  * Cualquier cambio o evento repentino

Mantén los prompts en un máximo de 200 palabras para obtener mejores resultados.

## 

​

Recursos

  * [Repositorio de GitHub](https://github.com/Lightricks/LTX-2)
  * [Modelo en Hugging Face](https://huggingface.co/Lightricks/LTX-2)
  * [Guía de prompts para LTX-2](https://ltx.video/blog/how-to-prompt-for-ltx-2)
  * [ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo/)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/video/ltx/ltx-2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/video/ltx/ltx-2)

[LTX-2.3](https://docs.comfy.org/es/tutorials/video/ltx/ltx-2-3)[LTX-0.9.5](https://docs.comfy.org/es/tutorials/video/ltxv)
