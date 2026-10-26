---
url: https://docs.comfy.org/es/built-in-nodes/LTXVAudioVAELoader/
title: Cargador de LTXV audio VAE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:01.204150+00:00
---

# Cargador de LTXV audio VAE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LTXVAudioVAELoader/

Cargadores

# Cargador de LTXV audio VAE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LTXV Audio VAE Loader carga un modelo de autoencoder variacional de audio (VAE) preentrenado desde un archivo de checkpoint.

Copiar páginaCopiar página

El nodo LTXV Audio VAE Loader carga un modelo de autoencoder variacional de audio (VAE) preentrenado desde un archivo de checkpoint. Lee el checkpoint especificado, conserva los pesos del VAE de audio y del vocoder, y prepara el modelo para usarlo en flujos de trabajo de generación o procesamiento de audio dentro de ComfyUI.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`ckpt_name`| Checkpoint del VAE de audio que se va a cargar. Es una lista desplegable que se completa con todos los archivos encontrados en el directorio `checkpoints` de ComfyUI.| COMBO| Sí| Todos los archivos de la carpeta `checkpoints`. La lista se genera en tiempo de ejecución.  
  
El archivo seleccionado debe ser un checkpoint válido del VAE de audio LTXV. El nodo conserva únicamente los pesos del VAE de audio y del vocoder del archivo, y lanza un error si el modelo cargado no es un VAE válido.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`Audio VAE`| El modelo de autoencoder variacional de audio (VAE) cargado, listo para conectarse a otros nodos de procesamiento de audio.| VAE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/es.md)

* * *

**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LTXVAudioVAELoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LTXVAudioVAELoader)

[Cargador de codificador de texto LTXV audio](https://docs.comfy.org/es/built-in-nodes/LTXAVTextEncoderLoader)[Cargar parche de modelo](https://docs.comfy.org/es/built-in-nodes/ModelPatchLoader)
