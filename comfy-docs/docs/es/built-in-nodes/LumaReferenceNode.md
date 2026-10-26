---
url: https://docs.comfy.org/es/built-in-nodes/LumaReferenceNode/
title: Referencia Luma - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:08.274461+00:00
---

# Referencia Luma - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LumaReferenceNode/

Luma

# Referencia Luma - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo contiene una imagen y un valor de peso para usarse con el nodo Luma Generate Image.

Copiar páginaCopiar página

Este nodo contiene una imagen y un valor de peso para usarse con el nodo Luma Generate Image. Crea una cadena de referencia que puede pasarse a otros nodos Luma para influir en la generación de imágenes. El nodo puede iniciar una nueva cadena de referencia o agregarse a una existente.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| Imagen a utilizar como referencia.| IMAGE| Sí| -  
`peso`| Peso de la referencia de imagen (predeterminado: 1.0).| FLOAT| Sí| 0.0 - 1.0  
`luma_ref`| Cadena de referencia Luma existente opcional a la que agregarse.| LUMA_REF| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`luma_ref`| La cadena de referencia Luma que contiene la imagen y el peso.| LUMA_REF  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/es.md)

* * *

**Source fingerprint (SHA-256):** `1ad653f0ad7c56702f607ebc3c3d117196295e4e3b044a2c6f1aa3db18869a40`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LumaReferenceNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LumaReferenceNode)

[Luma UNI-1 Image](https://docs.comfy.org/es/built-in-nodes/LumaImageNode2)[Magnific relight de imagen](https://docs.comfy.org/es/built-in-nodes/MagnificImageRelightNode)
