---
url: https://docs.comfy.org/es/built-in-nodes/ImageDeduplication/
title: Eliminaci\u00f3n de im\u00e1genes duplicadas - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.106092+00:00
---

# Eliminación de imágenes duplicadas - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageDeduplication/

Lote

# Eliminación de imágenes duplicadas - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo elimina imágenes duplicadas o muy similares de un lote.

Copiar páginaCopiar página

Este nodo elimina imágenes duplicadas o muy similares de un lote. Funciona creando un hash perceptual para cada imagen —una huella digital numérica simple basada en su contenido visual— y luego comparándolos. Las imágenes cuyos hashes sean más similares que un umbral establecido se consideran duplicados y se filtran.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imágenes`| El lote de imágenes a procesar para la deduplicación.| IMAGE| Sí| -  
`umbral_de_similitud`| Umbral de similitud (0-1). Un valor más alto indica mayor similitud. Las imágenes por encima de este umbral se consideran duplicados. (predeterminado: 0.95)| FLOAT| No| 0.0 - 1.0  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imágenes`| La lista filtrada de imágenes con los duplicados eliminados.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/es.md)

* * *

**Source fingerprint (SHA-256):** `8904f9dee4ca911821e76d2317983cbc230c4821a9ee7876180bd7dbe42b9a54`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageDeduplication.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageDeduplication)

[Eliminar fondo](https://docs.comfy.org/es/built-in-nodes/RemoveBackground)[Imagen desde lote](https://docs.comfy.org/es/built-in-nodes/ImageFromBatch)
