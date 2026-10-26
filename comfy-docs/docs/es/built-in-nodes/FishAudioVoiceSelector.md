---
url: https://docs.comfy.org/es/built-in-nodes/FishAudioVoiceSelector/
title: Selector de voz de Fish Audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:47.084205+00:00
---

# Selector de voz de Fish Audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/FishAudioVoiceSelector/

Fish Audio

# Selector de voz de Fish Audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Fish Audio Voice Selector selecciona una voz de la biblioteca de Fish Audio para la generación de texto a voz.

Copiar páginaCopiar página

El nodo Fish Audio Voice Selector selecciona una voz de la biblioteca de Fish Audio para la generación de texto a voz. Puedes elegir una de las voces predefinidas integradas o seleccionar “custom” para introducir cualquier ID de modelo de voz de fish.audio.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`voz`| Elige una voz, o ‘custom’ para introducir cualquier ID de modelo de voz de fish.audio.| DYNAMIC_COMBO| Sí| ”Energetic Male (en)"  
"Friendly Women (en)"  
"Sarah (en)"  
"Verity (en)"  
"Polo (en)"  
"Adrian (en)"  
"E-girl (en)"  
"Narrator (en)"  
"Warm Conversational Voice (en)"  
"Warm Storyteller (en)"  
"Dramatic Character Male (en)"  
"News Narrator (zh)"  
"Lively Female (zh)"  
"Gentle Female (zh)"  
"Energetic Female (ja)"  
"Calm Female (ja)"  
"Calm Male (ja)"  
"custom”  
  
Las opciones de voz predefinidas cubren voces en inglés (en), chino (zh) y japonés (ja), y no requieren entradas adicionales.

### 

​

Entradas personalizadas

Estas entradas aparecen cuando `voice` se establece en “custom”.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`voice_id`| ID del modelo de voz de fish.audio; por ejemplo, el ID en [https://fish.audio/m/&lt;id>/](https://fish.audio/m/&lt;id%3E/). Predeterminado: cadena vacía.| STRING| Sí| Cualquier ID válido de modelo de voz de Fish Audio  
  
Nota: Cuando `voice` se establece en “custom”, `voice_id` no debe estar vacío después de eliminar los espacios en blanco; de lo contrario, el nodo lanza un error “Custom voice ID is empty.” Si se pasa una opción de voz no reconocida, el nodo lanza un error “Unknown voice”.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`voice`| El ID del modelo de voz de Fish Audio seleccionado. Para una voz predefinida, se devuelve el ID de voz correspondiente de la biblioteca de Fish Audio; para “custom”, se devuelve el valor de `voice_id` introducido.| FISHAUDIO_VOICE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/es.md)

* * *

**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/FishAudioVoiceSelector.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/FishAudioVoiceSelector)

[Fish Audio Texto a voz](https://docs.comfy.org/es/built-in-nodes/FishAudioTextToSpeech)[HeyGen Texto a Voz](https://docs.comfy.org/es/built-in-nodes/HeyGenTextToSpeechNode)
