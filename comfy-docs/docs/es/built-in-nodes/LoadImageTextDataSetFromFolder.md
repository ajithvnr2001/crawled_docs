---
url: https://docs.comfy.org/es/built-in-nodes/LoadImageTextDataSetFromFolder/
title: Cargar conjunto de im\u00e1genes y texto desde carpeta - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:05.413421+00:00
---

# Cargar conjunto de imágenes y texto desde carpeta - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadImageTextDataSetFromFolder/

Imagen

# Cargar conjunto de imágenes y texto desde carpeta - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo carga un conjunto de pares de imagen y descripción de texto desde una carpeta seleccionada y los devuelve como una lista.

Copiar páginaCopiar página

Este nodo carga un conjunto de pares de imagen y descripción de texto desde una carpeta seleccionada y los devuelve como una lista. Admite imágenes PNG, JPG, JPEG y WEBP, y para cada imagen busca una descripción en un archivo `.txt` con el mismo nombre base. El nodo también admite la estructura de carpetas de kohya-ss/sd-scripts, donde un nombre de subcarpeta que comienza con un número (como `10_cats`) repite las imágenes dentro de esa subcarpeta esa cantidad de veces en la salida.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`folder`| La carpeta desde la que se cargan las imágenes y las descripciones de texto.| COMBO| Sí| Subcarpetas dentro del directorio de entrada de ComfyUI (cargadas dinámicamente)  
  
**Nota:** La carpeta seleccionada debe ser una subcarpeta del directorio de entrada de ComfyUI. El nodo espera un archivo de descripción `.txt` por imagen: para cada archivo de imagen (`.png`, `.jpg`, `.jpeg`, `.webp`), busca un archivo `.txt` con el mismo nombre base en la misma ubicación y utiliza su contenido recortado como descripción. Si no se encuentra ningún archivo de descripción, se utiliza una cadena vacía. El nodo también admite la estructura de carpetas de kohya-ss/sd-scripts: las subcarpetas cuyo nombre comienza con un número y un guion bajo (por ejemplo `5_cats`) repiten las imágenes de su interior esa cantidad de veces en la lista de salida final. Si la carpeta seleccionada no contiene imágenes válidas, el nodo genera un error.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`images`| Lista de las imágenes cargadas. Las imágenes se convierten a RGB y se normalizan al rango flotante de 0 a 1.| IMAGE  
`texts`| Lista de descripciones de texto, una por cada imagen cargada. Las descripciones son el contenido recortado del archivo `.txt` correspondiente, o una cadena vacía cuando no existe ningún archivo de descripción.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/es.md)

* * *

**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadImageTextDataSetFromFolder.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadImageTextDataSetFromFolder)

[LoadImageSetNode](https://docs.comfy.org/es/built-in-nodes/LoadImageSetNode)[LoadImageTextSetFromFolderNode](https://docs.comfy.org/es/built-in-nodes/LoadImageTextSetFromFolderNode)
