---
url: https://docs.comfy.org/es/built-in-nodes/LatentApplyOperation/
title: Aplicar operaci\u00f3n a latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:02.736169+00:00
---

# Aplicar operación a latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentApplyOperation/

Operaciones

# Aplicar operación a latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentApplyOperation aplica una operación latente especificada a las muestras latentes.

Copiar páginaCopiar página

El nodo LatentApplyOperation aplica una operación latente especificada a las muestras latentes. Toma datos latentes y una operación como entradas, procesa las muestras latentes utilizando la operación proporcionada y devuelve los datos latentes modificados. Este nodo le permite transformar o manipular representaciones latentes en su flujo de trabajo. Este nodo está actualmente marcado como experimental.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`muestras`| Las muestras latentes que serán procesadas por la operación| LATENT| Sí| -  
`operación`| La operación a aplicar a las muestras latentes| LATENT_OPERATION| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| Las muestras latentes modificadas después de aplicar la operación| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/es.md)

* * *

**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentApplyOperation.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentApplyOperation)

[Audio latente Ace Step 1.0 vacío](https://docs.comfy.org/es/built-in-nodes/EmptyAceStepLatentAudio)[Aplicar operación CFG a latente](https://docs.comfy.org/es/built-in-nodes/LatentApplyOperationCFG)
