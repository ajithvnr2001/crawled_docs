---
url: https://docs.comfy.org/es/built-in-nodes/MeshyAnimateModelNode/
title: Meshy: Animar modelo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:10.488873+00:00
---

# Meshy: Animar modelo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MeshyAnimateModelNode/

Meshy

# Meshy: Animar modelo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo aplica una acción de animación específica a un personaje 3D previamente riggeado mediante el servicio Meshy.

Copiar páginaCopiar página

Este nodo aplica una acción de animación específica a un personaje 3D previamente riggeado mediante el servicio Meshy. Toma un ID de tarea de una operación de rigging anterior y un ID de acción para seleccionar la animación deseada de la biblioteca, y luego devuelve el modelo animado tanto en formato de archivo GLB como FBX.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`rig_task_id`| El ID de tarea único de una operación de rigging de personaje de Meshy completada previamente.| MESHY_RIGGED_TASK_ID| Sí| N/A  
`action_id`| El número de ID de la acción de animación que se aplicará. Visite <https://docs.meshy.ai/en/api/animation-library> para obtener una lista de los valores disponibles. (predeterminado: 0)| INT| Sí| 0 a 696  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model_file`| Un identificador de cadena para el modelo animado. Esta salida se proporciona únicamente por compatibilidad con versiones anteriores.| STRING  
`GLB`| El archivo de modelo 3D animado en formato GLB.| FILE3DGLB  
`FBX`| El archivo de modelo 3D animado en formato FBX.| FILE3DFBX  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/es.md)

* * *

**Source fingerprint (SHA-256):** `760e94d3a92910051d9b473545191842dc9672e6c4a59c3d1cd9cfdc5eb2589d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MeshyAnimateModelNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MeshyAnimateModelNode)

[Entrenar LoRA](https://docs.comfy.org/es/built-in-nodes/TrainLoraNode)[Meshy: Imagen a modelo](https://docs.comfy.org/es/built-in-nodes/MeshyImageToModelNode)
