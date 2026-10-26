---
url: https://docs.comfy.org/es/built-in-nodes/CreateHookKeyframesInterpolated/
title: Crear hook keyframes Interp. - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:42.035917+00:00
---

# Crear hook keyframes Interp. - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CreateHookKeyframesInterpolated/

Programación

# Crear hook keyframes Interp. - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Crea una secuencia de fotogramas clave de hook con valores de intensidad interpolados entre un punto inicial y final.

Copiar páginaCopiar página

Crea una secuencia de fotogramas clave de hook con valores de intensidad interpolados entre un punto inicial y final. El nodo genera múltiples fotogramas clave que realizan una transición suave del parámetro de intensidad a lo largo de un rango porcentual específico del proceso de generación, utilizando varios métodos de interpolación para controlar la curva de transición.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`strength_start`| Valor de intensidad inicial para la secuencia de interpolación (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 10.0  
`strength_end`| Valor de intensidad final para la secuencia de interpolación (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 10.0  
`interpolación`| Método de interpolación utilizado para la transición entre valores de intensidad (predeterminado: LINEAR)| COMBO| Sí| `LINEAR`  
`EASE_IN`  
`EASE_OUT`  
`EASE_IN_OUT`  
`EASE_OUT_IN`  
`SINE`  
`CUBIC`  
`QUARTIC`  
`QUINTIC`  
`EXPO`  
`CIRC`  
`BACK`  
`BOUNCE`  
`ELASTIC`  
`start_percent`| Posición porcentual inicial en el proceso de generación (predeterminado: 0.0)| FLOAT| Sí| 0.0 - 1.0  
`end_percent`| Posición porcentual final en el proceso de generación (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 1.0  
`keyframes_count`| Número de fotogramas clave a generar en la secuencia de interpolación (predeterminado: 5)| INT| Sí| 2 - 100  
`print_keyframes`| Si se debe imprimir la información de los fotogramas clave generados en el registro (predeterminado: False)| BOOLEAN| Sí| True/False  
`prev_hook_kf`| Grupo opcional de fotogramas clave de hook anterior al que añadir| HOOK_KEYFRAMES| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`HOOK_KF`| El grupo de fotogramas clave de hook generado que contiene la secuencia interpolada| HOOK_KEYFRAMES  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/es.md)

* * *

**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CreateHookKeyframesInterpolated.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CreateHookKeyframesInterpolated)

[Crear hook keyframes desde flotantes](https://docs.comfy.org/es/built-in-nodes/CreateHookKeyframesFromFloats)[Establecer fotogramas clave de gancho](https://docs.comfy.org/es/built-in-nodes/SetHookKeyframes)
