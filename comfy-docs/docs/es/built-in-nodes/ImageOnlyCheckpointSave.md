---
url: https://docs.comfy.org/es/built-in-nodes/ImageOnlyCheckpointSave/
title: Guardar punto de control (solo imagen) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.584585+00:00
---

# Guardar punto de control (solo imagen) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageOnlyCheckpointSave/

Fusión

# Guardar punto de control (solo imagen) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo guarda un archivo de checkpoint que empaqueta un modelo junto con su codificador de visión CLIP y su VAE.

Copiar páginaCopiar página

Este nodo guarda un archivo de checkpoint que empaqueta un modelo junto con su codificador de visión CLIP y su VAE. El archivo se escribe en formato safetensors en el directorio de salida, usando el prefijo de nombre de archivo proporcionado, de modo que los componentes relacionados con imágenes de un modelo puedan almacenarse como un único checkpoint.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo que se guardará en el checkpoint| MODEL| Sí| -  
`clip_vision`| El codificador de visión CLIP que se guardará en el checkpoint| CLIP_VISION| Sí| -  
`vae`| El VAE (autoencoder variacional) que se guardará en el checkpoint| VAE| Sí| -  
`prefijo_nombre_archivo`| El prefijo para el nombre del archivo de salida (predeterminado: “checkpoints/ComfyUI”)| STRING| Sí| -  
`prompt`| Parámetro oculto que recibe los datos del prompt del flujo de trabajo| PROMPT| No| -  
`extra_pnginfo`| Parámetro oculto que recibe metadatos PNG adicionales| EXTRA_PNGINFO| No| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
-| Este nodo no devuelve ninguna salida| -  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/es.md)

* * *

**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageOnlyCheckpointSave.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageOnlyCheckpointSave)

[Guardar CLIP](https://docs.comfy.org/es/built-in-nodes/CLIPSave)[Fusionar modelo (sumar)](https://docs.comfy.org/es/built-in-nodes/ModelMergeAdd)
