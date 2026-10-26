---
url: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-3-video/
title: FLUX 3 Video: generaci\u00f3n de video con IA y audio nativo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:46.750882+00:00
---

# FLUX 3 Video: generación de video con IA y audio nativo - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-3-video/

## En esta página

Volver arriba

  * En qué destaca FLUX 3 Video
  * Salidas de ejemplo
  * Úsalo
  * Flujo de trabajo de texto a video con FLUX 3
  * Flujo de trabajo de Flux 3 imagen a video
  * Empezar



Black Forest Labs

# FLUX 3 Video: generación de video con IA y audio nativo

Copiar páginaCopiar página

Genera videos con audio sincronizado usando FLUX 3 en ComfyUI, desde texto o imágenes, con hasta 20 segundos en una sola pasada

Copiar páginaCopiar página

FLUX 3 es el modelo fundacional multimodal de Black Forest Labs, anunciado el 23 de julio de 2026 y actualmente en Early Access. Aprende de forma conjunta a partir de imágenes, videos y audio dentro de una arquitectura unificada basada en Self-Flow, su enfoque para alinear la generación y la comprensión multimodales en un mismo modelo. En lugar de tratar cada modalidad de forma aislada, FLUX 3 aprende una representación compartida del mundo: cómo se sostienen los objetos, cómo se mueven las cosas y cómo suenan los eventos. Las capacidades y los límites pueden cambiar durante el despliegue de Early Access. En el caso de video, FLUX 3 crea clips muy diversos con audio nativo de hasta 20 segundos en una sola generación. Todas las salidas incluyen generación de audio sincronizado: sonido ambiente, voz y efectos. Admite generación de texto a video e imagen a video, con salida de múltiples tomas que encadena clips individuales en secuencias más largas y relaciones de aspecto flexibles.

## 

​

En qué destaca FLUX 3 Video

  * **Audio nativo** : Todos los videos incluyen audio sincronizado, con sonido ambiental, voz y efectos
  * **Hasta 20 segundos** : Genera clips largos en una sola pasada
  * **Entrada de texto e imagen** : Genera video a partir de un prompt de texto o continúa desde una imagen de fotograma inicial
  * **Formatos flexibles** : Resolución de 720p, 1080p, 1440p o 2160p, 24fps, relaciones de aspecto de 9:16 a 21:9
  * **Salida de varias tomas** : Encadena clips individuales en secuencias más largas para narrativas más extensas



## 

​

Salidas de ejemplo

Generación de texto a video a partir de un solo prompt, con audio, movimiento y física sincronizados: Generación de imagen a video a partir de un fotograma inicial y un prompt de texto:

## 

​

Úsalo

## Llámalo desde código

Llámalo por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript, Swift y cURL para copiar y pegar

Esto se ejecuta en la misma cuenta de Comfy y se factura con los mismos créditos que ejecutarlo en ComfyUI a continuación. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Flujo de trabajo de texto a video con FLUX 3

Genera un video completo a partir de un solo prompt de texto. FLUX 3 expande el lenguaje natural en una escena completa con audio sincronizado, movimiento y física, sin necesidad de imágenes de referencia ni configuraciones complejas.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX 3 Video” en la biblioteca de plantillas

## 

​

Flujo de trabajo de Flux 3 imagen a video

Genera un video completo a partir de un prompt de texto y una imagen de fotograma inicial. FLUX 3 expande automáticamente tu descripción en una escena coherente con audio, movimiento y física sincronizados.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX 3 Video” en la Biblioteca de plantillas

![Entrada de Flux 3 imagen a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/space_caravan.png)

## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `FLUX 3 Video`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/black-forest-labs/flux-3-video.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/black-forest-labs/flux-3-video)

[Flux 3 Max](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-3-max)[Flux Video Edit](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-video-edit)
