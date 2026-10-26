---
url: https://docs.comfy.org/es/built-in-nodes/GLIGENLoader/
title: Cargar GLIGEN - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:49.914105+00:00
---

# Cargar GLIGEN - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/GLIGENLoader/

Cargadores

# Cargar GLIGEN - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detecta los modelos ubicados en la carpeta ComfyUI/models/gligen

Copiar páginaCopiar página

Este nodo detecta los modelos ubicados en la carpeta `ComfyUI/models/gligen`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo desde la carpeta correspondiente. El nodo `GLIGENLoader` está diseñado para cargar modelos GLIGEN, que son modelos generativos especializados. Facilita el proceso de recuperación e inicialización de estos modelos desde rutas especificadas, preparándolos para tareas generativas posteriores.

## 

​

Entradas

Campo| Descripción| Tipo Comfy  
---|---|---  
`nombre_gligen`| El nombre del modelo GLIGEN que se va a cargar, especificando qué archivo de modelo recuperar y cargar, crucial para la inicialización del modelo GLIGEN.| `COMBO[STRING]`  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`gligen`| El modelo GLIGEN cargado, listo para su uso en tareas generativas, representando el modelo completamente inicializado cargado desde la ruta especificada.| `GLIGEN`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/GLIGENLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/GLIGENLoader)

[Cargar modelo de interpolación de fotogramas](https://docs.comfy.org/es/built-in-nodes/FrameInterpolationModelLoader)[Cargar hypernetwork](https://docs.comfy.org/es/built-in-nodes/HypernetworkLoader)
