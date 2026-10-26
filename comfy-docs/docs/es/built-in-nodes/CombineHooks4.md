---
url: https://docs.comfy.org/es/built-in-nodes/CombineHooks4/
title: Combinar hooks [4] - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:38.588767+00:00
---

# Combinar hooks [4] - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CombineHooks4/

Hooks

# Combinar hooks [4] - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Combinar Ganchos [4] fusiona hasta cuatro grupos de ganchos separados en un único grupo combinado.

Copiar páginaCopiar página

El nodo **Combinar Ganchos [4]** fusiona hasta cuatro grupos de ganchos separados en un único grupo combinado. Toma cualquier combinación de las cuatro entradas de ganchos disponibles y las combina utilizando el sistema de combinación de ganchos de ComfyUI. Esto permite consolidar múltiples configuraciones de ganchos para un procesamiento optimizado en flujos de trabajo avanzados.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Tipo de Entrada| Valor por Defecto| Rango  
---|---|---|---|---|---  
`hooks_A`| Primer grupo de ganchos a combinar| HOOKS| opcional| None| -  
`hooks_B`| Segundo grupo de ganchos a combinar| HOOKS| opcional| None| -  
`hooks_C`| Tercer grupo de ganchos a combinar| HOOKS| opcional| None| -  
`hooks_D`| Cuarto grupo de ganchos a combinar| HOOKS| opcional| None| -  
  
**Nota:** Las cuatro entradas de ganchos son opcionales. El nodo combinará únicamente los grupos de ganchos que se proporcionen y devolverá un grupo de ganchos vacío si no hay entradas conectadas.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`HOOKS`| Grupo de ganchos combinado que contiene todas las configuraciones de ganchos proporcionadas| HOOKS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks4/es.md)

* * *

**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CombineHooks4.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CombineHooks4)

[Combinar hooks [2]](https://docs.comfy.org/es/built-in-nodes/CombineHooks2)[Combinar hooks [8]](https://docs.comfy.org/es/built-in-nodes/CombineHooks8)
