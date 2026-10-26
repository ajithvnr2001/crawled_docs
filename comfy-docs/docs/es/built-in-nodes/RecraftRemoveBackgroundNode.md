---
url: https://docs.comfy.org/es/built-in-nodes/RecraftRemoveBackgroundNode/
title: Recraft eliminar fondo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:21.552590+00:00
---

# Recraft eliminar fondo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RecraftRemoveBackgroundNode/

Recraft

# Recraft eliminar fondo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo elimina el fondo de las imágenes utilizando el servicio de API de Recraft.

Copiar páginaCopiar página

Este nodo elimina el fondo de las imágenes utilizando el servicio de API de Recraft. Procesa cada imagen del lote de entrada individualmente y devuelve tanto las imágenes procesadas con fondos transparentes como las máscaras alfa correspondientes que indican las áreas de fondo eliminadas.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen o imágenes de entrada a procesar para la eliminación del fondo. Cada imagen del lote se procesa individualmente.| IMAGE| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| Imágenes procesadas con fondos transparentes (formato RGBA)| IMAGE  
`mask`| Máscaras del canal alfa que indican las áreas de fondo eliminadas, en formato B,H,W| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/es.md)

* * *

**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RecraftRemoveBackgroundNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RecraftRemoveBackgroundNode)

[Recraft Imagen a Imagen](https://docs.comfy.org/es/built-in-nodes/RecraftImageToImageNode)[Recraft reemplazar fondo](https://docs.comfy.org/es/built-in-nodes/RecraftReplaceBackgroundNode)
