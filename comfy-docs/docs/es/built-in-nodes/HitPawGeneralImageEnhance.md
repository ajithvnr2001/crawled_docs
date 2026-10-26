---
url: https://docs.comfy.org/es/built-in-nodes/HitPawGeneralImageEnhance/
title: HitPaw mejora general de imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:53.254151+00:00
---

# HitPaw mejora general de imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HitPawGeneralImageEnhance/

Hitpaw

# HitPaw mejora general de imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo mejora imágenes de baja resolución al escalarlas a superresolución mientras elimina artefactos y ruido.

Copiar páginaCopiar página

Este nodo mejora imágenes de baja resolución al escalarlas a superresolución mientras elimina artefactos y ruido. Envía la imagen a una API externa para su procesamiento y puede ajustar automáticamente el tamaño de entrada para mantenerse dentro del límite de salida permitido. El tamaño máximo de salida permitido es de 32 megapíxeles.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de mejora a usar. El modelo `generative_portrait` está optimizado para retratos, mientras que `generative` es un modelo de propósito general.| COMBO| Sí| `"generative_portrait"`  
`"generative"`  
`imagen`| La imagen de entrada que se va a mejorar.| IMAGE| Sí| -  
`factor de escalado`| El factor por el que se escalan las dimensiones de la imagen. Un factor de 1 significa que no hay escalado, 2 duplica las dimensiones y 4 las cuadruplica.| COMBO| Sí| `1`  
`2`  
`4`  
`reducción automática`| Reduce automáticamente la escala de la imagen de entrada si la salida superara el límite. (predeterminado: `False`)| BOOLEAN| No| -  
  
**Nota:** El nodo lanza un error si el tamaño de salida calculado (ancho de entrada × `upscale_factor` × alto de entrada × `upscale_factor`) supera los 32.000.000 píxeles (32MP) y `auto_downscale` está deshabilitado. Cuando `auto_downscale` está habilitado, el nodo reduce automáticamente el tamaño de la imagen de entrada o el factor de escalado (o ambos) para que la salida quepa dentro del límite de 32MP. El `model` seleccionado y el `upscale_factor` se combinan en el nombre del modelo enviado al servicio.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| La imagen de salida mejorada y escalada.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/es.md)

* * *

**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HitPawGeneralImageEnhance.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HitPawGeneralImageEnhance)

[Imagen Grok](https://docs.comfy.org/es/built-in-nodes/GrokImageNode)[Edición de Ideogram 4.5](https://docs.comfy.org/es/built-in-nodes/IdeogramEditApi)
