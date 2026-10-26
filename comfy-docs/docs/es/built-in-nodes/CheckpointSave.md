---
url: https://docs.comfy.org/es/built-in-nodes/CheckpointSave/
title: Guardar punto de control - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:37.960661+00:00
---

# Guardar punto de control - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CheckpointSave/

Fusión

# Guardar punto de control - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Save Checkpoint está diseñado para guardar un modelo completo de Stable Diffusion (incluyendo los componentes UNet

Copiar páginaCopiar página

El nodo `Save Checkpoint` está diseñado para guardar un modelo completo de Stable Diffusion (incluyendo los componentes UNet, CLIP y VAE) como un archivo de punto de control en formato **.safetensors**. El nodo Save Checkpoint se utiliza principalmente en flujos de trabajo de fusión de modelos. Después de crear un nuevo modelo fusionado mediante nodos como `ModelMergeSimple`, `ModelMergeBlocks`, etc., puede usar este nodo para guardar el resultado como un archivo de punto de control reutilizable.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`modelo`| El parámetro `modelo` representa el modelo principal cuyo estado se va a guardar. Es esencial para capturar el estado actual del modelo para su futura restauración o análisis.| MODEL  
`clip`| El parámetro `clip` está destinado al modelo CLIP asociado con el modelo principal, permitiendo que su estado se guarde junto con el modelo principal.| CLIP  
`vae`| El parámetro `vae` es para el modelo de Autoencoder Variacional (VAE), permitiendo que su estado se guarde para uso o análisis futuro junto con el modelo principal y CLIP.| VAE  
`prefijo_nombre_archivo`| Este parámetro especifica el prefijo para el nombre del archivo bajo el cual se guardará el punto de control.| STRING  
  
Adicionalmente, el nodo tiene dos entradas ocultas para metadatos: **prompt (PROMPT)** : Información del prompt del flujo de trabajo **extra_pnginfo (EXTRA_PNGINFO)** : Información PNG adicional

## 

​

Salidas

Este nodo generará un archivo de punto de control, y la ruta del archivo de salida correspondiente es el directorio `output/checkpoints/`

## 

​

Compatibilidad de Arquitecturas

  * **Compatibilidad total actualmente** : SDXL, SD3, SVD y otras arquitecturas principales; consulte el [código fuente](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
  * **Compatibilidad básica** : Otras arquitecturas se pueden guardar pero sin información de metadatos estandarizada



## 

​

Enlaces Relacionados

Código fuente relacionado: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CheckpointSave.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CheckpointSave)

[Fusionar modelo WAN 2.1](https://docs.comfy.org/es/built-in-nodes/ModelMergeWAN2_1)[Fusionar CLIP (sumar)](https://docs.comfy.org/es/built-in-nodes/CLIPMergeAdd)
