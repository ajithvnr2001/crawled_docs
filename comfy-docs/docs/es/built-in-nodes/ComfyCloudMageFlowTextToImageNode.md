---
url: https://docs.comfy.org/es/built-in-nodes/ComfyCloudMageFlowTextToImageNode/
title: Comfy Cloud Mage Flow Texto a imagen [BETA] - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:38.786595+00:00
---

# Comfy Cloud Mage Flow Texto a imagen [BETA] - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ComfyCloudMageFlowTextToImageNode/

Avanzado

# Comfy Cloud Mage Flow Texto a imagen [BETA] - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo genera una imagen a partir de un prompt de texto enviando la solicitud al flujo de trabajo de texto a imagen Mage-Flow en Comfy Cloud.

Copiar páginaCopiar página

Este nodo genera una imagen a partir de un prompt de texto enviando la solicitud al flujo de trabajo de texto a imagen Mage-Flow en Comfy Cloud. Ejecuta la pasada de generación completa de 30 pasos en lugar de la pasada turbo destilada más rápida, y acepta un prompt negativo para que puedas describir el contenido que no deseas en la imagen final. El prompt negativo es compatible con este modo de 30 pasos; según el resumen del nodo, la variante turbo destilada no puede aprovecharlo bien.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| La descripción textual de la imagen a generar.| STRING| Sí| Texto libre  
`negative_prompt`| Texto que describe el contenido que no debería aparecer en la imagen generada. Esta entrada se utiliza durante la pasada de generación estándar de 30 pasos, pero la variante turbo destilada no aprovecha bien los prompts negativos.| STRING| No| Texto libre  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| La imagen generada a partir del prompt de texto y el prompt negativo proporcionados.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/es.md)

* * *

**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ComfyCloudMageFlowTextToImageNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ComfyCloudMageFlowTextToImageNode)

[Comfy Cloud Flux 2 Texto a imagen [BETA]](https://docs.comfy.org/es/built-in-nodes/ComfyCloudFlux2TextToImageNode)[Comfy Cloud Mage Flow Turbo Texto a imagen [BETA]](https://docs.comfy.org/es/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode)
