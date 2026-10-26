---
url: https://docs.comfy.org/es/built-in-nodes/CreateHookKeyframe/
title: Crear hook keyframe - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:42.190524+00:00
---

# Crear hook keyframe - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CreateHookKeyframe/

Programación

# Crear hook keyframe - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Crear Fotograma Clave de Hook permite definir puntos específicos en un proceso de generación donde cambia el comportamiento del hook.

Copiar páginaCopiar página

El nodo Crear Fotograma Clave de Hook permite definir puntos específicos en un proceso de generación donde cambia el comportamiento del hook. Crea fotogramas clave que modifican la intensidad de los hooks en porcentajes particulares del progreso de generación, y estos fotogramas clave pueden encadenarse para crear patrones de programación complejos.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`multiplicador_fuerza`| Multiplicador de la intensidad del hook en este fotograma clave (predeterminado: 1.0)| FLOAT| Sí| -20.0 a 20.0  
`porcentaje_inicio`| El punto porcentual en el proceso de generación donde este fotograma clave surte efecto (predeterminado: 0.0)| FLOAT| Sí| 0.0 a 1.0  
`prev_hook_kf`| Grupo opcional de fotogramas clave de hook anterior al que agregar este fotograma clave| HOOK_KEYFRAMES| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`HOOK_KF`| Un grupo de fotogramas clave de hook que incluye el fotograma clave recién creado| HOOK_KEYFRAMES  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/es.md)

* * *

**Source fingerprint (SHA-256):** `51893311a0623cafcf8c2d8af00e4005ca2fea2df9474e87d7d4b332b38435c3`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CreateHookKeyframe.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CreateHookKeyframe)

[Crear hook model como LoRA (MO)](https://docs.comfy.org/es/built-in-nodes/CreateHookModelAsLoraModelOnly)[Crear hook keyframes desde flotantes](https://docs.comfy.org/es/built-in-nodes/CreateHookKeyframesFromFloats)
