---
url: https://docs.comfy.org/es/built-in-nodes/VideoLinearCFGGuidance/
title: Gu\u00eda CFG lineal para video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:42.422726+00:00
---

# Guía CFG lineal para video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VideoLinearCFGGuidance/

Guiadores

# Guía CFG lineal para video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VideoLinearCFGGuidance aplica una escala de guía de condicionamiento lineal a un modelo de video

Copiar páginaCopiar página

El nodo VideoLinearCFGGuidance aplica una escala de guía de condicionamiento lineal a un modelo de video, ajustando la influencia de los componentes condicionados y no condicionados dentro de un rango específico. Esto permite un control dinámico sobre el proceso de generación, posibilitando el ajuste fino de la salida del modelo según el nivel deseado de condicionamiento.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`modelo`| El parámetro `modelo` representa el modelo de video al que se aplicará la guía CFG lineal. Es fundamental para definir el modelo base que se modificará con la escala de guía.| MODEL  
`min_cfg`| El parámetro `min_cfg` especifica la escala de guía de condicionamiento mínima que se aplicará, sirviendo como punto de partida para el ajuste lineal de la escala. Desempeña un papel clave en la determinación del límite inferior de la escala de guía, influyendo en la salida del modelo.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`modelo`| La salida es una versión modificada del modelo de entrada, con la escala de guía CFG lineal aplicada. Este modelo ajustado es capaz de generar resultados con distintos grados de condicionamiento, según la escala de guía especificada.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoLinearCFGGuidance/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VideoLinearCFGGuidance.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VideoLinearCFGGuidance)

[LTXV Dual CFG Guider](https://docs.comfy.org/es/built-in-nodes/LTXVDualCFGGuider)[Guía CFG triangular para video](https://docs.comfy.org/es/built-in-nodes/VideoTriangleCFGGuidance)
