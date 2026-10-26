---
url: https://docs.comfy.org/es/built-in-nodes/SamplerLCM/
title: SamplerLCM - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:27.710426+00:00
---

# SamplerLCM - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SamplerLCM/

Samplers

# SamplerLCM - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo proporciona un muestreador LCM (modelo de consistencia latente) con ruido ajustable por paso.

Copiar páginaCopiar página

Este nodo proporciona un muestreador LCM (modelo de consistencia latente) con ruido ajustable por paso. Te permite controlar cuánto ruido se aplica durante el muestreo: `s_noise` actúa como un multiplicador sobre la escala de ruido de entrenamiento del modelo, y el nivel de ruido puede variar desde el primer paso hasta el último paso. El muestreador configurado se puede conectar a un flujo de trabajo de muestreo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`s_noise`| Multiplicador de ruido por paso en el primer paso (1.0 = coincide con el entrenamiento). Predeterminado: 1.0.| FLOAT| Sí| 0.0 a 64.0 (paso: 0.01)  
`s_noise_end`| Multiplicador de ruido por paso en el último paso. Se establece igual a `s_noise` para una programación constante. Predeterminado: 1.0.| FLOAT| Sí| 0.0 a 64.0 (paso: 0.01)  
`noise_clip_std`| Limita el ruido por paso a +/- N*std. 0 lo desactiva. Predeterminado: 0.0.| FLOAT| Sí| 0.0 a 10.0 (paso: 0.01)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`SAMPLER`| El objeto muestreador LCM configurado, listo para usarse en un flujo de trabajo de muestreo.| SAMPLER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/es.md)

* * *

**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SamplerLCM.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SamplerLCM)

[SamplerEulerAncestralCFG++](https://docs.comfy.org/es/built-in-nodes/SamplerEulerAncestralCFGPP)[Muestreador LCM ampliar](https://docs.comfy.org/es/built-in-nodes/SamplerLCMUpscale)
