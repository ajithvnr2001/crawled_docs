---
url: https://docs.comfy.org/es/built-in-nodes/CreateList/
title: Crear lista - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:42.333182+00:00
---

# Crear lista - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CreateList/

Utilidades

# Crear lista - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Create List combina múltiples entradas en una única lista secuencial.

Copiar páginaCopiar página

El nodo Create List combina múltiples entradas en una única lista secuencial. Acepta cualquier cantidad de ranuras de entrada que compartan el mismo tipo de dato y concatena sus elementos en el orden en que se conectan las ranuras. El resultado es una lista que contiene todos los elementos conectados.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`entradas`| Una cantidad variable de ranuras de entrada denominadas `input`, `input_2`, `input_3`, etc. Cada ranura acepta una lista de elementos del mismo tipo de dato (por ejemplo, todos IMAGE o todos STRING). Las nuevas ranuras se crean automáticamente según sea necesario. El nodo concatena las listas en el orden de las ranuras.| Any| Sí| Cualquier cantidad de ranuras; cada ranura acepta cualquier cantidad de elementos  
  
**Nota:** Todas las entradas conectadas deben compartir el mismo tipo de dato. Cada ranura conectada proporciona una lista de elementos, y el nodo combina las listas en el orden de las ranuras (`input`, luego `input_2`, luego `input_3`, …). El nodo también se puede buscar con los alias “Image Iterator”, “Text Iterator” y “Iterator”.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`list`| Una única lista que contiene todos los elementos de las entradas conectadas, concatenados en el orden en que se proporcionaron las ranuras. El tipo de dato de salida coincide con el tipo de dato de entrada.| Any  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/es.md)

* * *

**Source fingerprint (SHA-256):** `4824fa6af46ab08cd3c10b033dbb3e43682b468e1dbd934fffb571349e025b96`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CreateList.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CreateList)

[Crear Cajas Delimitadoras](https://docs.comfy.org/es/built-in-nodes/CreateBoundingBoxes)[Editor de curvas](https://docs.comfy.org/es/built-in-nodes/CurveEditor)
