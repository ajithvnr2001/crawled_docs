---
url: https://docs.comfy.org/es/built-in-nodes/TripoSmartUVNode/
title: Tripo: UV inteligente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:07:52.250778+00:00
---

# Tripo: UV inteligente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TripoSmartUVNode/

3d

# Tripo: UV inteligente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Tripo: Smart UV vuelve a desplegar las UV de un modelo y reasigna sus texturas, rig y animación a la nueva disposición.

Copiar páginaCopiar página

Tripo: Smart UV vuelve a desplegar las UV de un modelo y reasigna sus texturas, rig y animación a la nueva disposición. Úsalo cuando la disposición UV original de un modelo no sea utilizable, por ejemplo, después de un retopología o cuando sea necesario rehacer las costuras de textura. El modelo de entrada no debe superar los 80.000 triángulos (un quad cuenta como dos), así que reduce primero los modelos más grandes con Tripo: Retopology o un `face_limit`.

> **Nota:** Tripo conserva los registros de tareas en sus servidores durante 7 días (a partir del 1 de diciembre de 2026). Un ID de tarea más antiguo que ese ya no se puede resolver, por lo que volver a ejecutar un flujo de trabajo guardado una vez transcurrido ese plazo falla en este nodo. Vuelve a ejecutar los nodos Tripo de origen que produjeron la tarea, o vuelve a importar un modelo descargado con **Tripo: Import Model**. Descarga el modelo antes de que venza el plazo: un recurso caducado no se puede recuperar del registro de la tarea.

## Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model_task_id`| ID de tarea del modelo que se va a volver a desplegar. Acepta un ID de tarea de modelo de un nodo de generación de Tripo, o un ID de tarea de rig, retarget o segmentación.| MODEL_TASK_ID| Sí| ID de tarea de Tripo  
`bake`| Hornea las texturas existentes en la nueva disposición UV. Desactivado omite el horneado y devuelve el modelo sin sus texturas de color (predeterminado: True).| BOOLEAN| Sí| `True`  
`False`  
  
## Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model task_id`| ID de tarea de la tarea UV finalizada. Se puede pasar a otros nodos Tripo, por ejemplo Tripo: Texture.| MODEL_TASK_ID  
`GLB`| El modelo con las UV vueltas a desplegar en formato GLB. Vacío cuando el modelo de origen es FBX.| FILE_3D_GLB  
`FBX`| El modelo con las UV vueltas a desplegar en formato FBX. Solo se rellena cuando el modelo de origen es FBX, por ejemplo, una malla de quads.| FILE_3D_FBX  
`UV atlas`| La disposición UV renderizada del modelo como una imagen.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/es.md)

* * *

**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TripoSmartUVNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TripoSmartUVNode)

[Mapas de material PBR Patina](https://docs.comfy.org/es/built-in-nodes/PatinaPBRMapsNode)[Tencent HY](https://docs.comfy.org/es/built-in-nodes/TencentHyNode)
