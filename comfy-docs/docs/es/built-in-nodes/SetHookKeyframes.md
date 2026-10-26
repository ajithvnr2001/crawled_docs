---
url: https://docs.comfy.org/es/built-in-nodes/SetHookKeyframes/
title: Establecer fotogramas clave de gancho - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:31.234897+00:00
---

# Establecer fotogramas clave de gancho - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SetHookKeyframes/

Programación

# Establecer fotogramas clave de gancho - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Set Hook Keyframes permite aplicar programación de fotogramas clave a grupos de hooks existentes.

Copiar páginaCopiar página

El nodo Set Hook Keyframes permite aplicar programación de fotogramas clave a grupos de hooks existentes. Toma un grupo de hooks y, opcionalmente, aplica información de temporización de fotogramas clave para controlar cuándo se ejecutan los diferentes hooks durante el proceso de generación. Cuando se proporcionan fotogramas clave, el nodo clona el grupo de hooks y establece la temporización de fotogramas clave en todos los hooks dentro del grupo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`ganchos`| El grupo de hooks al que se aplicará la programación de fotogramas clave| HOOKS| Sí| -  
`gancho_kf`| Grupo opcional de fotogramas clave que contiene información de temporización para la ejecución de hooks| HOOK_KEYFRAMES| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`ganchos`| El grupo de hooks modificado con la programación de fotogramas clave aplicada (clonado si se proporcionaron fotogramas clave)| HOOKS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/es.md)

* * *

**Source fingerprint (SHA-256):** `48908e5247b18e5b7b1d894c2f1adcf6403e499125b0c3eb05978584b3d5759b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SetHookKeyframes.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SetHookKeyframes)

[Crear hook keyframes Interp.](https://docs.comfy.org/es/built-in-nodes/CreateHookKeyframesInterpolated)[Rango de pasos de tiempo](https://docs.comfy.org/es/built-in-nodes/ConditioningTimestepsRange)
