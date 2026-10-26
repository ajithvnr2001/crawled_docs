---
url: https://docs.comfy.org/es/built-in-nodes/KlingImageToVideoWithAudio/
title: Kling imagen (Primer fotograma) a video con audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:59.039470+00:00
---

# Kling imagen (Primer fotograma) a video con audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/KlingImageToVideoWithAudio/

Kling

# Kling imagen (Primer fotograma) a video con audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Kling Image(First Frame) to Video with Audio utiliza el modelo de IA Kling para generar un video corto a partir de una única imagen inicial y un

Copiar páginaCopiar página

El nodo Kling Image(First Frame) to Video with Audio utiliza el modelo de IA Kling para generar un video corto a partir de una única imagen inicial y un mensaje de texto. Crea una secuencia de video que comienza con la imagen proporcionada y puede incluir opcionalmente audio generado por IA para acompañar el contenido visual.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`model_name`| La versión específica del modelo de IA Kling a utilizar para la generación del video.| COMBO| Sí| `"kling-v2-6"`  
`fotograma_inicial`| La imagen que servirá como primer fotograma del video generado. La imagen debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1.| IMAGE| Sí| -  
`prompt`| Mensaje de texto positivo. Describe el contenido del video que deseas generar. El mensaje debe tener entre 1 y 2500 caracteres.| STRING| Sí| -  
`modo`| El modo operativo para la generación del video.| COMBO| Sí| `"pro"`  
`duración`| La duración del video a generar, en segundos.| COMBO| Sí| `5`  
`10`  
`generar_audio`| Cuando está habilitado, el nodo generará audio para acompañar el video. Cuando está deshabilitado, el video será silencioso. (valor predeterminado: True)| BOOLEAN| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`video`| El archivo de video generado, que puede incluir audio dependiendo de la entrada `generar_audio`.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `f161eedbc5d780805e3d0ca32b6be94cc78afcd2749e065c032ea20991b782fc`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/KlingImageToVideoWithAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/KlingImageToVideoWithAudio)

[Kling imagen (primer fotograma) a video](https://docs.comfy.org/es/built-in-nodes/KlingImage2VideoNode)[Sincronización labial Kling: vídeo con audio](https://docs.comfy.org/es/built-in-nodes/KlingLipSyncAudioToVideoNode)
