---
url: https://docs.comfy.org/es/built-in-nodes/UpscaleModelLoader/
title: Cargar modelo de escala superior - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:39.966967+00:00
---

# Cargar modelo de escala superior - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/UpscaleModelLoader/

Cargadores

# Cargar modelo de escala superior - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detectará los modelos ubicados en la carpeta ComfyUI/models/upscalemodels

Copiar páginaCopiar página

Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/upscale_models`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo desde la carpeta correspondiente. El nodo UpscaleModelLoader está diseñado para cargar modelos de escalado desde un directorio específico. Facilita la recuperación y preparación de modelos de escalado para tareas de ampliación de imágenes, asegurando que los modelos se carguen y configuren correctamente para su evaluación.

## 

​

Entradas

Campo| Descripción| Tipo Comfy  
---|---|---  
`nombre_modelo`| Especifica el nombre del modelo de escalado a cargar, identificando y recuperando el archivo de modelo correcto desde el directorio de modelos de escalado.| `COMBO[STRING]`  
  
## 

​

Salidas

Campo| Descripción| Tipo Comfy  
---|---|---  
`upscale_model`| Devuelve el modelo de escalado cargado y preparado, listo para su uso en tareas de ampliación de imágenes.| `UPSCALE_MODEL`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/UpscaleModelLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/UpscaleModelLoader)

[Cargar modelo de difusión](https://docs.comfy.org/es/built-in-nodes/UNETLoader)[Cargar VAE](https://docs.comfy.org/es/built-in-nodes/VAELoader)
