---
url: https://docs.comfy.org/es/built-in-nodes/ImageScaleToTotalPixels/
title: Escalar imagen a total de p\u00edxeles - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.489983+00:00
---

# Escalar imagen a total de píxeles - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageScaleToTotalPixels/

Escalado

# Escalar imagen a total de píxeles - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageScaleToTotalPixels está diseñado para redimensionar imágenes a un número total de píxeles especificado, manteniendo la relación de aspecto.

Copiar páginaCopiar página

El nodo ImageScaleToTotalPixels está diseñado para redimensionar imágenes a un número total de píxeles especificado, manteniendo la relación de aspecto. Proporciona varios métodos para escalar la imagen y alcanzar la cantidad de píxeles deseada.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen de entrada que se escalará al número total de píxeles especificado.| `IMAGE`  
`metodo_ampliacion`| El método utilizado para escalar la imagen. Afecta la calidad y las características de la imagen escalada.| COMBO[STRING]  
`megapixeles`| El tamaño objetivo de la imagen en megapíxeles. Esto determina el número total de píxeles en la imagen escalada.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen escalada con el número total de píxeles especificado, manteniendo la relación de aspecto original.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageScaleToTotalPixels.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageScaleToTotalPixels)

[Escalar imagen a dimensión máxima](https://docs.comfy.org/es/built-in-nodes/ImageScaleToMaxDimension)[Ampliar imagen (usando modelo)](https://docs.comfy.org/es/built-in-nodes/ImageUpscaleWithModel)
