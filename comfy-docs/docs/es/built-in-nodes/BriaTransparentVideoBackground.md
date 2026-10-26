---
url: https://docs.comfy.org/es/built-in-nodes/BriaTransparentVideoBackground/
title: Bria Eliminar Fondo de Video (Transparente) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:34.013351+00:00
---

# Bria Eliminar Fondo de Video (Transparente) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BriaTransparentVideoBackground/

Bria

# Bria Eliminar Fondo de Video (Transparente) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo elimina el fondo de un video mediante el servicio de IA de Bria y genera los fotogramas recortados junto con una máscara alfa.

Copiar páginaCopiar página

Este nodo elimina el fondo de un video mediante el servicio de IA de Bria y genera los fotogramas recortados junto con una máscara alfa. Conecta ambas salidas a un nodo de composición, o envíalas a un nodo Save WEBM para escribir un video transparente.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`video`| El video de entrada a procesar. El video debe durar 60 segundos o menos.| VIDEO| Sí| -  
`semilla`| La semilla controla si el nodo debe ejecutarse de nuevo; los resultados no son deterministas independientemente de la semilla (predeterminado: 0)| INT| Sí| 0 a 2147483647  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`imágenes`| Los fotogramas del video con el fondo eliminado, como imágenes RGB en el rango de 0.0 a 1.0| IMAGE  
`mask`| La máscara alfa para los fotogramas del video, siguiendo la convención de Load Image donde 1 significa transparente| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/es.md)

* * *

**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BriaTransparentVideoBackground.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BriaTransparentVideoBackground)

[Bria: Quitar fondo de video](https://docs.comfy.org/es/built-in-nodes/BriaRemoveVideoBackground)[Borrador de vídeo Bria](https://docs.comfy.org/es/built-in-nodes/BriaVideoEraser)
