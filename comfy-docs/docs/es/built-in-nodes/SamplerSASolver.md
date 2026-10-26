---
url: https://docs.comfy.org/es/built-in-nodes/SamplerSASolver/
title: Muestreador SA-Solver - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:27.833037+00:00
---

# Muestreador SA-Solver - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SamplerSASolver/

Samplers

# Muestreador SA-Solver - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SamplerSASolver crea y configura un sampler personalizado para modelos de difusión.

Copiar páginaCopiar página

El nodo SamplerSASolver crea y configura un sampler personalizado para modelos de difusión. Utiliza el algoritmo de muestreo `sa_solver` con un esquema predictor-corrector configurable y ajustes de ecuación diferencial estocástica (SDE), y devuelve un objeto sampler que se puede conectar a un nodo de muestreo. Los valores `sde_start_percent` y `sde_end_percent` se convierten en valores sigma usando el programa de muestreo del modelo conectado para definir el intervalo en el que se aplica el componente estocástico.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de difusión cuyo programa de muestreo se usa para construir el sampler| MODEL| Sí| -  
`eta`| Controla el factor de escala del tamaño de paso del solucionador SDE (predeterminado: 1.0)| FLOAT| No| 0.0 - 10.0  
`porcentaje_inicio_sde`| Porcentaje inicial del proceso de muestreo donde comienza el componente estocástico (SDE); se convierte en un valor sigma usando el programa del modelo (predeterminado: 0.2)| FLOAT| No| 0.0 - 1.0  
`porcentaje_fin_sde`| Porcentaje final del proceso de muestreo donde se detiene el componente estocástico (SDE); se convierte en un valor sigma usando el programa del modelo (predeterminado: 0.8)| FLOAT| No| 0.0 - 1.0  
`s_ruido`| Controla la cantidad de ruido añadido durante el muestreo (predeterminado: 1.0)| FLOAT| No| 0.0 - 100.0  
`orden_predictor`| El orden del componente predictor en el solucionador (predeterminado: 3)| INT| No| 1 - 6  
`orden_corrector`| El orden del componente corrector en el solucionador (predeterminado: 4)| INT| No| 0 - 6  
`usar_pece`| Habilita el método PECE (Predict-Evaluate-Correct-Evaluate) (predeterminado: deshabilitado)| BOOLEAN| No| -  
`orden_simple_2`| Habilita cálculos simplificados de segundo orden (predeterminado: deshabilitado)| BOOLEAN| No| -  
  
Todas las entradas opcionales están marcadas como avanzadas en la interfaz.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`sampler`| Un objeto sampler configurado (usando el algoritmo `sa_solver`) que pueden usar los nodos de muestreo| SAMPLER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/es.md)

* * *

**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SamplerSASolver.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SamplerSASolver)

[Muestreador LMS](https://docs.comfy.org/es/built-in-nodes/SamplerLMS)[Muestreador SEEDS2](https://docs.comfy.org/es/built-in-nodes/SamplerSEEDS2)
