---
url: https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-4-0/
title: Kling 4.0 en ComfyUI: texto, imagen, referencias y edici\u00f3n de video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:32.434872+00:00
---

# Kling 4.0 en ComfyUI: texto, imagen, referencias y edición de video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-4-0/

## En esta página

Volver arriba

  * Kling 4.0: texto a video
  * Kling 4.0: imagen a video
  * Kling 4.0: referencias a video
  * Kling 4.0: edición de video
  * Límites de entrada



Kling

# Kling 4.0 en ComfyUI: texto, imagen, referencias y edición de video

Copiar páginaCopiar página

Genera y edita video con Kling 4.0 en ComfyUI: texto a video, fotogramas clave, referencias y ediciones por prompt, todo con audio estéreo.

Copiar páginaCopiar página

Kling 4.0 es el modelo de generación de video de Kling AI, disponible en ComfyUI como Partner Nodes. Cada generación dura hasta 30 segundos en 720p o 1080p, y produce audio estéreo junto con la imagen. Cuatro plantillas cubren los flujos siguientes. Cada nodo ofrece además la opción de modelo `kling-4.0-flash`, más rápida y limitada a 720p y 20 segundos.

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

Kling 4.0: texto a video

Genera un clip solo con un prompt. Describe los planos y sus movimientos de cámara en orden, porque una ejecución puede contener varios cortes.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling 4.0: Text to Video” en la biblioteca de plantillas

## 

​

Kling 4.0: imagen a video

Anima una sola imagen, o una secuencia de fotogramas clave: un primer fotograma opcional, hasta ocho intermedios y uno final opcional, diez imágenes en total. El clip toma la relación de aspecto del primer fotograma. `kling-4.0-flash` anima un único primer fotograma.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling 4.0: Image to Video” en la biblioteca de plantillas

**Material de entrada**

## kling4_editorial_portrait.png

Carga en `first_frame`

## 

​

Kling 4.0: referencias a video

Rueda un clip nuevo a partir de referencias en lugar de un único fotograma inicial: hasta diez imágenes (los fotogramas opcionales cuentan para ese límite) y cinco clips de referencia, con un último fotograma opcional en `kling-4.0`. En el prompt se nombran como `@Image1` y `@Video1`, en el orden en que se conectan.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling 4.0: Reference to Video” en la biblioteca de plantillas

**Material de entrada**

## kling4_r2v_woman_copper_bob.png

Referencia de personaje, carga en `reference_images`

## kling4_r2v_brutalist_hall.png

Referencia de localización, carga en `reference_images`

## 

​

Kling 4.0: edición de video

Reescribe un clip que ya tienes. El resultado conserva la duración de `video_1`, y con `audio` en `original` mantiene el sonido original en lugar de generar uno nuevo.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling 4.0: Video Edit” en la biblioteca de plantillas

**Material de entrada**

## kling4_gown_input.mp4

Carga en `video_1`

## 

​

Límites de entrada

  * Imágenes: al menos 300 x 300 px, relación de aspecto entre 2:5 y 5:2, hasta diez por ejecución, fotogramas clave incluidos.
  * Videos: de 3 a 30 segundos cada uno (de 3 a 20 con `kling-4.0-flash`), 30 segundos en total entre todos los clips, al menos 24 fps, de 700 a 4553 px por lado, como máximo 8,294,400 px en total, relación de aspecto entre 2:5 y 5:2.
  * En los nodos de imagen a video, referencias a video y edición, un prompt que nombre `@ImageN` o `@VideoN` por encima del número de entradas conectadas hace fallar la ejecución.

Todos los parámetros están en las páginas de referencia de los nodos: [texto a video](https://docs.comfy.org/es/built-in-nodes/Kling4TextToVideoNode), [imagen a video](https://docs.comfy.org/es/built-in-nodes/Kling4ImageToVideoNode), [referencias a video](https://docs.comfy.org/es/built-in-nodes/Kling4ReferenceToVideoNode), [edición de video](https://docs.comfy.org/es/built-in-nodes/Kling4EditVideoNode).

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/kling/kling-4-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/kling/kling-4-0)

[HitPaw Video Enhance](https://docs.comfy.org/es/tutorials/partner-nodes/hitpaw/hitpaw-video-enhance)[Kling 3.0](https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-3-0)
