---
url: https://docs.comfy.org/es/built-in-nodes/PairConditioningCombine/
title: Combinar pares de acondicionamiento - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:16.744118+00:00
---

# Combinar pares de acondicionamiento - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PairConditioningCombine/

Par de condicionamiento

# Combinar pares de acondicionamiento - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo PairConditioningCombine fusiona dos pares de condicionamiento separados (cada uno compuesto por un condicionamiento positivo y uno negativo) en un

Copiar páginaCopiar página

El nodo PairConditioningCombine fusiona dos pares de condicionamiento separados (cada uno compuesto por un condicionamiento positivo y uno negativo) en un único par combinado. Toma el condicionamiento positivo y negativo de dos fuentes diferentes y los combina utilizando la lógica interna de ComfyUI, generando un condicionamiento positivo final y un condicionamiento negativo final. Este nodo es experimental y está diseñado para flujos de trabajo avanzados de manipulación de condicionamiento.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`positivo_A`| Primera entrada de condicionamiento positivo| CONDITIONING| Sí| -  
`negativo_A`| Primera entrada de condicionamiento negativo| CONDITIONING| Sí| -  
`positivo_B`| Segunda entrada de condicionamiento positivo| CONDITIONING| Sí| -  
`negativo_B`| Segunda entrada de condicionamiento negativo| CONDITIONING| Sí| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`positivo`| Salida de condicionamiento positivo combinado| CONDITIONING  
`negativo`| Salida de condicionamiento negativo combinado| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/es.md)

* * *

**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PairConditioningCombine.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PairConditioningCombine)

[Establecer ganchos CLIP](https://docs.comfy.org/es/built-in-nodes/SetClipHooks)[Establecer propiedades de pares de acondicionamiento](https://docs.comfy.org/es/built-in-nodes/PairConditioningSetProperties)
