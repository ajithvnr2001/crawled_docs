---
url: https://docs.comfy.org/es/built-in-nodes/LatentOperationBlend/
title: Mezcla de operaci\u00f3n latent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:03.537452+00:00
---

# Mezcla de operación latent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentOperationBlend/

Operaciones

# Mezcla de operación latent - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo crea una operación sobre latentes que mezcla un latente hacia un latente de referencia

Copiar páginaCopiar página

Este nodo crea una operación sobre latentes que mezcla un latente hacia un latente de referencia, y devuelve esa operación para que pueda conectarse en nodos como Latent Apply Operation o Latent Apply Operation CFG. Cuando la referencia tiene un tamaño espacial diferente, se redimensiona al latente objetivo con interpolación de vecino más cercano, y una referencia con un lote más pequeño se repite para coincidir con el tamaño de lote objetivo. Una fuerza de 0 deja el latente sin cambios. Este nodo está marcado como experimental.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`reference`| El latente hacia el que se mezcla. Sus muestras se convierten al dispositivo y dtype del latente que se está procesando, y luego se redimensionan y repiten para coincidir con él.| LATENT| Sí| -  
`strength`| Cuánto mezclar hacia la referencia: 0 deja el latente sin cambios, 1 iguala el latente de referencia redimensionado (predeterminado: 1.0).| FLOAT| Sí| 0.0 a 1.0 (paso 0.0001)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`operation`| Una operación de mezcla que se puede aplicar a muestras de latente.| LATENT_OPERATION  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationBlend/es.md)

* * *

**Source fingerprint (SHA-256):** `5890089afddf83ddd4edd992606509b118aac9ef13eb89589f73fa75e0b9dd5a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentOperationBlend.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentOperationBlend)

[Aplicar operación CFG a latente](https://docs.comfy.org/es/built-in-nodes/LatentApplyOperationCFG)[Operación de enfoque de latente](https://docs.comfy.org/es/built-in-nodes/LatentOperationSharpen)
