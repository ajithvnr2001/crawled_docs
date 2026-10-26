---
url: https://docs.comfy.org/es/built-in-nodes/LatentInterpolate/
title: Interpolar latentes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:03.778536+00:00
---

# Interpolar latentes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentInterpolate/

Avanzado

# Interpolar latentes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentInterpolate está diseñado para realizar interpolación entre dos conjuntos de muestras latentes basándose en una proporción especificada

Copiar páginaCopiar página

El nodo LatentInterpolate está diseñado para realizar interpolación entre dos conjuntos de muestras latentes basándose en una proporción especificada, combinando las características de ambos conjuntos para producir un nuevo conjunto intermedio de muestras latentes.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras1`| El primer conjunto de muestras latentes a interpolar. Sirve como punto de partida para el proceso de interpolación.| `LATENT`  
`muestras2`| El segundo conjunto de muestras latentes a interpolar. Sirve como punto final para el proceso de interpolación.| `LATENT`  
`proporción`| Un valor de punto flotante que determina el peso de cada conjunto de muestras en la salida interpolada. Una proporción de 0 produce una copia del primer conjunto, mientras que una proporción de 1 produce una copia del segundo conjunto.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La salida es un nuevo conjunto de muestras latentes que representan un estado interpolado entre los dos conjuntos de entrada, basado en la proporción especificada.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentInterpolate.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentInterpolate)

[Cortar latente a lote](https://docs.comfy.org/es/built-in-nodes/LatentCutToBatch)[Multiplicar latente](https://docs.comfy.org/es/built-in-nodes/LatentMultiply)
