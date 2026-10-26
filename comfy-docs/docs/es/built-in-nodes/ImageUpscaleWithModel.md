---
url: https://docs.comfy.org/es/built-in-nodes/ImageUpscaleWithModel/
title: Ampliar imagen (usando modelo) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.903724+00:00
---

# Ampliar imagen (usando modelo) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageUpscaleWithModel/

Escalado

# Ampliar imagen (usando modelo) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para escalar imágenes utilizando un modelo de escalado específico.

Copiar páginaCopiar página

Este nodo está diseñado para escalar imágenes utilizando un modelo de escalado específico. Gestiona eficientemente el proceso de escalado ajustando la imagen al dispositivo adecuado, optimizando el uso de memoria y aplicando el modelo de escalado en mosaicos para evitar posibles errores de memoria insuficiente.

## 

​

Entradas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`modelo_ampliacion`| El modelo de escalado que se utilizará para escalar la imagen. Es fundamental para definir el algoritmo de escalado y sus parámetros.| `UPSCALE_MODEL`  
`imagen`| La imagen que se va a escalar. Esta entrada es esencial para determinar el contenido de origen que se someterá al proceso de escalado.| `IMAGE`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen escalada, procesada por el modelo de escalado. Esta salida es el resultado de la operación de escalado, mostrando la resolución o calidad mejorada.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageUpscaleWithModel/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageUpscaleWithModel.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageUpscaleWithModel)

[Escalar imagen a total de píxeles](https://docs.comfy.org/es/built-in-nodes/ImageScaleToTotalPixels)[WanDancerPadKeyframes](https://docs.comfy.org/es/built-in-nodes/WanDancerPadKeyframes)
