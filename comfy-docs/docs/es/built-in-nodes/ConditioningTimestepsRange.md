---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningTimestepsRange/
title: Rango de pasos de tiempo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:41.119753+00:00
---

# Rango de pasos de tiempo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningTimestepsRange/

Hooks

# Rango de pasos de tiempo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ConditioningTimestepsRange crea tres rangos de pasos de tiempo distintos para controlar cuándo se aplican los efectos de condicionamiento durante el

Copiar páginaCopiar página

El nodo `ConditioningTimestepsRange` crea tres rangos de pasos de tiempo distintos para controlar cuándo se aplican los efectos de condicionamiento durante el proceso de generación. Toma valores de porcentaje de inicio y fin y divide el rango completo de pasos de tiempo (0.0 a 1.0) en tres segmentos: el rango principal entre los porcentajes especificados, el rango anterior al porcentaje de inicio y el rango posterior al porcentaje de fin.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`porcentaje_inicio`| El porcentaje inicial del rango de pasos de tiempo (predeterminado: 0.0)| FLOAT| Sí| 0.0 - 1.0  
`porcentaje_fin`| El porcentaje final del rango de pasos de tiempo (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 1.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`TIMESTEPS_RANGE`| El rango principal de pasos de tiempo definido por start_percent y end_percent| TIMESTEPS_RANGE  
`ANTES_DE_RANGO`| El rango de pasos de tiempo desde 0.0 hasta start_percent| TIMESTEPS_RANGE  
`DESPUÉS_DE_RANGO`| El rango de pasos de tiempo desde end_percent hasta 1.0| TIMESTEPS_RANGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/es.md)

* * *

**Source fingerprint (SHA-256):** `dee21b5ac80fabdeacf3f4a985550fff795702e02911400ae49a97baae834e5e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningTimestepsRange.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningTimestepsRange)

[Establecer fotogramas clave de gancho](https://docs.comfy.org/es/built-in-nodes/SetHookKeyframes)[Combinar hooks [2]](https://docs.comfy.org/es/built-in-nodes/CombineHooks2)
