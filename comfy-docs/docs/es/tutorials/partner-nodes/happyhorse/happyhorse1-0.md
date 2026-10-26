---
url: https://docs.comfy.org/es/tutorials/partner-nodes/happyhorse/happyhorse1-0/
title: Generaci\u00f3n de video con HappyHorse 1.0 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:49.718733+00:00
---

# Generación de video con HappyHorse 1.0 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/happyhorse/happyhorse1-0/

## En esta página

Volver arriba

  * En qué destaca HappyHorse 1.0
  * Salidas de ejemplo
  * HappyHorse 1.0 imagen a video
  * HappyHorse 1.0 texto a video
  * HappyHorse 1.0 referencia a video
  * Editar video con HappyHorse 1.0



HappyHorse

# Generación de video con HappyHorse 1.0 en ComfyUI

Copiar páginaCopiar página

Genera video cinematográfico con HappyHorse 1.0 de Alibaba en ComfyUI: clips a partir de imágenes, texto y referencias, más flujos de edición.

Copiar páginaCopiar página

HappyHorse 1.0 es un modelo de generación de video cinematográfico de Alibaba, ahora disponible en ComfyUI a través de los Nodos asociados. Está diseñado para video narrativo de alta calidad y flujos de trabajo creativos listos para producción. HappyHorse 1.0 se centra en una estética sólida, la secuenciación de múltiples tomas y potentes flujos de trabajo de edición (generación + edición). Es una gran opción para creadores que producen anuncios, imágenes de comercio electrónico, contenido de formato corto y videos de marketing en redes sociales.

## 

​

En qué destaca HappyHorse 1.0

  * **Rutas de creación multimodal** : texto a video (T2V), imagen a video (I2V) y sujeto a video (S2V)
  * **Estética cinematográfica** : encuadres de apertura amplia, profundidad de campo reducida, textura refinada y tono atmosférico
  * **Salida de múltiples tomas** : hasta **15s** a **1080p** , con énfasis en la consistencia entre tomas durante las transiciones de corte
  * **Flujos de trabajo de edición** : V2V y SV2V para transformar material de video o reemplazar/insertar sujetos mientras se conservan el movimiento y la composición



## 

​

Salidas de ejemplo

Generación de imagen a video con estética cinematográfica y consistencia entre tomas:

Generación de texto a video con secuencias de varias tomas y una atmósfera visual refinada:

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

HappyHorse 1.0 imagen a video

Genera video cinematográfico a partir de una sola imagen con un fuerte control estético y consistencia entre múltiples tomas.

## Ejecutar HappyHorse 1.0 I2V en Cloud

Prueba el flujo de trabajo de imagen a video al instante en Comfy Cloud.

## Flujo de trabajo I2V de HappyHorse 1.0

Obtén el archivo del flujo de trabajo de imagen a video de HappyHorse 1.0.

![Vista previa del flujo de trabajo de imagen a video de HappyHorse 1.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_i2v-1.webp)

## Descargar imagen de entrada de ejemplo

Obtén la imagen de entrada de ejemplo para este flujo de trabajo.

## 

​

HappyHorse 1.0 texto a video

Genera video cinematográfico a partir de prompts de solo texto, con secuencias de múltiples tomas y una atmósfera visual refinada.

## Ejecuta HappyHorse 1.0 T2V en Cloud

Prueba el flujo de trabajo de texto a video al instante en Comfy Cloud.

## Flujo de trabajo HappyHorse 1.0 T2V

Obtén el archivo del flujo de trabajo de texto a video de HappyHorse 1.0.

![Vista previa del flujo de trabajo de texto a video de HappyHorse 1.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_t2v-1.webp)

## 

​

HappyHorse 1.0 referencia a video

Usa un sujeto de referencia para dirigir la generación de video, conservando la identidad a lo largo de secuencias cinematográficas de múltiples tomas.

## Ejecutar HappyHorse 1.0 R2V en Cloud

Prueba el flujo de trabajo de referencia a video al instante en Comfy Cloud.

## Flujo de trabajo HappyHorse 1.0 R2V

Obtén el archivo del flujo de trabajo de referencia a video de HappyHorse 1.0.

![Vista previa del flujo de trabajo de referencia a video de HappyHorse 1.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_r2v-1.webp)

## Descargar imagen de referencia del auto

Obtén la imagen de referencia del auto del ejemplo.

## Descargar imagen de referencia de la persona

Obtén la imagen de referencia de la persona del ejemplo.

## 

​

Editar video con HappyHorse 1.0

Transforma material audiovisual existente o reemplaza o inserta sujetos conservando el movimiento y la composición con flujos de trabajo de edición V2V y SV2V.

## Ejecutar la edición de video de HappyHorse 1.0 en Comfy Cloud

Prueba el flujo de trabajo de edición de video al instante en Comfy Cloud.

## Flujo de trabajo de edición de video de HappyHorse 1.0

Obtén el archivo del flujo de trabajo de edición de video de HappyHorse 1.0.

![Vista previa del flujo de trabajo de edición de video de HappyHorse 1.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_0_video_edit-1.webp)

## Descargar imagen de entrada de ejemplo

Obtén la imagen de entrada de ejemplo para el flujo de trabajo de edición de video.

## Descargar video de entrada de ejemplo

Obtén el video de entrada de ejemplo para el flujo de trabajo de edición de video.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/happyhorse/happyhorse1-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/happyhorse/happyhorse1-0)

[Happyhorse1 1](https://docs.comfy.org/es/tutorials/partner-nodes/happyhorse/happyhorse1-1)[HeyGen Video 1.0](https://docs.comfy.org/es/tutorials/partner-nodes/heygen/heygen-video-1)
