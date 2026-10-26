---
url: https://docs.comfy.org/es/built-in-nodes/LoadImageOutput/
title: Cargar imagen (desde salidas) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:05.179811+00:00
---

# Cargar imagen (desde salidas) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadImageOutput/

Imagen

# Cargar imagen (desde salidas) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LoadImageOutput carga imágenes desde la carpeta de salida.

Copiar páginaCopiar página

El nodo LoadImageOutput carga imágenes desde la carpeta de salida. Al hacer clic en el botón de actualizar, actualiza la lista de imágenes disponibles y selecciona automáticamente la primera, facilitando la iteración a través de las imágenes generadas.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| Carga una imagen desde la carpeta de salida. Incluye una opción de carga y un botón de actualizar para renovar la lista de imágenes. Al hacer clic en el botón de actualizar, el nodo actualizará la lista de imágenes y seleccionará automáticamente la primera, permitiendo una iteración sencilla.| COMBO| Sí| Múltiples opciones disponibles  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen cargada desde la carpeta de salida| IMAGE  
`mask`| La máscara asociada a la imagen cargada| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/es.md)

* * *

**Source fingerprint (SHA-256):** `d1de0140765c9d5dd393715faa84dc5c3f0e49117391b8823a51b176bcb568d8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadImageOutput.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadImageOutput)

[Cargar imagen (como máscara)](https://docs.comfy.org/es/built-in-nodes/LoadImageMask)[LoadImageSetFromFolderNode](https://docs.comfy.org/es/built-in-nodes/LoadImageSetFromFolderNode)
