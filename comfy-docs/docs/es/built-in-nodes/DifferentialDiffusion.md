---
url: https://docs.comfy.org/es/built-in-nodes/DifferentialDiffusion/
title: Difusi\u00f3n diferencial - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:43.753306+00:00
---

# Difusión diferencial - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/DifferentialDiffusion/

Experimental

# Difusión diferencial - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Difusión Diferencial modifica el proceso de eliminación de ruido aplicando una máscara binaria basada en umbrales de paso de tiempo.

Copiar páginaCopiar página

El nodo Difusión Diferencial modifica el proceso de eliminación de ruido aplicando una máscara binaria basada en umbrales de paso de tiempo. Crea una máscara que combina entre la máscara de eliminación de ruido original y una máscara binaria basada en umbrales, permitiendo un ajuste controlado de la intensidad del proceso de difusión.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de difusión a modificar| MODEL| Sí| -  
`intensidad`| Controla la intensidad de combinación entre la máscara de eliminación de ruido original y la máscara binaria de umbral (predeterminado: 1.0)| FLOAT| No| 0.0 - 1.0  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`modelo`| El modelo de difusión modificado con la función de máscara de eliminación de ruido actualizada| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/es.md)

* * *

**Source fingerprint (SHA-256):** `3b1727baa6c546516f5dfb53e6e39f27fc7429cde2ac7fd7dfbab99eebb39816`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/DifferentialDiffusion.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/DifferentialDiffusion)

[Super resolución ControlNet Stable Cascade](https://docs.comfy.org/es/built-in-nodes/StableCascade_SuperResolutionControlnet)[Flux KV cache](https://docs.comfy.org/es/built-in-nodes/FluxKVCache)
