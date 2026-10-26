---
url: https://docs.comfy.org/es/built-in-nodes/CreateHookModelAsLoraModelOnly/
title: Crear hook model como LoRA (MO) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:42.463464+00:00
---

# Crear hook model como LoRA (MO) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CreateHookModelAsLoraModelOnly/

Crear

# Crear hook model como LoRA (MO) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo crea un hook que aplica un modelo LoRA (Adaptación de Bajo Rango) para modificar únicamente el componente de modelo de una red neuronal.

Copiar páginaCopiar página

Este nodo crea un hook que aplica un modelo LoRA (Adaptación de Bajo Rango) para modificar únicamente el componente de modelo de una red neuronal. Carga un archivo checkpoint y lo aplica con una intensidad específica al modelo, dejando el componente CLIP sin cambios. Este es un nodo experimental que extiende la funcionalidad de la clase base CreateHookModelAsLora.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`ckpt_name`| El archivo checkpoint a cargar como modelo LoRA. Las opciones disponibles dependen del contenido de la carpeta de checkpoints.| STRING| Sí| Múltiples opciones disponibles  
`strength_model`| El multiplicador de intensidad para aplicar la LoRA al componente del modelo (predeterminado: 1.0)| FLOAT| Sí| -20.0 a 20.0  
`prev_hooks`| Hooks previos opcionales para encadenar con este hook| HOOKS| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`hooks`| El grupo de hooks creado que contiene la modificación del modelo LoRA| HOOKS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/es.md)

* * *

**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CreateHookModelAsLoraModelOnly.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CreateHookModelAsLoraModelOnly)

[Crear hook model como LoRA](https://docs.comfy.org/es/built-in-nodes/CreateHookModelAsLora)[Crear hook keyframe](https://docs.comfy.org/es/built-in-nodes/CreateHookKeyframe)
