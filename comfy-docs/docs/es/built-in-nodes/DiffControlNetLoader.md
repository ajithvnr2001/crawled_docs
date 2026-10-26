---
url: https://docs.comfy.org/es/built-in-nodes/DiffControlNetLoader/
title: Cargar modelo ControlNet (diff) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:43.695266+00:00
---

# Cargar modelo ControlNet (diff) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/DiffControlNetLoader/

Cargadores

# Cargar modelo ControlNet (diff) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detectará los modelos ubicados en la carpeta ComfyUI/models/controlnet

Copiar páginaCopiar página

Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/controlnet`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo de la carpeta correspondiente. El nodo DiffControlNetLoader está diseñado para cargar redes de control diferenciales, que son modelos especializados capaces de modificar el comportamiento de otro modelo según especificaciones de redes de control. Este nodo permite el ajuste dinámico de comportamientos del modelo mediante la aplicación de redes de control diferenciales, facilitando la creación de salidas de modelo personalizadas.

## 

​

Entradas

Campo| Descripción| Tipo Comfy  
---|---|---  
`modelo`| El modelo base al que se aplicará la red de control diferencial, permitiendo la personalización del comportamiento del modelo.| `MODEL`  
`control_net_name`| Identifica la red de control diferencial específica que se cargará y aplicará al modelo base para modificar su comportamiento.| `COMBO[STRING]`  
  
## 

​

Salidas

Campo| Descripción| Tipo Comfy  
---|---|---  
`control_net`| Una red de control diferencial que ha sido cargada y está lista para aplicarse a un modelo base para la modificación de su comportamiento.| `CONTROL_NET`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffControlNetLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/DiffControlNetLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/DiffControlNetLoader)

[Cargar condicionamiento](https://docs.comfy.org/es/built-in-nodes/ConditioningLoader)[Cargar modelo Diffusers (obsoleto)](https://docs.comfy.org/es/built-in-nodes/DiffusersLoader)
