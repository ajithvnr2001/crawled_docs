---
url: https://docs.comfy.org/es/built-in-nodes/UNetCrossAttentionMultiply/
title: Multiplicar atenci\u00f3n cruzada UNet - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:39.834625+00:00
---

# Multiplicar atención cruzada UNet - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/UNetCrossAttentionMultiply/

Experimentos de atención

# Multiplicar atención cruzada UNet - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo UNetCrossAttentionMultiply aplica factores de multiplicación al mecanismo de atención cruzada en un modelo UNet.

Copiar páginaCopiar página

El nodo UNetCrossAttentionMultiply aplica factores de multiplicación al mecanismo de atención cruzada en un modelo UNet. Permite escalar los componentes de consulta, clave, valor y salida de las capas de atención cruzada para experimentar con diferentes comportamientos y efectos de atención.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo UNet a modificar con factores de escala de atención| MODEL| Sí| -  
`q`| Factor de escala para componentes de consulta en atención cruzada (predeterminado: 1.0)| FLOAT| No| 0.0 - 10.0  
`k`| Factor de escala para componentes de clave en atención cruzada (predeterminado: 1.0)| FLOAT| No| 0.0 - 10.0  
`v`| Factor de escala para componentes de valor en atención cruzada (predeterminado: 1.0)| FLOAT| No| 0.0 - 10.0  
`salida`| Factor de escala para componentes de salida en atención cruzada (predeterminado: 1.0)| FLOAT| No| 0.0 - 10.0  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`modelo`| El modelo UNet modificado con componentes de atención cruzada escalados| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/es.md)

* * *

**Source fingerprint (SHA-256):** `2623858c11e93ab5952194670c9e4ea74bba4e2ea32089540665eea361dc1491`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/UNetCrossAttentionMultiply.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/UNetCrossAttentionMultiply)

[Multiplicar atención CLIP](https://docs.comfy.org/es/built-in-nodes/CLIPAttentionMultiply)[Multiplicar autoatención UNet](https://docs.comfy.org/es/built-in-nodes/UNetSelfAttentionMultiply)
