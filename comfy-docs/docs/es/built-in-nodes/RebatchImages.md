---
url: https://docs.comfy.org/es/built-in-nodes/RebatchImages/
title: Reagrupar im\u00e1genes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:20.825901+00:00
---

# Reagrupar imágenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RebatchImages/

Lote

# Reagrupar imágenes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo RebatchImages está diseñado para reorganizar un lote de imágenes en una nueva configuración de lotes

Copiar páginaCopiar página

El nodo RebatchImages está diseñado para reorganizar un lote de imágenes en una nueva configuración de lotes, ajustando el tamaño del lote según lo especificado. Este proceso es esencial para gestionar y optimizar el procesamiento de datos de imagen en operaciones por lotes, garantizando que las imágenes se agrupen según el tamaño de lote deseado para un manejo eficiente.

## 

​

Entradas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagenes`| Una lista de imágenes que se reorganizarán en lotes. Este parámetro es crucial para determinar los datos de entrada que se someterán al proceso de reorganización.| `IMAGE`  
`tamaño_lote`| Especifica el tamaño deseado de los lotes de salida. Este parámetro influye directamente en cómo se agrupan y procesan las imágenes de entrada, afectando la estructura de la salida.| `INT`  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`image`| La salida consiste en una lista de lotes de imágenes, reorganizados según el tamaño de lote especificado. Esto permite un procesamiento flexible y eficiente de los datos de imagen en operaciones por lotes.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchImages/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RebatchImages.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RebatchImages)

[Unir listas de imágenes](https://docs.comfy.org/es/built-in-nodes/MergeImageLists)[Repetir lote de imágenes](https://docs.comfy.org/es/built-in-nodes/RepeatImageBatch)
