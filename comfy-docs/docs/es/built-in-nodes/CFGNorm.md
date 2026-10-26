---
url: https://docs.comfy.org/es/built-in-nodes/CFGNorm/
title: Normalizaci\u00f3n CFG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:35.935178+00:00
---

# Normalización CFG - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CFGNorm/

Guía

# Normalización CFG - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

CFGNorm ajusta cómo se aplica la guía libre de clasificador (CFG) en modelos de difusión al comparar el tamaño (norma) de la predicción condicional con la

Copiar páginaCopiar página

CFGNorm ajusta cómo se aplica la guía libre de clasificador (CFG) en modelos de difusión al comparar el tamaño (norma) de la predicción condicional con la predicción guiada y reescalar el resultado. Un valor de `strength` controla cuánto del ajuste se aplica. De forma predeterminada, el escalado solo atenúa la salida de la guía, mientras que habilitar `pre_cfg` hace que se reescale el ruido combinado antes de la combinación CFG del muestreador, sin limitación, lo que puede amplificar el resultado.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo de difusión al que se aplicará la normalización CFG| MODEL| Sí| -  
`intensidad`| Controla la intensidad del efecto de normalización aplicado al escalado de CFG (predeterminado: 1.0)| FLOAT| Sí| 0.0 a 100.0 (paso 0.01)  
`pre_cfg`| Si es verdadero, reescala el ruido combinado ANTES de la combinación CFG del muestreador, sin limitación (puede amplificar). Coincide con la CFG escalada por norma que usan modelos como Lens. El valor predeterminado (falso) conserva el comportamiento original posterior a CFG en el espacio x0, de solo atenuación. (predeterminado: falso)| BOOLEAN| No| true / false  
  
Nota: Este nodo está marcado como experimental.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`patched_model`| Devuelve el modelo modificado con la normalización CFG aplicada a su proceso de muestreo| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/es.md)

* * *

**Source fingerprint (SHA-256):** `427dda498ebda2642489aa2591f063355a77b1e064e0dc7fa8570ed8200c2734`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CFGNorm.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CFGNorm)

[Tipo de dato de cómputo del modelo](https://docs.comfy.org/es/built-in-nodes/ModelComputeDtype)[CFGZeroStar](https://docs.comfy.org/es/built-in-nodes/CFGZeroStar)
