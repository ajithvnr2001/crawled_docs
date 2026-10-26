---
url: https://docs.comfy.org/es/built-in-nodes/WavespeedImageUpscaleNode/
title: WaveSpeed escalado de imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:47.528247+00:00
---

# WaveSpeed escalado de imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WavespeedImageUpscaleNode/

Wavespeed

# WaveSpeed escalado de imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo WaveSpeed Image Upscale utiliza un servicio de IA externo para aumentar la resolución y calidad de una imagen.

Copiar páginaCopiar página

El nodo WaveSpeed Image Upscale utiliza un servicio de IA externo para aumentar la resolución y calidad de una imagen. Toma una sola foto de entrada y la amplía a una resolución objetivo superior, como 2K, 4K u 8K, produciendo un resultado más nítido y detallado.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de IA a utilizar para la ampliación. “SeedVR2” y “Ultimate” ofrecen diferentes niveles de calidad y precios.| STRING| Sí| `"SeedVR2"`  
`"Ultimate"`  
`imagen`| La imagen de entrada que se va a ampliar.| IMAGE| Sí|   
`resolución_objetivo`| La resolución de salida deseada para la imagen ampliada.| STRING| Sí| `"2K"`  
`"4K"`  
`"8K"`  
  
**Nota:** Este nodo requiere exactamente una imagen de entrada. Proporcionar un lote de imágenes generará un error.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`imagen`| La imagen de salida ampliada y de alta resolución.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/es.md)

* * *

**Source fingerprint (SHA-256):** `b14056f981f6e34c67d8126391acc11878f92f5f406559afbac803c86da42bcc`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WavespeedImageUpscaleNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WavespeedImageUpscaleNode)

[Wan texto a imagen](https://docs.comfy.org/es/built-in-nodes/WanTextToImageApi)[Eliminación guiada de fondo de Bria](https://docs.comfy.org/es/built-in-nodes/BriaGuidedRemoveBackground)
