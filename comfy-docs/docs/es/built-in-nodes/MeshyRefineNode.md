---
url: https://docs.comfy.org/es/built-in-nodes/MeshyRefineNode/
title: Meshy: Refinar modelo borrador - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:10.211239+00:00
---

# Meshy: Refinar modelo borrador - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MeshyRefineNode/

Meshy

# Meshy: Refinar modelo borrador - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Meshy: Refine Draft Model toma un modelo 3D preliminar de una tarea Meshy anterior y lo mejora

Copiar páginaCopiar página

El nodo Meshy: Refine Draft Model toma un modelo 3D preliminar de una tarea Meshy anterior y lo mejora, añadiendo opcionalmente texturas usando una indicación de texto o una imagen de referencia. Envía el trabajo de refinamiento a la API de Meshy y devuelve el modelo terminado como archivos GLB y FBX una vez que la tarea se completa.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo de IA utilizado para refinar el modelo preliminar.| COMBO| Sí| `"meshy-7.1"`  
`"meshy-7"`  
`"meshy-6"`  
`"latest"`  
`meshy_task_id`| El ID de tarea único del modelo preliminar que deseas refinar.| MESHY_TASK_ID| Sí| -  
`habilitar_pbr`| Genera mapas PBR (metálico, rugosidad, normal) además del color base. Nota: esto debe establecerse en false al usar el estilo Sculpture, ya que el estilo Sculpture genera su propio conjunto de mapas PBR. (predeterminado: False)| BOOLEAN| Sí| -  
`texto_de_textura`| Proporciona una indicación de texto para guiar el proceso de texturizado. Máximo 600 caracteres. No puede usarse al mismo tiempo que `texture_image`. (predeterminado: cadena vacía)| STRING| Sí| -  
`imagen_de_textura`| Solo puede usarse uno de `texture_image` o `texture_prompt` al mismo tiempo.| IMAGE| No| -  
`resolución de textura`| Resolución de textura de color base. Las resoluciones más altas capturan más detalle de superficie.| COMBO| Sí| `"2k"`  
`"4k"`  
`"8k"`  
  
**Nota:** Las entradas `texture_prompt` y `texture_image` son mutuamente excluyentes. No puedes proporcionar tanto una indicación de texto como una imagen para el texturizado en la misma operación.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model_file`| El nombre del archivo del modelo GLB generado. (Solo para compatibilidad con versiones anteriores)| STRING  
`meshy_task_id`| El ID de tarea único para el trabajo de refinamiento enviado.| MESHY_TASK_ID  
`GLB`| El modelo 3D refinado final en formato GLB.| FILE3DGLB  
`FBX`| El modelo 3D refinado final en formato FBX.| FILE3DFBX  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/es.md)

* * *

**Source fingerprint (SHA-256):** `d9aac584e6abf9688c97bf01ea515bca13844d08c93923a672fb2853266926c8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MeshyRefineNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MeshyRefineNode)

[Meshy: Multi-Imagen a modelo](https://docs.comfy.org/es/built-in-nodes/MeshyMultiImageToModelNode)[Meshy: Riggear modelo](https://docs.comfy.org/es/built-in-nodes/MeshyRigModelNode)
