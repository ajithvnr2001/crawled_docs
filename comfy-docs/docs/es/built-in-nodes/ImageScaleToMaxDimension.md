---
url: https://docs.comfy.org/es/built-in-nodes/ImageScaleToMaxDimension/
title: Escalar imagen a dimensi\u00f3n m\u00e1xima - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.564580+00:00
---

# Escalar imagen a dimensión máxima - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageScaleToMaxDimension/

Escalado

# Escalar imagen a dimensión máxima - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageScaleToMaxDimension redimensiona imágenes para que encajen dentro de una dimensión máxima especificada

Copiar páginaCopiar página

El nodo `ImageScaleToMaxDimension` redimensiona imágenes para que encajen dentro de una dimensión máxima especificada, manteniendo la relación de aspecto original. Calcula si la imagen está orientada en formato vertical u horizontal, luego escala la dimensión más grande para que coincida con el tamaño objetivo, ajustando proporcionalmente la dimensión más pequeña. El nodo admite múltiples métodos de escalado ascendente para diferentes requisitos de calidad y rendimiento.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada que se va a escalar| IMAGE| Sí| -  
`método_de_escalado`| El método de interpolación utilizado para escalar la imagen (predeterminado: “area”)| STRING| Sí| ”area"  
"lanczos"  
"bilinear"  
"nearest-exact"  
"bilinear"  
"bicubic”  
`tamaño_máximo`| La dimensión máxima para la imagen escalada (predeterminado: 512)| INT| Sí| 0 a 16384  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`imagen`| La imagen escalada con la dimensión más grande coincidiendo con el tamaño especificado| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/es.md)

* * *

**Source fingerprint (SHA-256):** `be113c1a98ab9d884b2c728b790c41fb236857d59af567e43e2be0ef0362cc5e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageScaleToMaxDimension.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageScaleToMaxDimension)

[Ampliar imagen por](https://docs.comfy.org/es/built-in-nodes/ImageScaleBy)[Escalar imagen a total de píxeles](https://docs.comfy.org/es/built-in-nodes/ImageScaleToTotalPixels)
