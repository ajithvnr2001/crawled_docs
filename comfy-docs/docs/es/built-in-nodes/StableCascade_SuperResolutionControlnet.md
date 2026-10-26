---
url: https://docs.comfy.org/es/built-in-nodes/StableCascade_SuperResolutionControlnet/
title: Super resoluci\u00f3n ControlNet Stable Cascade - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:32.889123+00:00
---

# Super resolución ControlNet Stable Cascade - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/StableCascade_SuperResolutionControlnet/

Stable Cascade

# Super resolución ControlNet Stable Cascade - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo forma parte del grupo experimental Stable Cascade.

Copiar páginaCopiar página

Este nodo forma parte del grupo experimental Stable Cascade. Prepara las entradas para el procesamiento de superresolución de Stable Cascade mediante la codificación de una imagen de entrada con un VAE para crear una entrada de controlnet, y mediante la generación de marcadores de posición latentes vacíos (rellenos de ceros) para la etapa C y la etapa B del pipeline de Stable Cascade.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada que se procesará para superresolución. Solo se utilizan los primeros 3 canales de color (RGB) de la imagen para la codificación.| IMAGE| Sí| -  
`vae`| El modelo VAE utilizado para codificar la imagen de entrada| VAE| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`controlnet_input`| La representación de imagen codificada por VAE adecuada para la entrada de controlnet| IMAGE  
`stage_c`| Representación latente de marcador de posición (rellena de ceros) para la etapa C del procesamiento de Stable Cascade, con 16 canales y dimensiones basadas en el tamaño de la imagen de entrada dividido por 16| LATENT  
`stage_b`| Representación latente de marcador de posición (rellena de ceros) para la etapa B del procesamiento de Stable Cascade, con 4 canales y dimensiones basadas en el tamaño de la imagen de entrada dividido por 2| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/es.md)

* * *

**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/StableCascade_SuperResolutionControlnet.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/StableCascade_SuperResolutionControlnet)

[Multiplicar atención temporal UNet](https://docs.comfy.org/es/built-in-nodes/UNetTemporalAttentionMultiply)[Difusión diferencial](https://docs.comfy.org/es/built-in-nodes/DifferentialDiffusion)
