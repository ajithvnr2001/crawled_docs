---
url: https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeControlnet/
title: Codificar texto CLIP para ControlNet - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:36.668742+00:00
---

# Codificar texto CLIP para ControlNet - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeControlnet/

Acondicionamiento

# Codificar texto CLIP para ControlNet - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CLIP Text Encode (Controlnet) codifica un prompt de texto con un modelo CLIP y agrega la codificación de texto resultante a los datos de

Copiar páginaCopiar página

El nodo CLIP Text Encode (Controlnet) codifica un prompt de texto con un modelo CLIP y agrega la codificación de texto resultante a los datos de condicionamiento existentes. Almacena las incrustaciones de texto como parámetros de atención cruzada de controlnet dentro de cada entrada de condicionamiento, por lo que el condicionamiento devuelto incluye esa información adicional de controlnet.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP usado para la tokenización y codificación de texto| CLIP| Sí| -  
`condicionamiento`| Datos de condicionamiento existentes que se combinarán con la codificación de texto de CLIP| CONDITIONING| Sí| -  
`texto`| El prompt de texto que procesará el modelo CLIP. Admite texto multilínea y prompts dinámicos| STRING| Sí| -  
  
**Nota:** Las tres entradas (`clip`, `conditioning` y `text`) son necesarias para que este nodo funcione. La entrada `text` admite texto multilínea y prompts dinámicos para un procesamiento de texto flexible. Este nodo está marcado como experimental en el código fuente.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`CONDITIONING`| Datos de condicionamiento mejorados con los parámetros de atención cruzada de controlnet agregados (`cross_attn_controlnet` y `pooled_output_controlnet`) derivados de la codificación de texto de CLIP| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/es.md)

* * *

**Source fingerprint (SHA-256):** `95a798684ca8734bfff53c7b979b320f6834dc1a9553163d0e567243761000f1`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CLIPTextEncodeControlnet.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CLIPTextEncodeControlnet)

[Codificar texto CLIP (Prompt)](https://docs.comfy.org/es/built-in-nodes/CLIPTextEncode)[Codificar CLIP Vision](https://docs.comfy.org/es/built-in-nodes/CLIPVisionEncode)
