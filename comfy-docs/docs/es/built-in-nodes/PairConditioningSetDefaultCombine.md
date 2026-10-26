---
url: https://docs.comfy.org/es/built-in-nodes/PairConditioningSetDefaultCombine/
title: Combinar pares de acondicionamiento (Establecer por defecto) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:16.920706+00:00
---

# Combinar pares de acondicionamiento (Establecer por defecto) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PairConditioningSetDefaultCombine/

Hooks

# Combinar pares de acondicionamiento (Establecer por defecto) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo PairConditioningSetDefaultAndCombine establece valores de condicionamiento predeterminados y los combina con los datos de condicionamiento de

Copiar páginaCopiar página

El nodo **PairConditioningSetDefaultAndCombine** establece valores de condicionamiento predeterminados y los combina con los datos de condicionamiento de entrada. Toma entradas de condicionamiento positivo y negativo junto con sus contrapartes predeterminadas, luego las procesa a través del sistema de hooks de ComfyUI para producir salidas de condicionamiento finales que incorporan los valores predeterminados.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`positive`| La entrada de condicionamiento positivo principal a procesar| CONDITIONING| Sí| -  
`negative`| La entrada de condicionamiento negativo principal a procesar| CONDITIONING| Sí| -  
`positive_DEFAULT`| Los valores de condicionamiento positivo predeterminados a utilizar como respaldo| CONDITIONING| Sí| -  
`negative_DEFAULT`| Los valores de condicionamiento negativo predeterminados a utilizar como respaldo| CONDITIONING| Sí| -  
`hooks`| Grupo opcional de hooks para lógica de procesamiento personalizada| HOOKS| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`positive`| El condicionamiento positivo procesado con valores predeterminados incorporados| CONDITIONING  
`negative`| El condicionamiento negativo procesado con valores predeterminados incorporados| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultCombine/es.md)

* * *

**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PairConditioningSetDefaultCombine.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PairConditioningSetDefaultCombine)

[Acondicionamiento (Establecer combinación predeterminada)](https://docs.comfy.org/es/built-in-nodes/ConditioningSetDefaultCombine)[DeprecatedCheckpointLoader](https://docs.comfy.org/es/built-in-nodes/DeprecatedCheckpointLoader)
