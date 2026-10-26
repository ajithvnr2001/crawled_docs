---
url: https://docs.comfy.org/es/built-in-nodes/SaveAudio/
title: Guardar audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:28.515932+00:00
---

# Guardar audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveAudio/

Audio

# Guardar audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo guarda datos de audio en un archivo en formato FLAC.

Copiar páginaCopiar página

Este nodo guarda datos de audio en un archivo en formato FLAC. Toma una entrada de audio y la escribe en el directorio de salida usando el prefijo de nombre de archivo especificado, y también transfiere el audio a su salida. Este nodo está obsoleto y debe reemplazarse con el nodo Save Audio actual.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`audio`| Los datos de audio que se van a guardar| AUDIO| Sí| -  
`prefijo_nombre_archivo`| El prefijo para el nombre del archivo de salida (predeterminado: “audio/ComfyUI”)| STRING| No| -  
  
_Nota: Los parámetros`prompt` y `extra_pnginfo` están ocultos y son gestionados automáticamente por el sistema._ Si la entrada `audio` no recibe datos (por ejemplo, cuando el video de origen no tiene pista de audio), el nodo genera un error y no se guarda ningún archivo.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`audio`| Los datos de audio que se proporcionaron a la entrada, transferidos a la salida después de guardar el archivo| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveAudio)

[Grabar audio](https://docs.comfy.org/es/built-in-nodes/RecordAudio)[Guardar audio (avanzado)](https://docs.comfy.org/es/built-in-nodes/SaveAudioAdvanced)
