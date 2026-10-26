---
url: https://docs.comfy.org/es/built-in-nodes/HeyGenVideoTranslateNode/
title: HeyGen Video Translate - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:52.918659+00:00
---

# HeyGen Video Translate - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HeyGenVideoTranslateNode/

Heygen

# HeyGen Video Translate - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Traduce un video con habla a otro idioma mediante clonación de voz y sincronización de labios.

Copiar páginaCopiar página

Traduce un video con habla a otro idioma mediante clonación de voz y sincronización de labios. Este nodo clona la voz del hablante original y reanima la boca para que coincida con el habla traducida, produciendo un resultado de aspecto natural.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`video`| Video con habla para traducir.| VIDEO| Sí| -  
`output_language`| Idioma de destino para el video traducido.| COMBO| Sí| ”Arabic"  
"Bengali"  
"Chinese"  
"Danish"  
"Dutch"  
"English"  
"French"  
"German"  
"Greek"  
"Hindi"  
"Indonesian"  
"Italian"  
"Japanese"  
"Korean"  
"Malay"  
"Polish"  
"Portuguese"  
"Russian"  
"Spanish"  
"Swedish"  
"Tamil"  
"Telugu"  
"Thai"  
"Turkish"  
"Ukrainian"  
"Vietnamese”  
`mode`| ’speed’ es más rápido; ‘precision’ produce una sincronización de labios de mayor calidad a un precio más alto. (predeterminado: “speed”)| COMBO| Sí| ”speed"  
"precision”  
`translate_audio_only`| Solo intercambia la pista de audio, manteniendo los movimientos originales de la boca (sin sincronización de labios). (predeterminado: False)| BOOLEAN| No| True  
False  
`speaker_count`| Número de hablantes en el video. 0 = detectar automáticamente. Los valores superiores a 0 se envían a la API como el número de hablantes. (predeterminado: 0)| INT| No| 0 a 10  
`seed`| No se envía a HeyGen; cámbialo para forzar una nueva ejecución. (predeterminado: 42)| INT| No| 0 a 2147483647  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`video`| El video traducido con clonación de voz y sincronización de labios aplicadas.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/es.md)

* * *

**Source fingerprint (SHA-256):** `709438c0c713d6db750643cc48f75352c6f293ae1ff2fd82c1bacb03b2581923`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HeyGenVideoTranslateNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HeyGenVideoTranslateNode)

[HeyGen Talking Photo](https://docs.comfy.org/es/built-in-nodes/HeyGenTalkingPhotoNode)[Transferencia de movimiento Higgsfield Genjutsu](https://docs.comfy.org/es/built-in-nodes/HiggsfieldMotionTransferNode)
