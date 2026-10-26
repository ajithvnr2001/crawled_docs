---
url: https://docs.comfy.org/es/built-in-nodes/LoadImageSetFromFolderNode/
title: LoadImageSetFromFolderNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:05.035798+00:00
---

# LoadImageSetFromFolderNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadImageSetFromFolderNode/

Imagen

# LoadImageSetFromFolderNode - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LoadImageSetFromFolderNode carga múltiples imágenes desde un directorio de carpeta especificado con fines de entrenamiento.

Copiar páginaCopiar página

El nodo `LoadImageSetFromFolderNode` carga múltiples imágenes desde un directorio de carpeta especificado con fines de entrenamiento. Detecta automáticamente formatos de imagen comunes y puede redimensionar opcionalmente las imágenes usando diferentes métodos antes de devolverlas como un lote.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`folder`| La carpeta desde la cual cargar las imágenes.| STRING| Sí| Varias opciones disponibles  
`resize_method`| El método a utilizar para redimensionar las imágenes (predeterminado: “None”).| STRING| No| ”None"  
"Stretch"  
"Crop"  
"Pad”  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`IMAGE`| El lote de imágenes cargadas como un único tensor.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/es.md)

* * *

**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadImageSetFromFolderNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadImageSetFromFolderNode)

[Cargar imagen (desde salidas)](https://docs.comfy.org/es/built-in-nodes/LoadImageOutput)[LoadImageSetNode](https://docs.comfy.org/es/built-in-nodes/LoadImageSetNode)
