---
url: https://docs.comfy.org/es/built-in-nodes/ResizeImagesByShorterEdge/
title: Redimensionar im\u00e1genes por el borde m\u00e1s corto - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:24.002127+00:00
---

# Redimensionar imágenes por el borde más corto - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ResizeImagesByShorterEdge/

Transformación

# Redimensionar imágenes por el borde más corto - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo redimensiona imágenes para que el borde más corto coincida con una longitud específica, manteniendo la relación de aspecto original.

Copiar páginaCopiar página

Este nodo redimensiona imágenes para que el borde más corto coincida con una longitud específica, manteniendo la relación de aspecto original. Calcula las nuevas dimensiones basándose en la longitud objetivo para el lado más corto y devuelve la imagen redimensionada.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`image`| La imagen de entrada que se va a redimensionar.| IMAGE| Sí| -  
`borde_más_corto`| Longitud objetivo para el borde más corto. (predeterminado: 512)| INT| Sí| 1 a 8192  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imágenes`| La imagen redimensionada con el borde más corto coincidiendo con la longitud objetivo especificada.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/es.md)

* * *

**Source fingerprint (SHA-256):** `011949390faa9032587aec210d9e38d55b79e474c7a6dcd5d3c0e75594a1fc29`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ResizeImagesByShorterEdge.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ResizeImagesByShorterEdge)

[Redimensionar imágenes por el borde más largo](https://docs.comfy.org/es/built-in-nodes/ResizeImagesByLongerEdge)[Rellenar imagen](https://docs.comfy.org/es/built-in-nodes/PadImageNode)
