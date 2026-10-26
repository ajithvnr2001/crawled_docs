---
url: https://docs.comfy.org/es/built-in-nodes/SamplerARVideo/
title: Muestreador de video autorregresivo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:26.705309+00:00
---

# Muestreador de video autorregresivo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SamplerARVideo/

Samplers

# Muestreador de video autorregresivo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Sampler AR Video proporciona un método de muestreo especializado para modelos de video autorregresivos

Copiar páginaCopiar página

El nodo Sampler AR Video proporciona un método de muestreo especializado para modelos de video autorregresivos, como los que utilizan técnicas de Causal Forcing o Self-Forcing. Gestiona todos los parámetros relacionados con el bucle autorregresivo (AR) directamente dentro del flujo de trabajo, lo que facilita la configuración de cómo el modelo genera los fotogramas de video paso a paso.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| ¿Requerido?| Rango  
---|---|---|---|---  
`num_frame_per_block`| Fotogramas por bloque autorregresivo. Un valor de 1 significa que el modelo genera un fotograma a la vez (fotograma por fotograma), mientras que un valor de 3 significa que genera tres fotogramas juntos (por bloques). Este ajuste debe coincidir con el modo de entrenamiento del checkpoint. Por defecto: 1.| INT| Sí| 1 a 64  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`SAMPLER`| Un objeto muestreador configurado que utiliza la función de muestreo “ar_video” con los parámetros autorregresivos especificados.| SAMPLER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SamplerARVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SamplerARVideo)

[Seleccionar KSampler](https://docs.comfy.org/es/built-in-nodes/KSamplerSelect)[Muestreador DPM adaptativo](https://docs.comfy.org/es/built-in-nodes/SamplerDPMAdaptative)
