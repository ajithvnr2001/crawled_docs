---
url: https://docs.comfy.org/es/built-in-nodes/T5TokenizerOptions/
title: Opciones de tokenizador T5 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:34.133088+00:00
---

# Opciones de tokenizador T5 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/T5TokenizerOptions/

Acondicionamiento

# Opciones de tokenizador T5 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo T5TokenizerOptions configura los ajustes del tokenizador para varios tipos de modelo T5.

Copiar páginaCopiar página

## 

​

Descripción general

El nodo T5TokenizerOptions configura los ajustes del tokenizer para varios tipos de modelos T5. Establece los parámetros de padding mínimo y longitud mínima para múltiples variantes de modelos T5, incluyendo t5xxl, pile_t5xl, t5base, mt5xl y umt5xxl. El nodo toma una entrada CLIP, aplica la configuración a una copia de esta y devuelve el CLIP modificado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP para el que se configurarán las opciones del tokenizer| CLIP| Sí| -  
`mín_relleno`| Valor mínimo de padding a establecer para todos los tipos de modelo T5 (predeterminado: 0)| INT| Sí| 0 a 10000  
`mín_longitud`| Valor mínimo de longitud a establecer para todos los tipos de modelo T5 (predeterminado: 0)| INT| Sí| 0 a 10000  
  
Nota: Este nodo está marcado como experimental en ComfyUI. La configuración se aplica a todas las variantes T5 compatibles a la vez: t5xxl, pile_t5xl, t5base, mt5xl y umt5xxl. La entrada `clip` se clona antes de la modificación, por lo que el CLIP original no se altera.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El modelo CLIP modificado con opciones de tokenizer actualizadas aplicadas a todas las variantes de T5| CLIP  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/es.md)

* * *

**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/T5TokenizerOptions.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/T5TokenizerOptions)

[Aplicar modelo de estilo](https://docs.comfy.org/es/built-in-nodes/StyleModelApply)[Acondicionamiento unCLIP](https://docs.comfy.org/es/built-in-nodes/unCLIPConditioning)
