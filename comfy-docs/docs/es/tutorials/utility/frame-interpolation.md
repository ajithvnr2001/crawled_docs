---
url: https://docs.comfy.org/es/tutorials/utility/frame-interpolation/
title: Flujo de trabajo de interpolaci\u00f3n de fotogramas en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:57.431023+00:00
---

# Flujo de trabajo de interpolación de fotogramas en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/utility/frame-interpolation/

## En esta página

Volver arriba

  * ¿Qué es la interpolación de fotogramas?
  * Casos de uso
  * Por qué importa la interpolación de fotogramas
  * Flujo de trabajo de interpolación de fotogramas
  * Empezar



Video

# Flujo de trabajo de interpolación de fotogramas en ComfyUI

Copiar páginaCopiar página

Interpola fotogramas para suavizar el movimiento y aumentar la frecuencia de fotogramas en flujos de trabajo de video de ComfyUI

Copiar páginaCopiar página

## 

​

¿Qué es la interpolación de fotogramas?

Este flujo de trabajo contiene nodos personalizados. Debes instalarlos usando [ComfyUI Manager](https://docs.comfy.org/es/manager/overview) antes de ejecutar el flujo de trabajo.

La interpolación de fotogramas genera fotogramas intermedios entre los fotogramas existentes, lo que produce un movimiento más fluido y una mejor consistencia temporal. Esta técnica es esencial para el posprocesamiento de video y puede mejorar significativamente la calidad de los videos generados.

## 

​

Casos de uso

La interpolación de fotogramas permite:

  * **Aumentar la frecuencia de fotogramas en clips cortos** : convierte videos con FPS bajos a frecuencias de fotogramas más altas
  * **Suavizar el movimiento en video generado o editado** : reduce el tartamudeo y los artefactos de escalonamiento
  * **Preparar secuencias para modelos de video posteriores** : estandariza la frecuencia de fotogramas para un procesamiento uniforme
  * **Corregir generaciones con FPS bajos** : muchos flujos de trabajo de generación de video usan 16fps de forma predeterminada, lo que puede introducir un tartamudeo notorio



## 

​

Por qué importa la interpolación de fotogramas

Muchos flujos de trabajo de generación de imágenes y video todavía usan 16fps de forma predeterminada, lo que puede introducir tartamudeo, efecto de escalón y movimiento irregular notables, especialmente en movimientos de cámara y animación de personajes. La interpolación de fotogramas es una forma eficaz de suavizar estos artefactos sin regenerar los fotogramas de origen, lo que hace que el movimiento se sienta más natural y conserva la composición y el ritmo originales. En lugar de tratar siempre la interpolación como un posprocesamiento final, también puedes usarla como paso de preprocesamiento, lo que te permite estandarizar la frecuencia de fotogramas desde el principio y enviar datos temporales más limpios a flujos de trabajo de animación y video más grandes.

## 

​

Flujo de trabajo de interpolación de fotogramas

El flujo de trabajo Frame Interpolation está disponible en la Biblioteca de plantillas de ComfyUI. Inserta nuevos fotogramas entre los existentes con un modelo FILM o RIFE, para que puedas aumentar la frecuencia de fotogramas de un clip sin regenerarlo. ![Vista previa del flujo de trabajo Frame Interpolation](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_frame_interpolation-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descargar el JSON o buscar “Frame Interpolation: FILM or RIFE” en la Biblioteca de plantillas

El flujo de trabajo carga un modelo de interpolación desde `ComfyUI/models/frame_interpolation/`. Descarga [film_net_fp16.safetensors](https://huggingface.co/Comfy-Org/frame_interpolation/resolve/main/frame_interpolation/film_net_fp16.safetensors) en esa carpeta o elige una variante de RIFE del repositorio [Comfy-Org/frame_interpolation](https://huggingface.co/Comfy-Org/frame_interpolation).

## 

​

Empezar

  1. Actualiza ComfyUI a la última versión e instala los nodos personalizados requeridos con [ComfyUI Manager](https://docs.comfy.org/es/manager/overview).
  2. Descarga el modelo FILM en `ComfyUI/models/frame_interpolation/`.
  3. Abre la Biblioteca de plantillas y busca `Frame Interpolation`.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/utility/frame-interpolation.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/utility/frame-interpolation)

[MoGe](https://docs.comfy.org/es/tutorials/utility/moge)[Relleno de video con VOID](https://docs.comfy.org/es/tutorials/utility/void-video-inpainting)
