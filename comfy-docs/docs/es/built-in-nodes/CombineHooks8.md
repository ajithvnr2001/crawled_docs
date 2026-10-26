---
url: https://docs.comfy.org/es/built-in-nodes/CombineHooks8/
title: Combinar hooks [8] - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:38.946035+00:00
---

# Combinar hooks [8] - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CombineHooks8/

Hooks

# Combinar hooks [8] - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Combinar Hooks [8] fusiona hasta ocho grupos de hooks diferentes en un único grupo combinado.

Copiar páginaCopiar página

El nodo Combinar Hooks [8] fusiona hasta ocho grupos de hooks diferentes en un único grupo combinado. Toma múltiples entradas de hooks y las combina utilizando la funcionalidad de combinación de hooks de ComfyUI. Esto permite consolidar múltiples configuraciones de hooks para un procesamiento optimizado en flujos de trabajo avanzados.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Tipo de Entrada| Valor por Defecto| Rango  
---|---|---|---|---|---  
`hooks_A`| Primer grupo de hooks a combinar| HOOKS| opcional| None| -  
`hooks_B`| Segundo grupo de hooks a combinar| HOOKS| opcional| None| -  
`hooks_C`| Tercer grupo de hooks a combinar| HOOKS| opcional| None| -  
`hooks_D`| Cuarto grupo de hooks a combinar| HOOKS| opcional| None| -  
`hooks_E`| Quinto grupo de hooks a combinar| HOOKS| opcional| None| -  
`hooks_F`| Sexto grupo de hooks a combinar| HOOKS| opcional| None| -  
`hooks_G`| Séptimo grupo de hooks a combinar| HOOKS| opcional| None| -  
`hooks_H`| Octavo grupo de hooks a combinar| HOOKS| opcional| None| -  
  
**Nota:** Todos los parámetros de entrada son opcionales. El nodo combinará únicamente los grupos de hooks que se proporcionen, ignorando aquellos que se dejen vacíos. Puedes proporcionar desde uno hasta ocho grupos de hooks para su combinación.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`HOOKS`| Un único grupo de hooks combinado que contiene todas las configuraciones de hooks proporcionadas| HOOKS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks8/es.md)

* * *

**Source fingerprint (SHA-256):** `8cd13ec6710a9b2905c14301cfd15be616c00f1b4140451cdf0915f091c77197`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CombineHooks8.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CombineHooks8)

[Combinar hooks [4]](https://docs.comfy.org/es/built-in-nodes/CombineHooks4)[Acondicionamiento (Establecer combinación predeterminada)](https://docs.comfy.org/es/built-in-nodes/ConditioningSetDefaultCombine)
