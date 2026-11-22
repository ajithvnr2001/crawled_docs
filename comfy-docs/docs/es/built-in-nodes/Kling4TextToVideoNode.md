---
url: https://docs.comfy.org/es/built-in-nodes/Kling4TextToVideoNode/
title: Kling 4.0 Texto a v\u00eddeo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:07:53.250424+00:00
---

# Kling 4.0 Texto a vídeo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Kling4TextToVideoNode/

Video

# Kling 4.0 Texto a vídeo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera un video a partir de un prompt de texto con el modelo Kling 4.0, incluyendo el audio.

Copiar páginaCopiar página

Genera un video a partir de un prompt de texto con el modelo Kling 4.0, incluyendo el audio. Este nodo envía el prompt y los ajustes de generación a la API de Kling, espera a que finalice la tarea y devuelve el video terminado. Úsalo cuando deba crearse un clip a partir únicamente de una descripción, sin medios de referencia.

## Entradas

### Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| Selector de modelo. `"kling-4.0"` admite hasta 4K HDR y 30 segundos; `"kling-4.0-flash"` está limitado a 720p y 20 segundos. Al seleccionar un modelo, se muestran sus entradas a continuación.| DYNAMIC_COMBO| Sí| `"kling-4.0"`  
`"kling-4.0-flash"`  
  
### Entradas de kling-4.0

Estas entradas aparecen cuando `model` se establece en `"kling-4.0"`.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Descripción de texto del video que se va a generar. Debe tener entre 1 y 26000 caracteres.| STRING| Sí| 1 a 26000 caracteres  
`resolution`| Resolución del video de salida; una opción con `HDR` en su nombre devuelve un video HDR. Predeterminado: `"720p"`.| COMBO| Sí| `"720p"`  
`"1080p"`  
`"4k"`  
`"1080p HDR"`  
`"4k HDR"`  
`aspect_ratio`| Relación de aspecto del video de salida. Predeterminado: `"16:9"`.| COMBO| Sí| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"21:9"`  
`"4:3"`  
`"3:4"`  
`duration`| Duración del video generado en segundos. Predeterminado: 5.| INT| Sí| 3 a 30  
`seed`| La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Predeterminado: 42.| INT| Sí| 0 a 2147483647  
  
### Entradas de kling-4.0-flash

Estas entradas aparecen cuando `model` se establece en `"kling-4.0-flash"`.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Descripción de texto del video que se va a generar. Debe tener entre 1 y 26000 caracteres.| STRING| Sí| 1 a 26000 caracteres  
`resolution`| Resolución del video de salida. Flash solo renderiza en 720p. Predeterminado: `"720p"`.| COMBO| Sí| `"720p"`  
`aspect_ratio`| Relación de aspecto del video de salida. Predeterminado: `"16:9"`.| COMBO| Sí| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"21:9"`  
`"4:3"`  
`"3:4"`  
`duration`| Duración del video generado en segundos. Predeterminado: 5.| INT| Sí| 3 a 20  
`seed`| La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Predeterminado: 42.| INT| Sí| 0 a 2147483647  
  
## Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| El video generado, descargado del proveedor una vez que finaliza la tarea.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `7a5d99aa6f5fdb923ce9e2c89f64e92d46fad14d28002a033ddedc24c7d27894`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Kling4TextToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Kling4TextToVideoNode)

[Kling 4.0: referencia a vídeo](https://docs.comfy.org/es/built-in-nodes/Kling4ReferenceToVideoNode)[Pika H3 Flex de referencia a vídeo](https://docs.comfy.org/es/built-in-nodes/PikaH3FlexReferenceVideoNode)
