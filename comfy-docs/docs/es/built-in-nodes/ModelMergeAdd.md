---
url: https://docs.comfy.org/es/built-in-nodes/ModelMergeAdd/
title: Fusionar modelo (sumar) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:12.979665+00:00
---

# Fusionar modelo (sumar) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelMergeAdd/

Fusión

# Fusionar modelo (sumar) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ModelMergeAdd está diseñado para fusionar dos modelos añadiendo parches clave de un modelo a otro.

Copiar páginaCopiar página

El nodo ModelMergeAdd está diseñado para fusionar dos modelos añadiendo parches clave de un modelo a otro. Este proceso implica clonar el primer modelo y luego aplicar parches del segundo modelo, lo que permite combinar características o comportamientos de ambos modelos.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`modelo1`| El primer modelo que se clonará y al cual se le añadirán los parches del segundo modelo. Sirve como modelo base para el proceso de fusión.| `MODEL`  
`modelo2`| El segundo modelo del cual se extraen parches clave y se añaden al primer modelo. Aporta características o comportamientos adicionales al modelo fusionado.| `MODEL`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`model`| El resultado de fusionar dos modelos añadiendo parches clave del segundo modelo al primero. Este modelo fusionado combina características o comportamientos de ambos modelos.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAdd/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelMergeAdd.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelMergeAdd)

[Guardar punto de control (solo imagen)](https://docs.comfy.org/es/built-in-nodes/ImageOnlyCheckpointSave)[Fusionar modelo (bloques)](https://docs.comfy.org/es/built-in-nodes/ModelMergeBlocks)
