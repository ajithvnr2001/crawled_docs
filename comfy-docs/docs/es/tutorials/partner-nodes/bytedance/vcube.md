---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/vcube/
title: ByteDance vCube Video Enhance en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:47.374050+00:00
---

# ByteDance vCube Video Enhance en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/vcube/

## En esta página

Volver arriba

  * Para qué sirve vCube Video Enhance
  * Flujo de trabajo de mejora de video con ByteDance vCube
    * Opciones del nodo



ByteDance

# ByteDance vCube Video Enhance en ComfyUI

Copiar páginaCopiar página

Mejora y restaura video con ByteDance vCube en ComfyUI: superresolución hasta 8K, eliminación de artefactos, mejora de color e interpolación de fotogramas.

Copiar páginaCopiar página

ByteDance vCube es la tecnología de mejora de video con IA de ByteDance. Escala video de baja resolución con superresolución hasta 8K, a la vez que elimina artefactos de compresión y ruido, mejora el color y la nitidez y, de forma opcional, interpola fotogramas para lograr una mayor frecuencia de cuadros. En ComfyUI, el nodo ByteDance vCube Video Enhance toma un video, lo escala a un preajuste de resolución objetivo y restaura su calidad. El video de origen debe ser de 2560x1440 como máximo, y el tamaño de la salida se define con la entrada de resolución.

## 

​

Para qué sirve vCube Video Enhance

  * **Superresolución de hasta 8K** : Escala video de baja resolución a presets de salida desde 720P hasta 8K, o a un lado corto personalizado de 128 a 4320 píxeles
  * **Eliminación de artefactos y ruido** : Limpia artefactos de compresión y ruido mientras restaura la calidad del video
  * **Mejora de color y nitidez** : Mejora el color y la nitidez, con un aspecto natural en alta definición o un resultado más suave
  * **Interpolación de cuadros con IA** : Aumenta la frecuencia de cuadros por encima de la fuente, hasta 120 fps
  * **Presets según la escena** : Modos ajustados para material generado por IA, video general, clips de teléfono comprimidos, dramas con rostros y material de archivo con rayas o parpadeos



Para usar los Nodos asociados, debes asegurarte de haber iniciado sesión correctamente y de estar utilizando un entorno de red permitido. Consulta la sección [Descripción general de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/overview) de la documentación para conocer los requisitos específicos de uso de los Nodos asociados.

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

Flujo de trabajo de mejora de video con ByteDance vCube

Sube un video, elige la resolución y la frecuencia de cuadros objetivo, y ejecuta el flujo de trabajo para obtener un video restaurado y con upscale.

## Ejecutar en Comfy Cloud

Ejecuta el flujo de trabajo de mejora de video al instante en Comfy Cloud.

## Descargar flujo de trabajo

Descarga el archivo JSON del flujo de trabajo para usarlo de forma local.

![Vista previa del flujo de trabajo de mejora de video con ByteDance vCube](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_vcube_video_enhance-1.webp)

## Descargar video de entrada de ejemplo

Obtén el video de entrada de ejemplo para este flujo de trabajo.

### 

​

Opciones del nodo

  * **Preajuste de escena** : Ajustado al contenido, con `aigc` para material generado por IA, `common` para video general, `ugc` para clips de teléfono comprimidos, `short_series` para dramas con rostros y `old_film` para material de archivo rayado o con parpadeo
  * **Estilo de mejora** : `hd` para un aspecto natural en alta definición, o `natural` para un resultado más suave
  * **Resolución** : Preajustes de salida desde 720P hasta 8K, `source` para mantener el tamaño de origen, o un lado corto personalizado de 128 a 4320 píxeles
  * **Frecuencia de cuadros** : `source`, o 24, 25, 30, 48, 50, 60 y 120 fps. Las frecuencias superiores a la de origen activan la interpolación de cuadros con IA; las frecuencias superiores a 30 fps cuestan 2x, y por encima de 60 fps, 4x
  * **Suavidad** : Nivel de bitrate `low`, `medium` o `high` para el archivo entregado



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bytedance/vcube.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bytedance/vcube)

[Seedance 2 0 Real Human](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-0-real-human)[Crystal Video Upscale](https://docs.comfy.org/es/tutorials/partner-nodes/clarityai/crystal-video-upscale)
