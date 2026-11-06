---
url: https://docs.comfy.org/es/built-in-nodes/PikaSFXNode/
title: PikaSFXNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-06T14:51:54.533661+00:00
---

# PikaSFXNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PikaSFXNode/

Audio

# PikaSFXNode - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo genera un efecto de sonido a partir de una descripción de texto con Pika.

Copiar páginaCopiar página

Este nodo genera un efecto de sonido a partir de una descripción de texto con Pika. Describe el sonido y cuánto tiempo debe durar, y el nodo devuelve un clip de audio.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`prompt`| Qué debe ser el efecto de sonido. No debe estar vacío. Predeterminado: "" (cadena vacía).| STRING| Sí| 1 a 4000 caracteres  
`duration`| Duración del efecto de sonido en segundos. Predeterminado: 5.0.| FLOAT| Sí| 1.0 a 20.0 (paso: 0.1)  
`seed`| Semilla para el muestreo. Predeterminado: 42.| INT| Sí| 0 a 2147483647  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`AUDIO`| El efecto de sonido generado.| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSFXNode/es.md)

* * *

**Source fingerprint (SHA-256):** `a1dcd374d158009aceae2aecd87ed08f8105bff7db75160a99e8624be9459dfa`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PikaSFXNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PikaSFXNode)

[PikaMusicNode](https://docs.comfy.org/es/built-in-nodes/PikaMusicNode)[SoniloMusic15](https://docs.comfy.org/es/built-in-nodes/SoniloMusic15)
