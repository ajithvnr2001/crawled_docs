---
url: https://docs.comfy.org/es/built-in-nodes/CFGOverride/
title: Anulaci\u00f3n de CFG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:36.282385+00:00
---

# Anulación de CFG - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CFGOverride/

Guiadores

# Anulación de CFG - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CFG Override sobrescribe la escala CFG (Guía libre de clasificador) a un valor fijo durante un rango porcentual (sigma) del proceso de muestreo.

Copiar páginaCopiar página

El nodo CFG Override sobrescribe la escala CFG (Guía libre de clasificador) a un valor fijo durante un rango porcentual (sigma) del proceso de muestreo. Cuando se utilizan varios nodos CFG Override, la sobrescritura más cercana al muestreador prevalece en los rangos superpuestos.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo al que se aplicará la sobrescritura de CFG.| MODEL| Sí|   
`cfg`| El valor fijo de escala CFG que se usará durante el rango de sobrescritura. Predeterminado: 1.0.| FLOAT| Sí| 0.0 a 100.0 (paso: 0.1)  
`porcentaje_inicio`| El punto de inicio del rango de sobrescritura como porcentaje del proceso de muestreo. Predeterminado: 0.0.| FLOAT| Sí| 0.0 a 1.0 (paso: 0.001)  
`porcentaje_fin`| El punto final del rango de sobrescritura como porcentaje del proceso de muestreo. Predeterminado: 1.0.| FLOAT| Sí| 0.0 a 1.0 (paso: 0.001)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`MODEL`| El modelo con el wrapper de sobrescritura de CFG aplicado.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/es.md)

* * *

**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CFGOverride.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CFGOverride)

[Guía CFG](https://docs.comfy.org/es/built-in-nodes/CFGGuider)[Guía CFG dual](https://docs.comfy.org/es/built-in-nodes/DualCFGGuider)
