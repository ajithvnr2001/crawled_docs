---
url: https://docs.comfy.org/es/built-in-nodes/SDPoseFaceBBoxes/
title: Cajas delimitadoras faciales SDPose - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:26.335478+00:00
---

# Cajas delimitadoras faciales SDPose - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SDPoseFaceBBoxes/

Detección

# Cajas delimitadoras faciales SDPose - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SDPoseFaceBBoxes procesa datos de puntos clave de pose para detectar y generar cuadros delimitadores alrededor de rostros humanos.

Copiar páginaCopiar página

El nodo SDPoseFaceBBoxes procesa datos de puntos clave de pose para detectar y generar cuadros delimitadores alrededor de rostros humanos. Analiza los puntos clave faciales 2D de cada persona en un fotograma, calcula un cuadro delimitador basado en esos puntos y puede ajustar el tamaño y la forma del cuadro. Los cuadros delimitadores resultantes se formatean para ser compatibles con otros nodos en el flujo de trabajo SDPose, como el SDPoseKeypointExtractor.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`puntos clave`| Datos de puntos clave de pose que contienen información sobre personas detectadas y sus puntos de referencia corporales/faciales por fotograma.| POSE_KEYPOINT| Sí| -  
`escala`| Multiplicador del área del cuadro delimitador alrededor de cada rostro detectado. Un valor más grande crea un cuadro más grande. (predeterminado: 1.5)| FLOAT| No| 1.0 - 10.0  
`forzar cuadrado`| Expande el eje más corto del cuadro delimitador para que la región de recorte sea siempre cuadrada. (predeterminado: True)| BOOLEAN| No| -  
  
**Nota:** La entrada `keypoints` debe estar en el formato específico producido por nodos como SDPoseKeypointExtractor, que contiene datos de `canvas_height`, `canvas_width` y `people` con `face_keypoints_2d` para cada persona.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`cajas delimitadoras`| Una lista de cuadros delimitadores faciales para cada fotograma. Cada cuadro delimitador se define por sus coordenadas de esquina superior izquierda (`x`, `y`), `width` (ancho) y `height` (alto). Esta salida es compatible con la entrada `bboxes` del nodo SDPoseKeypointExtractor.| BOUNDINGBOX  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/es.md)

* * *

**Source fingerprint (SHA-256):** `bffbcddb882f6743a6cace6a4884fa5a257b746897c79ba9260c15260fab874e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SDPoseFaceBBoxes.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SDPoseFaceBBoxes)

[Dibujar puntos clave SDPose](https://docs.comfy.org/es/built-in-nodes/SDPoseDrawKeypoints)[Extractor de puntos clave SDPose](https://docs.comfy.org/es/built-in-nodes/SDPoseKeypointExtractor)
