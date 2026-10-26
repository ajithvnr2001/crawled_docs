---
url: https://docs.comfy.org/es/built-in-nodes/RunwayAleph2VideoToVideoNode/
title: Runway Aleph2 Video a Video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:24.840355+00:00
---

# Runway Aleph2 Video a Video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RunwayAleph2VideoToVideoNode/

Runway

# Runway Aleph2 Video a Video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo edita un video con un prompt de texto usando el modelo Aleph2 de Runway.

Copiar páginaCopiar página

## 

​

Descripción general

Este nodo edita un video utilizando una instrucción de texto con el modelo Aleph2 de Runway. Transforma tu metraje mediante cambios de estilo, iluminación, adición o eliminación de elementos, o modificación del punto de vista, preservando el movimiento y la sincronización originales.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Describe lo que debe aparecer en la salida (1-1000 caracteres).| STRING| Sí| 1-1000 caracteres  
`video`| Video de entrada para editar. Debe durar 2-30 segundos a 30 fps o menos.| VIDEO| Sí| Duración de 2-30 segundos, máximo 30 fps  
`seed`| Semilla aleatoria para la generación (predeterminado: 0).| INT| Sí| 0 a 4294967295  
`public_figure_threshold`| Moderación de contenido para figuras públicas reconocibles (predeterminado: “low”).| COMBO| Sí| ”auto"  
"low”  
`keyframes`| Imágenes guía ancladas al video de entrada, desde nodos Aleph2 Keyframe (hasta 5). Usa keyframes o imágenes de instrucción, no ambos.| KEYFRAME| No| Hasta 5 elementos  
`prompt_images`| Imágenes guía ancladas al video de salida, desde nodos Aleph2 Prompt Image (hasta 5). Usa keyframes o imágenes de instrucción, no ambos.| PROMPT_IMAGE| No| Hasta 5 elementos  
  
**Restricciones importantes:**

  * El video de entrada debe tener una duración entre 2 y 30 segundos y una tasa de fotogramas de 30 fps o inferior.
  * Puedes usar `keyframes` o `prompt_images` como guía, pero no ambos al mismo tiempo.
  * Cada entrada de guía (keyframes o imágenes de instrucción) admite un máximo de 5 elementos.
  * Las marcas de tiempo de los keyframes y las marcas de tiempo de las imágenes de instrucción no deben exceder la duración del video de entrada.



## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`video`| El video editado generado por el modelo Aleph2.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2VideoToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `bda4d0f49843c1a8f311ddbce5911a2a157cae798a26f7a183b31fe41686d0b7`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RunwayAleph2VideoToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RunwayAleph2VideoToVideoNode)

[Runway Aleph2 Imagen de Guía](https://docs.comfy.org/es/built-in-nodes/RunwayAleph2PromptImageNode)[Runway Primer-Fotograma-Último a video](https://docs.comfy.org/es/built-in-nodes/RunwayFirstLastFrameNode)
