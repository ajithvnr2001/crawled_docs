---
url: https://docs.comfy.org/es/built-in-nodes/ElevenLabsInstantVoiceClone/
title: ElevenLabs clonaci\u00f3n instant\u00e1nea de voz - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:44.277544+00:00
---

# ElevenLabs clonación instantánea de voz - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ElevenLabsInstantVoiceClone/

Elevenlabs

# ElevenLabs clonación instantánea de voz - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo de Clonación Instantánea de Voz de ElevenLabs crea un modelo de voz nuevo y único mediante el análisis de 1 a 8 grabaciones de audio de la voz de una

Copiar páginaCopiar página

El nodo de Clonación Instantánea de Voz de ElevenLabs crea un modelo de voz nuevo y único mediante el análisis de 1 a 8 grabaciones de audio de la voz de una persona. Envía estas muestras a la API de ElevenLabs, que las procesa para generar un clon de voz que puede utilizarse para síntesis de texto a voz.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`audio_*`| Grabaciones de audio para la clonación de voz. Debes proporcionar entre 1 y 8 archivos de audio.| AUDIO| Sí| 1 a 8 archivos  
`eliminar_ruido_de_fondo`| Elimina el ruido de fondo de las muestras de voz mediante aislamiento de audio. (predeterminado: Falso)| BOOLEAN| No| Verdadero / Falso  
  
**Nota:** Debes proporcionar al menos un archivo de audio, y puedes proporcionar hasta ocho. El nodo creará automáticamente ranuras de entrada para los archivos de audio que agregues.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`voz`| El identificador único del modelo de voz clonada recién creado. Esta salida puede conectarse a otros nodos de texto a voz de ElevenLabs.| ELEVENLABS_VOICE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/es.md)

* * *

**Source fingerprint (SHA-256):** `297598e183df3ccddabc75d6903c5c69f10648adeea430e546f9c5f6df49bdb2`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ElevenLabsInstantVoiceClone.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ElevenLabsInstantVoiceClone)

[ElevenLabs aislamiento de voz](https://docs.comfy.org/es/built-in-nodes/ElevenLabsAudioIsolation)[ElevenLabs conversión de voz a voz](https://docs.comfy.org/es/built-in-nodes/ElevenLabsSpeechToSpeech)
