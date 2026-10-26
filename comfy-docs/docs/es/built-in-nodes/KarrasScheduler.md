---
url: https://docs.comfy.org/es/built-in-nodes/KarrasScheduler/
title: Programador Karras - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:58.552963+00:00
---

# Programador Karras - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/KarrasScheduler/

Programadores

# Programador Karras - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo KarrasScheduler está diseñado para generar una secuencia de niveles de ruido (sigmas) basada en el programador de ruido de Karras et al. (2022).

Copiar páginaCopiar página

El nodo KarrasScheduler está diseñado para generar una secuencia de niveles de ruido (sigmas) basada en el programador de ruido de Karras et al. (2022). Este programador es útil para controlar el proceso de difusión en modelos generativos, permitiendo ajustes precisos en los niveles de ruido aplicados en cada paso del proceso de generación.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`pasos`| Especifica el número de pasos en el programador de ruido, afectando la granularidad de la secuencia de sigmas generada.| INT  
`sigma_max`| El valor máximo de sigma en el programador de ruido, estableciendo el límite superior de los niveles de ruido.| FLOAT  
`sigma_min`| El valor mínimo de sigma en el programador de ruido, estableciendo el límite inferior de los niveles de ruido.| FLOAT  
`rho`| Un parámetro que controla la forma de la curva del programador de ruido, influyendo en cómo los niveles de ruido progresan desde sigma_min hasta sigma_max.| FLOAT  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`sigmas`| La secuencia generada de niveles de ruido (sigmas) siguiendo el programador de ruido de Karras et al. (2022).| SIGMAS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KarrasScheduler/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/KarrasScheduler.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/KarrasScheduler)

[Planificador Ideogram 4](https://docs.comfy.org/es/built-in-nodes/Ideogram4Scheduler)[Programador Laplace](https://docs.comfy.org/es/built-in-nodes/LaplaceScheduler)
