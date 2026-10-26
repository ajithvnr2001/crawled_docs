---
url: https://docs.comfy.org/es/built-in-nodes/VideoTemporalCrop/
title: Recortar video (temporal) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:42.551900+00:00
---

# Recortar video (temporal) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VideoTemporalCrop/

Transformación

# Recortar video (temporal) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo recorta un rango continuo de fotogramas de un video.

Copiar páginaCopiar página

Este nodo recorta un rango continuo de fotogramas de un video. Funciona de manera completamente perezosa (lazy), lo que significa que solo procesa la porción seleccionada del video según sea necesario más adelante en el flujo de trabajo.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`video`| Video de entrada.| VIDEO| Sí| –  
`fotograma_inicio`| Índice del fotograma inicial (predeterminado: 0).| INT| Sí| 0 a 99999  
`longitud`| Número de fotogramas a conservar (predeterminado: 16).| INT| Sí| 1 a 99999  
Nota: `start_frame` está limitado al último fotograma del video, y `length` se reduce si se extendería más allá de los fotogramas disponibles.| | | |   
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`video`| Video recortado (perezoso).| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTemporalCrop/es.md)

* * *

**Source fingerprint (SHA-256):** `1d28a55399c9fe7ca47f0aaa872751ac89c5419a6f6be6636fbf7f020a02749d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VideoTemporalCrop.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VideoTemporalCrop)

[Recortar video (temporal aleatorio)](https://docs.comfy.org/es/built-in-nodes/VideoRandomTemporalCrop)[Concatenar vídeo](https://docs.comfy.org/es/built-in-nodes/ConcatenateVideo)
