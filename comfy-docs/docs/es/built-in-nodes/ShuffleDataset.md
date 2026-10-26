---
url: https://docs.comfy.org/es/built-in-nodes/ShuffleDataset/
title: Barajar conjunto de im\u00e1genes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:31.644288+00:00
---

# Barajar conjunto de imágenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ShuffleDataset/

Lote

# Barajar conjunto de imágenes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Shuffle Dataset toma una lista de imágenes y cambia aleatoriamente su orden.

Copiar páginaCopiar página

El nodo Shuffle Dataset toma una lista de imágenes y cambia aleatoriamente su orden. Utiliza un valor de semilla para controlar la aleatoriedad, lo que permite reproducir el mismo orden de mezcla. Esto es útil para aleatorizar la secuencia de imágenes en un conjunto de datos antes de procesarlo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`images`| La lista de imágenes que se mezclará.| IMAGE| Sí| -  
`seed`| Semilla aleatoria. Un valor de 0 producirá una mezcla diferente cada vez. (predeterminado: 0)| INT| No| 0 a 18446744073709551615  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`images`| La misma lista de imágenes, pero en un nuevo orden mezclado aleatoriamente.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/es.md)

* * *

**Source fingerprint (SHA-256):** `0b8442029995bdcedf1df0cb8d27d87aa529fb1021d911ed3016a6a7e788b246`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ShuffleDataset.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ShuffleDataset)

[Repetir lote de imágenes](https://docs.comfy.org/es/built-in-nodes/RepeatImageBatch)[Barajar conjunto de imágenes y textos](https://docs.comfy.org/es/built-in-nodes/ShuffleImageTextDataset)
