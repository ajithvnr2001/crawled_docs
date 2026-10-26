---
url: https://docs.comfy.org/es/built-in-nodes/ImageFromBatch/
title: Imagen desde lote - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.447486+00:00
---

# Imagen desde lote - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageFromBatch/

Lote

# Imagen desde lote - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageFromBatch está diseñado para extraer un segmento específico de imágenes de un lote, basándose en el índice y la longitud proporcionados.

Copiar páginaCopiar página

El nodo `ImageFromBatch` está diseñado para extraer un segmento específico de imágenes de un lote, basándose en el índice y la longitud proporcionados. Permite un control más detallado sobre las imágenes agrupadas, facilitando operaciones en imágenes individuales o subconjuntos dentro de un lote más grande.

## 

​

Entradas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen`| El lote de imágenes del cual se extraerá un segmento. Este parámetro es crucial para especificar el lote de origen.| `IMAGE`  
`indice_lote`| El índice inicial dentro del lote desde el cual comienza la extracción. Determina la posición inicial del segmento a extraer del lote.| `INT`  
`longitud`| La cantidad de imágenes a extraer del lote a partir de `indice_lote`. Este parámetro define el tamaño del segmento a extraer.| `INT`  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen`| El segmento extraído de imágenes del lote especificado. Esta salida representa un subconjunto del lote original, determinado por los parámetros `indice_lote` y `longitud`.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFromBatch/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageFromBatch.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageFromBatch)

[Eliminación de imágenes duplicadas](https://docs.comfy.org/es/built-in-nodes/ImageDeduplication)[Cuadrícula de imágenes](https://docs.comfy.org/es/built-in-nodes/ImageGrid)
