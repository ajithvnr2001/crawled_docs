---
url: https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-image-4-0/
title: Kling Image 4.0 en ComfyUI: texto a imagen, edici\u00f3n de imagen y long image - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-23T19:03:23.845318+00:00
---

# Kling Image 4.0 en ComfyUI: texto a imagen, edición de imagen y long image - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-image-4-0/

## En esta página

Volver arriba

  * Kling 4.0: Texto a imagen
  * Kling 4.0: edición de imagen
  * Kling 4.0: Imagen larga
  * Límites de entrada



Kling

# Kling Image 4.0 en ComfyUI: texto a imagen, edición de imagen y long image

Copiar páginaCopiar página

Genera y edita imágenes con Kling Image 4.0 en ComfyUI: texto a imagen hasta 8K, ediciones que mantienen rostro y encuadre, y páginas largas web y de producto.

Copiar páginaCopiar página

Kling Image 4.0 es el modelo de imagen de Kling AI, disponible en ComfyUI como Partner Nodes. `Kling 4.0 Image` genera imágenes de hasta 8K a partir de un prompt, con hasta diez imágenes de referencia y la opción de una serie de imágenes relacionadas. `Kling 4.0 Long Image` genera una página muy alta para un sitio web o una ficha de producto. Tres plantillas cubren los flujos siguientes.

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

## Kling 4.0: Texto a imagen

Genera una imagen a partir de un prompt en 2K, 4K u 8K con ocho relaciones de aspecto, o `auto` para seguir las imágenes de referencia. Conecta hasta diez imágenes de referencia y nómbralas en el prompt como `@Image1` en adelante para dirigir el resultado. Define `series_amount` en `auto` o en un número del 2 al 10 para obtener un conjunto de imágenes relacionadas que mantienen los mismos personajes y el mismo estilo. ![Vista previa del flujo de trabajo Kling 4.0: Texto a imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_image_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling 4.0: Texto a imagen” en la Biblioteca de plantillas

## Kling 4.0: edición de imagen

Cambia el estilo de una imagen sin alterar lo que debe permanecer igual. Conecta la foto como primera imagen de referencia y luego describe tanto el cambio como lo que se mantiene: la plantilla conserva el rostro, el encuadre y el fondo, y cambia solo el cabello, el maquillaje y el vestuario. El nodo es el mismo que en Text to Image, con una imagen de referencia conectada. ![Vista previa del flujo de trabajo Kling 4.0: Image Edit](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling 4.0: Image Edit” en la Biblioteca de plantillas

**Material de entrada**

## kling4_image_edit_portrait.png

Cárgala en la primera ranura de imagen de referencia · `@Image1`

## Kling 4.0: Imagen larga

Genera una imagen muy alta en una sola pasada. Elige el tipo de página con `skill`:

  * `webpage`: imágenes opcionales de estilo y de sujeto, identificadas como `@Image1` y `@Image2`. Describe la página banda por banda e indica el idioma del texto visible.
  * `ecommerce`: de una a tres imágenes de producto, identificadas desde `@Image1` en adelante, y un `length` de `short`, `medium` o `long`.

Ambas habilidades generan en 1K o 2K. ![Vista previa del flujo de trabajo Kling 4.0: Imagen larga](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_long_image-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling 4.0: Long Image (Webpage)” en la biblioteca de plantillas

## Límites de entrada

  * Imágenes: al menos 300 x 300 px, relación de aspecto entre 2:5 y 5:2. `Kling 4.0 Image` admite hasta diez imágenes de referencia y `Kling 4.0 Long Image` toma de una a tres imágenes de producto en el modo `ecommerce`.
  * En los nodos de imagen, un prompt que nombre `@ImageN` por encima del número de entradas conectadas hace fallar la ejecución. En el modo `webpage`, `@Image1` es `style_image` y `@Image2` es `subject_image`, así que `@Image2` sigue valiendo si solo conectas la imagen de sujeto.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/kling/kling-image-4-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/kling/kling-image-4-0)

[HitPaw Video Enhance](https://docs.comfy.org/es/tutorials/partner-nodes/hitpaw/hitpaw-video-enhance)[Kling 4.0](https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-4-0)
