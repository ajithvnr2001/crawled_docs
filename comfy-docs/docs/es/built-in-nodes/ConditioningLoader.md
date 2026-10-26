---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningLoader/
title: Cargar condicionamiento - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:40.028229+00:00
---

# Cargar condicionamiento - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningLoader/

Cargadores

# Cargar condicionamiento - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo carga un condicionamiento que se guardó previamente con el nodo Save Conditioning

Copiar páginaCopiar página

Este nodo carga un condicionamiento que se guardó previamente con el nodo Save Conditioning, o cualquier archivo safetensors que contenga un tensor `conditioning`, desde la carpeta embeddings. También restaura las opciones extra y los valores de listas numeradas almacenados junto con el condicionamiento.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`conditioning_name`| El archivo a cargar desde la carpeta embeddings. La lista de opciones se construye a partir de los archivos disponibles actualmente en esa carpeta.| COMBO| Sí| Todos los archivos en la carpeta embeddings  
  
**Nota:** El archivo seleccionado debe contener un tensor `conditioning`. Cualquier clave adicional almacenada en el archivo se restaura: las claves numeradas (por ejemplo, `key.0`, `key.1`) se agrupan de nuevo en listas ordenadas, y las demás claves se restauran como opciones simples. Las opciones extra se leen desde los metadatos `conditioning_options` del archivo cuando están presentes.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`CONDITIONING`| El condicionamiento cargado desde el archivo, junto con las opciones restauradas.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningLoader/es.md)

* * *

**Source fingerprint (SHA-256):** `08fc58bcaa2309fcf03d4e4cc634b930aaf6ccf8097181fd3d45924abda144eb`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningLoader)

[Cargar CLIP vision](https://docs.comfy.org/es/built-in-nodes/CLIPVisionLoader)[Cargar modelo ControlNet (diff)](https://docs.comfy.org/es/built-in-nodes/DiffControlNetLoader)
