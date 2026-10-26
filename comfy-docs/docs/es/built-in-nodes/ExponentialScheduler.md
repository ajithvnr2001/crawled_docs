---
url: https://docs.comfy.org/es/built-in-nodes/ExponentialScheduler/
title: Programador exponencial - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:46.452960+00:00
---

# Programador exponencial - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ExponentialScheduler/

Programadores

# Programador exponencial - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ExponentialScheduler está diseñado para generar una secuencia de valores sigma siguiendo un programa exponencial para procesos de muestreo por

Copiar páginaCopiar página

El nodo `ExponentialScheduler` está diseñado para generar una secuencia de valores sigma siguiendo un programa exponencial para procesos de muestreo por difusión. Proporciona un enfoque personalizable para controlar los niveles de ruido aplicados en cada paso del proceso de difusión, permitiendo un ajuste fino del comportamiento del muestreo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`pasos`| Especifica el número de pasos en el proceso de difusión. Influye en la longitud de la secuencia sigma generada y, por lo tanto, en la granularidad de la aplicación del ruido.| INT  
`sigma_max`| Define el valor sigma máximo, estableciendo el límite superior de intensidad de ruido en el proceso de difusión. Desempeña un papel crucial en la determinación del rango de niveles de ruido aplicados.| FLOAT  
`sigma_min`| Establece el valor sigma mínimo, fijando el límite inferior de intensidad de ruido. Este parámetro ayuda a ajustar el punto de inicio de la aplicación del ruido.| FLOAT  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`sigmas`| Una secuencia de valores sigma generados según el programa exponencial. Estos valores se utilizan para controlar los niveles de ruido en cada paso del proceso de difusión.| SIGMAS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExponentialScheduler/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ExponentialScheduler.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ExponentialScheduler)

[Programador de muestreo beta](https://docs.comfy.org/es/built-in-nodes/BetaSamplingScheduler)[Programador Flux 2](https://docs.comfy.org/es/built-in-nodes/Flux2Scheduler)
