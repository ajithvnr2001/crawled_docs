---
url: https://docs.comfy.org/es/built-in-nodes/ImageToMask/
title: Convertir imagen a m\u00e1scara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.628409+00:00
---

# Convertir imagen a máscara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageToMask/

Máscara

# Convertir imagen a máscara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageToMask está diseñado para convertir una imagen en una máscara basada en un canal de color específico.

Copiar páginaCopiar página

El nodo ImageToMask está diseñado para convertir una imagen en una máscara basada en un canal de color específico. Permite extraer capas de máscara correspondientes a los canales rojo, verde, azul o alfa de una imagen, facilitando operaciones que requieren enmascaramiento o procesamiento específico por canal.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`imagen`| El parámetro `imagen` representa la imagen de entrada a partir de la cual se generará una máscara basada en el canal de color especificado. Desempeña un papel crucial en la determinación del contenido y las características de la máscara resultante.| `IMAGE`  
`canal`| El parámetro `canal` especifica qué canal de color (rojo, verde, azul o alfa) de la imagen de entrada debe utilizarse para generar la máscara. Esta elección influye directamente en la apariencia de la máscara y en qué partes de la imagen se resaltan o se enmascaran.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`mask`| La máscara de salida `mask` es una representación binaria o en escala de grises del canal de color especificado de la imagen de entrada, útil para operaciones posteriores de procesamiento de imágenes o enmascaramiento.| `MASK`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageToMask/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageToMask.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageToMask)

[Color de imagen a máscara](https://docs.comfy.org/es/built-in-nodes/ImageColorToMask)[Invertir máscara](https://docs.comfy.org/es/built-in-nodes/InvertMask)
