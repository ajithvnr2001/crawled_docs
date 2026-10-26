---
url: https://docs.comfy.org/es/built-in-nodes/ResizeImagesByLongerEdge/
title: Redimensionar im\u00e1genes por el borde m\u00e1s largo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:23.864793+00:00
---

# Redimensionar imágenes por el borde más largo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ResizeImagesByLongerEdge/

Transformación

# Redimensionar imágenes por el borde más largo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Redimensionar imágenes por el borde más largo redimensiona una o más imágenes de modo que su lado más largo coincida con una longitud objetivo

Copiar páginaCopiar página

El nodo **Redimensionar imágenes por el borde más largo** redimensiona una o más imágenes de modo que su lado más largo coincida con una longitud objetivo especificada. Determina automáticamente si el ancho o el alto es mayor y escala la otra dimensión de forma proporcional para conservar la relación de aspecto original. Esto es útil para estandarizar tamaños de imagen según su dimensión más grande.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`image`| La imagen o lote de imágenes de entrada que se redimensionarán.| IMAGE| Sí| -  
`borde_más_largo`| Longitud objetivo para el borde más largo. El borde más corto se escalará proporcionalmente. (valor predeterminado: 1024)| INT| Sí| 1 - 8192  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`imágenes`| La imagen o lote de imágenes redimensionadas. La salida tendrá la misma cantidad de imágenes que la entrada, y el borde más largo de cada una coincidirá con la longitud especificada en `borde_más_largo`.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/es.md)

* * *

**Source fingerprint (SHA-256):** `687d5f159967eccbf64f0ec529ae6edeb94f4707ae10a3c75a5d0b08c86dd828`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ResizeImagesByLongerEdge.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ResizeImagesByLongerEdge)

[Redimensionar y rellenar imagen](https://docs.comfy.org/es/built-in-nodes/ResizeAndPadImage)[Redimensionar imágenes por el borde más corto](https://docs.comfy.org/es/built-in-nodes/ResizeImagesByShorterEdge)
