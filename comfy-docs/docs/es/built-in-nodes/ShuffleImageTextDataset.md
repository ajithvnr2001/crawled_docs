---
url: https://docs.comfy.org/es/built-in-nodes/ShuffleImageTextDataset/
title: Barajar conjunto de im\u00e1genes y textos - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:31.425802+00:00
---

# Barajar conjunto de imágenes y textos - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ShuffleImageTextDataset/

Lote

# Barajar conjunto de imágenes y textos - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo mezcla una lista de imágenes y una lista de textos de forma conjunta, manteniendo intactos sus emparejamientos.

Copiar páginaCopiar página

Este nodo mezcla una lista de imágenes y una lista de textos de forma conjunta, manteniendo intactos sus emparejamientos. Utiliza una semilla aleatoria para determinar el orden de la mezcla, lo que garantiza que las mismas listas de entrada se mezclarán de la misma manera cada vez que se reutilice la semilla.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`images`| Lista de imágenes a mezclar.| IMAGE| Sí| -  
`texts`| Lista de textos a mezclar.| STRING| Sí| -  
`seed`| Semilla aleatoria. El orden de la mezcla está determinado por este valor (predeterminado: 0).| INT| No| 0 a 18446744073709551615  
  
**Nota:** Las entradas `images` y `texts` deben ser listas de la misma longitud. El nodo emparejará la primera imagen con el primer texto, la segunda imagen con el segundo texto, y así sucesivamente, antes de mezclar estos pares de forma conjunta.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`images`| La lista mezclada de imágenes.| IMAGE  
`texts`| La lista mezclada de textos, manteniendo sus emparejamientos originales con las imágenes.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/es.md)

* * *

**Source fingerprint (SHA-256):** `c87cef780c98b1cf2a58a7d5faf4399c85edd647a9fdba693d008152e43d9c99`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ShuffleImageTextDataset.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ShuffleImageTextDataset)

[Barajar conjunto de imágenes](https://docs.comfy.org/es/built-in-nodes/ShuffleDataset)[Dividir imagen en lista de mosaicos](https://docs.comfy.org/es/built-in-nodes/SplitImageToTileList)
