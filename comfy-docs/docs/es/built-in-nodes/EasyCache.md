---
url: https://docs.comfy.org/es/built-in-nodes/EasyCache/
title: EasyCache - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:44.346758+00:00
---

# EasyCache - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EasyCache/

Depuración

# EasyCache - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo EasyCache agrega un sistema de caché nativo a un modelo de difusión que acelera el muestreo al reutilizar resultados de pasos calculados previamente en

Copiar páginaCopiar página

El nodo EasyCache agrega un sistema de caché nativo a un modelo de difusión que acelera el muestreo al reutilizar resultados de pasos calculados previamente en lugar de recalcular cada paso. Se activa solo entre un punto de inicio y fin configurables del proceso de muestreo y omite pasos cuando el cambio estimado en la salida se mantiene por debajo de un umbral definido por el usuario. Este es un nodo experimental destinado a uso de depuración avanzada.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo al que se agregará EasyCache.| MODEL| Sí| -  
`umbral_de_reutilización`| El umbral para reutilizar pasos en caché (predeterminado: 0.2).| FLOAT| Sí| 0.0 - 3.0  
`porcentaje_inicial`| El paso de muestreo relativo para comenzar a usar EasyCache (predeterminado: 0.15).| FLOAT| Sí| 0.0 - 1.0  
`porcentaje_final`| El paso de muestreo relativo para finalizar el uso de EasyCache (predeterminado: 0.95).| FLOAT| Sí| 0.0 - 1.0  
`detallado`| Si se debe registrar información detallada (predeterminado: False).| BOOLEAN| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo con la funcionalidad EasyCache agregada.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/es.md)

* * *

**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EasyCache.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EasyCache)

[Voxel a malla (básico)](https://docs.comfy.org/es/built-in-nodes/VoxelToMeshBasic)[LazyCache](https://docs.comfy.org/es/built-in-nodes/LazyCache)
