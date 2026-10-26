---
url: https://docs.comfy.org/es/built-in-nodes/MergeTextLists/
title: Unir listas de textos - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:09.925742+00:00
---

# Unir listas de textos - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MergeTextLists/

Texto

# Unir listas de textos - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo combina múltiples listas de texto en una única lista combinada.

Copiar páginaCopiar página

Este nodo combina múltiples listas de texto en una única lista combinada. Está diseñado para recibir entradas de texto como listas y concatenarlas. El nodo registra el número total de textos en la lista combinada.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`textos`| Las listas de texto que se van a combinar. Se pueden conectar múltiples listas a la entrada, y se concatenarán en una sola.| STRING| Sí| N/A  
  
**Nota:** Este nodo está configurado como un proceso grupal (`is_group_process = True`), lo que significa que maneja automáticamente múltiples entradas de lista concatenándolas antes de que se ejecute la función de procesamiento principal.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`textos`| La única lista combinada que contiene todos los textos de entrada.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeTextLists/es.md)

* * *

**Source fingerprint (SHA-256):** `043a39a373d03f1ff79dd0746070171bab4d5d915c985e4e64fd35f802b09f69`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MergeTextLists.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MergeTextLists)

[Extraer cadena de JSON](https://docs.comfy.org/es/built-in-nodes/JsonExtractString)[Extracción regex](https://docs.comfy.org/es/built-in-nodes/RegexExtract)
