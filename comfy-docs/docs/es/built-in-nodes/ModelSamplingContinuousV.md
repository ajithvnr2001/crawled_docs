---
url: https://docs.comfy.org/es/built-in-nodes/ModelSamplingContinuousV/
title: Muestreo de modelo V continuo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:14.905632+00:00
---

# Muestreo de modelo V continuo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelSamplingContinuousV/

Parches

# Muestreo de modelo V continuo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ModelSamplingContinuousV ajusta el comportamiento de muestreo de un modelo aplicando muestreo de predicción V continua.

Copiar páginaCopiar página

El nodo ModelSamplingContinuousV ajusta el comportamiento de muestreo de un modelo aplicando muestreo de predicción V continua. Crea un clon del modelo de entrada y lo configura con valores sigma mínimos y máximos personalizados para un control más preciso sobre el proceso de muestreo.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`model`| El modelo de entrada que se modificará con muestreo de predicción V continua| MODEL| Sí| -  
`muestreo`| El método de muestreo a aplicar; actualmente la predicción V es la única opción disponible (predeterminado: `"v_prediction"`)| COMBO| Sí| `"v_prediction"`  
`sigma_max`| El valor sigma máximo para el muestreo (parámetro avanzado, predeterminado: 500.0)| FLOAT| Sí| 0.0 - 1000.0  
`sigma_min`| El valor sigma mínimo para el muestreo (parámetro avanzado, predeterminado: 0.03)| FLOAT| Sí| 0.0 - 1000.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`model`| El modelo modificado con muestreo de predicción V continua aplicado| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/es.md)

* * *

**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelSamplingContinuousV.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelSamplingContinuousV)

[Muestreo de modelo EDM continuo](https://docs.comfy.org/es/built-in-nodes/ModelSamplingContinuousEDM)[Muestreo de modelo discreto](https://docs.comfy.org/es/built-in-nodes/ModelSamplingDiscrete)
