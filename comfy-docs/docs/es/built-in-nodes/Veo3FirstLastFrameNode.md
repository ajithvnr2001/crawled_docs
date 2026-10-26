---
url: https://docs.comfy.org/es/built-in-nodes/Veo3FirstLastFrameNode/
title: Google Veo 3 Primer-\u00daltimo fotograma a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:41.841952+00:00
---

# Google Veo 3 Primer-Último fotograma a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Veo3FirstLastFrameNode/

Veo

# Google Veo 3 Primer-Último fotograma a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Veo3FirstLastFrameNode utiliza el modelo Veo 3 de Google para generar un video basado en un prompt de texto

Copiar páginaCopiar página

El nodo Veo3FirstLastFrameNode utiliza el modelo Veo 3 de Google para generar un video basado en un prompt de texto, con un primer y último fotograma proporcionados que definen el inicio y el final de la secuencia de video.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Descripción textual del video (valor predeterminado: cadena vacía).| STRING| Sí| N/A  
`negative_prompt`| Prompt de texto negativo para guiar qué evitar en el video (valor predeterminado: cadena vacía).| STRING| No| N/A  
`resolución`| La resolución del video de salida.| COMBO| Sí| `"720p"`  
`"1080p"`  
`"4k"`  
`relación de aspecto`| Relación de aspecto del video de salida (valor predeterminado: “16:9”).| COMBO| No| `"16:9"`  
`"9:16"`  
`duración`| Duración del video de salida en segundos (valor predeterminado: 8).| INT| No| 4 a 8  
`semilla`| Semilla para la generación del video (valor predeterminado: 0).| INT| No| 0 a 4294967295  
`primer_fotograma`| El fotograma de inicio del video.| IMAGE| Sí| N/A  
`último_fotograma`| El fotograma final del video.| IMAGE| Sí| N/A  
`modelo`| El modelo Veo 3 específico a utilizar para la generación (valor predeterminado: “veo-3.1-generate”).| COMBO| No| `"veo-3.1-generate"`  
`"veo-3.1-fast-generate"`  
`"veo-3.1-lite"`  
`generar_audio`| Generar audio para el video (valor predeterminado: True).| BOOLEAN| No| N/A  
  
**Nota:** El modelo `veo-3.1-lite` no admite resolución 4K. Si seleccionas `veo-3.1-lite` y resolución `4k`, se producirá un error.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| El archivo de video generado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/es.md)

* * *

**Source fingerprint (SHA-256):** `b486b22e71a305172700760bb3eff256b0e571bba75e68f27e23a1e1a1319b5a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Veo3FirstLastFrameNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Veo3FirstLastFrameNode)

[Topaz Video Enhance](https://docs.comfy.org/es/built-in-nodes/TopazVideoEnhanceV2)[Generación de video Google Veo 3](https://docs.comfy.org/es/built-in-nodes/Veo3VideoGenerationNode)
