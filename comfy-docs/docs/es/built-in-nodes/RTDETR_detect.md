---
url: https://docs.comfy.org/es/built-in-nodes/RTDETR_detect/
title: Detecci\u00f3n RT-DETR - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:20.522102+00:00
---

# Detección RT-DETR - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RTDETR_detect/

Detección

# Detección RT-DETR - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo RT-DETR Detect realiza la detección de objetos en imágenes de entrada utilizando un modelo RT-DETR.

Copiar páginaCopiar página

El nodo RT-DETR Detect realiza la detección de objetos en imágenes de entrada utilizando un modelo RT-DETR. Identifica objetos, devuelve cuadros delimitadores a su alrededor y los etiqueta según las clases del conjunto de datos COCO. Puedes filtrar los resultados por puntuación de confianza, clase de objeto y limitar el número total de detecciones.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo RT-DETR utilizado para la detección de objetos.| MODEL| Sí| N/A  
`imagen`| La(s) imagen(es) de entrada en las que se detectan objetos. El nodo procesa imágenes en lotes de hasta 32.| IMAGE| Sí| N/A  
`umbral`| La puntuación de confianza mínima que debe tener una detección para incluirse en los resultados (predeterminado: 0.5).| FLOAT| Sí| N/A  
`nombre_clase`| Filtra las detecciones por clase. Establecer en ‘all’ para desactivar el filtrado (predeterminado: “all”).| COMBO| Sí| `"all"`  
`"person"`  
`"bicycle"`  
`"car"`  
`"motorcycle"`  
`"airplane"`  
`"bus"`  
`"train"`  
`"truck"`  
`"boat"`  
`"traffic light"`  
`"fire hydrant"`  
`"stop sign"`  
`"parking meter"`  
`"bench"`  
`"bird"`  
`"cat"`  
`"dog"`  
`"horse"`  
`"sheep"`  
`"cow"`  
`"elephant"`  
`"bear"`  
`"zebra"`  
`"giraffe"`  
`"backpack"`  
`"umbrella"`  
`"handbag"`  
`"tie"`  
`"suitcase"`  
`"frisbee"`  
`"skis"`  
`"snowboard"`  
`"sports ball"`  
`"kite"`  
`"baseball bat"`  
`"baseball glove"`  
`"skateboard"`  
`"surfboard"`  
`"tennis racket"`  
`"bottle"`  
`"wine glass"`  
`"cup"`  
`"fork"`  
`"knife"`  
`"spoon"`  
`"bowl"`  
`"banana"`  
`"apple"`  
`"sandwich"`  
`"orange"`  
`"broccoli"`  
`"carrot"`  
`"hot dog"`  
`"pizza"`  
`"donut"`  
`"cake"`  
`"chair"`  
`"couch"`  
`"potted plant"`  
`"bed"`  
`"dining table"`  
`"toilet"`  
`"tv"`  
`"laptop"`  
`"mouse"`  
`"remote"`  
`"keyboard"`  
`"cell phone"`  
`"microwave"`  
`"oven"`  
`"toaster"`  
`"sink"`  
`"refrigerator"`  
`"book"`  
`"clock"`  
`"vase"`  
`"scissors"`  
`"teddy bear"`  
`"hair drier"`  
`"toothbrush"`  
`máx_detecciones`| Número máximo de detecciones a devolver por imagen. En orden descendente de puntuación de confianza (predeterminado: 100).| INT| Sí| N/A  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`bboxes`| Una lista de cuadros delimitadores para cada imagen de entrada. Cada cuadro contiene coordenadas (x, y, ancho, alto), una etiqueta de clase y una puntuación de confianza.| BOUNDINGBOX  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/es.md)

* * *

**Source fingerprint (SHA-256):** `658a47cae788da207a52edc6bf8a428c9f3d8cf415e5f20f71d6125ad6d49734`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RTDETR_detect.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RTDETR_detect)

[Visualizar Malla Facial de MediaPipe](https://docs.comfy.org/es/built-in-nodes/MediaPipeFaceMeshVisualize)[Detector SAM3](https://docs.comfy.org/es/built-in-nodes/SAM3_Detect)
