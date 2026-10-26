---
url: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-3-image/
title: FLUX 3 Image en ComfyUI: texto a imagen y edici\u00f3n de im\u00e1genes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:46.016646+00:00
---

# FLUX 3 Image en ComfyUI: texto a imagen y edición de imágenes - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-3-image/

## En esta página

Volver arriba

  * Para qué sirve FLUX 3 Image
  * Úsalo
  * Flujo de trabajo de texto a imagen con FLUX 3 Image
    * Pasos para texto a imagen
  * Flujo de trabajo de edición de imágenes con FLUX 3
    * Pasos para editar la imagen
  * Editar con cajas delimitadoras en FLUX 3 Image
    * Pasos para editar con cajas delimitadoras
  * Empezar



Black Forest Labs

# FLUX 3 Image en ComfyUI: texto a imagen y edición de imágenes

Copiar páginaCopiar página

Genera texto a imagen, ediciones con múltiples referencias y control de diseño por cajas con FLUX 3 Image en ComfyUI, hasta 4K y con búsqueda web.

Copiar páginaCopiar página

FLUX 3 es el modelo fundacional multimodal de Black Forest Labs, anunciado el 23 de julio de 2026 y disponible en Early Access. Aprende de imágenes, video y audio en una sola arquitectura construida sobre Self-Flow, su enfoque para alinear la generación y la comprensión multimodales en un único modelo. FLUX 3 Image es la parte que genera y edita imágenes fijas. Las capacidades y los límites pueden cambiar durante el despliegue de Early Access. FLUX 3 Image convierte un prompt de texto en una imagen, o edita y combina hasta 10 imágenes de referencia. Te refieres a las referencias en el prompt como `image 1`, `image 2`, etc., y el modelo interpreta y expande el prompt antes de generar. El grounding con búsqueda web y búsqueda de imágenes está activado de forma predeterminada, así que puede buscar los sujetos que menciones. Devuelve una sola imagen en cualquiera de dieciséis relaciones de aspecto y en uno de cinco niveles de resolución, desde 0.75K (alrededor de 0.6 megapíxeles) hasta 4K (alrededor de 16.8 megapíxeles). En ComfyUI, FLUX 3 Image se ejecuta a través del nodo asociado **FLUX 3 Image** y se factura en créditos por imagen generada, según la resolución. Hay tres plantillas que cubren texto a imagen, edición con múltiples referencias y control de la composición mediante cajas delimitadoras.

## 

​

Para qué sirve FLUX 3 Image

  * **Texto a imagen** : genera una imagen a partir de un prompt, que el modelo interpreta y amplía primero
  * **Edición con múltiples referencias** : edita o combina hasta 10 imágenes de referencia, a las que te diriges como `image 1` a `image 10` en el prompt
  * **Control de diseño con cajas delimitadoras** : coloca objetos y texto donde quieras con las cajas del nodo Create Bounding Boxes
  * **Búsqueda fundamentada** : la búsqueda web y de imágenes está activada de forma predeterminada, así que el modelo puede investigar sujetos con nombre antes de dibujar
  * **Salida flexible** : dieciséis relaciones de aspecto y cinco niveles de resolución, de 0.75K a 4K
  * **Tipografía y diseño** : adecuado para pósters, titulares, pies de foto y trabajos de diseño basados en el layout



## 

​

Úsalo

## Llámalo desde código

Llámalo por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript, Swift y cURL listos para copiar y pegar

Esto se ejecuta en la misma cuenta de Comfy y se factura con los mismos créditos que ejecutarlo en ComfyUI a continuación. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas por resolución y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Flujo de trabajo de texto a imagen con FLUX 3 Image

Genera una imagen a partir de un prompt de texto. FLUX 3 Image interpreta y amplía el prompt, y luego lo renderiza a la resolución que elijas. No se necesitan archivos de entrada. ![Flujo de trabajo de texto a imagen con FLUX 3 Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX 3 Image: Text to Image” en la Biblioteca de plantillas

### 

​

Pasos para texto a imagen

  1. Ingresa un prompt en el nodo **FLUX 3 Image**
  2. Define `resolution` (de 0.75K a 4K) y, si quieres, un `aspect_ratio` distinto de `auto`
  3. Deja `grounding` activado para que el modelo busque en la web y en imágenes los sujetos que menciones
  4. Haz clic en **Queue** para generar la imagen



## 

​

Flujo de trabajo de edición de imágenes con FLUX 3

Edita una imagen, o combina varias, a partir de una instrucción de texto. Conecta hasta 10 imágenes de referencia y nómbralas en el prompt como `image 1`, `image 2`, y así sucesivamente. ![Flujo de trabajo de edición de imágenes con FLUX 3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX.3 Image: Image Edit” en la Biblioteca de plantillas

### 

​

Pasos para editar la imagen

  1. Sube tus imágenes de referencia al nodo **Load Image** y agrega más con las ranuras Autogrow, hasta 10
  2. Describe la edición en el nodo **FLUX 3 Image** , nombrando cada referencia como `image 1`, `image 2`, y así sucesivamente
  3. Define `resolution` y `aspect_ratio` para el resultado
  4. Haz clic en **Queue** para generar la imagen editada



## 

​

Editar con cajas delimitadoras en FLUX 3 Image

Coloca objetos y texto en posiciones exactas al introducir cajas desde el nodo **Create Bounding Boxes** en el nodo **FLUX 3 Image**. Las cajas son relativas al lienzo, así que configura la salida con la misma relación de aspecto. Cada caja lleva su propia descripción, que se suma al prompt. ![Flujo de trabajo para editar con cajas delimitadoras en FLUX 3 Image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux3_image_bboxes-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “FLUX 3 Image: Bounding Box Edit” en la Biblioteca de plantillas

### 

​

Pasos para editar con cajas delimitadoras

  1. Sube la imagen al nodo **Load Image**
  2. Dibuja cajas con **Create Bounding Boxes** y asigna una descripción a cada una
  3. Escribe la instrucción general en el nodo **FLUX 3 Image**
  4. Establece `aspect_ratio` para que coincida con el lienzo sobre el que dibujaste las cajas
  5. Haz clic en **Queue** para generar la imagen



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión (0.38.2 o posterior)
  2. Abre Biblioteca de plantillas y busca `FLUX 3 Image`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/black-forest-labs/flux-3-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/black-forest-labs/flux-3-image)

[Descripción](https://docs.comfy.org/es/tutorials/partner-nodes/image/overview)[Imagen FLUX 1 1 Pro Ultra](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image)
