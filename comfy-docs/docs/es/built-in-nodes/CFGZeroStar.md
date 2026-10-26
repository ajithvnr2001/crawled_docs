---
url: https://docs.comfy.org/es/built-in-nodes/CFGZeroStar/
title: CFGZeroStar - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:35.867438+00:00
---

# CFGZeroStar - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CFGZeroStar/

Guía

# CFGZeroStar - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CFGZeroStar aplica una técnica especializada de escalado de guía a modelos de difusión.

Copiar páginaCopiar página

El nodo CFGZeroStar aplica una técnica especializada de escalado de guía a modelos de difusión. Modifica el proceso de guía sin clasificador calculando un factor de escala optimizado basado en la diferencia entre las predicciones condicionales e incondicionales. Este enfoque ajusta la salida final para proporcionar un control mejorado sobre el proceso de generación, manteniendo al mismo tiempo la estabilidad del modelo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Tipo de Entrada| Valor por Defecto| Rango  
---|---|---|---|---|---  
`modelo`| El modelo de difusión que se modificará con la técnica de escalado de guía CFGZeroStar| MODEL| Sí| -| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`modelo_modificado`| El modelo modificado con el escalado de guía CFGZeroStar aplicado| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/es.md)

* * *

**Source fingerprint (SHA-256):** `1f5fcd1377c64609e28d85e453aaaa0bcc8f3ac322b7b7240f34f71aa113562a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CFGZeroStar.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CFGZeroStar)

[Normalización CFG](https://docs.comfy.org/es/built-in-nodes/CFGNorm)[LTXV Modality Guidance (A/V coupling)](https://docs.comfy.org/es/built-in-nodes/LTXVModalityGuidance)
