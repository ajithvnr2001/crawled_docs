---
url: https://docs.comfy.org/es/built-in-nodes/unCLIPConditioning/
title: Acondicionamiento unCLIP - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:48.677691+00:00
---

# Acondicionamiento unCLIP - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/unCLIPConditioning/

Acondicionamiento

# Acondicionamiento unCLIP - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para integrar las salidas de visión CLIP en el proceso de condicionamiento

Copiar páginaCopiar página

Este nodo está diseñado para integrar las salidas de visión CLIP en el proceso de condicionamiento, ajustando la influencia de estas salidas según parámetros específicos de intensidad y aumento de ruido. Enriquece el condicionamiento con contexto visual, mejorando el proceso de generación.

## 

​

Entradas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`acondicionamiento`| Los datos de condicionamiento base a los que se agregarán las salidas de visión CLIP, sirviendo como base para modificaciones posteriores.| `CONDITIONING`  
`salida_vision_clip`| La salida de un modelo de visión CLIP, que proporciona contexto visual que se integra en el condicionamiento.| `CLIP_VISION_OUTPUT`  
`fuerza`| Determina la intensidad de la influencia de la salida de visión CLIP sobre el condicionamiento.| `FLOAT`  
`aumento_ruido`| Especifica el nivel de aumento de ruido que se aplicará a la salida de visión CLIP antes de integrarla en el condicionamiento.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`acondicionamiento`| Los datos de condicionamiento enriquecidos, que ahora contienen las salidas de visión CLIP integradas con la intensidad y el aumento de ruido aplicados.| `CONDITIONING`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/unCLIPConditioning.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/unCLIPConditioning)

[Opciones de tokenizador T5](https://docs.comfy.org/es/built-in-nodes/T5TokenizerOptions)[Control de color/profundidad de MOSS-Image](https://docs.comfy.org/es/built-in-nodes/MOSSImageControl)
