---
url: https://docs.comfy.org/es/built-in-nodes/StyleModelApply/
title: Aplicar modelo de estilo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:33.930778+00:00
---

# Aplicar modelo de estilo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/StyleModelApply/

Acondicionamiento

# Aplicar modelo de estilo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo aplica un modelo de estilo a un condicionamiento dado, mejorando o alterando su estilo basándose en la salida de un modelo de visión CLIP.

Copiar páginaCopiar página

Este nodo aplica un modelo de estilo a un condicionamiento dado, mejorando o alterando su estilo basándose en la salida de un modelo de visión CLIP. Integra el condicionamiento del modelo de estilo en el condicionamiento existente, permitiendo una combinación fluida de estilos en el proceso de generación.

## 

​

Entradas

### 

​

Requeridas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`acondicionamiento`| Los datos de condicionamiento originales a los que se aplicará el condicionamiento del modelo de estilo. Es fundamental para definir el contexto o estilo base que se mejorará o alterará.| `CONDITIONING`  
`modelo_de_estilo`| El modelo de estilo utilizado para generar un nuevo condicionamiento basado en la salida del modelo de visión CLIP. Desempeña un papel clave en la definición del nuevo estilo a aplicar.| `STYLE_MODEL`  
`salida_de_clip_vision`| La salida de un modelo de visión CLIP, que el modelo de estilo utiliza para generar un nuevo condicionamiento. Proporciona el contexto visual necesario para la aplicación del estilo.| `CLIP_VISION_OUTPUT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`acondicionamiento`| El condicionamiento mejorado o alterado, que incorpora la salida del modelo de estilo. Representa el condicionamiento final estilizado, listo para su posterior procesamiento o generación.| `CONDITIONING`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelApply/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/StyleModelApply.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/StyleModelApply)

[Aplicar Condicionamiento SeedVR2](https://docs.comfy.org/es/built-in-nodes/SeedVR2Conditioning)[Opciones de tokenizador T5](https://docs.comfy.org/es/built-in-nodes/T5TokenizerOptions)
