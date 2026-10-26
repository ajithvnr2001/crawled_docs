---
url: https://docs.comfy.org/es/built-in-nodes/LatentRotate/
title: Rotar latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:04.105084+00:00
---

# Rotar latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentRotate/

Transformación

# Rotar latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentRotate está diseñado para rotar representaciones latentes de imágenes según ángulos específicos.

Copiar páginaCopiar página

El nodo LatentRotate está diseñado para rotar representaciones latentes de imágenes según ángulos específicos. Abstrae la complejidad de manipular el espacio latente para lograr efectos de rotación, permitiendo a los usuarios transformar fácilmente imágenes en el espacio latente de un modelo generativo.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`muestras`| El parámetro ‘samples’ representa las representaciones latentes de las imágenes a rotar. Es crucial para determinar el punto de inicio de la operación de rotación.| `LATENT`  
`rotación`| El parámetro ‘rotation’ especifica el ángulo con el que deben rotarse las imágenes latentes. Influye directamente en la orientación de las imágenes resultantes.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`latent`| La salida es una versión modificada de las representaciones latentes de entrada, rotadas según el ángulo especificado.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentRotate/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentRotate.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentRotate)

[Voltear latente](https://docs.comfy.org/es/built-in-nodes/LatentFlip)[Estructura latente Trellis2 vacía](https://docs.comfy.org/es/built-in-nodes/EmptyTrellis2LatentStructure)
