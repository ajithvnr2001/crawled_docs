---
url: https://docs.comfy.org/es/built-in-nodes/CLIPMergeSubtract/
title: Fusionar CLIP (restar) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:36.062088+00:00
---

# Fusionar CLIP (restar) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CLIPMergeSubtract/

Fusión

# Fusionar CLIP (restar) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CLIPMergeSubtract realiza la fusión de modelos restando los pesos de un modelo CLIP de otro.

Copiar páginaCopiar página

El nodo CLIPMergeSubtract realiza la fusión de modelos restando los pesos de un modelo CLIP de otro. Crea un nuevo modelo CLIP clonando el primer modelo y luego restando los parches de clave del segundo modelo, con un multiplicador ajustable para controlar la fuerza de la resta. Esto permite un ajuste fino de la combinación de modelos al eliminar características específicas del modelo base.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`clip1`| El modelo CLIP base que será clonado y modificado| CLIP| Sí| -  
`clip2`| El modelo CLIP cuyos parches de clave se restarán del modelo base| CLIP| Sí| -  
`multiplicador`| Controla la fuerza de la operación de resta (predeterminado: 1.0)| FLOAT| Sí| -10.0 a 10.0 (paso: 0.01)  
  
**Nota:** El nodo excluye los parámetros `.position_ids` y `.logit_scale` de la operación de resta, independientemente del valor del multiplicador.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`clip`| El modelo CLIP resultante tras restar los pesos del segundo modelo del primero| CLIP  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/es.md)

* * *

**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CLIPMergeSubtract.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CLIPMergeSubtract)

[Fusionar CLIP (simple)](https://docs.comfy.org/es/built-in-nodes/CLIPMergeSimple)[Guardar CLIP](https://docs.comfy.org/es/built-in-nodes/CLIPSave)
