---
url: https://docs.comfy.org/es/built-in-nodes/LumaRay32VideoEditNode/
title: Luma Ray 3.2 Edici\u00f3n de video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:08.212779+00:00
---

# Luma Ray 3.2 Edición de video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LumaRay32VideoEditNode/

Luma

# Luma Ray 3.2 Edición de video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo vuelve a renderizar un video existente con un nuevo prompt usando Luma Ray 3.2, lo que te permite cambiar el estilo, la iluminación, añadir

Copiar páginaCopiar página

## 

​

Descripción general

Este nodo vuelve a renderizar un video existente bajo un nuevo prompt usando Luma Ray 3.2, lo que te permite cambiar el estilo, la iluminación, agregar o eliminar elementos mientras se mantiene el movimiento original. El video de origen puede tener hasta 18 segundos, y el video editado conserva la duración original de la fuente.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`video`| Video de origen que se va a editar. Hasta 18 segundos.| VIDEO| Sí| -  
`prompt`| Describe la edición deseada.| STRING| Sí| -  
`resolution`| La resolución de salida para el video editado. (predeterminado: “720p”)| COMBO| Sí| `"360p"`  
`"540p"`  
`"720p"`  
`"1080p"`  
`strength`| Con qué fuerza preservar frente a reimaginar la fuente. “auto” permite que Ray 3.2 elija; adhere_* conserva más, flex_* es equilibrado, reimagine_* cambia más. (predeterminado: “auto”)| COMBO| Sí| `"auto"`  
`"adhere_1"`  
`"adhere_2"`  
`"adhere_3"`  
`"flex_1"`  
`"flex_2"`  
`"flex_3"`  
`"reimagine_1"`  
`"reimagine_2"`  
`"reimagine_3"`  
`seed`| Semilla para reproducibilidad.| INT| Sí| -  
  
**Nota:** El `prompt` debe tener entre 1 y 6000 caracteres. El video de origen no debe superar los 18 segundos de duración.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`VIDEO`| El video editado de salida.| VIDEO  
`generation_id`| El identificador único para la solicitud de generación.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoEditNode/es.md)

* * *

**Source fingerprint (SHA-256):** `936d9d7da3fdee9b0b468781fd470751db01f772f3c5c20582da7fb1ff85e6e6`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LumaRay32VideoEditNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LumaRay32VideoEditNode)

[Luma Ray 3.2 Texto a video](https://docs.comfy.org/es/built-in-nodes/LumaRay32TextToVideoNode)[Luma Ray 3.2 Reencuadre de Video](https://docs.comfy.org/es/built-in-nodes/LumaRay32VideoReframeNode)
