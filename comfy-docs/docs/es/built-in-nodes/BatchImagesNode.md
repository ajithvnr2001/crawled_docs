---
url: https://docs.comfy.org/es/built-in-nodes/BatchImagesNode/
title: Procesar im\u00e1genes por lotes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:31.656074+00:00
---

# Procesar imágenes por lotes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BatchImagesNode/

Imagen

# Procesar imágenes por lotes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo “Combinar Imágenes” agrupa múltiples imágenes individuales en un solo lote.

Copiar páginaCopiar página

El nodo “Combinar Imágenes” agrupa múltiples imágenes individuales en un solo lote. Toma una cantidad variable de entradas de imagen y las envía como un único tensor de imágenes agrupadas, lo que permite procesarlas juntas en nodos posteriores.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imágenes`| Una lista dinámica de entradas de imagen. Puedes agregar entre 2 y 50 imágenes para combinarlas en un lote. La interfaz del nodo te permite añadir más ranuras de entrada de imagen según sea necesario.| IMAGE| Sí| 2 a 50 entradas  
  
**Nota:** Debes conectar al menos dos imágenes para que el nodo funcione. La primera ranura de entrada siempre es obligatoria, y puedes agregar más usando el botón ”+” que aparece en la interfaz del nodo.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| Un único tensor de imágenes agrupadas que contiene todas las imágenes de entrada apiladas juntas.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/es.md)

* * *

**Source fingerprint (SHA-256):** `f756fb15760cd2518da9c3f88281d3ab3361b4c2b4820fe2be152e4db1cf102c`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BatchImagesNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BatchImagesNode)

[Agregar capa](https://docs.comfy.org/es/built-in-nodes/AddLayer)[Acondicionamiento (Combinar)](https://docs.comfy.org/es/built-in-nodes/ConditioningCombine)
