---
url: https://docs.comfy.org/es/built-in-nodes/LTXVConditioning/
title: Acondicionamiento LTXV - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:01.143408+00:00
---

# Acondicionamiento LTXV - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LTXVConditioning/

Ltxv

# Acondicionamiento LTXV - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LTXVConditioning añade información de velocidad de fotogramas tanto a las entradas de condicionamiento positivo como negativo para modelos de

Copiar páginaCopiar página

El nodo LTXVConditioning añade información de velocidad de fotogramas tanto a las entradas de condicionamiento positivo como negativo para modelos de generación de video. Toma los datos de condicionamiento existentes y aplica el valor de velocidad de fotogramas especificado a ambos conjuntos de condicionamiento, haciéndolos adecuados para el procesamiento de modelos de video.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`positivo`| La entrada de condicionamiento positivo que recibirá la información de velocidad de fotogramas| CONDITIONING| Sí| -  
`negativo`| La entrada de condicionamiento negativo que recibirá la información de velocidad de fotogramas| CONDITIONING| Sí| -  
`tasa_fotogramas`| El valor de velocidad de fotogramas que se aplicará a ambos conjuntos de condicionamiento (predeterminado: 25.0)| FLOAT| Sí| 0.0 - 1000.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`positivo`| El condicionamiento positivo con la información de velocidad de fotogramas aplicada| CONDITIONING  
`negativo`| El condicionamiento negativo con la información de velocidad de fotogramas aplicada| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/es.md)

* * *

**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LTXVConditioning.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LTXVConditioning)

[LTXV Añadir guía latente](https://docs.comfy.org/es/built-in-nodes/LTXVAddLatentGuide)[Recortar guías LTXV](https://docs.comfy.org/es/built-in-nodes/LTXVCropGuides)
