---
url: https://docs.comfy.org/es/built-in-nodes/TextEncodeQwenImageEditPlus/
title: Codificaci\u00f3n de texto para edici\u00f3n de Qwen Image Plus - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:35.981815+00:00
---

# Codificación de texto para edición de Qwen Image Plus - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TextEncodeQwenImageEditPlus/

Qwen Image

# Codificación de texto para edición de Qwen Image Plus - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo TextEncodeQwenImageEditPlus procesa un prompt de texto y hasta tres imágenes opcionales para producir datos de condicionamiento para tareas de

Copiar páginaCopiar página

El nodo TextEncodeQwenImageEditPlus procesa un prompt de texto y hasta tres imágenes opcionales para producir datos de condicionamiento para tareas de generación o edición de imágenes. Utiliza una plantilla especializada que primero solicita al modelo que describa las características clave de las imágenes de entrada y luego explique cómo la instrucción de texto del usuario debería modificarlas, de modo que el resultado codificado comprenda tanto las imágenes como la modificación solicitada. Cuando se proporciona una VAE, el nodo también crea latentes de referencia a partir de las imágenes de entrada.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP utilizado para la tokenización y codificación| CLIP| Sí| -  
`prompt`| Instrucción de texto que describe la modificación de imagen deseada (admite entrada multilínea y prompts dinámicos)| STRING| Sí| -  
`vae`| Modelo VAE opcional para generar latentes de referencia a partir de las imágenes de entrada| VAE| No| -  
`imagen1`| Primera imagen de entrada opcional para análisis y modificación| IMAGE| No| -  
`imagen2`| Segunda imagen de entrada opcional para análisis y modificación| IMAGE| No| -  
`imagen3`| Tercera imagen de entrada opcional para análisis y modificación| IMAGE| No| -  
  
**Nota:** Cuando se proporciona una VAE, el nodo genera latentes de referencia a partir de todas las imágenes de entrada proporcionadas. Se pueden procesar hasta tres imágenes a la vez. Las imágenes se escalan a un área objetivo de 384x384 píxeles (relación de aspecto preservada) para el procesamiento de visión-lenguaje, y a dimensiones divisibles por 8 (con un área objetivo de 1024x1024 píxeles) para la codificación VAE.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`CONDITIONING`| Datos de condicionamiento codificados que contienen tokens de texto y latentes de referencia opcionales para la generación de imágenes| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/es.md)

* * *

**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TextEncodeQwenImageEditPlus.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TextEncodeQwenImageEditPlus)

[Codificación de texto para edición de Qwen Image](https://docs.comfy.org/es/built-in-nodes/TextEncodeQwenImageEdit)[Acondicionamiento Stable Audio](https://docs.comfy.org/es/built-in-nodes/ConditioningStableAudio)
