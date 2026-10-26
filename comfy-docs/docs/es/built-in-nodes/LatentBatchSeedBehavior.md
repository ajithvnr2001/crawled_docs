---
url: https://docs.comfy.org/es/built-in-nodes/LatentBatchSeedBehavior/
title: Comportamiento semilla de lote latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:03.096056+00:00
---

# Comportamiento semilla de lote latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentBatchSeedBehavior/

Avanzado

# Comportamiento semilla de lote latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentBatchSeedBehavior está diseñado para modificar el comportamiento de la semilla en un lote de muestras latentes.

Copiar páginaCopiar página

El nodo `LatentBatchSeedBehavior` está diseñado para modificar el comportamiento de la semilla en un lote de muestras latentes. Permite aleatorizar o fijar la semilla en todo el lote, influyendo así en el proceso de generación al introducir variabilidad o mantener consistencia en los resultados generados.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras`| El parámetro `muestras` representa el lote de muestras latentes a procesar. Su modificación depende del comportamiento de semilla elegido, afectando la consistencia o variabilidad de los resultados generados.| `LATENT`  
`comportamiento_de_semilla`| El parámetro `comportamiento_de_semilla` determina si la semilla para el lote de muestras latentes debe aleatorizarse o fijarse. Esta elección impacta significativamente el proceso de generación al introducir variabilidad o garantizar consistencia en todo el lote.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La salida es una versión modificada de las muestras latentes de entrada, con ajustes realizados según el comportamiento de semilla especificado. Mantiene o altera el índice del lote para reflejar el comportamiento de semilla elegido.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentBatchSeedBehavior.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentBatchSeedBehavior)

[Sumar latentes](https://docs.comfy.org/es/built-in-nodes/LatentAdd)[Concatenar latentes](https://docs.comfy.org/es/built-in-nodes/LatentConcat)
