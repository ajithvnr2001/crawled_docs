---
url: https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-image-to-video/
title: Gu\u00eda del nodo asociado Luma imagen a video (heredado) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.627370+00:00
---

# Guía del nodo asociado Luma imagen a video (heredado) - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-image-to-video/

## En esta página

Volver arriba

  * En qué destaca Luma Image to Video
  * Flujo de trabajo de imagen a video con los nodos asociados de Luma
    * 1\. Descargar el flujo de trabajo
    * 2\. Notas adicionales



Luma

# Guía del nodo asociado Luma imagen a video (heredado)

Copiar páginaCopiar página

Cómo funcionaba el nodo asociado Luma imagen a video en ComfyUI, por qué dejó de funcionar y qué nodo lo reemplaza.

Copiar páginaCopiar página

**Obsoleto** : El nodo heredado **Luma Image to Video** está obsoleto, y Luma elimina los endpoints que utiliza el 24 de octubre de 2026. Usa el nodo [**Luma Ray 3.2 Image to Video**](https://docs.comfy.org/es/built-in-nodes/LumaRay32ImageToVideoNode) en su lugar.

El nodo Luma Image to Video te permite convertir imágenes estáticas en videos fluidos y dinámicos con la tecnología avanzada de Luma AI, dando vida y movimiento a tus imágenes.

## 

​

En qué destaca Luma Image to Video

  * **Animación de imágenes** : convierte imágenes estáticas en videos dinámicos y suaves, dando vida y movimiento a tus imágenes.
  * **Movimiento guiado por prompts** : los prompts de texto determinan los efectos de movimiento del video.
  * **Control de cámara** : la función Luma Concepts controla el movimiento de la cámara para una cinematografía profesional.
  * **Entradas de imagen flexibles** : funciona a partir de una `first_image`, una `last_image` o ambas.
  * **Salida ajustable** : puedes ajustar la resolución y la duración del video, y seleccionar distintos modelos de generación de video mediante el parámetro de modelo.



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

Flujo de trabajo de imagen a video con los nodos asociados de Luma

El nodo Luma Image to Video requiere al menos una imagen de entrada (`first_image` o `last_image`) junto con prompts de texto para determinar los efectos de movimiento del video. En esta guía creamos un ejemplo con `first_image` y `luma_concepts` para mostrar las capacidades de generación de video de Luma AI.

### 

​

1\. Descargar el flujo de trabajo

Esta página documenta el nodo **Luma Image to Video** retirado y el flujo de trabajo de ejemplo que incluía, el cual seleccionaba `ray-2`. Luma deja de ofrecer ese modelo el 24 de octubre de 2026, así que ni el nodo ni el ejemplo pueden ejecutarse. El ejemplo y su guía de pasos permanecen en el código fuente de esta página como comentario. El reemplazo es un nodo aparte. Su propia guía:

## Luma Ray 3.2: Image to Video

Consulta el nodo de reemplazo y sus entradas.

### 

​

2\. Notas adicionales

  * **Requisitos de la imagen de entrada** : Se requiere al menos uno de `first_image` o `last_image`, con un máximo de 1 imagen por entrada
  * **Luma Concepts** : Controla el movimiento de cámara para efectos de video profesionales
  * **Parámetro de semilla** : Solo determina si el nodo debe volver a ejecutarse; no afecta los resultados de la generación
  * **Habilitar nodos de entrada** : Haz clic derecho en los nodos morados en modo “Bypass” y establece “mode” en “always” para habilitar las entradas
  * **Selección de modelo** : Los distintos modelos de generación de video tienen características únicas, ajustables mediante el parámetro de modelo
  * **Resolución y duración** : Ajusta la resolución y la duración del video de salida con los parámetros de resolución y duración



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/luma/luma-image-to-video.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/luma/luma-image-to-video)

[Luma Text to Video (heredado)](https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-text-to-video)[MiniMax (Hailuo)](https://docs.comfy.org/es/tutorials/partner-nodes/minimax/overview)
