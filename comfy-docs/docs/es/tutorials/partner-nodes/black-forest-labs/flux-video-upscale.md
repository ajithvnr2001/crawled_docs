---
url: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-video-upscale/
title: FLUX Video Upscale: ampliaci\u00f3n de video con IA a 4K en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:46.472729+00:00
---

# FLUX Video Upscale: ampliación de video con IA a 4K en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-video-upscale/

## En esta página

Volver arriba

  * Para qué sirve FLUX Video Upscale
  * Salidas de ejemplo
  * Úsalo
  * Flujo de trabajo de ampliación de video FLUX
  * Modo preciso o creativo
  * Consejos para el prompt
  * Límites
  * Empezar



Black Forest Labs

# FLUX Video Upscale: ampliación de video con IA a 4K en ComfyUI

Copiar páginaCopiar página

Amplía video a 1080p, 2K o 4K con el nodo asociado FLUX Video Upscale en ComfyUI. El modo preciso conserva la fuente; el creativo añade detalle fino.

Copiar páginaCopiar página

FLUX Video Upscale es la herramienta de superresolución para video impulsada por FLUX 3 de Black Forest Labs, disponible en ComfyUI como nodo asociado. Amplía clips a 1080p, 2K o 4K manteniendo la relación de aspecto de la fuente y su pista de audio.

## 

​

Para qué sirve FLUX Video Upscale

  * **Escala a 4K** : Eleva la resolución del video a 1080p, 2K o 4K en una sola llamada a la API
  * **Dos modos** : El modo preciso conserva la fuente tal cual; el modo creativo restaura e inventa detalles finos
  * **Audio conservado** : La salida mantiene la pista de audio del clip de origen
  * **Hasta 20 segundos** : Acepta clips de hasta 20 segundos con una resolución de origen de hasta 2560x1440



## 

​

Salidas de ejemplo

Ampliar un clip existente manteniendo su relación de aspecto y su pista de audio:

## 

​

Úsalo

## Llámalo desde código

Llámalo por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript, Swift y cURL listos para copiar y pegar

Esto se ejecuta en la misma cuenta de Comfy y se factura con los mismos créditos que ejecutarlo en ComfyUI más abajo. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Flujo de trabajo de ampliación de video FLUX

Amplía un clip de video existente: carga el video, elige un modo y un factor de ampliación, y luego ejecuta. El flujo de trabajo usa el nodo asociado FLUX Video Upscale para procesar el clip mediante la API de Black Forest Labs.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX Video Upscale” en la Biblioteca de plantillas

## 

​

Modo preciso o creativo

La opción **mode** del nodo selecciona cómo trata el upscaler tu metraje:

  * **Precise** : Aumenta la nitidez de la fuente sin cambiarla. Úsalo cuando la identidad importe: rostros, productos, recursos de marca y metraje de personas reales.
  * **Creative (default)** : Restaura e inventa detalles finos. Ideal para metraje generado, texturas, multitudes y paisajes. La identidad no se conserva con tanto rigor, por lo que los rostros y los productos pueden desviarse.



## 

​

Consejos para el prompt

  * Parte de la fuente menos comprimida que tengas. Los artefactos de compresión limitan cuánto detalle real puede recuperar el ampliador.
  * Usa el modo creativo para material generado, paisajes, texturas y multitudes; usa el modo preciso cuando los rostros, los productos o los recursos de marca deban permanecer exactamente como están.
  * Un prompt breve que describa el contenido del clip puede orientar el modo creativo hacia el tipo de detalle adecuado, por ejemplo “detailed armor plating and reptilian skin texture”. Déjalo vacío para una ampliación neutra.
  * El prompt no cambia el contenido del clip. Solo orienta el detalle mejorado, así que no se necesitan cadenas de acciones, movimientos de cámara ni indicaciones de audio.
  * Realiza la ampliación como último paso, después de editar y recortar, para que solo pagues por el material que conserves.



## 

​

Límites

  * Los clips de entrada están limitados a entre 1 y 20 segundos, con al menos 64px y una relación de aspecto entre 1:4 y 4:1. Las fuentes con un área mayor a 3840x2160 necesitan **auto_downscale** habilitado.
  * El factor de upscale va de 1.5x a 3x, y la salida mantiene la relación de aspecto de la fuente. Las fuentes muy grandes reciben un upscale menor al solicitado.
  * La salida es de 24 fps, limitada a aproximadamente 14.4 megapíxeles por fotograma, y mantiene la pista de audio de la fuente.



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a Biblioteca de plantillas y busca `FLUX Video Upscale`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/black-forest-labs/flux-video-upscale.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/black-forest-labs/flux-video-upscale)

[Flux Video Edit](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-video-edit)[Seedance 2 5](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-5)
