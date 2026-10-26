---
url: https://docs.comfy.org/es/built-in-nodes/LumaRay32ImageToVideoNode/
title: Luma Ray 3.2 Imagen a Video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:07.678145+00:00
---

# Luma Ray 3.2 Imagen a Video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LumaRay32ImageToVideoNode/

Luma

# Luma Ray 3.2 Imagen a Video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera un video a partir de un fotograma inicial y/o final utilizando el modelo Ray 3.2 de Luma.

Copiar páginaCopiar página

Genera un video a partir de un fotograma inicial y/o final utilizando el modelo Ray 3.2 de Luma. Las generaciones ancladas a una imagen siempre tienen una duración de 5 segundos.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Indicación textual para la generación del video.| STRING| Sí| 1 a 6000 caracteres  
`resolution`| La resolución de salida del video generado (predeterminado: “720p”).| COMBO| Sí| ”360p"  
"540p"  
"720p"  
"1080p”  
`loop`| Hace que el video se reproduzca en bucle sin interrupciones. No disponible cuando se define un `end_frame`.| BOOLEAN| Sí| True  
False  
`seed`| Valor semilla para una generación reproducible.| INT| Sí| 0 a 2147483647  
`start_frame`| Primer fotograma del video generado.| IMAGE| No| -  
`end_frame`| Último fotograma del video generado.| IMAGE| No| -  
  
**Nota:** Debe proporcionarse al menos uno de los parámetros `start_frame` o `end_frame`. Si se proporcionan ambos, el video generado realizará una transición del fotograma inicial al final. La opción `loop` no se puede activar cuando se define un `end_frame`.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`generation_id`| El video generado como salida.| VIDEO  
`generation_id`| El identificador único de la solicitud de generación.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ImageToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `ff479c196f10153ffa09af6acfb4e286d1934aa28a5e9b413613097a2cfb5f2a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LumaRay32ImageToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LumaRay32ImageToVideoNode)

[Luma Ray 3.2 Extender Video](https://docs.comfy.org/es/built-in-nodes/LumaRay32ExtendVideoNode)[Luma Ray 3.2 Fotograma Clave](https://docs.comfy.org/es/built-in-nodes/LumaRay32KeyframeNode)
