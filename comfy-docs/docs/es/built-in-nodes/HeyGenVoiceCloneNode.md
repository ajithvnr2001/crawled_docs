---
url: https://docs.comfy.org/es/built-in-nodes/HeyGenVoiceCloneNode/
title: Clonaci\u00f3n instant\u00e1nea de voz HeyGen Voice 1.0 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:53.175952+00:00
---

# Clonación instantánea de voz HeyGen Voice 1.0 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HeyGenVoiceCloneNode/

Audio

# Clonación instantánea de voz HeyGen Voice 1.0 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Clona una voz a partir de una grabación de un solo hablante con el motor Voice 1.0 de HeyGen.

Copiar páginaCopiar página

Clona una voz a partir de una grabación de un solo hablante con el motor Voice 1.0 de HeyGen. El nodo sube la grabación, crea un clon de voz instantáneo, espera hasta que HeyGen termine de procesarlo y devuelve el `voice_id`. Conéctalo a HeyGen Voice 1.0 Text to Speech, o a `custom_voice_id` en HeyGen Avatar Video y HeyGen Talking Photo. Crear el clon es gratis; se te cobrará por el habla que generes con la voz.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`audio`| Grabación de un solo hablante. Usa al menos 10 segundos de habla clara; solo se utilizan los primeros 3 minutos.| AUDIO| Sí| N/A  
`language`| Idioma que se habla en la grabación (predeterminado: “auto”).| COMBO| Sí| `"auto"`  
Múltiples preajustes de idioma  
`similarity`| Qué tan fielmente sigue la voz a la grabación (predeterminado: “max”).| COMBO| Sí| `"medium"`  
`"high"`  
`"extra_high"`  
`"max"`  
`remove_background_noise`| Limpia el ruido de fondo de la grabación antes de clonar (predeterminado: True).| BOOLEAN| Sí| True  
False  
`seed`| Cambia la semilla para clonar la grabación de nuevo; cada clon es una voz ligeramente diferente (predeterminado: 42).| INT| Sí| 0 a 2147483647  
  
**Nota:** La voz se crea como “ComfyUI Voice” en tu cuenta de HeyGen, y el nodo imprime el `voice_id` en la interfaz de usuario para que puedas copiarlo y reutilizarlo. Deja `language` en “auto” a menos que el hablante hable un idioma que se confunda fácilmente con uno estrechamente relacionado. La entrada `seed` incluye un control fijo Control After Generate en la interfaz de usuario, así que cámbialo manualmente cuando quieras otro clon.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`voice_id`| El ID de la voz clonada, para reutilizarla en el nodo HeyGen Voice 1.0 Text to Speech o como `custom_voice_id`.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneNode/es.md)

* * *

**Source fingerprint (SHA-256):** `0bf5c7170d140936841cc4afd28022574df8e4c2280137607dcfca8e36862317`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HeyGenVoiceCloneNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HeyGenVoiceCloneNode)

[Sonilo Video a Música](https://docs.comfy.org/es/built-in-nodes/SoniloVideoToMusic)[Texto a voz de HeyGen Voice 1.0](https://docs.comfy.org/es/built-in-nodes/HeyGenVoiceTextToSpeechNode)
