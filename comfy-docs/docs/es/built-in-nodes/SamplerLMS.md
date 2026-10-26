---
url: https://docs.comfy.org/es/built-in-nodes/SamplerLMS/
title: Muestreador LMS - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:27.953967+00:00
---

# Muestreador LMS - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SamplerLMS/

Samplers

# Muestreador LMS - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SamplerLMS crea un muestreador de mínimos cuadrados medios (LMS) para usar en modelos de difusión.

Copiar páginaCopiar página

El nodo SamplerLMS crea un muestreador de mínimos cuadrados medios (LMS) para usar en modelos de difusión. Genera un objeto muestreador que puede utilizarse en el proceso de muestreo y permite controlar el orden del algoritmo LMS para lograr estabilidad y precisión numéricas.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`orden`| El parámetro de orden para el algoritmo del muestreador LMS, que controla la precisión y estabilidad del método numérico (predeterminado: 4). Este parámetro se muestra en la sección avanzada de la interfaz del nodo.| INT| Sí| 1 a 100  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`sampler`| Un objeto muestreador LMS configurado que se puede utilizar en el proceso de muestreo| SAMPLER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/es.md)

* * *

**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SamplerLMS.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SamplerLMS)

[Muestreador LCM ampliar](https://docs.comfy.org/es/built-in-nodes/SamplerLCMUpscale)[Muestreador SA-Solver](https://docs.comfy.org/es/built-in-nodes/SamplerSASolver)
