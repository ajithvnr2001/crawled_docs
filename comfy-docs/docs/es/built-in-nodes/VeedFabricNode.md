---
url: https://docs.comfy.org/es/built-in-nodes/VeedFabricNode/
title: VEED Fabric 1.0 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:41.934133+00:00
---

# VEED Fabric 1.0 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VeedFabricNode/

Video

# VEED Fabric 1.0 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Convierte una imagen fija y una pista de voz en un video con habla y sincronización labial con VEED Fabric.

Copiar páginaCopiar página

Convierte una imagen fija y una pista de voz en un video con habla y sincronización labial con VEED Fabric. Funciona con fotos, ilustraciones y personajes mascota siempre que el rostro sea claramente visible; el video mantiene la relación de aspecto de la imagen y tiene la misma duración que el audio.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| Modelo a utilizar. Al seleccionar un modelo, se muestran los parámetros específicos de este: `image`, `audio` y `resolution`.| DYNAMIC_COMBO| Sí| `"fabric-1.0"`  
`image`| Imagen con un rostro claramente visible. El video mantiene su relación de aspecto.| IMAGE| Sí| -  
`audio`| Audio de voz para sincronizar los labios, de hasta 300 segundos. Establece la duración del video.| AUDIO| Sí| Hasta 300 segundos  
`resolution`| Clase de tamaño de salida: aproximadamente 0.4 megapíxeles en `"480p"` (864x480 en 16:9) y 0.9 megapíxeles en `"720p"` (1312x736 en 16:9). (predeterminado: `"720p"`)| COMBO| Sí| `"480p"`  
`"720p"`  
  
El nodo se detiene con un error cuando la pista de voz supera los 300 segundos.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`VIDEO`| El video con habla: la imagen de entrada animada para coincidir con la pista de voz.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedFabricNode/es.md)

* * *

**Source fingerprint (SHA-256):** `69cabfa5f03885ce770e8502419305dacee49d7e89a748f31abe3775d682a33a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VeedFabricNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VeedFabricNode)

[VEED Clean Audio (en vídeo)](https://docs.comfy.org/es/built-in-nodes/VeedCleanVideoAudioNode)[VEED Lipsync 2.0](https://docs.comfy.org/es/built-in-nodes/VeedLipsyncNode)
