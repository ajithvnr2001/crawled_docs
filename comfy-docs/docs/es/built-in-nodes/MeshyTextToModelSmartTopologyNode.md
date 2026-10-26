---
url: https://docs.comfy.org/es/built-in-nodes/MeshyTextToModelSmartTopologyNode/
title: Meshy: Texto a modelo (topolog\u00eda inteligente) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:10.905995+00:00
---

# Meshy: Texto a modelo (topología inteligente) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MeshyTextToModelSmartTopologyNode/

3D

# Meshy: Texto a modelo (topología inteligente) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo genera una malla triangular lista para juegos con un recuento objetivo de caras usando Meshy T2.5.

Copiar páginaCopiar página

Este nodo genera una malla triangular lista para juegos con un recuento objetivo de caras usando Meshy T2.5. La topología se construye con el recuento de polígonos solicitado en lugar de decimarse después, por lo que el resultado está listo para un motor de juegos sin una pasada de retopología separada.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| La versión del modelo Meshy que se utilizará para la generación.| COMBO| Sí| `"meshy-t2.5"`  
`prompt`| La descripción de texto del modelo 3D que se va a generar.| STRING| Sí| 1 a 800 caracteres  
`target_polycount`| Número aproximado de triángulos en la malla generada. Predeterminado: 15000.| INT| Sí| 100 a 30000  
`pose_mode`| La pose del personaje generado. Una cadena vacía solicita que no se aplique una pose específica. Esta es una configuración avanzada. Predeterminado: `""` (cadena vacía).| COMBO| Sí| `""`  
`"A-pose"`  
`"T-pose"`  
`seed`| La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Predeterminado: 42.| INT| Sí| 0 a 2147483647  
  
**Restricciones:**

  * El `prompt` debe contener entre 1 y 800 caracteres.
  * `target_polycount` es el número de triángulos con el que se construye la malla, no un límite aplicado después de la generación.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`meshy_task_id`| El identificador único de la tarea de la API de Meshy.| MESHY_TASK_ID  
`GLB`| El modelo 3D generado en formato GLB.| FILE3DGLB  
`FBX`| El modelo 3D generado en formato FBX.| FILE3DFBX  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelSmartTopologyNode/es.md)

* * *

**Source fingerprint (SHA-256):** `9fcdc846a4ba39cf3d099629637fbb0cf6d9c8d65bcee8aff5ec6ac5c76b6af3`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MeshyTextToModelSmartTopologyNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MeshyTextToModelSmartTopologyNode)

[Meshy: Imagen a modelo (topología inteligente)](https://docs.comfy.org/es/built-in-nodes/MeshyImageToModelSmartTopologyNode)[ByteDance Seed Audio 1.0](https://docs.comfy.org/es/built-in-nodes/ByteDanceSeedAudio)
