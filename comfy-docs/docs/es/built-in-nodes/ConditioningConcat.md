---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningConcat/
title: Acondicionamiento (Concatenar) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:39.853025+00:00
---

# Acondicionamiento (Concatenar) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningConcat/

Transformación

# Acondicionamiento (Concatenar) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ConditioningConcat está diseñado para concatenar vectores de condicionamiento

Copiar páginaCopiar página

El nodo ConditioningConcat está diseñado para concatenar vectores de condicionamiento, fusionando específicamente el vector ‘conditioning_from’ en el vector ‘conditioning_to’. Esta operación es fundamental en escenarios donde la información de condicionamiento de dos fuentes debe combinarse en una única representación unificada.

## 

​

Entradas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`acondicionamiento_a`| Representa el conjunto principal de vectores de condicionamiento al que se concatenarán los vectores ‘conditioning_from’. Sirve como base para el proceso de concatenación.| `CONDITIONING`  
`acondicionamiento_de`| Contiene los vectores de condicionamiento que se concatenarán a los vectores ‘conditioning_to’. Este parámetro permite integrar información de condicionamiento adicional al conjunto existente.| `CONDITIONING`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`conditioning`| La salida es un conjunto unificado de vectores de condicionamiento, resultante de la concatenación de los vectores ‘conditioning_from’ en los vectores ‘conditioning_to’.| `CONDITIONING`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningConcat.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningConcat)

[Acondicionamiento StableZero123 (por lotes)](https://docs.comfy.org/es/built-in-nodes/StableZero123_Conditioning_Batched)[Condicionamiento (Multiplicar)](https://docs.comfy.org/es/built-in-nodes/ConditioningMultiply)
