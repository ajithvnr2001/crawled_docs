---
url: https://docs.comfy.org/es/built-in-nodes/KSamplerSelect/
title: Seleccionar KSampler - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:58.709759+00:00
---

# Seleccionar KSampler - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/KSamplerSelect/

Samplers

# Seleccionar KSampler - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo KSamplerSelect está diseñado para seleccionar un muestreador específico basado en el nombre proporcionado.

Copiar páginaCopiar página

El nodo KSamplerSelect está diseñado para seleccionar un muestreador específico basado en el nombre proporcionado. Abstrae la complejidad de la selección del muestreador, permitiendo a los usuarios cambiar fácilmente entre diferentes estrategias de muestreo para sus tareas.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`nombre_del_muestreador`| Especifica el nombre del muestreador a seleccionar. Este parámetro determina qué estrategia de muestreo se utilizará, afectando el comportamiento general del muestreo y los resultados.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`sampler`| Devuelve el objeto muestreador seleccionado, listo para ser utilizado en tareas de muestreo.| `SAMPLER`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/KSamplerSelect.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/KSamplerSelect)

[Ruido aleatorio](https://docs.comfy.org/es/built-in-nodes/RandomNoise)[Muestreador de video autorregresivo](https://docs.comfy.org/es/built-in-nodes/SamplerARVideo)
