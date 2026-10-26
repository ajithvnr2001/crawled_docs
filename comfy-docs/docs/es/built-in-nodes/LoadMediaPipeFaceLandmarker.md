---
url: https://docs.comfy.org/es/built-in-nodes/LoadMediaPipeFaceLandmarker/
title: Cargar MediaPipe Face Landmarker - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:05.503278+00:00
---

# Cargar MediaPipe Face Landmarker - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadMediaPipeFaceLandmarker/

Cargadores

# Cargar MediaPipe Face Landmarker - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo carga un modelo MediaPipe Face Landmarker v2, que detecta rostros y puntos de referencia faciales (como ojos, nariz y boca) en imágenes.

Copiar páginaCopiar página

Este nodo carga un modelo MediaPipe Face Landmarker v2, que detecta rostros y puntos de referencia faciales (como ojos, nariz y boca) en imágenes. El modelo cargado incluye dos variantes de detección (de corto alcance y de rango completo) junto con datos de malla compartidos, blendshapes y geometría canónica utilizados para el análisis facial.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`model_name`| Modelo de detección facial de models/detection/.| COMBO| Sí| Lista de nombres de archivo de modelos disponibles en el directorio `models/detection/`  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`FACE_DETECTION_MODEL`| Un objeto de modelo FaceLandmarker cargado que contiene ambas variantes de detección (short/full), conjuntos de conexiones para la topología facial, datos canónicos y parcheadores de modelo para la gestión de GPU.| FACE_DETECTION_MODEL  
  
**Nota:** La salida es un objeto complejo que puede ser utilizado por otros nodos para tareas de detección facial y extracción de puntos de referencia. Contiene dos variantes de detección: “short” para detección de corto alcance y “full” para detección de rango completo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/es.md)

* * *

**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadMediaPipeFaceLandmarker.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadMediaPipeFaceLandmarker)

[Cargar LoRA (codificador de texto)](https://docs.comfy.org/es/built-in-nodes/LoadLoraTextEncoder)[Cargar modelo MoGe](https://docs.comfy.org/es/built-in-nodes/LoadMoGeModel)
