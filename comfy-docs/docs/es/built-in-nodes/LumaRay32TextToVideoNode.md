---
url: https://docs.comfy.org/es/built-in-nodes/LumaRay32TextToVideoNode/
title: Luma Ray 3.2 Texto a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:08.122404+00:00
---

# Luma Ray 3.2 Texto a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LumaRay32TextToVideoNode/

Luma

# Luma Ray 3.2 Texto a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo genera un video a partir de un mensaje de texto utilizando el modelo Ray 3.2 de Luma.

Copiar páginaCopiar página

Este nodo genera un video a partir de un mensaje de texto utilizando el modelo Ray 3.2 de Luma. Envía tu mensaje y configuración de video a la API de Luma y devuelve el video generado junto con un ID de generación.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Indicación de texto para la generación de video.| STRING| Sí| 1 a 6000 caracteres  
`aspect_ratio`| La relación de aspecto del video generado.| STRING| Sí| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`"21:9"`  
`resolution`| La resolución de salida del video (predeterminado: “720p”).| STRING| Sí| `"360p"`  
`"540p"`  
`"720p"`  
`"1080p"`  
`duration`| La duración del video generado.| STRING| Sí| `"5s"`  
`"10s"`  
`loop`| Hace que el video se reproduzca en bucle sin interrupciones. Solo disponible con duración de 5s.| BOOLEAN| No| True/False (predeterminado: False)  
`seed`| Semilla para generación reproducible.| INT| No| 0 a 2147483647  
  
**Nota:** El parámetro `loop` solo se puede habilitar cuando `duration` está configurado en “5s”. Si establece `duration` en ”10s” y habilita `loop`, el nodo devuelve un error.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`generation_id`| El archivo de video generado.| VIDEO  
`generation_id`| El identificador único para la solicitud de generación de video.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32TextToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `04358a872530e5a2622bf0f148a694f2c707ce8535586d8f860bdf9911e1fa6a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LumaRay32TextToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LumaRay32TextToVideoNode)

[Luma Ray 3.2 Fotogramas clave a video](https://docs.comfy.org/es/built-in-nodes/LumaRay32KeyframesToVideoNode)[Luma Ray 3.2 Edición de video](https://docs.comfy.org/es/built-in-nodes/LumaRay32VideoEditNode)
