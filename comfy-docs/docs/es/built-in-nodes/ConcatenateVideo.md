---
url: https://docs.comfy.org/es/built-in-nodes/ConcatenateVideo/
title: Concatenar v\u00eddeo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:39.786139+00:00
---

# Concatenar vídeo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConcatenateVideo/

Video

# Concatenar vídeo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Concatena varios segmentos de video en un solo video, preservando el orden en que se conectan.

Copiar páginaCopiar página

Concatena varios segmentos de video en un solo video, preservando el orden en que se conectan. Las entradas codificadas compatibles se combinan sin decodificarse, y se puede proporcionar una pista de audio separada opcional para reemplazar el audio original.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`videos`| Segmentos de video que se concatenarán en el orden de entrada. Conecte de 1 a 100 videos; cada video aparece como una ranura de entrada separada etiquetada `video_1`, `video_2`, etc.| VIDEO| Sí| 1 a 100 segmentos  
`codec`| Códec utilizado para codificar tensores de video. La opción Auto usa H.264; los videos ya codificados compatibles permanecen sin cambios. Valor predeterminado: `"auto"`| COMBO| Sí| `"auto"`  
Otras opciones se definen según los tipos de códec de video disponibles.  
`complete_audio`| Banda sonora completa opcional para el video concatenado. Anula el audio que llevan los videos de entrada.| AUDIO| No| N/A  
  
**Nota:** La entrada `videos` acepta entre 1 y 100 segmentos de video. Si se proporciona `complete_audio`, reemplaza el audio de todos los videos de entrada. Cuando `codec` se establece en `"auto"`, las entradas codificadas compatibles se concatenan sin decodificación.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`VIDEO`| El video concatenado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConcatenateVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `f591aecb83754127e1c86ed0488548f9e7d99f3559c95a1c86c55fa5d430713d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConcatenateVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConcatenateVideo)

[Recortar video (temporal)](https://docs.comfy.org/es/built-in-nodes/VideoTemporalCrop)[Crear video](https://docs.comfy.org/es/built-in-nodes/CreateVideo)
