---
url: https://docs.comfy.org/es/built-in-nodes/Vidu4ImageToVideoNode/
title: Generaci\u00f3n de imagen a v\u00eddeo Vidu Q4 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:43.357872+00:00
---

# Generación de imagen a vídeo Vidu Q4 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Vidu4ImageToVideoNode/

Vidu

# Generación de imagen a vídeo Vidu Q4 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera un video a partir de un fotograma inicial y un prompt opcional con un modelo Vidu Q4.

Copiar páginaCopiar página

Genera un video a partir de un fotograma inicial y un prompt opcional con un modelo Vidu Q4. La salida conserva la relación de aspecto de la imagen de entrada. Al seleccionar un `model`, se muestran los parámetros específicos de ese modelo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`image`| Fotograma inicial del video generado. La relación de aspecto debe estar entre 1:5 y 5:1.| IMAGE| Sí| N/A  
`model`| Modelo que se usará para la generación de video. Al seleccionar un `model`, se muestran los parámetros específicos de este: `prompt`, `resolution`, `duration`, `audio` y `seed`.| DYNAMIC_COMBO| Sí| `"Vidu Q4 Preview"`  
`prompt`| Prompt de texto opcional para la generación de video, de hasta 5000 caracteres (predeterminado: vacío).| STRING| Sí| Cualquier texto  
`resolution`| Resolución del video de salida (predeterminado: `"720p"`).| COMBO| Sí| `"540p"`  
`"720p"`  
`"1080p"`  
`"2K"`  
`"4K"`  
`duration`| Duración del video de salida en segundos (predeterminado: 5).| INT| Sí| 3 a 16  
`audio`| Cuando está habilitado, genera video con sonido, incluidos diálogos y efectos de sonido (predeterminado: True).| BOOLEAN| Sí| `True`  
`False`  
`seed`| La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Este parámetro tiene funcionalidad de “control después de generar” (predeterminado: 42).| INT| Sí| 1 a 2147483647  
  
**Nota:** La relación de aspecto de `image` debe mantenerse entre 1:5 y 5:1, y el `prompt` no puede superar los 5000 caracteres. El resultado conserva la relación de aspecto de la imagen de entrada, por lo que el tamaño de salida sigue la configuración de `resolution` solo dentro de esa relación.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`VIDEO`| El archivo de video generado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ImageToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `8778696edbdfb821afaa99dcba09cbebff57fd4cd2378273e82ad9fb18600b62`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Vidu4ImageToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Vidu4ImageToVideoNode)

[Generación de video de texto a video Vidu Q3](https://docs.comfy.org/es/built-in-nodes/Vidu3TextToVideoNode)[Generación de referencia a vídeo Vidu Q4](https://docs.comfy.org/es/built-in-nodes/Vidu4ReferenceVideoNode)
