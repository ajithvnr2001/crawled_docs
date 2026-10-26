---
url: https://docs.comfy.org/es/built-in-nodes/SetFirstSigma/
title: Establecer primera sigma - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:30.817086+00:00
---

# Establecer primera sigma - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SetFirstSigma/

Sigmas

# Establecer primera sigma - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SetFirstSigma modifica una secuencia sigma reemplazando solo su primer valor con un valor sigma personalizado.

Copiar páginaCopiar página

El nodo SetFirstSigma modifica una secuencia sigma reemplazando solo su primer valor con un valor sigma personalizado. Toma una secuencia sigma existente y un nuevo valor sigma, y devuelve una nueva secuencia sigma donde todos los valores excepto el primero permanecen sin cambios.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`sigmas`| La secuencia de entrada de valores sigma que se va a modificar| SIGMAS| Sí| -  
`sigma`| El nuevo valor sigma que se establecerá como primer elemento de la secuencia (por defecto: 136.0)| FLOAT| Sí| 0.0 a 20000.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`sigmas`| La secuencia sigma modificada con el primer elemento reemplazado por el valor sigma personalizado| SIGMAS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/es.md)

* * *

**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SetFirstSigma.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SetFirstSigma)

[Porcentaje de muestreo a sigma](https://docs.comfy.org/es/built-in-nodes/SamplingPercentToSigma)[Dividir sigmas](https://docs.comfy.org/es/built-in-nodes/SplitSigmas)
