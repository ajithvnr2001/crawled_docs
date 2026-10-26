---
url: https://docs.comfy.org/es/built-in-nodes/LoadImageSetNode/
title: LoadImageSetNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:05.275200+00:00
---

# LoadImageSetNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadImageSetNode/

Imagen

# LoadImageSetNode - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LoadImageSetNode carga múltiples imágenes desde el directorio de entrada para su procesamiento por lotes y fines de entrenamiento.

Copiar páginaCopiar página

El nodo LoadImageSetNode carga múltiples imágenes desde el directorio de entrada para su procesamiento por lotes y fines de entrenamiento. Admite varios formatos de imagen y puede redimensionar opcionalmente las imágenes utilizando diferentes métodos. Este nodo procesa todas las imágenes seleccionadas como un lote y las devuelve como un único tensor.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`images`| Selecciona múltiples imágenes del directorio de entrada. Admite formatos PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF y TIFF. Permite la selección por lotes de imágenes.| IMAGE| Sí| Múltiples archivos de imagen  
`resize_method`| Método opcional para redimensionar las imágenes cargadas (predeterminado: “None”). Elija “None” para mantener los tamaños originales, “Stretch” para forzar el redimensionamiento, “Crop” para mantener la relación de aspecto recortando, o “Pad” para mantener la relación de aspecto añadiendo relleno.| STRING| No| ”None"  
"Stretch"  
"Crop"  
"Pad”  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`IMAGE`| Un tensor que contiene todas las imágenes cargadas como un lote para su procesamiento posterior.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/es.md)

* * *

**Source fingerprint (SHA-256):** `acf0255bcf170ef3ac3b86a3f3e060c3b81064ca8924918a026ec8e3b86f7ac0`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadImageSetNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadImageSetNode)

[LoadImageSetFromFolderNode](https://docs.comfy.org/es/built-in-nodes/LoadImageSetFromFolderNode)[Cargar conjunto de imágenes y texto desde carpeta](https://docs.comfy.org/es/built-in-nodes/LoadImageTextDataSetFromFolder)
