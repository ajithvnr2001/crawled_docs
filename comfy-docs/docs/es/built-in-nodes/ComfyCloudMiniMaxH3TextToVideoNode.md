---
url: https://docs.comfy.org/es/built-in-nodes/ComfyCloudMiniMaxH3TextToVideoNode/
title: Comfy Cloud MiniMax H3 Texto a v\u00eddeo [BETA] - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:39.080708+00:00
---

# Comfy Cloud MiniMax H3 Texto a vídeo [BETA] - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ComfyCloudMiniMaxH3TextToVideoNode/

Avanzado

# Comfy Cloud MiniMax H3 Texto a vídeo [BETA] - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Ejecuta el flujo de trabajo de texto a vídeo de MiniMax H3 en una GPU de Comfy Cloud y devuelve un vídeo con una banda sonora acorde.

Copiar páginaCopiar página

Ejecuta el flujo de trabajo de texto a vídeo de MiniMax H3 en una GPU de Comfy Cloud y devuelve un vídeo con una banda sonora acorde. La imagen y el audio se generan en la misma pasada, en lugar de añadirse posteriormente mediante doblaje. Este es un nodo beta y se factura por segundo de GPU.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| La descripción textual del vídeo, incluidos los sonidos que debe contener la toma. Los espacios en blanco iniciales y finales se eliminan antes del envío.| STRING| Sí| 1 a 4096 caracteres  
`seed`| Semilla aleatoria que controla el resultado generado (predeterminado: 42).| INT| Sí| 0 a 18446744073709551615  
`aspect_ratio`| Relación de aspecto del vídeo generado (predeterminado: `"16:9"`).| COMBO| Sí| `"1:1"`  
`"3:4"`  
`"2:3"`  
`"3:2"`  
`"4:3"`  
`"16:9"`  
`"9:16"`  
`"21:9"`  
`resolution`| Presupuesto de tamaño de fotograma (predeterminado: `"480p"`). 720p cuesta aproximadamente el doble de segundos de GPU que 480p.| COMBO| Sí| `"480p"`  
`"720p"`  
`duration_seconds`| Duración en segundos (predeterminado: 5). El pipeline cuantiza en pasos de 17 fotogramas a 24 fps, por lo que el clip queda dentro de aproximadamente dos tercios de segundo de este valor.| INT| Sí| 5 a 15  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`VIDEO`| El vídeo generado con su banda sonora.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3TextToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `bd1cbc80baa3b77ba48b529119495052252570b949676742b4c77cfe86b70ee2`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ComfyCloudMiniMaxH3TextToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ComfyCloudMiniMaxH3TextToVideoNode)

[Comfy Cloud MiniMax H3 Imagen a vídeo [BETA]](https://docs.comfy.org/es/built-in-nodes/ComfyCloudMiniMaxH3ImageToVideoNode)[Comfy Cloud MiniMax Music 3 Texto a audio [BETA]](https://docs.comfy.org/es/built-in-nodes/ComfyCloudMiniMaxMusic3TextToAudioNode)
