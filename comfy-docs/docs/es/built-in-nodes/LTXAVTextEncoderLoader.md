---
url: https://docs.comfy.org/es/built-in-nodes/LTXAVTextEncoderLoader/
title: Cargador de codificador de texto LTXV audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:00.626582+00:00
---

# Cargador de codificador de texto LTXV audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LTXAVTextEncoderLoader/

Cargadores

# Cargador de codificador de texto LTXV audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo carga un codificador de texto especializado para el modelo de audio LTXV.

Copiar páginaCopiar página

Este nodo carga un codificador de texto especializado para el modelo de audio LTXV. Combina un archivo de codificador de texto con un archivo de checkpoint para crear un modelo CLIP utilizado para el condicionamiento de texto en la generación de audio. Según la descripción del nodo, el codificador de texto debe ser un Gemma 3 12B o un modelo Gemma 4 compatible.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`text_encoder`| El nombre del archivo del codificador de texto LTXV a cargar. Las opciones disponibles se cargan desde la carpeta `text_encoders`.| COMBO| Sí| Múltiples opciones disponibles  
`ckpt_name`| El nombre del archivo de checkpoint a cargar. Las opciones disponibles se cargan desde la carpeta `checkpoints`.| COMBO| Sí| Múltiples opciones disponibles  
`device`| Especifica el dispositivo en el que se cargará el modelo. Usa `"cpu"` para forzar la carga en la CPU. El comportamiento predeterminado (`"default"`) usa la colocación automática de dispositivos del sistema (predeterminado: `"default"`). Este es un parámetro avanzado.| COMBO| No| `"default"`  
`"cpu"`  
  
**Nota:** Los parámetros `text_encoder` y `ckpt_name` funcionan juntos. El nodo carga ambos archivos especificados para crear un único modelo CLIP funcional. Los archivos deben ser compatibles con la arquitectura LTXV, y el codificador de texto debe ser un Gemma 3 12B o un modelo Gemma 4 compatible.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`clip`| El modelo CLIP LTXV cargado, listo para usarse para codificar indicaciones de texto para la generación de audio.| CLIP  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/es.md)

* * *

**Source fingerprint (SHA-256):** `1f3df2c1791203ba849a87897de14052e0cb8370100dbca19df4cf30169a0a2a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LTXAVTextEncoderLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LTXAVTextEncoderLoader)

[Cargar modelo LoRA](https://docs.comfy.org/es/built-in-nodes/LoraModelLoader)[Cargador de LTXV audio VAE](https://docs.comfy.org/es/built-in-nodes/LTXVAudioVAELoader)
