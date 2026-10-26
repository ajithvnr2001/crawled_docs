---
url: https://docs.comfy.org/es/built-in-nodes/DeprecatedDiffusersLoader/
title: DeprecatedDiffusersLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:43.634461+00:00
---

# DeprecatedDiffusersLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/DeprecatedDiffusersLoader/

Cargadores

# DeprecatedDiffusersLoader - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo DiffusersLoader está diseñado para cargar modelos de la biblioteca diffusers, manejando específicamente la carga de modelos UNet

Copiar páginaCopiar página

El nodo DiffusersLoader está diseñado para cargar modelos de la biblioteca diffusers, manejando específicamente la carga de modelos UNet, CLIP y VAE basándose en las rutas de modelo proporcionadas. Facilita la integración de estos modelos en el marco de ComfyUI, permitiendo funcionalidades avanzadas como generación de texto a imagen, manipulación de imágenes y más.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`model_path`| Especifica la ruta al modelo que se cargará. Esta ruta es crucial, ya que determina qué modelo se utilizará para operaciones posteriores, afectando la salida y las capacidades del nodo.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`model`| El modelo UNet cargado, que forma parte de la tupla de salida. Este modelo es esencial para tareas de síntesis y manipulación de imágenes dentro del marco de ComfyUI.| MODEL  
`clip`| El modelo CLIP cargado, incluido en la tupla de salida si se solicita. Este modelo permite capacidades avanzadas de comprensión y manipulación de texto e imágenes.| CLIP  
`vae`| El modelo VAE cargado, incluido en la tupla de salida si se solicita. Este modelo es crucial para tareas que implican manipulación del espacio latente y generación de imágenes.| VAE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/DeprecatedDiffusersLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/DeprecatedDiffusersLoader)

[DeprecatedCheckpointLoader](https://docs.comfy.org/es/built-in-nodes/DeprecatedCheckpointLoader)[SaveLoRANode](https://docs.comfy.org/es/built-in-nodes/SaveLoRANode)
