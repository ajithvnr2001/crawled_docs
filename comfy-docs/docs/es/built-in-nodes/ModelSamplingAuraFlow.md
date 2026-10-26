---
url: https://docs.comfy.org/es/built-in-nodes/ModelSamplingAuraFlow/
title: Muestreo de modelo AuraFlow - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:14.539695+00:00
---

# Muestreo de modelo AuraFlow - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelSamplingAuraFlow/

Parches

# Muestreo de modelo AuraFlow - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ModelSamplingAuraFlow aplica una configuración de muestreo especializada a los modelos de difusión

Copiar páginaCopiar página

El nodo ModelSamplingAuraFlow aplica una configuración de muestreo especializada a los modelos de difusión, diseñada específicamente para arquitecturas de modelos AuraFlow. Modifica el comportamiento de muestreo del modelo aplicando un valor de desplazamiento que ajusta la distribución de muestreo. Este nodo hereda del framework de muestreo del modelo SD3 y proporciona un control preciso sobre el proceso de muestreo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| El modelo de difusión al que se aplica la configuración de muestreo de AuraFlow| MODEL| Sí| -  
`shift`| El valor de desplazamiento que se aplica a la distribución de muestreo (predeterminado: 1.73, paso: 0.01)| FLOAT| Sí| 0.0 - 100.0  
`sampling`| El modo de muestreo utilizado al parchear el modelo (predeterminado: “flow”). Marcado como opción avanzada.| COMBO| No| ”flow"  
"img_to_img_velocity”  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo modificado con la configuración de muestreo de AuraFlow aplicada| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/es.md)

* * *

**Source fingerprint (SHA-256):** `5c1381d2dec9ac84a7ee6cd134de444ab50f657eafd960263c63a055d0a139d6`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelSamplingAuraFlow.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelSamplingAuraFlow)

[Escala de Ruido del Modelo](https://docs.comfy.org/es/built-in-nodes/ModelNoiseScale)[Muestreo de modelo EDM continuo](https://docs.comfy.org/es/built-in-nodes/ModelSamplingContinuousEDM)
