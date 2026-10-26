---
url: https://docs.comfy.org/es/built-in-nodes/CheckpointLoaderSimple/
title: Cargar punto de control - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:38.201710+00:00
---

# Cargar punto de control - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CheckpointLoaderSimple/

Cargadores

# Cargar punto de control - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Carga un archivo de checkpoint de modelo de difusión y lo divide en tres componentes principales: el modelo principal usado para la eliminación de ruido de los

Copiar páginaCopiar página

Carga un archivo de checkpoint de modelo de difusión y lo divide en tres componentes principales: el modelo principal usado para la eliminación de ruido de los latentes, el codificador de texto CLIP y el codificador/decodificador de imágenes VAE. El nodo detecta automáticamente todos los archivos de modelo en la carpeta `ComfyUI/models/checkpoints` y cualquier ruta adicional configurada en tu archivo `extra_model_paths.yaml`.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`nombre_ckpt`| El nombre del checkpoint (modelo) a cargar. Selecciona el nombre del archivo de modelo de checkpoint, que determina el modelo de IA usado para la generación de imágenes posterior.| COMBO| Sí| Todos los archivos de modelo encontrados en la carpeta de checkpoints  
  
**Nota:** Si se agregan nuevos archivos de modelo mientras ComfyUI está en ejecución, necesitas actualizar el navegador (Ctrl+R) para ver los nuevos archivos en la lista desplegable.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`MODEL`| El modelo usado para la eliminación de ruido de los latentes. Este es el modelo de difusión central usado para la generación de imágenes.| MODEL  
`CLIP`| El modelo CLIP usado para codificar prompts de texto, convirtiendo descripciones de texto en información que la IA puede entender.| CLIP  
`VAE`| El modelo VAE usado para codificar y decodificar imágenes hacia y desde el espacio latente.| VAE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/es.md)

* * *

**Source fingerprint (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CheckpointLoaderSimple.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CheckpointLoaderSimple)

[Cargar punto de control con configuración (OBSOLETO)](https://docs.comfy.org/es/built-in-nodes/CheckpointLoader)[Cargar CLIP](https://docs.comfy.org/es/built-in-nodes/CLIPLoader)
