---
url: https://docs.comfy.org/es/built-in-nodes/ImageMergeTileList/
title: Unir lista de mosaicos en imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.373370+00:00
---

# Unir lista de mosaicos en imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageMergeTileList/

Lote

# Unir lista de mosaicos en imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo toma una lista de teselas de imagen y las fusiona nuevamente en una sola imagen más grande.

Copiar páginaCopiar página

Este nodo toma una lista de teselas de imagen y las fusiona nuevamente en una sola imagen más grande. Está diseñado para reconstruir una imagen que previamente se dividió en una cuadrícula de teselas superpuestas, utilizando una técnica de mezcla ponderada para crear un resultado final sin costuras.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`image_list`| Una lista de teselas de imagen que se fusionarán. La primera tesela de la lista se utiliza para determinar las dimensiones de las teselas y el tipo de dato para todo el proceso.| IMAGE| Sí| N/A  
`final_width`| El ancho de la imagen fusionada final en píxeles (valor predeterminado: 1024).| INT| Sí| 64 - 32768  
`final_height`| La altura de la imagen fusionada final en píxeles (valor predeterminado: 1024).| INT| Sí| 64 - 32768  
`overlap`| La cantidad de superposición entre teselas adyacentes en píxeles. Un valor mayor que 0 permite un efecto de mezcla suave en las uniones de las teselas (valor predeterminado: 128).| INT| Sí| 0 - 4096  
  
**Nota:** La `image_list` es una lista de entrada dinámica. El nodo procesará las teselas en el orden en que se proporcionen, hasta la cantidad necesaria para llenar la cuadrícula definida por `final_width`, `final_height` y las dimensiones de la primera tesela. Si la lista contiene más teselas de las necesarias, las teselas adicionales se ignoran.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`image`| La imagen fusionada final, reconstruida a partir de las teselas de entrada.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/es.md)

* * *

**Source fingerprint (SHA-256):** `f8f770ca2e9806d2feb55bb1dfe2c26b09d7a3506caf664990d8536ec5660c92`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageMergeTileList.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageMergeTileList)

[Cuadrícula de imágenes](https://docs.comfy.org/es/built-in-nodes/ImageGrid)[Unir listas de imágenes](https://docs.comfy.org/es/built-in-nodes/MergeImageLists)
