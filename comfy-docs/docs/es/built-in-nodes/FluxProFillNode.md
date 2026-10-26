---
url: https://docs.comfy.org/es/built-in-nodes/FluxProFillNode/
title: Flux.1 rellenar imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:49.064670+00:00
---

# Flux.1 rellenar imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/FluxProFillNode/

BFL

# Flux.1 rellenar imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Pinta imágenes basándose en una máscara y un mensaje de texto.

Copiar páginaCopiar página

Pinta imágenes basándose en una máscara y un mensaje de texto. Este nodo utiliza el modelo Flux.1 para rellenar las áreas enmascaradas de una imagen según la descripción de texto proporcionada, generando nuevo contenido que coincida con la imagen circundante.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada que se va a pintar| IMAGE| Sí| -  
`mask`| La máscara que define qué áreas de la imagen deben rellenarse| MASK| Sí| -  
`prompt`| Mensaje de texto para la generación de la imagen (predeterminado: cadena vacía)| STRING| No| -  
`re-muestreo de prompt`| Si se debe realizar un sobremuestreo en el mensaje de texto. Si está activo, modifica automáticamente el mensaje para una generación más creativa, pero los resultados no son deterministas (la misma semilla no producirá exactamente el mismo resultado). (predeterminado: false)| BOOLEAN| No| -  
`guía`| Intensidad de guía para el proceso de generación de la imagen (predeterminado: 60)| FLOAT| No| 1.5-100  
`pasos`| Número de pasos para el proceso de generación de la imagen (predeterminado: 50)| INT| No| 15-50  
`semilla`| La semilla aleatoria utilizada para crear el ruido. (predeterminado: 0)| INT| No| 0-18446744073709551615  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output_image`| La imagen generada con las áreas enmascaradas rellenadas según el mensaje de texto| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/es.md)

* * *

**Source fingerprint (SHA-256):** `ae2708d9e4b99ecb142fca0693c3973957c5677e8121eb5e34d30f872d7102c0`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/FluxProFillNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/FluxProFillNode)

[Flux.1 expandir imagen](https://docs.comfy.org/es/built-in-nodes/FluxProExpandNode)[Flux 1.1 [pro] Ultra imagen](https://docs.comfy.org/es/built-in-nodes/FluxProUltraImageNode)
