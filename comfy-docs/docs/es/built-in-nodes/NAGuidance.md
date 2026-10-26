---
url: https://docs.comfy.org/es/built-in-nodes/NAGuidance/
title: Gu\u00eda de atenci\u00f3n normalizada - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:15.447515+00:00
---

# Guía de atención normalizada - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/NAGuidance/

Guía

# Guía de atención normalizada - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo NAGuidance aplica Orientación de Atención Normalizada a un modelo.

Copiar páginaCopiar página

El nodo NAGuidance aplica Orientación de Atención Normalizada a un modelo. Esta técnica permite el uso de prompts negativos con modelos destilados o schnell modificando el mecanismo de atención del modelo durante el proceso de muestreo para dirigir la generación lejos de conceptos no deseados.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo al que se aplicará Orientación de Atención Normalizada.| MODEL| Sí| -  
`escala_nag`| El factor de escala de orientación. Valores más altos empujan la generación más lejos del prompt negativo. (predeterminado: 5.0)| FLOAT| Sí| 0.0 - 50.0  
`nag_alpha`| El factor de mezcla para la atención normalizada. Un valor de 1.0 reemplaza completamente la atención original, mientras que 0.0 no tiene efecto. (predeterminado: 0.5)| FLOAT| Sí| 0.0 - 1.0  
`nag_tau`| Un factor de escala utilizado para limitar la relación de normalización. (predeterminado: 1.5)| FLOAT| Sí| 1.0 - 10.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo parcheado con Orientación de Atención Normalizada habilitada.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NAGuidance/es.md)

* * *

**Source fingerprint (SHA-256):** `42b4d601312dcbb1c934c6a79bbb5e9fd6598fa5f32b18f5c0affcb596672cba`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/NAGuidance.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/NAGuidance)

[LTXV Spatio-Temporal Guidance (STG)](https://docs.comfy.org/es/built-in-nodes/LTXVSpatioTemporalGuidance)[Guía saltar capa DiT](https://docs.comfy.org/es/built-in-nodes/SkipLayerGuidanceDiT)
