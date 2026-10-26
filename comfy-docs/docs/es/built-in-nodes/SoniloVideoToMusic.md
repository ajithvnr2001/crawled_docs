---
url: https://docs.comfy.org/es/built-in-nodes/SoniloVideoToMusic/
title: Sonilo Video a M\u00fasica - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:31.708358+00:00
---

# Sonilo Video a Música - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SoniloVideoToMusic/

Sonilo

# Sonilo Video a Música - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

Copiar páginaCopiar página

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento: Genera música a partir de video utilizando el modelo de IA de Sonilo. Este nodo analiza el contenido de un video de entrada y crea una pieza musical que lo acompaña. Utiliza un servicio de IA externo para procesar el video y generar el audio.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`video`| Video de entrada para generar música. Duración máxima: 6 minutos.| VIDEO| Sí| -  
`prompt`| Indicación textual opcional para guiar la generación musical. Déjelo vacío para obtener la mejor calidad: el modelo analizará completamente el contenido del video. (predeterminado: cadena vacía)| STRING| No| -  
`seed`| Semilla para reproducibilidad. Actualmente ignorada por el servicio Sonilo, pero se mantiene para la consistencia del grafo. (predeterminado: 0)| INT| No| 0 a 18446744073709551615  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`audio`| La música generada como archivo de audio.| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/es.md)

* * *

**Source fingerprint (SHA-256):** `542fff1d8db8e48156bf9d1ff4690c91a7d71676332eef4708a6d36686abb31e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SoniloVideoToMusic.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SoniloVideoToMusic)

[Sonilo Texto a Música](https://docs.comfy.org/es/built-in-nodes/SoniloTextToMusic)[Clonación instantánea de voz HeyGen Voice 1.0](https://docs.comfy.org/es/built-in-nodes/HeyGenVoiceCloneNode)
