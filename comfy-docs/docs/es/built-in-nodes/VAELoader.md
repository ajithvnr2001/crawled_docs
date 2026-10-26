---
url: https://docs.comfy.org/es/built-in-nodes/VAELoader/
title: Cargar VAE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:40.697247+00:00
---

# Cargar VAE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VAELoader/

Cargadores

# Cargar VAE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detectará los modelos ubicados en la carpeta ComfyUI/models/vae

Copiar páginaCopiar página

Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/vae`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, puede ser necesario **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo desde la carpeta correspondiente. El nodo VAELoader está diseñado para cargar modelos de Autoencoder Variacional (VAE), específicamente adaptado para manejar tanto VAEs estándar como aproximados. Soporta la carga de VAEs por nombre, incluyendo manejo especializado para los modelos ‘taesd’ y ‘taesdxl’, y se ajusta dinámicamente según la configuración específica del VAE.

## 

​

Entradas

Campo| Descripción| Tipo Comfy  
---|---|---  
`nombre_vae`| Especifica el nombre del VAE a cargar, determinando qué modelo VAE se obtiene y carga, con soporte para una variedad de nombres de VAE predefinidos, incluyendo ‘taesd’ y ‘taesdxl’.| `COMBO[STRING]`  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`vae`| Devuelve el modelo VAE cargado, listo para operaciones posteriores como codificación o decodificación. La salida es un objeto modelo que encapsula el estado del modelo cargado.| `VAE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAELoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VAELoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VAELoader)

[Cargar modelo de escala superior](https://docs.comfy.org/es/built-in-nodes/UpscaleModelLoader)[Fusionar modelo Auraflow](https://docs.comfy.org/es/built-in-nodes/ModelMergeAuraflow)
