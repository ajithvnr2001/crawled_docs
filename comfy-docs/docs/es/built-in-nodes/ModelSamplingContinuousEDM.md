---
url: https://docs.comfy.org/es/built-in-nodes/ModelSamplingContinuousEDM/
title: Muestreo de modelo EDM continuo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:14.682291+00:00
---

# Muestreo de modelo EDM continuo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelSamplingContinuousEDM/

Parches

# Muestreo de modelo EDM continuo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para mejorar las capacidades de muestreo de un modelo mediante la integración de técnicas continuas de muestreo EDM (Modelos de

Copiar páginaCopiar página

Este nodo está diseñado para mejorar las capacidades de muestreo de un modelo mediante la integración de técnicas continuas de muestreo EDM (Modelos de Difusión Basados en Energía). Permite el ajuste dinámico de los niveles de ruido dentro del proceso de muestreo del modelo, ofreciendo un control más refinado sobre la calidad y diversidad de la generación.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Tipo Python  
---|---|---|---  
`model`| El modelo a mejorar con capacidades continuas de muestreo EDM. Sirve como base para aplicar las técnicas avanzadas de muestreo.| `MODEL`| `torch.nn.Module`  
`muestreo`| Especifica el tipo de muestreo a aplicar, ya sea ‘eps’ para muestreo épsilon o ‘v_prediction’ para predicción de velocidad, influyendo en el comportamiento del modelo durante el proceso de muestreo.| COMBO[STRING]| `str`  
`sigma_max`| El valor sigma máximo para el nivel de ruido, permitiendo un control del límite superior en el proceso de inyección de ruido durante el muestreo.| `FLOAT`| `float`  
`sigma_min`| El valor sigma mínimo para el nivel de ruido, estableciendo el límite inferior para la inyección de ruido, afectando así la precisión del muestreo del modelo.| `FLOAT`| `float`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato| Tipo Python  
---|---|---|---  
`model`| El modelo mejorado con capacidades integradas de muestreo EDM continuo, listo para su uso posterior en tareas de generación.| MODEL| `torch.nn.Module`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelSamplingContinuousEDM.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelSamplingContinuousEDM)

[Muestreo de modelo AuraFlow](https://docs.comfy.org/es/built-in-nodes/ModelSamplingAuraFlow)[Muestreo de modelo V continuo](https://docs.comfy.org/es/built-in-nodes/ModelSamplingContinuousV)
