---
url: https://docs.comfy.org/es/built-in-nodes/WanDancerEncodeAudio/
title: WanDancerEncodeAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:45.252909+00:00
---

# WanDancerEncodeAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WanDancerEncodeAudio/

Dancer

# WanDancerEncodeAudio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo analiza un clip de audio y lo convierte en un conjunto de características que pueden guiar a un modelo de generación de video.

Copiar páginaCopiar página

Este nodo analiza un clip de audio y lo convierte en un conjunto de características que pueden guiar a un modelo de generación de video. Estima el tempo y los pulsos, extrae características de espectrograma Mel, MFCC, croma y onset, y luego las empaqueta junto con una tasa de fotogramas calculada para la sincronización.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`audio`| La entrada de audio que se va a analizar y codificar. Si el audio tiene varios canales, los canales se promedian a mono antes de la extracción de características.| AUDIO| Sí| -  
`video_frames`| El número de fotogramas del video objetivo. Se utiliza para calcular la tasa de fotogramas para la sincronización (predeterminado: 149).| INT| Sí| Mín: 1, Máx: 16384 (MAX_RESOLUTION), Paso: 4  
`audio_inject_scale`| La escala de las características de audio cuando se inyectan en el modelo de video (predeterminado: 1.0).| FLOAT| Sí| Mín: 0.0, Máx: 10.0, Paso: 0.01  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`audio_encoder_output`| Un diccionario que contiene las características de audio procesadas, la tasa de fotogramas calculada (fps) y la escala de inyección de audio. Esta salida se utiliza para condicionar el modelo de generación de video.| AUDIO_ENCODER_OUTPUT  
`fps_string`| Una cadena de texto que describe la tasa de fotogramas calculada (fps) según la duración del audio y el número de fotogramas del video. Esta cadena está pensada para usarse en el prompt del modelo de video. Está formateada en chino para coincidir con el pipeline de referencia.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WanDancerEncodeAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WanDancerEncodeAudio)

[Wan imagen con cámara a video](https://docs.comfy.org/es/built-in-nodes/WanCameraImageToVideo)[WanDancerVideo](https://docs.comfy.org/es/built-in-nodes/WanDancerVideo)
