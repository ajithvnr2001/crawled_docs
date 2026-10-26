---
url: https://docs.comfy.org/es/built-in-nodes/DualCLIPLoader/
title: Cargar CLIP dual - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:44.058398+00:00
---

# Cargar CLIP dual - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/DualCLIPLoader/

Cargadores

# Cargar CLIP dual - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo DualCLIPLoader está diseñado para cargar dos modelos CLIP simultáneamente

Copiar páginaCopiar página

El nodo DualCLIPLoader está diseñado para cargar dos modelos CLIP simultáneamente, facilitando operaciones que requieren la integración o comparación de características de ambos modelos. Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/text_encoders`.

## 

​

Entradas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`clip_name1`| Especifica el nombre del primer modelo CLIP a cargar. Este parámetro es crucial para identificar y recuperar el modelo correcto de una lista predefinida de modelos CLIP disponibles.| COMBO[STRING]  
`clip_name2`| Especifica el nombre del segundo modelo CLIP a cargar. Este parámetro permite cargar un segundo modelo CLIP distinto para realizar análisis comparativos o integradores junto con el primer modelo.| COMBO[STRING]  
`tipo`| Elija entre “sdxl”, “sd3”, “flux” para adaptarse a diferentes modelos.| `option`  
  
  * El orden de carga no afecta el resultado de salida



## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`clip`| La salida es un modelo CLIP combinado que integra las características o funcionalidades de los dos modelos CLIP especificados.| CLIP  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/DualCLIPLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/DualCLIPLoader)

[Cargar modelo Diffusers (obsoleto)](https://docs.comfy.org/es/built-in-nodes/DiffusersLoader)[Cargar modelo de interpolación de fotogramas](https://docs.comfy.org/es/built-in-nodes/FrameInterpolationModelLoader)
