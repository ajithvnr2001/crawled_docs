---
url: https://docs.comfy.org/es/built-in-nodes/TripoSplatConditioning/
title: Condicionamiento TripoSplat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:39.051899+00:00
---

# Condicionamiento TripoSplat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TripoSplatConditioning/

Triposplat

# Condicionamiento TripoSplat - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo codifica una imagen de entrada con el codificador de imágenes DINOv3 y el VAE Flux2 para producir datos de condicionamiento positivo y negativo para

Copiar páginaCopiar página

Este nodo codifica una imagen de entrada con el codificador de imágenes DINOv3 y el VAE Flux2 para producir datos de condicionamiento positivo y negativo para el modelo TripoSplat. También crea un objetivo de ruido de tamaño fijo (latent más datos de cámara) que sirve como punto de partida para el KSampler.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`clip_vision`| Codificador de imágenes DINOv3 ViT-H/16+| CLIP_VISION| Sí| -  
`vae`| Flux2 VAE| VAE| Sí| -  
`imagen`| La imagen de entrada que se va a codificar| IMAGE| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positive`| Datos de condicionamiento positivo que contienen la secuencia de características DINOv3 y el latent del VAE Flux2 transportado como latent de referencia| CONDITIONING  
`negative`| Datos de condicionamiento negativo que contienen características DINOv3 rellenadas con ceros y un latent de referencia del VAE Flux2 rellenado con ceros| CONDITIONING  
`latent`| El objetivo de ruido de tamaño fijo (latent + cámara) para el KSampler. El latent es una secuencia de códigos de forma (shape-code) de forma constante (8192 x 16) emparejada con un único token de cámara (1 x 5)| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/es.md)

* * *

**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TripoSplatConditioning.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TripoSplatConditioning)

[Etapa de aumento de resolución de Trellis2](https://docs.comfy.org/es/built-in-nodes/Trellis2UpsampleStage)[TripoSplat Preprocesar Imagen](https://docs.comfy.org/es/built-in-nodes/TripoSplatPreprocessImage)
