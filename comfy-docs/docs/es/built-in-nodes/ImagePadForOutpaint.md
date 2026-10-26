---
url: https://docs.comfy.org/es/built-in-nodes/ImagePadForOutpaint/
title: Rellenar imagen para pintar fuera - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.816906+00:00
---

# Rellenar imagen para pintar fuera - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImagePadForOutpaint/

Transformación

# Rellenar imagen para pintar fuera - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para preparar imágenes para el proceso de outpainting añadiendo relleno alrededor de ellas.

Copiar páginaCopiar página

Este nodo está diseñado para preparar imágenes para el proceso de outpainting añadiendo relleno alrededor de ellas. Ajusta las dimensiones de la imagen para garantizar la compatibilidad con los algoritmos de outpainting, facilitando la generación de áreas extendidas más allá de los límites originales.

## 

​

Inputs

Parámetro| Descripción| Tipo de dato  
---|---|---  
`imagen`| La entrada ‘image’ es la imagen principal que se preparará para outpainting, sirviendo como base para las operaciones de relleno.| `IMAGE`  
`izquierda`| Especifica la cantidad de relleno que se añadirá al lado izquierdo de la imagen, influyendo en el área expandida para outpainting.| `INT`  
`arriba`| Determina la cantidad de relleno que se añadirá en la parte superior de la imagen, afectando la expansión vertical para outpainting.| `INT`  
`derecha`| Define la cantidad de relleno que se añadirá al lado derecho de la imagen, impactando la expansión horizontal para outpainting.| `INT`  
`abajo`| Indica la cantidad de relleno que se añadirá en la parte inferior de la imagen, contribuyendo a la expansión vertical para outpainting.| `INT`  
`difuminado`| Controla la suavidad de la transición entre la imagen original y el relleno añadido, mejorando la integración visual para outpainting.| `INT`  
  
## 

​

Outputs

Parámetro| Descripción| Tipo de dato  
---|---|---  
`imagen`| La salida ‘image’ representa la imagen con relleno, lista para el proceso de outpainting.| `IMAGE`  
`mask`| La salida ‘mask’ indica las áreas de la imagen original y el relleno añadido, útil para guiar los algoritmos de outpainting.| `MASK`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImagePadForOutpaint.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImagePadForOutpaint)

[Voltear imagen](https://docs.comfy.org/es/built-in-nodes/ImageFlip)[RotarImagen](https://docs.comfy.org/es/built-in-nodes/ImageRotate)
