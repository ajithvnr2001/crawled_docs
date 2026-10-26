---
url: https://docs.comfy.org/es/built-in-nodes/KlingFirstLastFrameNode/
title: Kling 3.0 Primer-\u00daltimo fotograma a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:58.776356+00:00
---

# Kling 3.0 Primer-Último fotograma a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/KlingFirstLastFrameNode/

Kling

# Kling 3.0 Primer-Último fotograma a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo utiliza el modelo Kling 3.0 para generar un video.

Copiar páginaCopiar página

Este nodo utiliza el modelo Kling 3.0 para generar un video. Crea el video basado en un prompt de texto, una duración especificada y dos imágenes proporcionadas: un fotograma inicial y un fotograma final. El nodo también puede generar audio de acompañamiento para el video.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`modelo`| Configuración del modelo y de generación. Seleccionar esta opción revela un parámetro anidado `resolution`.| DYNAMIC_COMBO| Sí| `"kling-v3"`  
`prompt`| La descripción de texto que guía la generación del video. Debe tener entre 1 y 2500 caracteres.| STRING| Sí| N/A  
`duración`| La duración del video en segundos (predeterminado: 5).| INT| Sí| 3 a 15  
`primer_fotograma`| La imagen inicial del video. Debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1.| IMAGE| Sí| N/A  
`último_fotograma`| La imagen final del video. Debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1.| IMAGE| Sí| N/A  
`generar_audio`| Controla si se genera audio para el video (predeterminado: True).| BOOLEAN| Sí| N/A  
`semilla`| Seed controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0).| INT| Sí| 0 a 2147483647  
  
### 

​

Entradas de Kling V3

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`resolution`| La resolución del video generado (predeterminado: `"1080p"`).| COMBO| Sí| `"4k"`  
`"1080p"`  
`"720p"`  
  
**Nota:** Las imágenes `first_frame` y `end_frame` deben tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1 para que el nodo funcione correctamente. El `prompt` debe tener entre 1 y 2500 caracteres. La opción `resolution` se corresponde con un modo de generación de Kling: `"4k"`, `"1080p"` (pro) y `"720p"` (estándar).

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`output`| El archivo de video generado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/es.md)

* * *

**Source fingerprint (SHA-256):** `b71119c3267e2a74d2180e5182463c78828e892bfcf1eeb7c33a0f4d7019997f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/KlingFirstLastFrameNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/KlingFirstLastFrameNode)

[Kling avatar 2.0](https://docs.comfy.org/es/built-in-nodes/KlingAvatarNode)[Kling imagen (primer fotograma) a video](https://docs.comfy.org/es/built-in-nodes/KlingImage2VideoNode)
