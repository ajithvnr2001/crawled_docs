---
url: https://docs.comfy.org/es/built-in-nodes/VeedLipsyncNode/
title: VEED Lipsync 2.0 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:42.067925+00:00
---

# VEED Lipsync 2.0 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VeedLipsyncNode/

Video

# VEED Lipsync 2.0 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Resincroniza la boca de un hablante en un video con una nueva pista de voz usando VEED Lipsync.

Copiar páginaCopiar página

Resincroniza la boca de un hablante en un video con una nueva pista de voz usando VEED Lipsync. Úsalo para doblar un clip o reemplazar su diálogo manteniendo el metraje original. La salida conserva la resolución del video a 25 fps y tiene la misma duración que el audio, con un solo hablante por video.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| Modelo a usar. Al seleccionar un modelo se muestran los parámetros específicos de este: `video`, `audio` y `seed`.| DYNAMIC_COMBO| Sí| `"lipsync-2.0"`  
`video`| Metraje de un hablante de frente. Si es más corto que el audio, se reproduce hacia adelante y hacia atrás hasta que termina el audio.| VIDEO| Sí| -  
`audio`| Nueva locución, de hasta 600 segundos. Establece la duración del video.| AUDIO| Sí| Hasta 600 segundos  
`seed`| La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas, independientemente de la semilla. (predeterminado: 42)| INT| Sí| 0 a 2147483647  
  
El nodo se detiene con un error cuando la pista de voz supera los 600 segundos o cuando falla el trabajo de VEED.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`VIDEO`| El video resincronizado: el metraje original con la boca ajustada a la nueva locución.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedLipsyncNode/es.md)

* * *

**Source fingerprint (SHA-256):** `1a1e854b6923b5bad0fd6f3a79e76c70231dee31a12e9cf0b22be6bdcc741168`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VeedLipsyncNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VeedLipsyncNode)

[VEED Fabric 1.0](https://docs.comfy.org/es/built-in-nodes/VeedFabricNode)[VEED Eliminar fondo de vídeo](https://docs.comfy.org/es/built-in-nodes/VeedRemoveVideoBackgroundNode)
