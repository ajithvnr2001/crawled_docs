---
url: https://docs.comfy.org/es/built-in-nodes/LatentCrop/
title: Recortar latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:03.172496+00:00
---

# Recortar latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentCrop/

Transformación

# Recortar latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentCrop está diseñado para realizar operaciones de recorte en representaciones latentes de imágenes.

Copiar páginaCopiar página

El nodo LatentCrop está diseñado para realizar operaciones de recorte en representaciones latentes de imágenes. Permite especificar las dimensiones y la posición del recorte, posibilitando modificaciones dirigidas en el espacio latente.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras`| El parámetro ‘samples’ representa las representaciones latentes que se recortarán. Es fundamental para definir los datos sobre los cuales se realizará la operación de recorte.| `LATENT`  
`ancho`| Especifica el ancho del área de recorte. Influye directamente en las dimensiones de la representación latente de salida.| `INT`  
`altura`| Especifica la altura del área de recorte, afectando el tamaño de la representación latente recortada resultante.| `INT`  
`x`| Determina la coordenada x inicial del área de recorte, influyendo en la posición del recorte dentro de la representación latente original.| `INT`  
`y`| Determina la coordenada y inicial del área de recorte, estableciendo la posición del recorte dentro de la representación latente original.| `INT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La salida es una representación latente modificada con el recorte especificado aplicado.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCrop/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentCrop.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentCrop)

[Imagen latente SD3 vacía](https://docs.comfy.org/es/built-in-nodes/EmptySD3LatentImage)[Voltear latente](https://docs.comfy.org/es/built-in-nodes/LatentFlip)
