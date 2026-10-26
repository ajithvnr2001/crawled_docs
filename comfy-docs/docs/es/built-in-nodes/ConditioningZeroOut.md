---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningZeroOut/
title: Acondicionamiento (Poner a cero) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:41.059211+00:00
---

# Acondicionamiento (Poner a cero) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningZeroOut/

Transformación

# Acondicionamiento (Poner a cero) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo pone a cero elementos específicos dentro de la estructura de datos de condicionamiento

Copiar páginaCopiar página

Este nodo pone a cero elementos específicos dentro de la estructura de datos de condicionamiento, neutralizando efectivamente su influencia en pasos posteriores del procesamiento. Está diseñado para operaciones avanzadas de condicionamiento donde se requiere la manipulación directa de la representación interna del condicionamiento.

## 

​

Entradas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`CONDITIONING`| La estructura de datos de condicionamiento que se modificará. Este nodo pone a cero los elementos ‘pooled_output’ dentro de cada entrada de condicionamiento, si están presentes.| CONDITIONING  
  
## 

​

Salidas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`CONDITIONING`| La estructura de datos de condicionamiento modificada, con los elementos ‘pooled_output’ establecidos en cero cuando corresponda.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningZeroOut.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningZeroOut)

[Acondicionamiento (Establecer rango de pasos)](https://docs.comfy.org/es/built-in-nodes/ConditioningSetTimestepRange)[Condicionamiento Pixal3D](https://docs.comfy.org/es/built-in-nodes/Pixal3DConditioning)
