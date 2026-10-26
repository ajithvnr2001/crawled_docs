---
url: https://docs.comfy.org/es/built-in-nodes/ReveImageCreateNode/
title: Reve crear imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:24.355312+00:00
---

# Reve crear imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ReveImageCreateNode/

Reve

# Reve crear imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Reve Image Create genera imágenes a partir de una descripción textual usando el modelo Reve AI.

Copiar páginaCopiar página

El nodo Reve Image Create genera imágenes a partir de una descripción textual usando el modelo Reve AI. Envía el prompt a la API de Reve y devuelve la imagen resultante, con postprocesamiento opcional para escalado y eliminación de fondo. Este nodo está obsoleto.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| Versión del modelo que se usará para la generación.| DYNAMIC_COMBO| Sí| `"reve-create@20250915"`  
`prompt`| Descripción textual de la imagen deseada. Máximo 2560 caracteres. Valor predeterminado: "" (vacío).| STRING| Sí| 1 a 2560 caracteres  
`escalar`| Amplía la imagen generada. Puede agregar un costo adicional. Valor predeterminado: “disabled”.| DYNAMIC_COMBO| No| `"disabled"`  
`"enabled"`  
`eliminar_fondo`| Elimina el fondo de la imagen generada. Puede agregar un costo adicional. Valor predeterminado: False.| BOOLEAN| No| N/A  
`semilla`| La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Valor predeterminado: 0.| INT| No| 0 a 2147483647  
  
### 

​

Entradas de reve-create@20250915

Opciones disponibles cuando `model` se establece en `"reve-create@20250915"`:

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`aspect_ratio`| Relación de aspecto de la imagen de salida.| COMBO| Sí| `"3:2"`  
`"16:9"`  
`"9:16"`  
`"2:3"`  
`"4:3"`  
`"3:4"`  
`"1:1"`  
`test_time_scaling`| Los valores más altos producen mejores imágenes, pero cuestan más créditos. Valor predeterminado: 1. Opción avanzada.| INT| No| 1 a 5  
  
### 

​

Entradas de escalado

Opciones disponibles cuando `upscale` se establece en `"enabled"`:

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`upscale_factor`| Factor de escalado (2x, 3x o 4x). Valor predeterminado: 2.| INT| No| 2 a 4  
  
**Nota:** El `prompt` debe contener entre 1 y 2560 caracteres. La entrada `upscale_factor` solo aparece cuando `upscale` se establece en `"enabled"`. El parámetro `seed` no garantiza salidas deterministas; los resultados no son deterministas independientemente del valor de la semilla. Tanto `upscale` como `remove_background` pueden agregar un costo adicional.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| La imagen generada por el modelo Reve basándose en el prompt de entrada.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/es.md)

* * *

**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ReveImageCreateNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ReveImageCreateNode)

[Recraft vectorizar imagen](https://docs.comfy.org/es/built-in-nodes/RecraftVectorizeImageNode)[Reve editar imagen](https://docs.comfy.org/es/built-in-nodes/ReveImageEditNode)
