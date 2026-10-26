---
url: https://docs.comfy.org/es/built-in-nodes/SetLatentNoiseMask/
title: Establecer m\u00e1scara de ruido latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:31.159123+00:00
---

# Establecer máscara de ruido latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SetLatentNoiseMask/

Latente

# Establecer máscara de ruido latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para aplicar una máscara de ruido a un conjunto de muestras latentes.

Copiar páginaCopiar página

Este nodo está diseñado para aplicar una máscara de ruido a un conjunto de muestras latentes. Modifica las muestras de entrada integrando una máscara específica, alterando así sus características de ruido.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras`| Las muestras latentes a las que se aplicará la máscara de ruido. Este parámetro es crucial para determinar el contenido base que será modificado.| `LATENT`  
`máscara`| La máscara que se aplicará a las muestras latentes. Define las áreas y la intensidad de la alteración del ruido dentro de las muestras.| `MASK`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| Las muestras latentes modificadas con la máscara de ruido aplicada.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SetLatentNoiseMask.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SetLatentNoiseMask)

[Guardar latente](https://docs.comfy.org/es/built-in-nodes/SaveLatent)[Recortar latente de video](https://docs.comfy.org/es/built-in-nodes/TrimVideoLatent)
