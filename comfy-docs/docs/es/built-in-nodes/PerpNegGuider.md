---
url: https://docs.comfy.org/es/built-in-nodes/PerpNegGuider/
title: Gu\u00eda PerpNeg - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:17.202800+00:00
---

# Guía PerpNeg - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PerpNegGuider/

Experimental

# Guía PerpNeg - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo PerpNegGuider crea un sistema de guía para controlar la generación de imágenes mediante condicionamiento negativo perpendicular.

Copiar páginaCopiar página

El nodo PerpNegGuider crea un sistema de guía para controlar la generación de imágenes mediante condicionamiento negativo perpendicular. Toma entradas de condicionamiento positivo, negativo y vacío, y aplica un algoritmo de guía especializado para dirigir el proceso de generación. Este nodo está diseñado para pruebas experimentales y proporciona un control preciso sobre la intensidad de la guía y la escala negativa.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo a utilizar para la generación de guía| MODEL| Sí| -  
`positivo`| El condicionamiento positivo que dirige la generación hacia el contenido deseado| CONDITIONING| Sí| -  
`negativo`| El condicionamiento negativo que aleja la generación del contenido no deseado| CONDITIONING| Sí| -  
`condicionamiento_vacío`| El condicionamiento vacío o neutral utilizado como referencia base| CONDITIONING| Sí| -  
`cfg`| La escala de guía libre de clasificador que controla la intensidad con la que el condicionamiento influye en la generación (predeterminado: 8.0)| FLOAT| Sí| 0.0 - 100.0  
`escala_neg`| El factor de escala negativa que ajusta la intensidad del condicionamiento negativo (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 100.0  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`guider`| Un sistema de guía configurado listo para usar en el proceso de generación| GUIDER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/es.md)

* * *

**Source fingerprint (SHA-256):** `efd3f78d461ade9d16885923875bacffb5afeafcbe32fc2d207598e0efe3a8c6`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PerpNegGuider.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PerpNegGuider)

[Perp-Neg (obsoleto; usar la guía Perp-Neg)](https://docs.comfy.org/es/built-in-nodes/PerpNeg)[SamplerEulerCFG++](https://docs.comfy.org/es/built-in-nodes/SamplerEulerCFGpp)
