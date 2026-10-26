---
url: https://docs.comfy.org/es/built-in-nodes/TripoRetargetNode/
title: Tripo: Redireccionar modelo con rig - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:38.462023+00:00
---

# Tripo: Redireccionar modelo con rig - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TripoRetargetNode/

Tripo

# Tripo: Redireccionar modelo con rig - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo TripoRetargetNode aplica una animación predefinida a un modelo 3D con rig existente.

Copiar páginaCopiar página

El nodo TripoRetargetNode aplica una animación predefinida a un modelo 3D con rig existente. Toma el ID de tarea de un modelo que fue rigueado previamente, envía una solicitud de retargeting a la API de Tripo y descarga el archivo animado resultante. El modelo animado se puede devolver como GLB o FBX, con geometría de malla opcional y reproducción en el lugar opcional.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`ID_de_tarea_del_modelo_original`| El ID de tarea del modelo 3D previamente rigueado al que se aplicará el retargeting. La tarea referenciada debe ser una tarea de rig.| RIG_TASK_ID| Sí| -  
`animación`| El preset de animación que se aplicará al modelo con rig. Las animaciones `preset:*` funcionan con ambos modelos de rig. Las animaciones `preset:biped:*` están hechas para rigs del modelo v1.0-20240301; un rig v2.5 acepta solo chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn y walk.| COMBO| Sí| `"preset:idle"`  
`"preset:walk"`  
`"preset:run"`  
`"preset:dive"`  
`"preset:climb"`  
`"preset:jump"`  
`"preset:slash"`  
`"preset:shoot"`  
`"preset:hurt"`  
`"preset:fall"`  
`"preset:turn"`  
`"preset:quadruped:walk"`  
`"preset:hexapod:walk"`  
`"preset:octopod:walk"`  
`"preset:serpentine:march"`  
`"preset:aquatic:march"`  
más opciones adicionales `"preset:biped:*"` mostradas en la UI  
`out_format`| Formato del archivo de salida; el resultado llega en la salida correspondiente. (predeterminado: glb)| COMBO| No| `"glb"`  
`"fbx"`  
`export_with_geometry`| Incluir la malla en la exportación; desactivado exporta solo el esqueleto animado. (predeterminado: True)| BOOLEAN| No| True  
False  
`animate_in_place`| Reproducir la animación en el lugar, sin desplazamiento de la raíz. (predeterminado: False)| BOOLEAN| No| True  
False  
`auth_token_comfy_org`| Token de autenticación para el acceso a la API de Comfy.org (parámetro oculto).| AUTH_TOKEN_COMFY_ORG| No| -  
`api_key_comfy_org`| Clave de API para el acceso al servicio de Comfy.org (parámetro oculto).| API_KEY_COMFY_ORG| No| -  
`unique_id`| Identificador único para el seguimiento de la operación (parámetro oculto).| UNIQUE_ID| No| -  
  
Nota: Las animaciones del grupo `preset:*` funcionan con ambos modelos de rig. Las animaciones del grupo `preset:biped:*` están hechas para rigs del modelo v1.0-20240301; un rig v2.5 acepta solo chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn y walk. Si el rig referenciado se creó con la especificación Mixamo y una versión de modelo que comience con `v1.0`, la llamada de retargeting falla con un error. El formato de salida solicitado debe ser GLB o FBX; si el servicio devuelve cualquier otro tipo de archivo, el nodo lanza un error.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model_file`| El archivo de modelo 3D animado generado (solo para compatibilidad hacia atrás).| STRING  
`retarget task_id`| El ID de tarea para el seguimiento de la operación de retargeting.| RETARGET_TASK_ID  
`GLB`| El modelo 3D animado en formato GLB. Se completa cuando `out_format` es glb.| FILE3DGLB  
`FBX`| El modelo 3D animado en formato FBX. Se completa cuando `out_format` es fbx.| FILE3DFBX  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/es.md)

* * *

**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TripoRetargetNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TripoRetargetNode)

[Tripo P2: Texto a modelo](https://docs.comfy.org/es/built-in-nodes/TripoPSeriesTextToModelNode)[Tripo: Retopología](https://docs.comfy.org/es/built-in-nodes/TripoRetopologyNode)
