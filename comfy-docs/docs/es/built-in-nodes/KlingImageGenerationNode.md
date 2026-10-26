---
url: https://docs.comfy.org/es/built-in-nodes/KlingImageGenerationNode/
title: Generaci\u00f3n de im\u00e1genes Kling - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:59.176919+00:00
---

# Generación de imágenes Kling - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/KlingImageGenerationNode/

Kling

# Generación de imágenes Kling - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Kling Image Generation genera imágenes a partir de prompts de texto con la opción de usar una imagen de referencia como guía.

Copiar páginaCopiar página

El nodo Kling Image Generation genera imágenes a partir de prompts de texto con la opción de usar una imagen de referencia como guía. Crea una o más imágenes basadas en la descripción de texto y la configuración de referencia, y luego devuelve las imágenes generadas como salida.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Prompt de texto positivo. Obligatorio; debe tener entre 1 y 500 caracteres.| STRING| Sí| Máximo 500 caracteres  
`negative_prompt`| Prompt de texto negativo.| STRING| Sí| Máximo 500 caracteres  
`image_type`| Selección del tipo de referencia de imagen (avanzado). Obligatorio cuando se proporciona una imagen de referencia.| COMBO| Sí| `"subject_reference"`  
`"style_reference"`  
`image_fidelity`| Intensidad de referencia para imágenes cargadas por el usuario (predeterminado: 0.5, avanzado)| FLOAT| Sí| 0.0 - 1.0  
`human_fidelity`| Similitud de referencia del sujeto (predeterminado: 0.45, avanzado)| FLOAT| Sí| 0.0 - 1.0  
`model_name`| Selección de modelo para la generación de imágenes (predeterminado: “kling-v3”)| COMBO| Sí| `"kling-v3"`  
`aspect_ratio`| Relación de aspecto para las imágenes generadas (predeterminado: “16:9”)| COMBO| Sí| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`"21:9"`  
`"9:21"`  
`n`| Número de imágenes generadas (predeterminado: 1)| INT| Sí| 1 - 9  
`image`| Imagen de referencia opcional| IMAGE| No| -  
`semilla`| La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0)| INT| No| 0 - 2147483647  
  
**Restricciones de los parámetros:**

  * El parámetro `image` es opcional. Cuando se proporciona una imagen de referencia, el parámetro `image_type` determina si la referencia se usa como referencia de sujeto o referencia de estilo.
  * Cuando no se proporciona una imagen de referencia, la configuración relacionada con la referencia (`image_type`, `image_fidelity`, `human_fidelity`) no tiene efecto en el resultado.
  * `prompt` y `negative_prompt` tienen una longitud máxima de 500 caracteres.
  * El parámetro `seed` es opcional y no garantiza resultados deterministas.
  * El parámetro `n` controla cuántas imágenes se producen y también determina el precio de la solicitud.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| Imagen(es) generada(s) según los parámetros de entrada. Cuando `n` es mayor que 1, se devuelven varias imágenes como un lote.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/es.md)

* * *

**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/KlingImageGenerationNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/KlingImageGenerationNode)

[Ideogram V4](https://docs.comfy.org/es/built-in-nodes/IdeogramV4)[Kling Omni imagen (Pro)](https://docs.comfy.org/es/built-in-nodes/KlingOmniProImageNode)
