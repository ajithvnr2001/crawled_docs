---
url: https://docs.comfy.org/es/built-in-nodes/ImageSharpen/
title: Enfocar imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.390600+00:00
---

# Enfocar imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageSharpen/

Filtros

# Enfocar imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageSharpen mejora la nitidez de una imagen acentuando sus bordes y detalles.

Copiar páginaCopiar página

El nodo ImageSharpen mejora la nitidez de una imagen acentuando sus bordes y detalles. Aplica un filtro de enfoque a la imagen, cuya intensidad y radio pueden ajustarse, haciendo que la imagen parezca más definida y nítida.

## 

​

Entradas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen de entrada que se va a enfocar. Este parámetro es fundamental, ya que determina la imagen base sobre la cual se aplicará el efecto de enfoque.| `IMAGE`  
`radio_afinado`| Define el radio del efecto de enfoque. Un radio mayor significa que más píxeles alrededor del borde se verán afectados, lo que genera un efecto de enfoque más pronunciado.| `INT`  
`sigma`| Controla la dispersión del efecto de enfoque. Un valor de sigma más alto produce una transición más suave en los bordes, mientras que un valor más bajo hace que el enfoque sea más localizado.| `FLOAT`  
`alfa`| Ajusta la intensidad del efecto de enfoque. Los valores de alfa más altos producen un efecto de enfoque más fuerte.| `FLOAT`  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen enfocada, con bordes y detalles mejorados, lista para su posterior procesamiento o visualización.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageSharpen.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageSharpen)

[Cuantizar imagen](https://docs.comfy.org/es/built-in-nodes/ImageQuantize)[MorfologiaDeImagen](https://docs.comfy.org/es/built-in-nodes/Morphology)
