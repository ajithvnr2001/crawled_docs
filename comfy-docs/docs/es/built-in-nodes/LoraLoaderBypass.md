---
url: https://docs.comfy.org/es/built-in-nodes/LoraLoaderBypass/
title: Cargar LoRA (Bypass) (Para depuraci\u00f3n) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:06.107728+00:00
---

# Cargar LoRA (Bypass) (Para depuración) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoraLoaderBypass/

Cargadores

# Cargar LoRA (Bypass) (Para depuración) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LoraLoaderBypass aplica una LoRA (Low-Rank Adaptation) a un modelo de difusión y a un modelo CLIP en un modo especial “bypass”.

Copiar páginaCopiar página

El nodo LoraLoaderBypass aplica una LoRA (Low-Rank Adaptation) a un modelo de difusión y a un modelo CLIP en un modo especial “bypass”. A diferencia de un cargador de LoRA estándar, este método no modifica permanentemente los pesos del modelo base. En su lugar, calcula el resultado sumando la contribución de la LoRA a la pasada hacia adelante normal del modelo, lo cual es útil para entrenamiento o cuando se trabaja con modelos cuyos pesos están descargados de memoria.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| El modelo de difusión al que se aplicará la LoRA.| MODEL| Sí| -  
`clip`| El modelo CLIP al que se aplicará la LoRA.| CLIP| Sí| -  
`lora_name`| El nombre de la LoRA. Los archivos LoRA disponibles se cargan desde la carpeta `loras`.| COMBO| Sí| Lista de archivos LoRA disponibles  
`strength_model`| Intensidad con la que se modifica el modelo de difusión. Este valor puede ser negativo (predeterminado: 1.0).| FLOAT| Sí| -100.0 a 100.0 (paso: 0.01)  
`strength_clip`| Intensidad con la que se modifica el modelo CLIP. Este valor puede ser negativo (predeterminado: 1.0).| FLOAT| Sí| -100.0 a 100.0 (paso: 0.01)  
  
**Nota:** Si tanto `strength_model` como `strength_clip` se establecen en 0, el nodo devuelve las entradas originales `model` y `clip` sin modificar y sin procesamiento. **Nota:** El archivo LoRA seleccionado se almacena en caché después de cargarse por primera vez. Solo se vuelve a leer desde el disco cuando se elige un `lora_name` diferente.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`MODEL`| El modelo de difusión modificado.| MODEL  
`CLIP`| El modelo CLIP modificado.| CLIP  
  
**Nota:** Este nodo está marcado como experimental.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/es.md)

* * *

**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoraLoaderBypass.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoraLoaderBypass)

[Cargar modelo MoGe](https://docs.comfy.org/es/built-in-nodes/LoadMoGeModel)[Cargar LoRA (Bypass, solo modelo) (para depuración)](https://docs.comfy.org/es/built-in-nodes/LoraLoaderBypassModelOnly)
