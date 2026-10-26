---
url: https://docs.comfy.org/es/built-in-nodes/SamplerSEEDS2/
title: Muestreador SEEDS2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:28.024756+00:00
---

# Muestreador SEEDS2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SamplerSEEDS2/

Samplers

# Muestreador SEEDS2 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo proporciona un muestreador configurable para la generación de imágenes.

Copiar páginaCopiar página

Este nodo proporciona un muestreador configurable para la generación de imágenes. Está basado en un solucionador de ecuaciones diferenciales estocásticas (SDE) y puede comportarse como varios muestreadores específicos según su configuración, incluidos `seeds_2`, `exp_heun_2_x0` y `exp_heun_2_x0_sde`.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`solver_type`| Selecciona el algoritmo de solucionador subyacente para el muestreador.| COMBO| Sí| ”phi_1"  
"phi_2”  
`eta`| Intensidad estocástica (predeterminado: 1.0).| FLOAT| No| 0.0 - 100.0  
`s_noise`| Multiplicador de ruido SDE (predeterminado: 1.0).| FLOAT| No| 0.0 - 100.0  
`r`| Tamaño de paso relativo para la etapa intermedia (nodo c2) (predeterminado: 0.5).| FLOAT| No| 0.01 - 1.0  
  
**Nota:** La descripción del nodo define los siguientes preajustes de muestreador:

  * `seeds_2`: ajustes predeterminados
  * `exp_heun_2_x0`: `solver_type` = “phi_2”, `r` = 1.0, `eta` = 0.0
  * `exp_heun_2_x0_sde`: `solver_type` = “phi_2”, `r` = 1.0, `eta` = 1.0, `s_noise` = 1.0



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`sampler`| Un objeto muestreador configurado que se puede pasar a otros nodos de muestreo.| SAMPLER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/es.md)

* * *

**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SamplerSEEDS2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SamplerSEEDS2)

[Muestreador SA-Solver](https://docs.comfy.org/es/built-in-nodes/SamplerSASolver)[VOIDSampler](https://docs.comfy.org/es/built-in-nodes/VOIDSampler)
