---
url: https://docs.comfy.org/es/built-in-nodes/PolyexponentialScheduler/
title: Programador poliexponencial - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:18.319223+00:00
---

# Programador poliexponencial - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PolyexponentialScheduler/

Programadores

# Programador poliexponencial - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo PolyexponentialScheduler está diseñado para generar una secuencia de niveles de ruido (sigmas) basada en un programación de ruido poliexponencial.

Copiar páginaCopiar página

El nodo PolyexponentialScheduler está diseñado para generar una secuencia de niveles de ruido (sigmas) basada en un programación de ruido poliexponencial. Esta programación es una función polinómica en el logaritmo de sigma, lo que permite una progresión flexible y personalizable de los niveles de ruido a lo largo del proceso de difusión.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`pasos`| Especifica el número de pasos en el proceso de difusión, afectando la granularidad de los niveles de ruido generados.| INT  
`sigma_max`| El nivel máximo de ruido, que establece el límite superior de la programación de ruido.| FLOAT  
`sigma_min`| El nivel mínimo de ruido, que establece el límite inferior de la programación de ruido.| FLOAT  
`rho`| Un parámetro que controla la forma de la programación de ruido poliexponencial, influyendo en cómo progresan los niveles de ruido entre los valores mínimo y máximo.| FLOAT  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`sigmas`| La salida es una secuencia de niveles de ruido (sigmas) adaptada a la programación de ruido poliexponencial especificada.| SIGMAS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PolyexponentialScheduler.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PolyexponentialScheduler)

[Programador de pasos óptimos](https://docs.comfy.org/es/built-in-nodes/OptimalStepsScheduler)[Programador SD Turbo](https://docs.comfy.org/es/built-in-nodes/SDTurboScheduler)
