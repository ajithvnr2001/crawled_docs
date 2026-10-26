---
url: https://docs.comfy.org/es/built-in-nodes/UNetTemporalAttentionMultiply/
title: Multiplicar atenci\u00f3n temporal UNet - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:39.771772+00:00
---

# Multiplicar atención temporal UNet - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/UNetTemporalAttentionMultiply/

Experimentos de atención

# Multiplicar atención temporal UNet - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo UNetTemporalAttentionMultiply aplica factores de multiplicación a diferentes tipos de mecanismos de atención en un modelo UNet temporal.

Copiar páginaCopiar página

El nodo UNetTemporalAttentionMultiply aplica factores de multiplicación a diferentes tipos de mecanismos de atención en un modelo UNet temporal. Modifica el modelo ajustando los pesos de las capas de autoatención y atención cruzada, distinguiendo entre componentes estructurales y temporales. Esto permite ajustar con precisión cuánta influencia tiene cada tipo de atención en la salida del modelo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de entrada a modificar con multiplicadores de atención| MODEL| Sí| -  
`auto_estructural`| Multiplicador para componentes estructurales de autoatención (predeterminado: 1.0)| FLOAT| No| 0.0 - 10.0  
`auto_temporal`| Multiplicador para componentes temporales de autoatención (predeterminado: 1.0)| FLOAT| No| 0.0 - 10.0  
`cruz_estructural`| Multiplicador para componentes estructurales de atención cruzada (predeterminado: 1.0)| FLOAT| No| 0.0 - 10.0  
`cruz_temporal`| Multiplicador para componentes temporales de atención cruzada (predeterminado: 1.0)| FLOAT| No| 0.0 - 10.0  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`modelo`| El modelo modificado con pesos de atención ajustados| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/es.md)

* * *

**Source fingerprint (SHA-256):** `98d62fb28a0cdf62154ae4e0b672b3a7bcb9ed61186a164a43992263c1f9439a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/UNetTemporalAttentionMultiply.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/UNetTemporalAttentionMultiply)

[Multiplicar autoatención UNet](https://docs.comfy.org/es/built-in-nodes/UNetSelfAttentionMultiply)[Super resolución ControlNet Stable Cascade](https://docs.comfy.org/es/built-in-nodes/StableCascade_SuperResolutionControlnet)
