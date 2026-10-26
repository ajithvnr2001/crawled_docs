---
url: https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-video/
title: Grok Imagine Video en ComfyUI: generaci\u00f3n, edici\u00f3n y extensi\u00f3n de video con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:49.797205+00:00
---

# Grok Imagine Video en ComfyUI: generación, edición y extensión de video con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-video/

## En esta página

Volver arriba

  * En qué destaca Grok Imagine Video
  * Salidas de ejemplo
  * Grok: Generación de video
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
  * Grok: Edición de video
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
  * Grok: Video Extend
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
  * Grok: Referencia a video
    * Resumen del flujo de trabajo
    * Pasos para ejecutar



Grok

# Grok Imagine Video en ComfyUI: generación, edición y extensión de video con IA

Copiar páginaCopiar página

Genera, edita y extiende videos con Grok Imagine en ComfyUI: de texto o imagen a video, edición, extensión y flujos de trabajo de referencia a video.

Copiar páginaCopiar página

Grok Imagine Video es la familia de generación de video de xAI, disponible en ComfyUI a través de los Nodos asociados de Grok. Cubre la generación de video a partir de texto o de una imagen, la edición de video, la extensión de video sin cortes y la generación de referencia a video guiada por imágenes de personaje o de estilo. Para conocer el modelo más reciente, consulta [Grok Imagine Video 1.5](https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-imagine-video-1-5).

## 

​

En qué destaca Grok Imagine Video

  * **Generación de video con audio** : produce clips de hasta 15 segundos con audio sincronizado a partir de un prompt de texto, con una imagen inicial opcional
  * **Edición de video en lenguaje natural** : cambia el estilo del metraje, modifica el escenario o aplica una nueva estética manteniendo el movimiento y el contenido originales
  * **Extensión de video continua** : continúa un video corto con un nuevo clip que da seguimiento al metraje original, a partir de una descripción en lenguaje natural de la siguiente escena
  * **De referencia a video** : genera video guiado por hasta 7 imágenes de referencia, manteniendo la coherencia de personajes, productos o estilos
  * **Opciones de resolución** : salidas en 480p o 720p



## 

​

Salidas de ejemplo

Generación de video a partir de un prompt de texto con audio sincronizado: Edición de video con instrucciones en lenguaje natural, manteniendo el movimiento original: Extensión de video, continuando un clip corto con una nueva escena: Referencia a video, manteniendo el sujeto consistente a partir de imágenes de referencia:

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

Grok: Generación de video

Genera un video corto a partir de un prompt de texto, con una imagen inicial opcional. Este flujo de trabajo usa el modelo `grok-imagine-video` para producir clips de hasta 15 segundos con audio sincronizado.

## Ejecutar en Comfy Cloud

Abre el flujo de trabajo al instante en Comfy Cloud.

## Descargar flujo de trabajo

Descarga el JSON o busca “Grok Imagine” en la Biblioteca de plantillas

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa tres nodos:

  * **LoadImage** : proporciona el fotograma de imagen inicial opcional
  * **GrokVideoNode** : el nodo principal, configurado con el modelo `grok-imagine-video`
  * **SaveVideo** : guarda el video generado con audio



### 

​

Pasos para ejecutar

  1. **Ingresa tu prompt** : describe el movimiento, la atmósfera y la dinámica de la escena en el nodo **GrokVideoNode**
  2. **Carga una imagen inicial de forma opcional** : conecta una imagen al nodo **LoadImage**
  3. **Establece la resolución** : `480p` o `720p`
  4. **Establece la duración** : elige una longitud de 1 a 15 segundos
  5. **Establece la semilla** : controla si el nodo se vuelve a ejecutar; las salidas no son reproducibles independientemente de la semilla
  6. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



## 

​

Grok: Edición de video

Edita un video cargado con instrucciones en lenguaje natural. Cambia el estilo del metraje, modifica el entorno o aplica una nueva estética manteniendo el movimiento y el contenido originales.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Grok Imagine” en la Biblioteca de plantillas

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa tres nodos:

  * **LoadVideo** : proporciona el video fuente que se va a editar
  * **GrokVideoEditNode** : el nodo principal, configurado con el modelo `grok-imagine-video`
  * **SaveVideo** : guarda el video editado



### 

​

Pasos para ejecutar

  1. **Carga un video** : conecta tu video al nodo **LoadVideo** (de 1 a 8.7 segundos, hasta 50MB)
  2. **Describe la edición** : indica al modelo cómo transformar el metraje en el prompt del nodo **GrokVideoEditNode**
  3. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



## 

​

Grok: Video Extend

Extiende un video corto con una continuación fluida. Describe la siguiente escena en lenguaje natural y el modelo generará un nuevo clip que continúa el metraje original.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Grok Imagine” en la Biblioteca de plantillas

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa tres nodos:

  * **LoadVideo** : proporciona el video de origen que se va a extender
  * **GrokVideoExtendNode** : el nodo principal, configurado con el modelo `grok-imagine-video`
  * **SaveVideo** : guarda el video extendido



### 

​

Pasos para ejecutar

  1. **Carga un video** : conecta tu video al nodo **LoadVideo** (MP4, de 2 a 15 segundos, hasta 50MB)
  2. **Describe la siguiente escena** : indica al modelo qué debe ocurrir a continuación en el prompt de **GrokVideoExtendNode**
  3. **Define la duración** : elige la longitud de la extensión (de 2 a 10 segundos)
  4. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



## 

​

Grok: Referencia a video

Genera un video guiado por hasta 7 imágenes de referencia. Usa referencias de personaje, producto o estilo para mantener la consistencia del sujeto mientras el prompt describe el movimiento y la escena.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Grok Imagine” en la Biblioteca de plantillas

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa cuatro nodos:

  * **LoadImage** x2: proporcionan las imágenes de referencia del personaje y del objeto
  * **GrokVideoReferenceNode** : el nodo principal, configurado con el modelo `grok-imagine-video` y las imágenes de referencia
  * **SaveVideo** : guarda el video generado



### 

​

Pasos para ejecutar

  1. **Carga tus referencias** : conecta hasta 7 imágenes de referencia a los nodos **LoadImage**
  2. **Ingresa tu prompt** : describe la escena, el movimiento y cómo aparecen las referencias en el **GrokVideoReferenceNode**
  3. **Configura la resolución** : `480p` o `720p`
  4. **Configura la relación de aspecto** : elige desde `16:9` hasta `9:16`
  5. **Configura la duración** : elige una longitud de 2 a 10 segundos
  6. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/grok/grok-video.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/grok/grok-video)

[Gemini Omni Flash](https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini-omni-flash)[Grok Imagine Video 1 5](https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-imagine-video-1-5)
