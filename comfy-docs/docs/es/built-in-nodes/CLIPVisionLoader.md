---
url: https://docs.comfy.org/es/built-in-nodes/CLIPVisionLoader/
title: Cargar CLIP vision - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:37.760478+00:00
---

# Cargar CLIP vision - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CLIPVisionLoader/

Cargadores

# Cargar CLIP vision - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detecta automáticamente los modelos ubicados en la carpeta ComfyUI/models/clipvision

Copiar páginaCopiar página

Este nodo detecta automáticamente los modelos ubicados en la carpeta `ComfyUI/models/clip_vision`, así como cualquier ruta de modelo adicional configurada en el archivo `extra_model_paths.yaml`. Si agregas modelos después de iniciar ComfyUI, **actualiza la interfaz de ComfyUI** para asegurarte de que los archivos de modelo más recientes aparezcan listados.

## 

​

Entradas

Campo| Descripción| Tipo de dato  
---|---|---  
`clip_name`| Lista todos los archivos de modelo compatibles en la carpeta `ComfyUI/models/clip_vision`.| COMBO[STRING]  
  
## 

​

Salidas

Campo| Descripción| Tipo de dato  
---|---|---  
`clip_vision`| Modelo CLIP Vision cargado, listo para codificar imágenes u otras tareas relacionadas con la visión.| CLIP_VISION  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CLIPVisionLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CLIPVisionLoader)

[Cargar CLIP](https://docs.comfy.org/es/built-in-nodes/CLIPLoader)[Cargar condicionamiento](https://docs.comfy.org/es/built-in-nodes/ConditioningLoader)
