---
url: https://docs.comfy.org/es/built-in-nodes/LoadDA3Model/
title: Cargar Depth Anything 3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:04.835772+00:00
---

# Cargar Depth Anything 3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadDA3Model/

Cargadores

# Cargar Depth Anything 3 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo carga un modelo Depth Anything 3 desde un archivo, preparándolo para su uso en tareas de estimación de profundidad.

Copiar páginaCopiar página

Este nodo carga un modelo Depth Anything 3 desde un archivo, preparándolo para su uso en tareas de estimación de profundidad. Permite seleccionar el archivo del modelo y, opcionalmente, especificar la precisión numérica (tipo de dato) para los pesos del modelo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`model_name`| El nombre del archivo del modelo Depth Anything 3 a cargar.| STRING| Sí| Lista de archivos de modelo disponibles en la carpeta `geometry_estimation`  
`weight_dtype`| La precisión numérica (tipo de dato) para los pesos del modelo. “default” utiliza la precisión original del modelo, “fp16” utiliza punto flotante de 16 bits, “bf16” utiliza bfloat16 y “fp32” utiliza punto flotante de 32 bits. (predeterminado: “default”)| STRING| No| `"default"`  
`"fp16"`  
`"bf16"`  
`"fp32"`  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`DA3_MODEL`| El modelo Depth Anything 3 cargado, listo para usar en flujos de trabajo de estimación de profundidad.| DA3_MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadDA3Model/es.md)

* * *

**Source fingerprint (SHA-256):** `b1b3f4075cd9172bc1f274848b9300bca20d3cbd53b23d3c4a9f0986b36e409e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadDA3Model.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadDA3Model)

[Cargar modelo de eliminación de fondo](https://docs.comfy.org/es/built-in-nodes/LoadBackgroundRemovalModel)[Cargar LoRA (modelo)](https://docs.comfy.org/es/built-in-nodes/LoadLoraModel)
