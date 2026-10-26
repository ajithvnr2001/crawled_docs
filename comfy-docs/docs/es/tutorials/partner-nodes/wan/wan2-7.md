---
url: https://docs.comfy.org/es/tutorials/partner-nodes/wan/wan2-7/
title: Wan2.7 en ComfyUI: T2V, I2V, R2V y edici\u00f3n de video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:57.359306+00:00
---

# Wan2.7 en ComfyUI: T2V, I2V, R2V y edición de video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/wan/wan2-7/

## En esta página

Volver arriba

  * Para qué es bueno Wan2.7
  * Puntos destacados
  * Wan2.7 imagen a video
  * Wan2.7 texto a video
  * Wan2.7 reference-to-video
  * Editar video con Wan2.7



Wan

# Wan2.7 en ComfyUI: T2V, I2V, R2V y edición de video

Copiar páginaCopiar página

Genera video con Wan2.7 mediante los Nodos asociados de ComfyUI: imagen a video, texto a video, referencia a video, continuación de video y edición guiada por prompt.

Copiar páginaCopiar página

Wan2.7 es el modelo de generación de video más reciente de Alibaba, ahora disponible en ComfyUI a través de los Nodos asociados. Es una mejora integral respecto a la versión 2.6, con avances significativos en calidad de imagen, audio, dinámica de movimiento, estilización y consistencia. Esta versión lleva un pipeline de video multimodal completamente renovado directamente a tu grafo de nodos, con soporte para entradas de texto, imagen, audio y video en cinco tipos de tareas.

## 

​

Para qué es bueno Wan2.7

  * **Imagen a video** : Generación desde el primer fotograma, desde el primer y el último fotograma, y generación guiada por audio
  * **Texto a video** : Prompts de solo texto con entrada de audio opcional y narración de varias tomas
  * **Continuación de video** : Extiende un clip existente con contenido nuevo guiado por un prompt de texto
  * **Referencia a video** : Toma como referencia tanto la apariencia visual como el timbre vocal de un sujeto; admite hasta 5 entradas de personas reales e interacciones entre varios personajes
  * **Edición de video** : Edita o replica videos mediante prompts de texto, una imagen de referencia o transferencia de estilo



## 

​

Puntos destacados

  * Admite hasta **5 entradas de imagen de personas reales** para escenas con varios personajes
  * Referencia de timbre vocal para una identidad audiovisual consistente
  * Generación de imágenes basada en cuadrícula de 3x3
  * Mejoras significativas en dinámica de movimiento, estilización y consistencia respecto a Wan2.6



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

Wan2.7 imagen a video

Genera video a partir de entradas de imagen. Compatible con los modos de generación de primer fotograma, primer y último fotograma, y generación guiada por audio. ![Vista previa del flujo de trabajo Wan2.7 I2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_i2v-1.webp)

## Flujo de trabajo Wan2.7 I2V

Obtén el archivo del flujo de trabajo de imagen a video Wan2.7.

## Ejecuta Wan2.7 I2V en Cloud

Prueba el flujo de trabajo de imagen a video al instante en Comfy Cloud.

## 

​

Wan2.7 texto a video

Genera video a partir de prompts de texto puros. De forma opcional, incluye entrada de audio y narración de múltiples tomas para una narrativa más rica. ![Vista previa del flujo de trabajo Wan2.7 T2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_t2v-1.webp)

## Flujo de trabajo Wan2.7 T2V

Obtén el archivo del flujo de trabajo de texto a video de Wan2.7.

## Ejecuta Wan2.7 T2V en Cloud

Prueba el flujo de trabajo de texto a video al instante en Comfy Cloud.

## 

​

Wan2.7 reference-to-video

Usa imágenes de referencia de la apariencia visual de un sujeto junto con una referencia opcional de timbre vocal. Admite hasta 5 entradas de personas reales para escenas de interacción entre varios personajes. ![Vista previa del flujo de trabajo Wan2.7 R2V](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_r2v-1.webp)

## Flujo de trabajo Wan2.7 R2V

Descarga el archivo del flujo de trabajo Wan2.7 Reference-to-Video.

## Ejecuta Wan2.7 R2V en Cloud

Prueba el flujo de trabajo Reference-to-Video al instante en Comfy Cloud.

## 

​

Editar video con Wan2.7

Edita o replica videos existentes con prompts de texto, una imagen de referencia o transferencia de estilo. ![Vista previa del flujo de trabajo Wan2.7 Video Edit](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan2_7_video_edit-1.webp)

## Flujo de trabajo Wan2.7 Video Edit

Descarga el archivo del flujo de trabajo Wan2.7 Video Edit.

## Ejecuta Wan2.7 Video Edit en Cloud

Prueba el flujo de trabajo Video Edit al instante en Comfy Cloud.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/wan/wan2-7.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/wan/wan2-7)

[Wan3 0](https://docs.comfy.org/es/tutorials/partner-nodes/wan/wan3-0)[WaveSpeed](https://docs.comfy.org/es/tutorials/partner-nodes/wavespeed/overview)
