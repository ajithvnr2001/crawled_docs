---
url: https://docs.comfy.org/es/built-in-nodes/WanCameraEmbedding/
title: Wan embedding de c\u00e1mara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:44.943240+00:00
---

# Wan embedding de cámara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WanCameraEmbedding/

Cámara

# Wan embedding de cámara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo genera un embedding de trayectoria de cámara usando embeddings de Plücker para la ruta de cámara que elijas.

Copiar páginaCopiar página

Este nodo genera un embedding de trayectoria de cámara usando embeddings de Plücker para la ruta de cámara que elijas. Construye una secuencia de poses de cámara simulando movimientos como paneo, zoom o rotación, y las convierte en un tensor de embedding que puede usarse en flujos de generación de video.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`pose_cámara`| El tipo de movimiento de cámara a simular (predeterminado: “Static”)| COMBO| Sí| ”Static"  
"Pan Up"  
"Pan Down"  
"Pan Left"  
"Pan Right"  
"Zoom In"  
"Zoom Out"  
"Anti Clockwise (ACW)"  
"ClockWise (CW)“  
`ancho`| El ancho de la salida en píxeles (predeterminado: 832, paso: 16)| INT| Sí| 16 a MAX_RESOLUTION  
`alto`| La altura de la salida en píxeles (predeterminado: 480, paso: 16)| INT| Sí| 16 a MAX_RESOLUTION  
`longitud`| La longitud de la secuencia de trayectoria de cámara (predeterminado: 81, paso: 4)| INT| Sí| 1 a MAX_RESOLUTION  
`velocidad`| La velocidad del movimiento de cámara (predeterminado: 1.0, paso: 0.1)| FLOAT| No| 0.0 a 10.0  
`fx`| El parámetro de longitud focal x (predeterminado: 0.5, paso: 0.000000001)| FLOAT| No| 0.0 a 1.0  
`fy`| El parámetro de longitud focal y (predeterminado: 0.5, paso: 0.000000001)| FLOAT| No| 0.0 a 1.0  
`cx`| La coordenada x del punto principal (predeterminado: 0.5, paso: 0.01)| FLOAT| No| 0.0 a 1.0  
`cy`| La coordenada y del punto principal (predeterminado: 0.5, paso: 0.01)| FLOAT| No| 0.0 a 1.0  
  
Nota: `fx`, `fy`, `cx` y `cy` son parámetros intrínsecos avanzados de la cámara. El parámetro `speed` escala el ángulo de rotación y la distancia de traslación del movimiento de cámara seleccionado.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`camera_embedding`| El tensor de embedding de cámara generado que contiene la secuencia de trayectoria| TENSOR  
`width`| El valor de ancho que se usó para el procesamiento| INT  
`height`| El valor de altura que se usó para el procesamiento| INT  
`length`| El valor de longitud que se usó para el procesamiento| INT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/es.md)

* * *

**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WanCameraEmbedding.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WanCameraEmbedding)

[Wan animar a video](https://docs.comfy.org/es/built-in-nodes/WanAnimateToVideo)[Wan imagen con cámara a video](https://docs.comfy.org/es/built-in-nodes/WanCameraImageToVideo)
