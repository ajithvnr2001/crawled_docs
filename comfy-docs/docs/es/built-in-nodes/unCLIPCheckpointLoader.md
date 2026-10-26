---
url: https://docs.comfy.org/es/built-in-nodes/unCLIPCheckpointLoader/
title: Cargar punto de control unCLIP - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:48.101826+00:00
---

# Cargar punto de control unCLIP - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/unCLIPCheckpointLoader/

Cargadores

# Cargar punto de control unCLIP - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detectará los modelos ubicados en la carpeta ComfyUI/models/checkpoints

Copiar páginaCopiar página

Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/checkpoints`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para permitir que lea los archivos de modelo desde la carpeta correspondiente. El nodo unCLIPCheckpointLoader está diseñado para cargar puntos de control (checkpoints) específicamente adaptados para modelos unCLIP. Facilita la recuperación e inicialización de modelos, módulos CLIP vision y VAEs desde un punto de control especificado, optimizando el proceso de configuración para operaciones o análisis posteriores.

## 

​

Entradas

Campo| Descripción| Tipo Comfy  
---|---|---  
`nombre_ckpt`| Especifica el nombre del punto de control a cargar, identificando y recuperando el archivo de punto de control correcto desde un directorio predefinido, determinando la inicialización de modelos y configuraciones.| `COMBO[STRING]`  
  
## 

​

Salidas

Campo| Descripción| Tipo Comfy| Tipo Python  
---|---|---|---  
`model`| Representa el modelo principal cargado desde el punto de control.| `MODEL`| `torch.nn.Module`  
`clip`| Representa el módulo CLIP cargado desde el punto de control, si está disponible.| `CLIP`| `torch.nn.Module`  
`vae`| Representa el módulo VAE cargado desde el punto de control, si está disponible.| `VAE`| `torch.nn.Module`  
`clip_vision`| Representa el módulo CLIP vision cargado desde el punto de control, si está disponible.| `CLIP_VISION`| `torch.nn.Module`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/unCLIPCheckpointLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/unCLIPCheckpointLoader)

[Cargar CLIP triple](https://docs.comfy.org/es/built-in-nodes/TripleCLIPLoader)[Cargar modelo de difusión](https://docs.comfy.org/es/built-in-nodes/UNETLoader)
