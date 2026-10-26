---
url: https://docs.comfy.org/es/built-in-nodes/GrokVideoExtendNode/
title: Extender video Grok - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:51.876779+00:00
---

# Extender video Grok - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/GrokVideoExtendNode/

Grok

# Extender video Grok - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Grok Video Extend extiende un video existente con una continuación fluida basada en un prompt de texto.

Copiar páginaCopiar página

El nodo Grok Video Extend extiende un video existente con una continuación fluida basada en un prompt de texto. Proporcione un video de origen corto y describa qué debería suceder a continuación; el nodo devuelve un nuevo clip de video que continúa desde el original.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo que se usará para la extensión de video. Seleccionar la opción `"grok-imagine-video"` revela su configuración específica del modelo.| DYNAMIC_COMBO| Sí| `"grok-imagine-video"`  
`prompt`| Descripción de texto de lo que debería suceder a continuación en el video.| STRING| Sí| N/A  
`video`| Video de origen que se extenderá. Formato MP4, 2-15 segundos.| VIDEO| Sí| MP4, 2-15 segundos, máximo 50MB  
`semilla`| Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0).| INT| Sí| 0 a 2147483647  
  
### 

​

Entradas de grok-imagine-video

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`duration`| Duración de la extensión en segundos (predeterminado: 8).| INT| Sí| 2 a 10  
  
**Restricciones de parámetros:**

  * La entrada `video` debe ser un archivo MP4 con una duración de entre 2 y 15 segundos y no puede superar los 50MB de tamaño.
  * El `prompt` debe contener al menos un carácter después de recortar los espacios en blanco.
  * El parámetro `model` es un combo dinámico. Seleccionar la opción `"grok-imagine-video"` revela el parámetro anidado `duration`.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`output`| La extensión de video recién generada.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/es.md)

* * *

**Source fingerprint (SHA-256):** `5009c007b6f93cd44f2742b024b65f1ac92ab9bca3b85a55554b1d99649e323b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/GrokVideoExtendNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/GrokVideoExtendNode)

[Edición de video Grok](https://docs.comfy.org/es/built-in-nodes/GrokVideoEditNode)[Video Grok](https://docs.comfy.org/es/built-in-nodes/GrokVideoNode)
