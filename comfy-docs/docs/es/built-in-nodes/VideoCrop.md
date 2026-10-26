---
url: https://docs.comfy.org/es/built-in-nodes/VideoCrop/
title: Recortar v\u00eddeo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:42.284104+00:00
---

# Recortar vídeo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VideoCrop/

Video

# Recortar vídeo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo recorta un video a una región rectangular definida en píxeles, conservando solo el área dentro de ese rectángulo.

Copiar páginaCopiar página

Este nodo recorta un video a una región rectangular definida en píxeles, conservando solo el área dentro de ese rectángulo. Guarda una vista previa temporal en MP4 del resultado recortado y produce como salida el video recortado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`video`| El video de origen que se recortará.| VIDEO| Sí| Cualquier video  
`crop`| Región de recorte en píxeles. Un ancho/alto de cero conserva el fotograma completo. El rectángulo de recorte proporciona valores `x`, `y`, `width` y `height`, todos con un valor predeterminado de 0.| VIDEO_EDIT| Sí| `x` ≥ 0  
`y` ≥ 0  
`width` ≥ 0  
`height` ≥ 0  
Todos los valores tienen un valor predeterminado de 0  
  
Nota: La región de recorte se describe en coordenadas de píxeles. Cuando el ancho y el alto son 0, no se aplica ningún recorte y el nodo produce como salida el video de entrada completo.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| El video recortado a la región rectangular seleccionada. Cuando el ancho y el alto del recorte son 0, la salida es el video de entrada completo. El resultado recortado también se guarda como un archivo MP4 temporal y se muestra como una vista previa de video.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoCrop/es.md)

* * *

**Source fingerprint (SHA-256):** `0c4ebd51027669fc232fe42a5e8840b5e4e95083b6794cd7b4c43123ddc0341b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VideoCrop.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VideoCrop)

[Corte de Video](https://docs.comfy.org/es/built-in-nodes/Video%20Slice)[Muestrear fotograma de video](https://docs.comfy.org/es/built-in-nodes/VideoFrameSample)
