---
url: https://docs.comfy.org/es/built-in-nodes/BreezeVoiceClone/
title: Clonaci\u00f3n de voz de Breeze - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:54.205462+00:00
---

# Clonación de voz de Breeze - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BreezeVoiceClone/

Audio

# Clonación de voz de Breeze - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Crea una voz de Breeze a partir de una grabación de un solo hablante.

Copiar páginaCopiar página

Crea una voz de Breeze a partir de una grabación de un solo hablante. La voz se guarda en tu cuenta y se devuelve como un identificador de voz, junto con una vista previa de audio de cómo suena.

## Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`audio`| Grabación de un solo hablante, de al menos 3 segundos de duración. Solo se utilizan los primeros 60 segundos.| AUDIO| Sí| -  
`remove_background_noise`| Limpia la grabación antes de la clonación. Predeterminado: false.| BOOLEAN| No| true  
false  
`seed`| Controla si el nodo se vuelve a ejecutar; los resultados no son deterministas independientemente de la semilla. Predeterminado: 42.| INT| No| 0 a 2147483647  
  
## Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`voice`| La nueva voz de Breeze, para Breeze Text to Speech.| BREEZE_VOICE  
`preview`| Vista previa de audio de la voz clonada.| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceClone/es.md)

* * *

**Source fingerprint (SHA-256):** `3c2e461a8e1a38bfa494a687f5b77a375e9e81c77964493181d7c622a682c56f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BreezeVoiceClone.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BreezeVoiceClone)

[Texto a voz de Breeze](https://docs.comfy.org/es/built-in-nodes/BreezeTextToSpeech)[Diseño de voz Breeze](https://docs.comfy.org/es/built-in-nodes/BreezeVoiceDesign)
