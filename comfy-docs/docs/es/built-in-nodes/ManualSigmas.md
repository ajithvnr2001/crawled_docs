---
url: https://docs.comfy.org/es/built-in-nodes/ManualSigmas/
title: Sigmas manuales - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:09.042512+00:00
---

# Sigmas manuales - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ManualSigmas/

Sigmas

# Sigmas manuales - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ManualSigmas te permite definir manualmente una secuencia personalizada de niveles de ruido (sigmas) para el proceso de muestreo.

Copiar páginaCopiar página

El nodo ManualSigmas te permite definir manualmente una secuencia personalizada de niveles de ruido (sigmas) para el proceso de muestreo. Ingresas una lista de números como una cadena de texto, y el nodo los convierte en un tensor SIGMAS que puede ser utilizado por otros nodos de muestreo. Esto es útil para realizar pruebas o crear programaciones de ruido específicas.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`sigmas`| Una cadena de texto que contiene los valores sigma. El nodo extrae todos los números de esta cadena, incluidos los decimales y los valores negativos. Por ejemplo, “1, 0.5, 0.1” o “1 0.5 0.1”. Valor predeterminado: “1, 0.5”.| STRING| Sí| Cualquier valor numérico separado por comas o espacios  
  
Nota: Este nodo está marcado como experimental.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`sigmas`| Un tensor que contiene la secuencia de valores sigma extraídos de la cadena de entrada.| SIGMAS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ManualSigmas/es.md)

* * *

**Source fingerprint (SHA-256):** `19d938ef0eac7343a3138393a039f63632b0763e3884636653c06b91b6f44ed6`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ManualSigmas.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ManualSigmas)

[Invertir sigmas](https://docs.comfy.org/es/built-in-nodes/FlipSigmas)[Porcentaje de muestreo a sigma](https://docs.comfy.org/es/built-in-nodes/SamplingPercentToSigma)
