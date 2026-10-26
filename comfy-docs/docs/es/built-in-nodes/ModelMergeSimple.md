---
url: https://docs.comfy.org/es/built-in-nodes/ModelMergeSimple/
title: Fusionar modelo (simple) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:14.220009+00:00
---

# Fusionar modelo (simple) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelMergeSimple/

Fusión

# Fusionar modelo (simple) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ModelMergeSimple está diseñado para fusionar dos modelos combinando sus parámetros en función de una proporción especificada.

Copiar páginaCopiar página

El nodo ModelMergeSimple está diseñado para fusionar dos modelos combinando sus parámetros en función de una proporción especificada. Este nodo facilita la creación de modelos híbridos que integran las fortalezas o características de ambos modelos de entrada. El parámetro `ratio` determina la proporción de mezcla entre los dos modelos. Cuando este valor es 1, el modelo de salida es 100% `model1`, y cuando este valor es 0, el modelo de salida es 100% `model2`.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`model1`| El primer modelo a fusionar. Actúa como modelo base sobre el cual se aplican los parches del segundo modelo.| `MODEL`  
`model2`| El segundo modelo cuyos parches se aplican sobre el primer modelo, influenciados por la proporción especificada.| `MODEL`  
`ratio`| Cuando este valor es 1, el modelo de salida es 100% `model1`, y cuando este valor es 0, el modelo de salida es 100% `model2`.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`model`| El modelo fusionado resultante, que incorpora elementos de ambos modelos de entrada según la proporción especificada.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSimple/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelMergeSimple.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelMergeSimple)

[Fusionar modelo (bloques)](https://docs.comfy.org/es/built-in-nodes/ModelMergeBlocks)[Fusionar modelo (restar)](https://docs.comfy.org/es/built-in-nodes/ModelMergeSubtract)
