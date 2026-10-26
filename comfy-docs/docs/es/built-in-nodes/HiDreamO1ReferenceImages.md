---
url: https://docs.comfy.org/es/built-in-nodes/HiDreamO1ReferenceImages/
title: Im\u00e1genes de Referencia HiDream-O1 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:53.412048+00:00
---

# Imágenes de Referencia HiDream-O1 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HiDreamO1ReferenceImages/

Hidream

# Imágenes de Referencia HiDream-O1 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo adjunta imágenes de referencia tanto al condicionamiento positivo como al negativo

Copiar páginaCopiar página

Este nodo adjunta imágenes de referencia tanto al condicionamiento positivo como al negativo, de modo que los nodos posteriores puedan usarlas para guiar la generación. Las imágenes de referencia se aplican en el orden numérico de sus conectores de entrada. Si no se conectan imágenes de referencia, el condicionamiento positivo y el negativo pasan sin cambios.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`positivo`| El condicionamiento positivo al que se le adjuntarán las imágenes de referencia.| CONDITIONING| Sí| -  
`negativo`| El condicionamiento negativo al que se le adjuntarán las imágenes de referencia.| CONDITIONING| Sí| -  
`imágenes`| Las imágenes de referencia se utilizan en el orden numérico de los conectores. Cuando se suministran imágenes, se adjuntan tanto al condicionamiento positivo como al negativo.| IMAGE| No| 0 a 100 imágenes (`image_1` a `image_100`)  
  
**Nota sobre el parámetro`images`:** Esta es una entrada de crecimiento automático que proporciona conectores numerados `image_1` hasta `image_100`. Las imágenes se utilizan en el orden numérico de los conectores. La entrada es opcional: si no se conectan imágenes de referencia, el nodo devuelve el condicionamiento `positive` y `negative` sin cambios. Cuando se conectan imágenes, el mismo conjunto de imágenes de referencia se adjunta a ambas salidas, y el condicionamiento negativo también se marca como negativo antes de adjuntar las imágenes.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positivo`| El condicionamiento positivo con las imágenes de referencia adjuntas.| CONDITIONING  
`negativo`| El condicionamiento negativo con las imágenes de referencia adjuntas.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/es.md)

* * *

**Source fingerprint (SHA-256):** `07f9f0ea19957523e95d04b9086dc994807bb0cd5262fe798dc784c1ecb4920d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HiDreamO1ReferenceImages.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HiDreamO1ReferenceImages)

[Codificar texto CLIP para HiDream](https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeHiDream)[Acondicionamiento Hunyuan 3D v2](https://docs.comfy.org/es/built-in-nodes/Hunyuan3Dv2Conditioning)
