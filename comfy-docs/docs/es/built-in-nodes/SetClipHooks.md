---
url: https://docs.comfy.org/es/built-in-nodes/SetClipHooks/
title: Establecer ganchos CLIP - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:30.884124+00:00
---

# Establecer ganchos CLIP - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SetClipHooks/

CLIP

# Establecer ganchos CLIP - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SetClipHooks permite aplicar hooks personalizados a un modelo CLIP, posibilitando modificaciones avanzadas en su comportamiento.

Copiar páginaCopiar página

El nodo `SetClipHooks` permite aplicar hooks personalizados a un modelo CLIP, posibilitando modificaciones avanzadas en su comportamiento. Puede aplicar hooks a las salidas de condicionamiento y habilitar opcionalmente la funcionalidad de programación de CLIP. Este nodo crea una copia clonada del modelo CLIP de entrada con las configuraciones de hooks especificadas aplicadas.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP al que se le aplicarán los hooks| CLIP| Sí| -  
`aplicar_a_conds`| Si se aplican hooks a las salidas de condicionamiento (predeterminado: True)| BOOLEAN| Sí| -  
`programar_clip`| Si se habilita la programación de CLIP (predeterminado: False)| BOOLEAN| Sí| -  
`ganchos`| Grupo de hooks opcional para aplicar al modelo CLIP| HOOKS| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`clip`| Un modelo CLIP clonado con los hooks especificados aplicados| CLIP  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/es.md)

* * *

**Source fingerprint (SHA-256):** `904a878638c015bdce1983ae0c11a2b580b271090fca39edb304f6ed90c8c66d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SetClipHooks.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SetClipHooks)

[Amortiguación tangencial CFG](https://docs.comfy.org/es/built-in-nodes/TCFG)[Combinar pares de acondicionamiento](https://docs.comfy.org/es/built-in-nodes/PairConditioningCombine)
