---
url: https://docs.comfy.org/es/built-in-nodes/CLIPAttentionMultiply/
title: Multiplicar atenci\u00f3n CLIP - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:36.343940+00:00
---

# Multiplicar atención CLIP - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CLIPAttentionMultiply/

Experimentos de atención

# Multiplicar atención CLIP - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CLIPAttentionMultiply permite ajustar el mecanismo de atención en modelos CLIP aplicando factores de multiplicación a diferentes componentes de las

Copiar páginaCopiar página

El nodo `CLIPAttentionMultiply` permite ajustar el mecanismo de atención en modelos CLIP aplicando factores de multiplicación a diferentes componentes de las capas de autoatención. Funciona modificando los pesos y sesgos de las proyecciones de consulta, clave, valor y salida en el mecanismo de atención del modelo CLIP. Este nodo experimental crea una copia modificada del modelo CLIP de entrada con los factores de escala especificados aplicados.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP a modificar| CLIP| Sí| -  
`q`| Factor de multiplicación para los pesos y sesgos de la proyección de consulta (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 10.0  
`k`| Factor de multiplicación para los pesos y sesgos de la proyección de clave (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 10.0  
`v`| Factor de multiplicación para los pesos y sesgos de la proyección de valor (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 10.0  
`salida`| Factor de multiplicación para los pesos y sesgos de la proyección de salida (predeterminado: 1.0)| FLOAT| Sí| 0.0 - 10.0  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`CLIP`| Devuelve un modelo CLIP modificado con los factores de escala de atención especificados aplicados| CLIP  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/es.md)

* * *

**Source fingerprint (SHA-256):** `43dab83ecfc928f3359eb7560658f43235bf3faa62c81084a2b4f482e3a4638f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CLIPAttentionMultiply.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CLIPAttentionMultiply)

[Acondicionamiento (Promediar)](https://docs.comfy.org/es/built-in-nodes/ConditioningAverage)[Multiplicar atención cruzada UNet](https://docs.comfy.org/es/built-in-nodes/UNetCrossAttentionMultiply)
