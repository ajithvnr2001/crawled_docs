---
url: https://docs.comfy.org/es/built-in-nodes/SplitImageToTileList/
title: Dividir imagen en lista de mosaicos - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:32.355679+00:00
---

# Dividir imagen en lista de mosaicos - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SplitImageToTileList/

Lote

# Dividir imagen en lista de mosaicos - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Dividir Imagen en Lista de Teselas divide una única imagen de entrada en una serie de secciones rectangulares más pequeñas y superpuestas llamadas

Copiar páginaCopiar página

El nodo **Dividir Imagen en Lista de Teselas** divide una única imagen de entrada en una serie de secciones rectangulares más pequeñas y superpuestas llamadas teselas. Crea una lista por lotes de estas teselas, que pueden procesarse individualmente mediante otros nodos. Se puede especificar el tamaño de cada tesela y la cantidad de superposición entre ellas.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`image`| La imagen de entrada que se dividirá en teselas.| IMAGE| Sí| -  
`tile_width`| El ancho de cada tesela de salida en píxeles (predeterminado: 1024).| INT| Sí| 64 a 1048576  
`tile_height`| La altura de cada tesela de salida en píxeles (predeterminado: 1024).| INT| Sí| 64 a 1048576  
`overlap`| La cantidad de píxeles que se superpondrán las teselas adyacentes (predeterminado: 128).| INT| Sí| 0 a 4096  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`image`| Una lista por lotes que contiene todas las teselas de imagen individuales.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/es.md)

* * *

**Source fingerprint (SHA-256):** `26991a325b7b9358cd7338348e93c57695b1ed1aa1983962794f889c94c34547`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SplitImageToTileList.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SplitImageToTileList)

[Barajar conjunto de imágenes y textos](https://docs.comfy.org/es/built-in-nodes/ShuffleImageTextDataset)[Convertir espacio de color de imagen](https://docs.comfy.org/es/built-in-nodes/ImageColorSpace)
