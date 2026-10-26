---
url: https://docs.comfy.org/es/built-in-nodes/TextEncodeQwenImageEdit/
title: Codificaci\u00f3n de texto para edici\u00f3n de Qwen Image - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:35.434041+00:00
---

# Codificación de texto para edición de Qwen Image - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TextEncodeQwenImageEdit/

Qwen Image

# Codificación de texto para edición de Qwen Image - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo TextEncodeQwenImageEdit convierte prompts de texto e imágenes opcionales en datos de condicionamiento para la generación o edición de imágenes.

Copiar páginaCopiar página

El nodo TextEncodeQwenImageEdit convierte prompts de texto e imágenes opcionales en datos de condicionamiento para la generación o edición de imágenes. Utiliza un modelo CLIP para tokenizar la entrada y, opcionalmente, puede codificar imágenes de referencia con un VAE para crear latentes de referencia. Cuando se proporciona una imagen, se redimensiona automáticamente para mantener una escala de procesamiento coherente.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP utilizado para la tokenización de texto e imágenes| CLIP| Sí| -  
`prompt`| Prompt de texto para la generación de condicionamiento; admite entrada multilínea y prompts dinámicos| STRING| Sí| -  
`vae`| Modelo VAE opcional para codificar imágenes de referencia en latentes| VAE| No| -  
`imagen`| Imagen de entrada opcional para fines de referencia o edición| IMAGE| No| -  
  
**Nota:** Cuando se proporciona una imagen, se redimensiona para que su número total de píxeles se mantenga cerca de 1.048.576 (1024 × 1024), y solo se utilizan sus canales RGB. La imagen redimensionada se pasa al tokenizador CLIP junto con el prompt. Cuando se proporcionan tanto `image` como `vae`, el nodo también codifica la imagen en latentes de referencia y los adjunta a la salida de condicionamiento.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`CONDITIONING`| Datos de condicionamiento que contienen tokens de texto y latentes de referencia opcionales para la generación de imágenes| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEdit/es.md)

* * *

**Source fingerprint (SHA-256):** `ec6980a63eab0d6c95be3abea00b2bf3018d30a1267f0b39a21be29a3e9228fe`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TextEncodeQwenImageEdit.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TextEncodeQwenImageEdit)

[Codificación de texto Qwen Image 2.1](https://docs.comfy.org/es/built-in-nodes/TextEncodeQwenImage21)[Codificación de texto para edición de Qwen Image Plus](https://docs.comfy.org/es/built-in-nodes/TextEncodeQwenImageEditPlus)
