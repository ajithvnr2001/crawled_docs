---
url: https://docs.comfy.org/es/built-in-nodes/KlingAvatarNode/
title: Kling avatar 2.0 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:58.650702+00:00
---

# Kling avatar 2.0 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/KlingAvatarNode/

Kling

# Kling avatar 2.0 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Kling Avatar 2.0 genera videos de humanos digitales estilo transmisión a partir de una sola foto de referencia y un archivo de audio.

Copiar páginaCopiar página

El nodo Kling Avatar 2.0 genera videos de humanos digitales estilo transmisión a partir de una sola foto de referencia y un archivo de audio. Crea un video de avatar parlante con un mensaje de texto opcional para definir las acciones, emociones y movimientos de cámara del avatar.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| Imagen de referencia del avatar. El ancho y alto deben ser de al menos 300 px. La relación de aspecto debe estar entre 1:2.5 y 2.5:1.| IMAGE| Sí| -  
`archivo_de_audio`| Entrada de audio. Debe tener una duración de entre 2 y 300 segundos.| AUDIO| Sí| -  
`modo`| El modo de generación a utilizar.| COMBO| Sí| `"std"`  
`"pro"`  
`prompt`| Mensaje opcional para definir acciones, emociones y movimientos de cámara del avatar. (predeterminado: cadena vacía)| STRING| No| -  
`semilla`| La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0)| INT| Sí| 0 a 2147483647  
  
**Nota:** Las entradas `image` y `sound_file` tienen requisitos de validación específicos. La imagen debe tener al menos 300x300 píxeles con una relación de aspecto entre 1:2.5 y 2.5:1. El archivo de audio debe tener una duración de entre 2 y 300 segundos.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| El video de humano digital generado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/es.md)

* * *

**Source fingerprint (SHA-256):** `85793d3820a89ef98bb54cb930486847d4fd64cce5470ba34574ec319f8ea8c6`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/KlingAvatarNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/KlingAvatarNode)

[HitPaw mejora de vídeo](https://docs.comfy.org/es/built-in-nodes/HitPawVideoEnhance)[Kling 3.0 Primer-Último fotograma a video](https://docs.comfy.org/es/built-in-nodes/KlingFirstLastFrameNode)
