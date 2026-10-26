---
url: https://docs.comfy.org/es/built-in-nodes/VOIDWarpedNoiseSource/
title: VOIDWarpedNoiseSource - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:41.190880+00:00
---

# VOIDWarpedNoiseSource - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VOIDWarpedNoiseSource/

Void

# VOIDWarpedNoiseSource - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo convierte un LATENT (como la salida del nodo VOIDWarpedNoise) en una fuente NOISE.

Copiar páginaCopiar página

Este nodo convierte un LATENT (como la salida del nodo VOIDWarpedNoise) en una fuente NOISE. Esto permite alimentar ruido deformado precalculado a nodos que esperan una fuente de ruido, como SamplerCustomAdvanced.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`warped_noise`| Latente de ruido deformado de VOIDWarpedNoise| LATENT| Sí| N/A  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`NOISE`| Una fuente de ruido que envuelve el latente suministrado, utilizable con SamplerCustomAdvanced| NOISE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/es.md)

* * *

**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VOIDWarpedNoiseSource.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VOIDWarpedNoiseSource)

[VOIDWarpedNoise](https://docs.comfy.org/es/built-in-nodes/VOIDWarpedNoise)[Audio latent vacío de YuE2](https://docs.comfy.org/es/built-in-nodes/EmptyYuE2LatentAudio)
