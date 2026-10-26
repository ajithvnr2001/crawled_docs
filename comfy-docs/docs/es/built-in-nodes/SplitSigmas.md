---
url: https://docs.comfy.org/es/built-in-nodes/SplitSigmas/
title: Dividir sigmas - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:32.503257+00:00
---

# Dividir sigmas - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SplitSigmas/

Sigmas

# Dividir sigmas - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SplitSigmas está diseñado para dividir una secuencia de valores sigma en dos partes basándose en un paso especificado.

Copiar páginaCopiar página

El nodo SplitSigmas está diseñado para dividir una secuencia de valores sigma en dos partes basándose en un paso especificado. Esta funcionalidad es crucial para operaciones que requieren un manejo o procesamiento diferente de las partes inicial y posterior de la secuencia sigma, permitiendo una manipulación más flexible y dirigida de estos valores.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`sigmas`| El parámetro ‘sigmas’ representa la secuencia de valores sigma que se va a dividir. Es esencial para determinar el punto de división y las dos secuencias resultantes de valores sigma, afectando la ejecución y los resultados del nodo.| `SIGMAS`  
`paso`| El parámetro ‘step’ especifica el índice en el cual se debe dividir la secuencia sigma. Desempeña un papel crítico en la definición del límite entre las dos secuencias sigma resultantes, influyendo en la funcionalidad del nodo y las características de la salida.| `INT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`sigmas_altos`| El nodo genera dos secuencias de valores sigma, cada una representando una parte de la secuencia original dividida en el paso especificado. Estas salidas son cruciales para operaciones posteriores que requieren un manejo diferenciado de los valores sigma.| `SIGMAS`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmas/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SplitSigmas.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SplitSigmas)

[Establecer primera sigma](https://docs.comfy.org/es/built-in-nodes/SetFirstSigma)[Dividir sigmas (desruidar)](https://docs.comfy.org/es/built-in-nodes/SplitSigmasDenoise)
