---
url: https://docs.comfy.org/es/built-in-nodes/UNETLoader/
title: Cargar modelo de difusi\u00f3n - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:39.552865+00:00
---

# Cargar modelo de difusión - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/UNETLoader/

Cargadores

# Cargar modelo de difusión - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo UNETLoader está diseñado para cargar modelos U-Net por nombre, facilitando el uso de arquitecturas U-Net preentrenadas dentro del sistema.

Copiar páginaCopiar página

El nodo UNETLoader está diseñado para cargar modelos U-Net por nombre, facilitando el uso de arquitecturas U-Net preentrenadas dentro del sistema. Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/diffusion_models`.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`nombre_unet`| Especifica el nombre del modelo U-Net a cargar. Este nombre se utiliza para localizar el modelo dentro de una estructura de directorios predefinida, permitiendo la carga dinámica de diferentes modelos U-Net.| COMBO[STRING]  
`tipo_dato_peso`| 🚧 fp8_e4m3fn fp9_e5m2| …  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`model`| Devuelve el modelo U-Net cargado, permitiendo su uso para procesamiento adicional o inferencia dentro del sistema.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNETLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/UNETLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/UNETLoader)

[Cargar punto de control unCLIP](https://docs.comfy.org/es/built-in-nodes/unCLIPCheckpointLoader)[Cargar modelo de escala superior](https://docs.comfy.org/es/built-in-nodes/UpscaleModelLoader)
