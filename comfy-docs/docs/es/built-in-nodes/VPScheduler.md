---
url: https://docs.comfy.org/es/built-in-nodes/VPScheduler/
title: Programador VP - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:41.465954+00:00
---

# Programador VP - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VPScheduler/

Programadores

# Programador VP - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VPScheduler está diseñado para generar una secuencia de niveles de ruido (sigmas) basada en el método de programación de Preservación de Varianza (VP).

Copiar páginaCopiar página

El nodo VPScheduler está diseñado para generar una secuencia de niveles de ruido (sigmas) basada en el método de programación de Preservación de Varianza (VP). Esta secuencia es crucial para guiar el proceso de eliminación de ruido en modelos de difusión, permitiendo la generación controlada de imágenes u otros tipos de datos.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`pasos`| Especifica el número de pasos en el proceso de difusión, afectando la granularidad de los niveles de ruido generados.| INT  
`beta_d`| Determina la distribución general del nivel de ruido, influyendo en la varianza de los niveles de ruido generados.| FLOAT  
`beta_min`| Establece el límite mínimo para el nivel de ruido, asegurando que el ruido no caiga por debajo de cierto umbral.| FLOAT  
`eps_s`| Ajusta el valor épsilon inicial, afinando el nivel de ruido inicial en el proceso de difusión.| FLOAT  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`sigmas`| Una secuencia de niveles de ruido (sigmas) generada según el método de programación VP, utilizada para guiar el proceso de eliminación de ruido en modelos de difusión.| SIGMAS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VPScheduler/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VPScheduler.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VPScheduler)

[Programador SD Turbo](https://docs.comfy.org/es/built-in-nodes/SDTurboScheduler)[Extender sigmas intermedias](https://docs.comfy.org/es/built-in-nodes/ExtendIntermediateSigmas)
