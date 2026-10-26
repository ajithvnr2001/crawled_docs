---
url: https://docs.comfy.org/es/built-in-nodes/SaveAudioOpus/
title: Guardar audio (Opus) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:28.575641+00:00
---

# Guardar audio (Opus) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveAudioOpus/

Audio

# Guardar audio (Opus) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SaveAudioOpus guarda datos de audio en un archivo en formato Opus

Copiar páginaCopiar página

El nodo SaveAudioOpus guarda datos de audio en un archivo en formato Opus, permitiéndote elegir la calidad de codificación (bitrate) y el prefijo del nombre de archivo para el archivo exportado. Este nodo está obsoleto y puede eliminarse en versiones futuras.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`audio`| Los datos de audio que se guardarán como archivo Opus. Se genera un ValueError si esto es None (por ejemplo, cuando el video de origen no tiene pista de audio).| AUDIO| Sí| -  
`prefijo_nombre_archivo`| El prefijo utilizado para el nombre del archivo de salida (predeterminado: “audio/ComfyUI”).| STRING| No| -  
`calidad`| El bitrate utilizado para codificar el archivo Opus; los valores más altos producen mejor calidad pero archivos más grandes (predeterminado: “128k”).| COMBO| No| `"64k"`  
`"96k"`  
`"128k"`  
`"192k"`  
`"320k"`  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`audio`| Los datos de audio que se guardaron en el archivo Opus.| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/es.md)

* * *

**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveAudioOpus.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveAudioOpus)

[Guardar audio (MP3)](https://docs.comfy.org/es/built-in-nodes/SaveAudioMP3)[Separar canales de audio](https://docs.comfy.org/es/built-in-nodes/SplitAudioChannels)
