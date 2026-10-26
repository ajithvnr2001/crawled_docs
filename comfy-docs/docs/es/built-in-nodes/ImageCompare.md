---
url: https://docs.comfy.org/es/built-in-nodes/ImageCompare/
title: Comparar im\u00e1genes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:55.787984+00:00
---

# Comparar imágenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageCompare/

Imagen

# Comparar imágenes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Image Compare ofrece una interfaz visual para comparar dos imágenes una al lado de la otra con un control deslizante arrastrable.

Copiar páginaCopiar página

## 

​

Descripción general

El nodo Image Compare proporciona una interfaz visual para comparar dos imágenes lado a lado mediante un control deslizante arrastrable. Está diseñado como un nodo de salida, lo que significa que no pasa datos a otros nodos, sino que muestra las imágenes directamente en la interfaz de usuario para su inspección.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`imagen_a`| La primera imagen a comparar.| IMAGE| No| -  
`imagen_b`| La segunda imagen a comparar.| IMAGE| No| -  
`vista_comparar`| El control que habilita la vista de comparación con control deslizante en la interfaz de usuario.| IMAGECOMPARE| Sí| -  
  
**Nota:** Este nodo es un nodo de salida. Aunque `image_a` e `image_b` son opcionales, se debe proporcionar al menos una imagen para que el nodo tenga un efecto visible. El nodo mostrará un área vacía para cualquier entrada de imagen que no esté conectada. Cada lote de imágenes proporcionado se guarda en almacenamiento temporal bajo los prefijos `comfy.compare.a` y `comfy.compare.b` respectivamente, y luego se muestra en la vista de control deslizante.

## 

​

Salidas

Este nodo es un nodo de salida y no produce datos de salida para su uso en otros nodos. Su función es mostrar las imágenes proporcionadas en la interfaz de ComfyUI.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/es.md)

* * *

**Source fingerprint (SHA-256):** `bc065572c5631ed80c0590aabae775c51d0f607895a87cb2cca78037ab9a6638`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageCompare.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageCompare)

[Lote de imágenes](https://docs.comfy.org/es/built-in-nodes/ImageBatch)[Crear imagen por capas](https://docs.comfy.org/es/built-in-nodes/ImageCompositor)
