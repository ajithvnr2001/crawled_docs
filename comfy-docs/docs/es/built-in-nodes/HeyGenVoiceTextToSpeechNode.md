---
url: https://docs.comfy.org/es/built-in-nodes/HeyGenVoiceTextToSpeechNode/
title: Texto a voz de HeyGen Voice 1.0 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:52.850529+00:00
---

# Texto a voz de HeyGen Voice 1.0 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HeyGenVoiceTextToSpeechNode/

Audio

# Texto a voz de HeyGen Voice 1.0 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Pronuncia texto con una voz clonada mediante HeyGen Voice 1.0 Instant Clone.

Copiar páginaCopiar página

Pronuncia texto con una voz clonada mediante HeyGen Voice 1.0 Instant Clone. El nodo envía el texto y el ID de voz a HeyGen y devuelve el habla generada como audio. Hay dos modelos disponibles: `heygen-voice-1` y el más rápido y económico `heygen-voice-1-turbo`. Al seleccionar un `model`, se muestran los parámetros específicos de ese modelo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| Modelo a usar. `heygen-voice-1-turbo` es más rápido y más económico. Al seleccionar un modelo se muestran los parámetros específicos de este: `voice_id`, `text`, `language` y `expressiveness_boost`.| DYNAMIC_COMBO| Sí| `"heygen-voice-1"`  
`"heygen-voice-1-turbo"`  
`voice_id`| Voz de HeyGen Voice 1.0 Instant Clone (predeterminado: vacío).| STRING| Sí| N/A  
`text`| Texto a pronunciar. Hasta 5000 caracteres; falla la síntesis de voz de más de aproximadamente 12 minutos, así que divida el texto chino o japonés muy largo (predeterminado: vacío).| STRING| Sí| 1 a 5000 caracteres  
`language`| Idioma del texto. Configúrelo para idiomas estrechamente relacionados, como serbio o malayo, que la detección automática puede confundir (predeterminado: “auto”).| COMBO| Sí| `"auto"`  
Múltiples preajustes de idioma  
`expressiveness_boost`| Los valores más altos son más expresivos; los valores más bajos se mantienen más cerca de la voz original (predeterminado: 0.5).| FLOAT| Sí| 0.0 a 1.0 (paso 0.05)  
  
**Nota:** `voice_id` debe ser una voz creada por HeyGen Voice 1.0 Instant Clone; el nodo se detiene con un error cuando está vacío. `text` debe contener al menos un carácter.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`AUDIO`| La voz generada a partir del texto, pronunciada con la voz clonada.| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceTextToSpeechNode/es.md)

* * *

**Source fingerprint (SHA-256):** `936cb63237681779dd4d9a74d048afae93160638d069be6b16e5855d333e584a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HeyGenVoiceTextToSpeechNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HeyGenVoiceTextToSpeechNode)

[Clonación instantánea de voz HeyGen Voice 1.0](https://docs.comfy.org/es/built-in-nodes/HeyGenVoiceCloneNode)[Mirelo de texto a SFX](https://docs.comfy.org/es/built-in-nodes/MireloTextToSFX)
