---
url: https://docs.comfy.org/es/built-in-nodes/PreviewAudio/
title: Vista previa de audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:18.727586+00:00
---

# Vista previa de audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PreviewAudio/

Audio

# Vista previa de audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Preview Audio te permite escuchar audio directamente dentro de ComfyUI sin guardarlo en el directorio de salida.

Copiar páginaCopiar página

El nodo Preview Audio te permite escuchar audio directamente dentro de ComfyUI sin guardarlo en el directorio de salida. Recibe una entrada de audio, comprueba que los datos de audio estén realmente presentes y luego lo reproduce mediante un reproductor de vista previa en la interfaz, mientras pasa el mismo audio como su salida.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`audio`| Los datos de audio que se van a previsualizar. Si esta entrada es None, el nodo genera un ValueError, lo cual puede ocurrir cuando el video de origen no tiene pista de audio.| AUDIO| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`audio`| Los datos de audio pasados sin cambios desde la entrada, de modo que el nodo se puede colocar en medio de un flujo de trabajo.| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PreviewAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PreviewAudio)

[Cargar audio](https://docs.comfy.org/es/built-in-nodes/LoadAudio)[Grabar audio](https://docs.comfy.org/es/built-in-nodes/RecordAudio)
