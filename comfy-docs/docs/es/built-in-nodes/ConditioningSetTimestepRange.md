---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningSetTimestepRange/
title: Acondicionamiento (Establecer rango de pasos) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:40.894881+00:00
---

# Acondicionamiento (Establecer rango de pasos) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningSetTimestepRange/

Transformación

# Acondicionamiento (Establecer rango de pasos) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para ajustar el aspecto temporal del condicionamiento estableciendo un rango específico de pasos de tiempo.

Copiar páginaCopiar página

Este nodo está diseñado para ajustar el aspecto temporal del condicionamiento estableciendo un rango específico de pasos de tiempo. Permite un control preciso sobre los puntos de inicio y finalización del proceso de condicionamiento, posibilitando una generación más dirigida y eficiente.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`CONDITIONING`| La entrada de condicionamiento representa el estado actual del proceso de generación, que este nodo modifica al establecer un rango específico de pasos de tiempo.| CONDITIONING  
`inicio`| El parámetro de inicio especifica el comienzo del rango de pasos de tiempo como un porcentaje del proceso total de generación, permitiendo un control preciso sobre cuándo comienzan los efectos del condicionamiento.| `FLOAT`  
`fin`| El parámetro de finalización define el punto final del rango de pasos de tiempo como un porcentaje, habilitando un control preciso sobre la duración y la conclusión de los efectos del condicionamiento.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`CONDITIONING`| La salida es el condicionamiento modificado con el rango de pasos de tiempo especificado aplicado, listo para su posterior procesamiento o generación.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetTimestepRange/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningSetTimestepRange.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningSetTimestepRange)

[Acondicionamiento (Establecer máscara)](https://docs.comfy.org/es/built-in-nodes/ConditioningSetMask)[Acondicionamiento (Poner a cero)](https://docs.comfy.org/es/built-in-nodes/ConditioningZeroOut)
