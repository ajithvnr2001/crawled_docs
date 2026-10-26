---
url: https://docs.comfy.org/es/built-in-nodes/ImageOnlyCheckpointLoader/
title: Cargador de puntos de control solo de imagen (modelo img2vid) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.646381+00:00
---

# Cargador de puntos de control solo de imagen (modelo img2vid) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageOnlyCheckpointLoader/

Cargadores

# Cargador de puntos de control solo de imagen (modelo img2vid) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detecta los modelos ubicados en la carpeta ComfyUI/models/checkpoints

Copiar páginaCopiar página

Este nodo detecta los modelos ubicados en la carpeta `ComfyUI/models/checkpoints`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para permitir que lea los archivos de modelo desde la carpeta correspondiente. Este nodo se especializa en cargar puntos de control específicamente para modelos basados en imágenes dentro de flujos de trabajo de generación de video. Recupera y configura de manera eficiente los componentes necesarios de un punto de control determinado, centrándose en los aspectos relacionados con imágenes del modelo.

## 

​

Entradas

Campo| Descripción| Tipo de Dato  
---|---|---  
`nombre_ckpt`| Especifica el nombre del punto de control a cargar, crucial para identificar y recuperar el archivo de punto de control correcto de una lista predefinida.| COMBO[STRING]  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`model`| Devuelve el modelo principal cargado desde el punto de control, configurado para el procesamiento de imágenes en contextos de generación de video.| MODEL  
`clip_vision`| Proporciona el componente de visión CLIP del punto de control, adaptado para la comprensión de imágenes y la extracción de características.| `CLIP_VISION`  
`vae`| Entrega el componente de Autoencoder Variacional (VAE), esencial para tareas de manipulación y generación de imágenes.| VAE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageOnlyCheckpointLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageOnlyCheckpointLoader)

[Cargar hypernetwork](https://docs.comfy.org/es/built-in-nodes/HypernetworkLoader)[Cargar modelo de escalado latent](https://docs.comfy.org/es/built-in-nodes/LatentUpscaleModelLoader)
