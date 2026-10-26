---
url: https://docs.comfy.org/es/built-in-nodes/AudioEncoderLoader/
title: Cargar codificador de audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:31.287800+00:00
---

# Cargar codificador de audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/AudioEncoderLoader/

Cargadores

# Cargar codificador de audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo AudioEncoderLoader carga un modelo de codificador de audio desde un archivo guardado en tu carpeta audioencoders.

Copiar páginaCopiar página

## 

​

Descripción general

El nodo AudioEncoderLoader carga un modelo de codificador de audio desde un archivo almacenado en su carpeta `audio_encoders`. Toma el nombre de archivo de un modelo de codificador de audio como entrada y devuelve el modelo cargado, que luego puede usarse para tareas de procesamiento de audio en su flujo de trabajo. Si el archivo seleccionado no contiene un modelo de codificador de audio válido, el nodo genera un error.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`nombre_codificador_audio`| Selecciona qué archivo de modelo de codificador de audio cargar desde la carpeta de codificadores de audio| COMBO| Sí| Lista de archivos de codificador de audio disponibles en la carpeta `audio_encoders`  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`audio_encoder`| El modelo de codificador de audio cargado, listo para usar en flujos de trabajo de procesamiento de audio| AUDIO_ENCODER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/es.md)

* * *

**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/AudioEncoderLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/AudioEncoderLoader)

[Codificación VAE (Mosaico)](https://docs.comfy.org/es/built-in-nodes/VAEEncodeTiled)[Cargar punto de control con configuración (OBSOLETO)](https://docs.comfy.org/es/built-in-nodes/CheckpointLoader)
