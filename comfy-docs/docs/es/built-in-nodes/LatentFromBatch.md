---
url: https://docs.comfy.org/es/built-in-nodes/LatentFromBatch/
title: Latente de lote - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:03.850077+00:00
---

# Latente de lote - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentFromBatch/

Lote

# Latente de lote - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para extraer un subconjunto específico de muestras latentes de un lote determinado

Copiar páginaCopiar página

Este nodo está diseñado para extraer un subconjunto específico de muestras latentes de un lote determinado, según el índice y la longitud del lote especificados. Permite el procesamiento selectivo de muestras latentes, facilitando operaciones en segmentos más pequeños del lote para lograr eficiencia o manipulación dirigida.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`muestras`| La colección de muestras latentes de la cual se extraerá un subconjunto. Este parámetro es crucial para determinar el lote fuente de muestras a procesar.| `LATENT`  
`índice_lote`| Especifica el índice inicial dentro del lote desde el cual comenzará el subconjunto de muestras. Este parámetro permite la extracción dirigida de muestras desde posiciones específicas en el lote.| `INT`  
`longitud`| Define la cantidad de muestras que se extraerán a partir del índice inicial especificado. Este parámetro controla el tamaño del subconjunto a procesar, permitiendo una manipulación flexible de los segmentos del lote.| `INT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`latent`| El subconjunto extraído de muestras latentes, ahora disponible para su posterior procesamiento o análisis.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFromBatch/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentFromBatch.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentFromBatch)

[Lote de latentes (obsoleto)](https://docs.comfy.org/es/built-in-nodes/LatentBatch)[Reagrupar latentes](https://docs.comfy.org/es/built-in-nodes/RebatchLatents)
