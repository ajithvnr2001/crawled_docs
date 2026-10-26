---
url: https://docs.comfy.org/es/built-in-nodes/ModelMergeSubtract/
title: Fusionar modelo (restar) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:14.160265+00:00
---

# Fusionar modelo (restar) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelMergeSubtract/

Fusión

# Fusionar modelo (restar) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para operaciones avanzadas de fusión de modelos

Copiar páginaCopiar página

Este nodo está diseñado para operaciones avanzadas de fusión de modelos, específicamente para restar los parámetros de un modelo de otro según un multiplicador especificado. Permite personalizar los comportamientos del modelo ajustando la influencia de los parámetros de un modelo sobre otro, facilitando la creación de nuevos modelos híbridos.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`model1`| El modelo base del cual se restarán los parámetros.| `MODEL`  
`model2`| El modelo cuyos parámetros se restarán del modelo base.| `MODEL`  
`multiplier`| Un valor de punto flotante que escala el efecto de sustracción sobre los parámetros del modelo base.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`model`| El modelo resultante después de restar los parámetros de un modelo de otro, escalados por el multiplicador.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSubtract/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelMergeSubtract.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelMergeSubtract)

[Fusionar modelo (simple)](https://docs.comfy.org/es/built-in-nodes/ModelMergeSimple)[Guardar modelo](https://docs.comfy.org/es/built-in-nodes/ModelSave)
