---
url: https://docs.comfy.org/es/built-in-nodes/ThresholdMask/
title: Umbralizar m\u00e1scara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:36.395396+00:00
---

# Umbralizar máscara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ThresholdMask/

Máscara

# Umbralizar máscara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ThresholdMask convierte una máscara en una máscara binaria aplicando un valor de umbral.

Copiar páginaCopiar página

El nodo ThresholdMask convierte una máscara en una máscara binaria aplicando un valor de umbral. Compara cada píxel de la máscara de entrada con el valor de umbral especificado y crea una nueva máscara donde los píxeles por encima del umbral se convierten en 1 (blanco) y los píxeles iguales o por debajo del umbral se convierten en 0 (negro).

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`máscara`| La máscara de entrada que se procesará| MASK| Sí| -  
`valor`| El valor de umbral para la binarización (predeterminado: 0.5)| FLOAT| Sí| 0.0 - 1.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`máscara`| La máscara binaria resultante después de aplicar el umbral| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/es.md)

* * *

**Source fingerprint (SHA-256):** `5c61433c05ef8106d928306b64035078e7598605512f20aaf992255f7b166456`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ThresholdMask.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ThresholdMask)

[Máscara sólida](https://docs.comfy.org/es/built-in-nodes/SolidMask)[VOIDQuadmaskPreprocess](https://docs.comfy.org/es/built-in-nodes/VOIDQuadmaskPreprocess)
