---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningStableAudio/
title: Acondicionamiento Stable Audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:40.959924+00:00
---

# Acondicionamiento Stable Audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningStableAudio/

Stable Audio

# Acondicionamiento Stable Audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ConditioningStableAudio añade información temporal tanto a las entradas de condicionamiento positivo como negativo para la generación de audio.

Copiar páginaCopiar página

El nodo ConditioningStableAudio añade información temporal tanto a las entradas de condicionamiento positivo como negativo para la generación de audio. Establece los parámetros de tiempo de inicio y duración total que ayudan a controlar cuándo y durante cuánto tiempo se debe generar el contenido de audio. Este nodo modifica los datos de condicionamiento existentes agregando metadatos temporales específicos de audio.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`positivo`| La entrada de condicionamiento positivo que se modificará con información temporal de audio| CONDITIONING| Sí| -  
`negativo`| La entrada de condicionamiento negativo que se modificará con información temporal de audio| CONDITIONING| Sí| -  
`segundos_inicio`| El tiempo de inicio en segundos para la generación de audio (por defecto: 0.0)| FLOAT| Sí| 0.0 a 1000.0  
`segundos_total`| La duración total en segundos para la generación de audio (por defecto: 47.0)| FLOAT| Sí| 0.0 a 1000.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positivo`| El condicionamiento positivo modificado con la información temporal de audio aplicada| CONDITIONING  
`negativo`| El condicionamiento negativo modificado con la información temporal de audio aplicada| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningStableAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningStableAudio)

[Codificación de texto para edición de Qwen Image Plus](https://docs.comfy.org/es/built-in-nodes/TextEncodeQwenImageEditPlus)[Acondicionamiento Stable Cascade etapa B](https://docs.comfy.org/es/built-in-nodes/StableCascade_StageB_Conditioning)
