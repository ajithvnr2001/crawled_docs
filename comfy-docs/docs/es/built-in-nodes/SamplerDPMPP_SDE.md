---
url: https://docs.comfy.org/es/built-in-nodes/SamplerDPMPP_SDE/
title: Muestreador DPM++ SDE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:27.643356+00:00
---

# Muestreador DPM++ SDE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SamplerDPMPP_SDE/

Samplers

# Muestreador DPM++ SDE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

SamplerDPMPPSDE crea un sampler DPM++ SDE (ecuación diferencial estocástica) para usarlo en el proceso de muestreo.

Copiar páginaCopiar página

## 

​

Descripción general

SamplerDPMPP_SDE crea un sampler DPM++ SDE (Ecuación Diferencial Estocástica) para su uso en el proceso de muestreo. Este sampler proporciona un método de muestreo estocástico con parámetros de ruido configurables y selección de dispositivo. Devuelve un objeto sampler que se puede usar en el pipeline de muestreo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`eta`| Controla la estocasticidad del proceso de muestreo (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 100.0  
`s_ruido`| Controla la cantidad de ruido añadido durante el muestreo (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 100.0  
`r`| Un parámetro que influye en el comportamiento del muestreo (predeterminado: 0.5)| FLOAT| Sí| 0.0 - 100.0  
`dispositivo_ruido`| Selecciona el dispositivo donde se realizan los cálculos de ruido. Cuando se establece en “cpu”, se crea el sampler `dpmpp_sde`; cuando se establece en “gpu”, se crea el sampler `dpmpp_sde_gpu` (predeterminado: “gpu”)| COMBO| Sí| ”gpu"  
"cpu”  
  
Nota: Todas las entradas están marcadas como parámetros avanzados. La selección de `noise_device` cambia la variante de sampler que se crea: “cpu” corresponde a `dpmpp_sde` y “gpu” corresponde a `dpmpp_sde_gpu`.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`sampler`| Devuelve un objeto sampler DPM++ SDE configurado para su uso en pipelines de muestreo| SAMPLER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/es.md)

* * *

**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SamplerDPMPP_SDE.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SamplerDPMPP_SDE)

[Muestreador DPM++ 3M SDE](https://docs.comfy.org/es/built-in-nodes/SamplerDPMPP_3M_SDE)[Muestreador ER SDE](https://docs.comfy.org/es/built-in-nodes/SamplerER_SDE)
