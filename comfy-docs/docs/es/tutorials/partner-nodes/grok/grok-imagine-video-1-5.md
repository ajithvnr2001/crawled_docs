---
url: https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-imagine-video-1-5/
title: Grok Imagine Video 1.5 en ComfyUI: de imagen y texto a video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:49.942492+00:00
---

# Grok Imagine Video 1.5 en ComfyUI: de imagen y texto a video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-imagine-video-1-5/

## En esta página

Volver arriba

  * En qué destaca Grok Imagine Video 1.5
  * Grok Imagine Video 1.5: imagen a video
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
    * Salida
    * Consejos
  * Grok Imagine Video 1.5 Lite
    * Flujo de trabajo Lite de texto a video
    * Flujo de trabajo Lite de imagen a video



Grok

# Grok Imagine Video 1.5 en ComfyUI: de imagen y texto a video

Copiar páginaCopiar página

Usa el nodo asociado Grok Imagine Video 1.5 en ComfyUI para generar video desde una imagen o un prompt de texto con audio nativo, incluidos flujos de trabajo Lite.

Copiar páginaCopiar página

El nodo asociado [Grok Imagine Video 1.5](https://docs.comfy.org/es/built-in-nodes/GrokVideoNode) permite generar video de alta calidad con audio nativo a partir de una imagen o un prompt de texto. Impulsado por el modelo Grok más reciente de xAI, produce movimiento realista con audio sincronizado y admite resoluciones de hasta **1080p**. El nodo admite tres variantes de modelo, seleccionadas con su parámetro `model`:

  * **`grok-imagine-video`** : el modelo de la generación anterior, admite entrada de imagen opcional
  * **`grok-imagine-video-1.5`** : el modelo 1.5 de calidad completa, admite salida en 1080p
  * **`grok-imagine-video-1.5-lite`** : una variante de 1.5 más rápida y de menor costo que genera a partir de un prompt de texto o de una imagen, con salida en 480p, 720p y 1080p

Todas las variantes generan **audio nativo** : los efectos de sonido, el ambiente y los diálogos se sintetizan en la misma pasada, sin necesidad de un pipeline de audio aparte. La duración del video va de **1 a 15 segundos**.

## 

​

En qué destaca Grok Imagine Video 1.5

  * **Generación de imagen a video** : produce video de alta calidad a partir de una sola imagen de entrada
  * **Generación de texto a video** : la variante `grok-imagine-video-1.5-lite` también genera a partir de un prompt de texto únicamente
  * **Opción más rápida y de menor costo** : `grok-imagine-video-1.5-lite` se ejecuta a una tarifa por segundo menor que la 1.5
  * **Audio nativo** : los efectos de sonido, el ambiente y los diálogos se sintetizan en la misma pasada, sin necesidad de un pipeline de audio independiente
  * **Movimiento realista** : el movimiento se mantiene sincronizado con el audio generado
  * **Salida de hasta 1080p** : los modelos 1.5 admiten resolución 1080p
  * **Duración flexible** : la longitud del video va de 1 a 15 segundos



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

Grok Imagine Video 1.5: imagen a video

![Flujo de trabajo de Grok Imagine Video 1.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_video_1_5-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Grok Imagine Video 1.5” en la Biblioteca de plantillas

## Descargar imagen de entrada de ejemplo

Obtén la imagen de entrada de ejemplo para este flujo de trabajo.

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa tres nodos:

  * **LoadImage** : proporciona el fotograma inicial de la imagen
  * **GrokVideoNode** : el nodo principal configurado con el modelo `grok-imagine-video-1.5`
  * **SaveVideo** : guarda el video generado con audio nativo



### 

​

Pasos para ejecutar

  1. **Sube una imagen inicial** : usa el nodo **LoadImage** para cargar tu imagen de referencia
  2. **Escribe tu prompt** : describe el movimiento, la atmósfera y la dinámica de la escena en el nodo **GrokVideoNode**
  3. **Selecciona el modelo** : asegúrate de que `grok-imagine-video-1.5` esté seleccionado
  4. **Establece la resolución** : elige la resolución de salida (`720p` recomendado)
  5. **Establece la duración** : elige la longitud del video en segundos
  6. **Establece la semilla** : controla si el nodo se vuelve a ejecutar; las salidas no son reproducibles independientemente de la semilla
  7. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



### 

​

Salida

El video generado incluye **audio nativo** sincronizado con el movimiento y se guarda automáticamente mediante el nodo **SaveVideo**.

### 

​

Consejos

  * Usa imágenes de entrada de alta calidad para obtener mejores resultados
  * El prompt funciona mejor cuando describe tanto la **escena visual** como la **dinámica del movimiento**
  * Para obtener resultados diferentes, prueba variar el valor de la semilla



## 

​

Grok Imagine Video 1.5 Lite

`grok-imagine-video-1.5-lite` es la variante más rápida y de menor costo de 1.5. Genera a partir de un prompt de texto o de una imagen inicial y admite salida en 480p, 720p y 1080p. Dos plantillas lo cubren.

### 

​

Flujo de trabajo Lite de texto a video

![Flujo de trabajo de texto a video de Grok Imagine Video 1.5 Lite](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_video_1_5_lite_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Grok Imagine Video 1.5 Lite: Text to Video” en la biblioteca de plantillas

  1. Selecciona `grok-imagine-video-1.5-lite` como `model` en el nodo **GrokVideoNode**
  2. Introduce un prompt que describa la escena, el movimiento y el sonido
  3. Configura `resolution` (480p, 720p o 1080p) y `duration` (de 1 a 15 segundos)
  4. Haz clic en **Queue** para generar el video



### 

​

Flujo de trabajo Lite de imagen a video

![Flujo de trabajo de imagen a video de Grok Imagine Video 1.5 Lite](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_video_1_5_lite_i2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Grok Imagine Video 1.5 Lite: Image to Video” en la biblioteca de plantillas

## Descargar imagen de entrada de ejemplo

Obtén la imagen de entrada de ejemplo para este flujo de trabajo.

  1. Sube una imagen inicial al nodo **LoadImage**
  2. Selecciona `grok-imagine-video-1.5-lite` como `model` en el nodo **GrokVideoNode**
  3. Describe el movimiento en el prompt y luego configura `resolution` y `duration`
  4. Haz clic en **Queue** para generar el video



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/grok/grok-imagine-video-1-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/grok/grok-imagine-video-1-5)

[Video Grok](https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-video)[Happyhorse1 1](https://docs.comfy.org/es/tutorials/partner-nodes/happyhorse/happyhorse1-1)
