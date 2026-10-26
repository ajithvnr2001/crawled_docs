---
url: https://docs.comfy.org/es/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode/
title: Comfy Cloud Mage Flow Turbo Texto a imagen [BETA] - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:39.294096+00:00
---

# Comfy Cloud Mage Flow Turbo Texto a imagen [BETA] - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode/

Avanzado

# Comfy Cloud Mage Flow Turbo Texto a imagen [BETA] - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo de Comfy Cloud genera una imagen a partir de un prompt de texto usando el flujo de trabajo Mage-Flow Turbo (mage-flow-turbo/text-to-image).

Copiar páginaCopiar página

Este nodo de Comfy Cloud genera una imagen a partir de un prompt de texto usando el flujo de trabajo Mage-Flow Turbo (`mage-flow-turbo/text-to-image`). Ejecuta una versión destilada del modelo Mage-Flow que produce la imagen en 4 pasos con un valor cfg de 1, tomando aproximadamente una séptima parte del tiempo de GPU de una pasada completa de Mage-Flow, lo que lo convierte en la variante pensada para iteración rápida.

## 

​

Entradas

La clase del nodo en sí no declara widgets de entrada en la fuente disponible; su esquema de entrada se hereda de la clase base compartida `_ComfyCloudMageFlowNode`, cuya definición no está incluida en la instantánea de la fuente. Según el resumen del nodo y el nombre del flujo de trabajo de texto a imagen, el nodo recibe un prompt de texto que describe la imagen a generar.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| El prompt de texto que describe la imagen a generar. El nombre exacto del parámetro lo establece el esquema base heredado `_ComfyCloudMageFlowNode` y puede diferir de esta etiqueta.| STRING| Sí| Texto libre  
  
Nota: pueden existir parámetros de entrada adicionales en la definición heredada del nodo base, que no está disponible en la fuente proporcionada.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`IMAGE`| La imagen generada a partir del prompt de texto.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/es.md)

* * *

**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode)

[Comfy Cloud Mage Flow Texto a imagen [BETA]](https://docs.comfy.org/es/built-in-nodes/ComfyCloudMageFlowTextToImageNode)[Comfy Cloud Z-Image Turbo Texto a imagen [BETA]](https://docs.comfy.org/es/built-in-nodes/ComfyCloudZImageTurboNode)
