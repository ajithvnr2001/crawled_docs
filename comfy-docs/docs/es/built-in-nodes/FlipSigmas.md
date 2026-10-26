---
url: https://docs.comfy.org/es/built-in-nodes/FlipSigmas/
title: Invertir sigmas - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:47.221275+00:00
---

# Invertir sigmas - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/FlipSigmas/

Sigmas

# Invertir sigmas - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo FlipSigmas está diseñado para manipular la secuencia de valores sigma utilizados en modelos de difusión

Copiar páginaCopiar página

El nodo `FlipSigmas` está diseñado para manipular la secuencia de valores sigma utilizados en modelos de difusión, invirtiendo su orden y asegurando que el primer valor no sea cero si originalmente lo era. Esta operación es crucial para adaptar los niveles de ruido en orden inverso, facilitando el proceso de generación en modelos que funcionan reduciendo gradualmente el ruido a partir de los datos.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`sigmas`| El parámetro `sigmas` representa la secuencia de valores sigma que se invertirá. Esta secuencia es crucial para controlar los niveles de ruido aplicados durante el proceso de difusión, y su inversión es esencial para el proceso de generación inversa.| `SIGMAS`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`sigmas`| La salida es la secuencia modificada de valores sigma, invertida y ajustada para garantizar que el primer valor no sea cero si originalmente lo era, lista para su uso en operaciones posteriores del modelo de difusión.| `SIGMAS`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FlipSigmas/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/FlipSigmas.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/FlipSigmas)

[Extender sigmas intermedias](https://docs.comfy.org/es/built-in-nodes/ExtendIntermediateSigmas)[Sigmas manuales](https://docs.comfy.org/es/built-in-nodes/ManualSigmas)
