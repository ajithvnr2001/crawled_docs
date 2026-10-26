---
url: https://docs.comfy.org/es/built-in-nodes/ImageBatch/
title: Lote de im\u00e1genes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:55.362099+00:00
---

# Lote de imágenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageBatch/

Imagen

# Lote de imágenes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageBatch está diseñado para combinar dos imágenes en un solo lote.

Copiar páginaCopiar página

El nodo `ImageBatch` está diseñado para combinar dos imágenes en un solo lote. Si las dimensiones de las imágenes no coinciden, reescala automáticamente la segunda imagen para que coincida con las dimensiones de la primera antes de combinarlas.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen1`| La primera imagen que se combinará en el lote. Sirve como referencia para las dimensiones a las que se ajustará la segunda imagen si es necesario.| `IMAGE`  
`imagen2`| La segunda imagen que se combinará en el lote. Se reescala automáticamente para que coincida con las dimensiones de la primera imagen si son diferentes.| `IMAGE`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`image`| El lote combinado de imágenes, con la segunda imagen reescalada para que coincida con las dimensiones de la primera si es necesario.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBatch/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageBatch.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageBatch)

[Obtener tamaño de imagen](https://docs.comfy.org/es/built-in-nodes/GetImageSize)[Comparar imágenes](https://docs.comfy.org/es/built-in-nodes/ImageCompare)
