---
url: https://docs.comfy.org/es/built-in-nodes/KlingTextToVideoNode/
title: Kling texto a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:59.860084+00:00
---

# Kling texto a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/KlingTextToVideoNode/

Kling

# Kling texto a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Kling Text to Video genera videos a partir de descripciones de texto usando la API de generación de video de Kling.

Copiar páginaCopiar página

El nodo Kling Text to Video genera videos a partir de descripciones de texto usando la API de generación de video de Kling. Envía el prompt y la configuración (relación de aspecto, modo de generación y escala CFG) a la API, espera a que se complete la tarea de generación y luego devuelve el video resultante junto con su ID y duración.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Prompt de texto positivo| STRING| Sí| Máximo 2500 caracteres  
`negative_prompt`| Prompt de texto negativo| STRING| No| Máximo 2500 caracteres  
`cfg_scale`| Valor de escala de configuración que controla qué tan fielmente el video sigue el prompt (predeterminado: 1.0)| FLOAT| No| 0.0 a 1.0  
`aspect_ratio`| Configuración de la relación de aspecto del video (predeterminado: “16:9”)| COMBO| No| ”16:9"  
"9:16"  
"1:1”  
`mode`| La configuración que se utilizará para la generación del video siguiendo el formato: modo / duración / nombre_del_modelo (predeterminado: “pro mode / 5s duration / kling-v2-5-turbo”)| COMBO| No| ”pro mode / 5s duration / kling-v2-5-turbo"  
"pro mode / 10s duration / kling-v2-5-turbo”  
  
Nota: El parámetro `prompt` es obligatorio y no debe estar vacío. Tanto `prompt` como `negative_prompt` están limitados a un máximo de 2500 caracteres. La opción `mode` de 10 segundos cuesta más que la opción de 5 segundos.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`output`| La salida de video generada| VIDEO  
`video_id`| Identificador único del video generado| STRING  
`duration`| Información de duración del video generado| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/KlingTextToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/KlingTextToVideoNode)

[Kling fotograma Inicial-Final a video](https://docs.comfy.org/es/built-in-nodes/KlingStartEndFrameNode)[Kling 2.6 texto a video con audio](https://docs.comfy.org/es/built-in-nodes/KlingTextToVideoWithAudio)
