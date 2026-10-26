---
url: https://docs.comfy.org/es/tutorials/partner-nodes/krea/krea-3/
title: Krea 3 en ComfyUI: texto a imagen y edici\u00f3n de im\u00e1genes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.402816+00:00
---

# Krea 3 en ComfyUI: texto a imagen y edición de imágenes - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/krea/krea-3/

## En esta página

Volver arriba

  * En qué destaca Krea 3
  * Flujo de trabajo de texto a imagen con Krea 3
  * Flujo de trabajo de edición de imagen con Krea 3
  * Parámetros del nodo Krea 3
  * Notas y límites



Krea

# Krea 3 en ComfyUI: texto a imagen y edición de imágenes

Copiar páginaCopiar página

Usa Krea 3 en ComfyUI con Nodos asociados: crea una imagen desde texto o edita una foto con instrucciones en lenguaje natural y hasta 8 imágenes de referencia.

Copiar páginaCopiar página

Krea 3 es el modelo de imagen alojado de [Krea](https://www.krea.ai). Está diseñado para la edición guiada por instrucciones: describes qué debe cambiar y qué debe permanecer igual, y el modelo devuelve la imagen editada. Si no conectas ninguna imagen, genera a partir del texto. Krea 3 se ejecuta en ComfyUI como un Partner Node, así que no hay pesos que descargar y nada se ejecuta en tu propia GPU. El nodo envía tu prompt y tus imágenes de referencia a los servidores de Krea y devuelve la imagen finalizada a tu flujo de trabajo.

## 

​

En qué destaca Krea 3

  * **Ediciones guiadas por instrucciones** : escribe el cambio en lenguaje natural (“reemplaza el auto verde por uno naranja”) y Krea 3 devuelve la imagen completa, conservando lo que no pediste cambiar
  * **Texto a imagen desde el mismo nodo** : deja las entradas de imagen vacías y el nodo genera solo con el prompt
  * **Hasta 8 imágenes de referencia** : conéctalas en el orden en que quieres referirte a ellas y luego menciónalas en el prompt como `@Image1`, `@Image2`, etcétera
  * **Tres modos de razonamiento** : `fast` es el valor predeterminado y la opción recomendada, `high` planifica las ediciones complejas con más detalle y tarda más, y `ultra` genera varios candidatos y devuelve el mejor
  * **Ediciones precisas** : activa `precise_edit` para mantener sin cambios todo lo que quede fuera del área editada
  * **Control de resolución** : salida en 1K o 2K, con la relación de aspecto `auto` siguiendo la primera imagen de referencia



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

Flujo de trabajo de texto a imagen con Krea 3

Genera una imagen solo a partir de un prompt. El nodo Krea 3 Image no tiene ninguna imagen conectada, así que usa el prompt y la configuración de relación de aspecto. ![Flujo de trabajo de texto a imagen con Krea 3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea3_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Krea 3” en Biblioteca de plantillas

  1. Escribe tu prompt en el nodo **Krea 3 Image**. El ejemplo incluido es una sola frase detallada que describe el sujeto, la iluminación y el encuadre
  2. Configura `aspect_ratio`. Déjalo en `auto` para seguir el prompt o elige una de las diez relaciones admitidas
  3. Elige la `resolution`: la plantilla incluye `1K` y `2K` ofrece un lienzo más grande con un costo mayor
  4. Deja `thinking_mode` en `fast` o cámbialo a `high` cuando el prompt describa una escena compleja
  5. Haz clic en **Queue**. El nodo `SaveImageAdvanced` guarda la imagen en `ComfyUI/output/`



## 

​

Flujo de trabajo de edición de imagen con Krea 3

Edita una imagen existente a partir de un prompt de instrucción. La imagen de referencia se conecta al nodo Krea 3 Image y el prompt describe el resultado que quieres obtener. ![Flujo de trabajo de edición de imagen con Krea 3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea3_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Krea 3” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` o usa tu propia imagen:

## wide_format_digital_render.png

Nodo `LoadImage` · `wide_format_digital_render.png`

![wide_format_digital_render.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/wide_format_digital_render.png)

  1. Carga la imagen que quieres editar en el nodo `LoadImage` y conéctala al nodo **Krea 3 Image**
  2. Escribe la edición como una instrucción. El ejemplo incluido reemplaza el auto verde de la escena por uno naranja y enumera lo que debe permanecer sin cambios: composición, fondo, edificio, polvo, iluminación y perspectiva
  3. Activa `precise_edit` si todo lo que está fuera del área editada debe conservarse. Requiere al menos una imagen de referencia
  4. Ajusta `aspect_ratio` y `resolution` para el lienzo de salida
  5. Haz clic en **Queue** y compara la entrada con el resultado

**Más imágenes de referencia** El nodo acepta hasta 8 imágenes. Añádelas en el orden en que quieras referirte a ellas y luego menciona cada una en el prompt como `@Image1`, `@Image2`, etc. Para una edición exigente, ajusta `thinking_mode` en `ultra`. Genera varios candidatos y devuelve el mejor, siempre entrega 2K, requiere al menos una imagen de referencia y no se puede combinar con `precise_edit`.

## 

​

Parámetros del nodo Krea 3

El nodo **Krea 3 Image** (`Krea3ImageNode`) expone las siguientes configuraciones:

  * `image_1` … `image_8`: hasta 8 imágenes de referencia, numeradas en el orden de conexión. Déjalas vacías para texto a imagen
  * `prompt`: la instrucción o la descripción de la escena. Para referirte a las imágenes de referencia, usa `@Image1`, `@Image2`, etc.
  * `aspect_ratio`: `auto`, o uno de `1:1`, `4:5`, `3:4`, `2:3`, `9:16`, `5:4`, `4:3`, `3:2`, `16:9`, `21:9`. `auto` sigue la primera imagen de referencia, o el prompt cuando no hay ninguna imagen conectada
  * `resolution`: salida en `1K` o `2K`
  * `thinking_mode`: se recomienda `fast`, `high` planifica las ediciones complejas con más detalle y tarda más, `ultra` genera varios candidatos y devuelve el mejor. `ultra` necesita al menos una imagen de referencia, siempre genera en 2K y no se puede combinar con `precise_edit`
  * `precise_edit`: mantiene sin cambios todo lo que queda fuera del área editada. Necesita al menos una imagen de referencia
  * `seed`: semilla de la solicitud. Krea reescribe el prompt antes de generar, por lo que la misma semilla no reproduce la misma imagen



## 

​

Notas y límites

  * **Reescritura del prompt** : Krea reescribe tu prompt antes de generar, por eso una semilla repetida no produce la misma imagen.
  * **Tamaño de las referencias** : cada referencia se escala al presupuesto de píxeles de la salida antes de subirse, así que el ajuste 2K conserva más detalle de la referencia que 1K.
  * **Facturación** : Krea 3 es un Nodo asociado, así que cada ejecución se factura a tu cuenta de Comfy. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.
  * **Versión** : el nodo Krea 3 Image viene con ComfyUI [PR #17067](https://github.com/comfyanonymous/ComfyUI/pull/17067), y las dos plantillas forman parte de la biblioteca de plantillas desde `workflow_templates` 0.11.84.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/krea/krea-3.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/krea/krea-3)

[Ideogram V4](https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-v4)[Krea2 T2I](https://docs.comfy.org/es/tutorials/partner-nodes/krea/krea-2-t2i)
