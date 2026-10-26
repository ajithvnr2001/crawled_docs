---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningMultiply/
title: Condicionamiento (Multiplicar) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:40.371738+00:00
---

# Condicionamiento (Multiplicar) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningMultiply/

Transformación

# Condicionamiento (Multiplicar) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo multiplica los valores de condicionamiento por un factor especificado

Copiar páginaCopiar página

Este nodo multiplica los valores de condicionamiento por un factor especificado, permitiéndote escalar la influencia del condicionamiento en el proceso de generación. Funciona aplicando el multiplicador tanto al tensor principal de condicionamiento como a los valores de salida agrupados.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`conditioning`| Los datos de condicionamiento que se escalarán| CONDITIONING| Sí| -  
`multiplier`| El factor por el cual multiplicar los valores de condicionamiento (predeterminado: 1.0)| FLOAT| Sí| -100.0 a 100.0 (paso: 0.01)  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`CONDITIONING`| Los datos de condicionamiento escalados con valores multiplicados| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningMultiply/es.md)

* * *

**Source fingerprint (SHA-256):** `8d241e3d5d91e513c24ade5b4bece4bf879fe093a4be6d53dab11a5a0bf55616`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningMultiply.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningMultiply)

[Acondicionamiento (Concatenar)](https://docs.comfy.org/es/built-in-nodes/ConditioningConcat)[Acondicionamiento (Establecer área)](https://docs.comfy.org/es/built-in-nodes/ConditioningSetArea)
