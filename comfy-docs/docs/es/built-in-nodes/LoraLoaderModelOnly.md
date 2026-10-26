---
url: https://docs.comfy.org/es/built-in-nodes/LoraLoaderModelOnly/
title: Cargar LoRA - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:06.683537+00:00
---

# Cargar LoRA - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoraLoaderModelOnly/

Imagen

# Cargar LoRA - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detecta los modelos ubicados en la carpeta ComfyUI/models/loras

Copiar páginaCopiar página

Este nodo detecta los modelos ubicados en la carpeta `ComfyUI/models/loras`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo desde la carpeta correspondiente. Este nodo se especializa en cargar un modelo LoRA sin requerir un modelo CLIP, enfocándose en mejorar o modificar un modelo determinado según los parámetros de LoRA. Permite el ajuste dinámico de la intensidad del modelo mediante parámetros LoRA, facilitando un control preciso sobre el comportamiento del modelo.

## 

​

Entradas

Campo| Descripción| Tipo Comfy  
---|---|---  
`modelo`| El modelo base para las modificaciones, al cual se aplicarán los ajustes de LoRA.| `MODEL`  
`nombre_lora`| El nombre del archivo LoRA que se cargará, especificando los ajustes a aplicar al modelo.| `COMBO[STRING]`  
`fuerza_modelo`| Determina la intensidad de los ajustes de LoRA; valores más altos indican modificaciones más fuertes.| `FLOAT`  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`modelo`| El modelo modificado con los ajustes de LoRA aplicados, reflejando cambios en el comportamiento o las capacidades del modelo.| `MODEL`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderModelOnly/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoraLoaderModelOnly.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoraLoaderModelOnly)

[Cargar LoRA (modelo y CLIP)](https://docs.comfy.org/es/built-in-nodes/LoraLoader)[Pintor](https://docs.comfy.org/es/built-in-nodes/Painter)
