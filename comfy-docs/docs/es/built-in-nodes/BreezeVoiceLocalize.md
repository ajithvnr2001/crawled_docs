---
url: https://docs.comfy.org/es/built-in-nodes/BreezeVoiceLocalize/
title: Localizaci\u00f3n de voz Breeze - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:54.347101+00:00
---

# Localización de voz Breeze - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BreezeVoiceLocalize/

Audio

# Localización de voz Breeze - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Crea una copia de una voz que habla otro idioma de forma nativa, en lugar de leer un idioma extranjero con su acento original.

Copiar páginaCopiar página

Crea una copia de una voz que habla otro idioma de forma nativa, en lugar de leer un idioma extranjero con su acento original. La copia se guarda en tu cuenta y se devuelve con una vista previa de audio.

## Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`voice`| Voz de Breeze a copiar.| BREEZE_VOICE| Sí| -  
`language`| Idioma que habla la nueva voz. Predeterminado: `"English"`.| COMBO| Sí| Múltiples opciones disponibles  
`seed`| Controla si el nodo se vuelve a ejecutar; los resultados no son deterministas independientemente de la semilla. Predeterminado: 42.| INT| No| 0 a 2147483647  
  
## Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`voice`| La copia localizada de la voz, nombrada según la voz original y el idioma.| BREEZE_VOICE  
`preview`| Vista previa de audio de la voz localizada.| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeVoiceLocalize/es.md)

* * *

**Source fingerprint (SHA-256):** `a997fbc3426669f6e5725c455f49f3e16d5e14806ea3fac26657459f63e99db1`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BreezeVoiceLocalize.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BreezeVoiceLocalize)

[Diseño de voz Breeze](https://docs.comfy.org/es/built-in-nodes/BreezeVoiceDesign)[Remezcla de voz Breeze](https://docs.comfy.org/es/built-in-nodes/BreezeVoiceRemix)
