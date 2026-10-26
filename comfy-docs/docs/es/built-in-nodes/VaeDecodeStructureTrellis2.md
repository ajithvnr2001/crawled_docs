---
url: https://docs.comfy.org/es/built-in-nodes/VaeDecodeStructureTrellis2/
title: Decodificaci\u00f3n de estructura VAE de Trellis2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:41.392772+00:00
---

# Decodificación de estructura VAE de Trellis2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VaeDecodeStructureTrellis2/

Trellis

# Decodificación de estructura VAE de Trellis2 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo convierte muestras latentes de estructura Trellis en una rejilla de vóxeles 3D utilizando el decodificador de estructura de una VAE.

Copiar páginaCopiar página

Este nodo convierte muestras latentes de estructura Trellis en una rejilla de vóxeles 3D utilizando el decodificador de estructura de una VAE. Lee solo los primeros 8 canales del latente, reconstruye la ocupación de vóxeles y ajusta la resolución de salida a 32 o 64 según se solicite.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`samples`| La representación latente de la estructura a decodificar. Solo los primeros 8 canales del latente se utilizan para la decodificación.| LATENT| Sí| -  
`vae`| La VAE cuyo decodificador de estructura convierte el latente en una rejilla de vóxeles. La decodificación se realiza en lotes.| VAE| Sí| -  
`resolution`| La resolución espacial objetivo de la rejilla de vóxeles de salida (predeterminado: “32”). Si la rejilla decodificada tiene una resolución diferente, se reduce su resolución para coincidir.| COMBO| Sí| ”32"  
"64”  
  
Nota: Cuando la resolución de la rejilla de vóxeles decodificada difiere de la `resolution` seleccionada, la rejilla se reduce mediante max pooling 3D al tamaño solicitado.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`voxel`| Una rejilla binaria de ocupación de vóxeles como tensor flotante con forma [batch, depth, height, width]. Los valores son 1.0 para vóxeles ocupados y 0.0 para vóxeles vacíos.| VOXEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeStructureTrellis2/es.md)

* * *

**Source fingerprint (SHA-256):** `37764ef7351b3619d4cddb57b11d9a0da24dadeedc0fc0f70d089038d37e03b0`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VaeDecodeStructureTrellis2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VaeDecodeStructureTrellis2)

[Decodificación de forma VAE de Trellis2](https://docs.comfy.org/es/built-in-nodes/VaeDecodeShapeTrellis)[Decodificación de textura VAE de Trellis2](https://docs.comfy.org/es/built-in-nodes/VaeDecodeTextureTrellis)
