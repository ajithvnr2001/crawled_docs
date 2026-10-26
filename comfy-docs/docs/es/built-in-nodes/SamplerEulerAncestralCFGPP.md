---
url: https://docs.comfy.org/es/built-in-nodes/SamplerEulerAncestralCFGPP/
title: SamplerEulerAncestralCFG++ - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:27.417254+00:00
---

# SamplerEulerAncestralCFG++ - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SamplerEulerAncestralCFGPP/

Samplers

# SamplerEulerAncestralCFG++ - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SamplerEulerAncestralCFG++ crea un sampler que utiliza el método Euler Ancestral con guía libre de clasificador (CFG++) para la generación de imágenes.

Copiar páginaCopiar página

El nodo SamplerEulerAncestralCFG++ crea un sampler que utiliza el método Euler Ancestral con guía libre de clasificador (CFG++) para la generación de imágenes. Este sampler combina técnicas de muestreo ancestral con condicionamiento de guía para producir variaciones de imagen diversas mientras mantiene la coherencia, y permite un ajuste fino mediante parámetros que controlan los ajustes de ruido y tamaño de paso.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`eta`| Controla el tamaño del paso durante el muestreo; valores más altos producen actualizaciones más agresivas (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 1.0  
`s_ruido`| Ajusta la cantidad de ruido añadido durante el proceso de muestreo (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 10.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`sampler`| Devuelve un objeto sampler configurado que se puede usar en el flujo de generación de imágenes| SAMPLER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/es.md)

* * *

**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SamplerEulerAncestralCFGPP.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SamplerEulerAncestralCFGPP)

[Muestreador Euler ancestral](https://docs.comfy.org/es/built-in-nodes/SamplerEulerAncestral)[SamplerLCM](https://docs.comfy.org/es/built-in-nodes/SamplerLCM)
