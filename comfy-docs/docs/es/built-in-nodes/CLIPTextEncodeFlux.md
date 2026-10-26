---
url: https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeFlux/
title: Codificar texto CLIP para Flux - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:36.806801+00:00
---

# Codificar texto CLIP para Flux - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeFlux/

FLUX

# Codificar texto CLIP para Flux - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

CLIPTextEncodeFlux es un nodo de codificación de texto diseñado para la arquitectura Flux.

Copiar páginaCopiar página

`CLIPTextEncodeFlux` es un nodo de codificación de texto diseñado para la arquitectura Flux. Procesa dos entradas de texto independientes a través de diferentes codificadores —CLIP-L y T5XXL— y las combina con una escala de guía para producir una salida de condicionamiento unificada para la generación de imágenes.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`clip`| Un modelo CLIP que admite la arquitectura Flux, incluidos los codificadores CLIP-L y T5XXL.| CLIP| Sí| -  
`clip_l`| Entrada de texto procesada por el codificador CLIP-L. Adecuada para descripciones concisas basadas en palabras clave, como estilo o temática. Admite entrada multilínea y prompts dinámicos.| STRING| Sí| -  
`t5xxl`| Entrada de texto procesada por el codificador T5XXL. Adecuada para descripciones detalladas en lenguaje natural, expresando escenas y detalles complejos. Admite entrada multilínea y prompts dinámicos.| STRING| Sí| -  
`orientación`| Controla la influencia de las condiciones de texto en el proceso de generación. Valores más altos implican un cumplimiento más estricto del texto. Predeterminado: 3.5. Ajustable en incrementos de 0.1.| FLOAT| Sí| 0.0 - 100.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`CONDITIONING`| Contiene las incrustaciones fusionadas de ambos codificadores y el parámetro `guidance`, utilizadas para la generación condicional de imágenes.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/es.md)

* * *

**Source fingerprint (SHA-256):** `022928fa6917102f5dc599364df9541b2451b42eb36a11813931b5fd71990b74`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CLIPTextEncodeFlux.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CLIPTextEncodeFlux)

[Cosmos Predict2 imagen a latente de video](https://docs.comfy.org/es/built-in-nodes/CosmosPredict2ImageToVideoLatent)[Prompt de diseño de FLUX 3 Image](https://docs.comfy.org/es/built-in-nodes/Flux3LayoutPrompt)
