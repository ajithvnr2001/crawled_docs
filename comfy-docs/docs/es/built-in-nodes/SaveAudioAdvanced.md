---
url: https://docs.comfy.org/es/built-in-nodes/SaveAudioAdvanced/
title: Guardar audio (avanzado) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:28.457285+00:00
---

# Guardar audio (avanzado) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveAudioAdvanced/

Audio

# Guardar audio (avanzado) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Guarda el audio de entrada en el directorio de salida de ComfyUI.

Copiar páginaCopiar página

Guarda el audio de entrada en el directorio de salida de ComfyUI. Este nodo permite exportar audio en varios formatos, incluyendo FLAC, MP3 y Opus, con ajustes de calidad configurables.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`audio`| El audio que se va a guardar.| AUDIO| Sí| -  
`prefijo_nombre_archivo`| El prefijo para el archivo que se va a guardar. Puede incluir tokens de formato como %date:yyyy-MM-dd%. (por defecto: “audio/ComfyUI”)| STRING| Sí| -  
`formato`| El formato de archivo en el que se guardará el audio.| DYNAMIC_COMBO| Sí| ”flac"  
"mp3"  
"opus”  
  
### 

​

Entradas de MP3

Cuando se selecciona “mp3” como formato, el siguiente ajuste está disponible.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`quality`| La calidad de codificación del archivo MP3 de salida. (por defecto: “V0”)| COMBO| No| ”V0"  
"128k"  
"320k”  
  
### 

​

Entradas de Opus

Cuando se selecciona “opus” como formato, el siguiente ajuste está disponible.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`quality`| La calidad de codificación del archivo Opus de salida. (por defecto: “128k”)| COMBO| No| ”64k"  
"96k"  
"128k"  
"192k"  
"320k”  
  
Nota: El ajuste `quality` solo está disponible cuando se selecciona el formato correspondiente. Cuando se selecciona “flac”, no hay ningún ajuste de calidad adicional disponible.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`audio`| El audio de entrada, pasado sin cambios después de guardarse.| AUDIO  
  
El nodo también devuelve información de interfaz de usuario que contiene la información del archivo de audio guardado.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/es.md)

* * *

**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveAudioAdvanced.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveAudioAdvanced)

[Guardar audio](https://docs.comfy.org/es/built-in-nodes/SaveAudio)[Guardar audio (MP3)](https://docs.comfy.org/es/built-in-nodes/SaveAudioMP3)
