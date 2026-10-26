---
url: https://docs.comfy.org/es/built-in-nodes/ElevenLabsVoiceSelector/
title: Selector de voz de ElevenLabs - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:44.626508+00:00
---

# Selector de voz de ElevenLabs - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ElevenLabsVoiceSelector/

Elevenlabs

# Selector de voz de ElevenLabs - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ElevenLabs Voice Selector permite elegir una voz específica de una lista predefinida de voces de texto a voz de ElevenLabs.

Copiar páginaCopiar página

El nodo **ElevenLabs Voice Selector** permite elegir una voz específica de una lista predefinida de voces de texto a voz de ElevenLabs. Toma un nombre de voz como entrada y genera el identificador de voz correspondiente necesario para la generación de audio. Este nodo simplifica el proceso de seleccionar una voz compatible para usar con otros nodos de audio de ElevenLabs.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`voz`| Elige una voz de la lista predefinida de voces de ElevenLabs.| STRING| Sí| `"Adam"`  
`"Antoni"`  
`"Arnold"`  
`"Bella"`  
`"Domi"`  
`"Elli"`  
`"Josh"`  
`"Rachel"`  
`"Sam"`  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`voz`| El identificador único de la voz seleccionada de ElevenLabs, que puede pasarse a otros nodos para la generación de texto a voz.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/es.md)

* * *

**Source fingerprint (SHA-256):** `b87f5b2b8accca87d0593ab1f4bcfccaa84b393ddb3fd9121758a87871592cee`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ElevenLabsVoiceSelector.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ElevenLabsVoiceSelector)

[ElevenLabs texto a voz](https://docs.comfy.org/es/built-in-nodes/ElevenLabsTextToSpeech)[Clonación instantánea de voz de Fish Audio](https://docs.comfy.org/es/built-in-nodes/FishAudioInstantVoiceClone)
