---
url: https://docs.comfy.org/es/built-in-nodes/VOIDSampler/
title: VOIDSampler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:41.319234+00:00
---

# VOIDSampler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VOIDSampler/

Samplers

# VOIDSampler - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

VOIDSampler es un muestreador DDIM especializado diseñado para modelos de inpainting VOID.

Copiar páginaCopiar página

VOIDSampler es un muestreador DDIM especializado diseñado para modelos de inpainting VOID. Reproduce el proceso exacto de eliminación de ruido con el que se entrenó VOID, omitiendo el escalado de ruido que aplican los KSamplers estándar. Utilice este nodo junto con SamplerCustom o SamplerCustomAdvanced, en combinación con RandomNoise o VOIDWarpedNoiseSource.

## 

​

Entradas

Este nodo no tiene parámetros de entrada configurables. Es un muestreador autocontenido que aplica un algoritmo de muestreo DDIM fijo.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
 _Sin entradas_|  Este nodo no acepta ningún parámetro de entrada.| -| -| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`SAMPLER`| Un objeto muestreador que implementa el algoritmo VOID DDIM, listo para conectarse a los nodos SamplerCustom o SamplerCustomAdvanced.| SAMPLER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/es.md)

* * *

**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VOIDSampler.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VOIDSampler)

[Muestreador SEEDS2](https://docs.comfy.org/es/built-in-nodes/SamplerSEEDS2)[Programador alinea tus pasos](https://docs.comfy.org/es/built-in-nodes/AlignYourStepsScheduler)
