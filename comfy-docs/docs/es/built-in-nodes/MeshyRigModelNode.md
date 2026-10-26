---
url: https://docs.comfy.org/es/built-in-nodes/MeshyRigModelNode/
title: Meshy: Riggear modelo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:10.847940+00:00
---

# Meshy: Riggear modelo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MeshyRigModelNode/

Meshy

# Meshy: Riggear modelo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Meshy: Rig Model toma un modelo 3D de una tarea previa de Meshy y crea automáticamente un esqueleto para él

Copiar páginaCopiar página

El nodo Meshy: Rig Model toma un modelo 3D de una tarea previa de Meshy y crea automáticamente un esqueleto para él, produciendo un personaje con rigging que se puede posar y animar. El nodo genera el modelo con rigging tanto en formato de archivo GLB como FBX.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`meshy_task_id`| El ID de tarea único de una operación previa de Meshy (p. ej., texto a 3D o imagen a 3D) que generó el modelo al que se le aplicará rigging.| MESHY_TASK_ID| Sí| N/A  
`altura_metros`| La altura aproximada del modelo de personaje en metros. Esto ayuda a la precisión del escalado y del rigging (predeterminado: 1.7).| FLOAT| Sí| 0.1 a 15.0  
`imagen_de_textura`| La imagen de textura de color base con desarrollo UV del modelo.| IMAGE| No| N/A  
  
**Nota:** El proceso de rigging automático actualmente no es adecuado para mallas sin textura, activos no humanoides o activos humanoides con estructura de extremidades y cuerpo poco clara.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model_file`| Una salida heredada que se conserva únicamente por compatibilidad con versiones anteriores y que contiene el nombre de archivo del modelo GLB.| STRING  
`rig_task_id`| El ID de tarea único para esta operación de rigging, que se puede usar para hacer referencia al resultado en nodos Meshy posteriores.| MESHY_RIGGED_TASK_ID  
`GLB`| El modelo de personaje 3D con rigging guardado en formato de archivo GLB.| FILE3DGLB  
`FBX`| El modelo de personaje 3D con rigging guardado en formato de archivo FBX.| FILE3DFBX  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/es.md)

* * *

**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MeshyRigModelNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MeshyRigModelNode)

[Meshy: Refinar modelo borrador](https://docs.comfy.org/es/built-in-nodes/MeshyRefineNode)[Meshy: Texto a modelo](https://docs.comfy.org/es/built-in-nodes/MeshyTextToModelNode)
