---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-5/
title: Seedance 2.5: generaci\u00f3n de video con IA y audio - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:47.279021+00:00
---

# Seedance 2.5: generación de video con IA y audio - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-5/

## En esta página

Volver arriba

  * En qué destaca Seedance 2.5
  * Salidas de ejemplo
  * Flujos de trabajo disponibles
    * Texto a video (T2V)
    * Imagen a video (I2V)
    * Primer y último fotograma a video (FLF2V)
    * Referencia a video (R2V)
    * Editar video
    * Modo borrador (vista previa en 480p y luego final en 1080p)
  * Empezar



ByteDance

# Seedance 2.5: generación de video con IA y audio

Copiar páginaCopiar página

Genera videos de 30 segundos con audio sincronizado, control de referencia multimodal y edición precisa con Seedance 2.5 en ComfyUI

Copiar páginaCopiar página

Seedance 2.5 es el modelo de creación de video de nueva generación de ByteDance, lanzado el 31 de julio de 2026. A partir de la arquitectura unificada de generación conjunta de audio y video multimodal de Seedance 2.0, cambia el enfoque: de generar un solo clip pasa a completar una obra creativa entera, con avances importantes en narración de formato largo, referencia multimodal y edición. El modelo genera hasta 30 segundos de audio y video de alta calidad en una sola pasada, con mejores transiciones de plano y cambios de escena para lograr una continuidad más sólida en videos más largos. Admite varias rondas de extensión, así que los creadores pueden construir contenido de varios minutos con un lenguaje audiovisual coherente y dar vida a una historia completa en una sola toma. La calidad de imagen, audio y movimiento mejora respecto de la generación anterior, lo que da como resultado visuales más naturales y pulidos.

## 

​

En qué destaca Seedance 2.5

  * **Generación de 30 segundos** : produce clips de audio y video de alta calidad de 30 segundos en una sola pasada, con extensión en varias rondas
  * **Sincronización de audio y video** : genera el video y el audio juntos, incluidos los diálogos y el habla con sincronización labial
  * **Referencia multimodal totalmente mejorada** : acepta hasta 30 imágenes de referencia, 10 clips de video y 10 clips de audio para controlar la consistencia de los personajes, el estilo visual y el ritmo del movimiento
  * **Edición precisa** : ofrece control a nivel de marca de tiempo para editar puntos concretos del video y del audio, además de edición con pantalla verde y edición basada en referencias
  * **Extensión en varias rondas** : extiende los clips para crear contenido de varios minutos con un lenguaje audiovisual consistente
  * **Casos de uso versátiles** : ideal para películas de marca, series por episodios, contenido de comercio electrónico, presentaciones de productos y series cortas centradas en personajes



## 

​

Salidas de ejemplo

Generación de texto a video, produciendo un clip cinematográfico de 30 segundos con sonido y música sincronizados: Generación de imagen a video, animando una sola imagen hasta convertirla en un clip de 1080p con sonido, música y diálogo:

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

Flujos de trabajo disponibles

### 

​

Texto a video (T2V)

Genera un video cinematográfico de 30 segundos a partir de un prompt de texto, con sonido y música sincronizados. El nodo admite resolución de salida de 480p, 720p y 1080p.

## Ejecutar texto a video en la nube

Prueba el flujo de trabajo de texto a video al instante en Comfy Cloud.

## Descargar el flujo de trabajo de texto a video

Descarga el JSON del flujo de trabajo.

También hay disponible una variante dedicada de 1080p de este flujo de trabajo:

## Ejecutar texto a video en 1080p en la nube

Prueba el flujo de trabajo de texto a video en 1080p al instante en Comfy Cloud.

## Descargar el flujo de trabajo de texto a video en 1080p

Descarga el JSON del flujo de trabajo.

### 

​

Imagen a video (I2V)

Anima una sola imagen y conviértela en un clip de video de 1080p con sonido, música y diálogo sincronizados. El flujo de trabajo admite clips de hasta 30 segundos en cualquier relación de aspecto y toma una sola imagen como entrada.

## Ejecutar imagen a video en la nube

Prueba el flujo de trabajo de imagen a video al instante en Comfy Cloud.

## Descargar el flujo de trabajo de imagen a video

Descarga el JSON del flujo de trabajo.

### 

​

Primer y último fotograma a video (FLF2V)

Indica un fotograma inicial y un fotograma final, y Seedance 2.5 genera el movimiento y las transiciones entre ambos, fijando los dos extremos. ![Vista previa del flujo de trabajo Seedance 2.5 FLF2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_flf2v-1.webp)

## Ejecutar FLF2V en Cloud

Prueba el flujo de trabajo de primer y último fotograma a video al instante en Comfy Cloud.

## Descargar el flujo de trabajo FLF2V

Descarga el JSON del flujo de trabajo.

### 

​

Referencia a video (R2V)

Usa imágenes de referencia, clips de video o audio para controlar la consistencia del personaje, el estilo visual y el ritmo del movimiento en una sola salida con sonido sincronizado y diálogo con sincronización labial. ![Vista previa del flujo de trabajo Referencia a video de Seedance 2.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_r2v-1.webp)

## Ejecuta Referencia a video en Comfy Cloud

Prueba el flujo de trabajo Referencia a video al instante en Comfy Cloud.

## Descargar flujo de trabajo Referencia a video

Descarga el JSON del flujo de trabajo.

### 

​

Editar video

Edita clips de video existentes describiendo los cambios en lenguaje natural. Reemplaza objetos, intercambia fondos, cambia escenas o transfiere estilos mientras conservas la composición y el movimiento originales. También puedes extender un clip existente hacia adelante o hacia atrás. Conecta el clip como video de referencia, define la opción **task_type** en **extend** y describe la continuación en el prompt, por ejemplo “extend forward”, “extend backward” o “continue”. La salida contiene únicamente el segmento recién generado con la duración que definas, y su relación de aspecto sigue la del clip de origen. ![Vista previa del flujo de trabajo Video Editing de Seedance 2.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_video_editing-1.webp)

## Ejecutar Video Editing en la nube

Prueba el flujo de trabajo Video Editing al instante en Comfy Cloud.

## Descargar el flujo de trabajo Video Editing

Descarga el JSON del flujo de trabajo.

### 

​

Modo borrador (vista previa en 480p y luego final en 1080p)

El modo borrador primero genera una vista previa en 480p de bajo costo y luego el resultado final en 1080p a partir de ese borrador. Se aplica a los flujos de trabajo Text to Video, First-Last-Frame to Video y Reference to Video. Consulta [Modo borrador de Seedance 2.5](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-5-draft) para ver las plantillas, las entradas de ejemplo y los consejos para el flujo de trabajo.

## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `Seedance 2.5`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bytedance/seedance-2-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bytedance/seedance-2-5)

[Flux Video Upscale](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-video-upscale)[Seedance 2.5 Draft](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-5-draft)
