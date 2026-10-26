---
url: https://docs.comfy.org/es/built-in-nodes/AudioEncoderEncode/
title: Codificar con codificador de audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:31.227014+00:00
---

# Codificar con codificador de audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/AudioEncoderEncode/

Acondicionamiento

# Codificar con codificador de audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo AudioEncoderEncode convierte audio en una representación codificada utilizando un modelo de codificador de audio.

Copiar páginaCopiar página

El nodo AudioEncoderEncode convierte audio en una representación codificada utilizando un modelo de codificador de audio. Toma un codificador de audio y una entrada de audio, luego extrae la forma de onda y la frecuencia de muestreo del audio y las pasa al codificador para producir una salida codificada.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`codificador_audio`| El modelo de codificador de audio utilizado para procesar la entrada de audio| AUDIO_ENCODER| Sí| -  
`audio`| Los datos de audio que contienen la información de la forma de onda y la frecuencia de muestreo| AUDIO| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| La representación de audio codificada producida por el codificador de audio| AUDIO_ENCODER_OUTPUT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/es.md)

* * *

**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/AudioEncoderEncode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/AudioEncoderEncode)

[Codificar texto ZImage Omni](https://docs.comfy.org/es/built-in-nodes/TextEncodeZImageOmni)[Establecer última capa de CLIP](https://docs.comfy.org/es/built-in-nodes/CLIPSetLastLayer)
