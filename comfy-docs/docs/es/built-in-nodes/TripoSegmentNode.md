---
url: https://docs.comfy.org/es/built-in-nodes/TripoSegmentNode/
title: Tripo: Segmentar modelo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:38.749819+00:00
---

# Tripo: Segmentar modelo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TripoSegmentNode/

Tripo

# Tripo: Segmentar modelo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo divide un modelo 3D en partes individuales.

Copiar páginaCopiar página

Este nodo divide un modelo 3D en partes individuales. Envía el modelo al servicio de segmentación de Tripo, espera a que finalice el trabajo y devuelve el modelo segmentado en formato GLB junto con una lista de nombres de partes separados por comas. Estos nombres de partes alimentan pasos posteriores, como Tripo: Complete Mesh Parts, Tripo: Retopology y Tripo: Convert model.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`model_task_id`| El ID de tarea del modelo 3D que se va a segmentar en partes.| MODEL_TASK_ID| Sí| N/A  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model_file`| Nombre del archivo de salida del modelo GLB segmentado, con el formato `<task_id>.glb`. Se conserva solo por compatibilidad con versiones anteriores.| STRING  
`segment task_id`| El ID de tarea del trabajo de segmentación que produjo el resultado.| SEGMENT_TASK_ID  
`GLB`| El modelo 3D segmentado, como archivo GLB.| GLB  
`part_names`| Nombres de las partes separados por comas.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/es.md)

* * *

**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TripoSegmentNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TripoSegmentNode)

[Tripo: Modelo con rig](https://docs.comfy.org/es/built-in-nodes/TripoRigNode)[Tripo: Segmentación inteligente](https://docs.comfy.org/es/built-in-nodes/TripoSmartSegmentNode)
