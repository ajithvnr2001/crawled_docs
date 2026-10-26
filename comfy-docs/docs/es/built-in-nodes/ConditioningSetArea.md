---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningSetArea/
title: Acondicionamiento (Establecer \u00e1rea) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:40.306583+00:00
---

# Acondicionamiento (Establecer área) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningSetArea/

Transformación

# Acondicionamiento (Establecer área) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para modificar la información de condicionamiento estableciendo áreas específicas dentro del contexto de condicionamiento.

Copiar páginaCopiar página

Este nodo está diseñado para modificar la información de condicionamiento estableciendo áreas específicas dentro del contexto de condicionamiento. Permite la manipulación espacial precisa de los elementos de condicionamiento, posibilitando ajustes y mejoras dirigidas según dimensiones e intensidad especificadas.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`CONDITIONING`| Los datos de condicionamiento que se modificarán. Sirven como base para aplicar ajustes espaciales.| CONDITIONING  
`ancho`| Especifica el ancho del área a establecer dentro del contexto de condicionamiento, influyendo en el alcance horizontal del ajuste.| `INT`  
`alto`| Determina la altura del área a establecer, afectando la extensión vertical de la modificación del condicionamiento.| `INT`  
`x`| El punto de inicio horizontal del área a establecer, posicionando el ajuste dentro del contexto de condicionamiento.| `INT`  
`y`| El punto de inicio vertical para el ajuste del área, estableciendo su posición dentro del contexto de condicionamiento.| `INT`  
`fuerza`| Define la intensidad de la modificación del condicionamiento dentro del área especificada, permitiendo un control matizado sobre el impacto del ajuste.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`CONDITIONING`| Los datos de condicionamiento modificados, que reflejan los ajustes y configuraciones de área especificados.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetArea/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningSetArea.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningSetArea)

[Condicionamiento (Multiplicar)](https://docs.comfy.org/es/built-in-nodes/ConditioningMultiply)[Acondicionamiento (Establecer área con porcentaje)](https://docs.comfy.org/es/built-in-nodes/ConditioningSetAreaPercentage)
