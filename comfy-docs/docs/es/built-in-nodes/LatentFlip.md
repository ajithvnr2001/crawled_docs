---
url: https://docs.comfy.org/es/built-in-nodes/LatentFlip/
title: Voltear latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:03.234910+00:00
---

# Voltear latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentFlip/

Transformación

# Voltear latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentFlip está diseñado para manipular representaciones latentes volteándolas vertical u horizontalmente.

Copiar páginaCopiar página

El nodo LatentFlip está diseñado para manipular representaciones latentes volteándolas vertical u horizontalmente. Esta operación permite transformar el espacio latente, lo que puede revelar nuevas variaciones o perspectivas dentro de los datos.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras`| El parámetro ‘samples’ representa las representaciones latentes que se van a voltear. La operación de volteo altera estas representaciones, ya sea vertical u horizontalmente, según el parámetro ‘flip_method’, transformando así los datos en el espacio latente.| `LATENT`  
`método_volteo`| El parámetro ‘flip_method’ especifica el eje a lo largo del cual se voltearán las muestras latentes. Puede ser ‘x-axis: vertically’ (eje X: verticalmente) o ‘y-axis: horizontally’ (eje Y: horizontalmente), determinando la dirección del volteo y, por lo tanto, la naturaleza de la transformación aplicada a las representaciones latentes.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La salida es una versión modificada de las representaciones latentes de entrada, que han sido volteadas según el método especificado. Esta transformación puede introducir nuevas variaciones dentro del espacio latente.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFlip/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentFlip.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentFlip)

[Recortar latente](https://docs.comfy.org/es/built-in-nodes/LatentCrop)[Rotar latente](https://docs.comfy.org/es/built-in-nodes/LatentRotate)
