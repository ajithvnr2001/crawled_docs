---
url: https://docs.comfy.org/es/built-in-nodes/JoinImageWithAlpha/
title: Unir imagen con alfa - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:58.414289+00:00
---

# Unir imagen con alfa - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/JoinImageWithAlpha/

Composición

# Unir imagen con alfa - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para operaciones de composición

Copiar páginaCopiar página

Este nodo está diseñado para operaciones de composición, específicamente para unir una imagen con su máscara alfa correspondiente y producir una única imagen de salida. Combina eficazmente el contenido visual con la información de transparencia, permitiendo la creación de imágenes donde ciertas áreas son transparentes o semitransparentes.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen`| El contenido visual principal que se combinará con una máscara alfa. Representa la imagen sin información de transparencia.| `IMAGE`  
`alfa`| La máscara alfa que define la transparencia de la imagen correspondiente. Se utiliza para determinar qué partes de la imagen deben ser transparentes o semitransparentes.| `MASK`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La salida es una única imagen que combina la imagen de entrada con la máscara alfa, incorporando información de transparencia en el contenido visual.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinImageWithAlpha/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/JoinImageWithAlpha.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/JoinImageWithAlpha)

[Componer imagen con máscara](https://docs.comfy.org/es/built-in-nodes/ImageCompositeMasked)[Composición de imagen Porter-Duff](https://docs.comfy.org/es/built-in-nodes/PorterDuffImageComposite)
