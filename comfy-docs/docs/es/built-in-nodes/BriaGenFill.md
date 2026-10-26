---
url: https://docs.comfy.org/es/built-in-nodes/BriaGenFill/
title: Relleno generativo de Bria - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:32.821437+00:00
---

# Relleno generativo de Bria - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BriaGenFill/

Bria

# Relleno generativo de Bria - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo genera objetos o escenarios dentro de una región enmascarada de una imagen usando Bria.

Copiar páginaCopiar página

Este nodo genera objetos o escenarios dentro de una región enmascarada de una imagen usando Bria. Carga la imagen y la máscara, envía el prompt al servicio de relleno generativo de Bria, espera a que finalice la operación y devuelve la imagen editada. Esta es una operación de API de pago (US$0.0429 por solicitud).

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`image`| La imagen de entrada que se va a editar.| IMAGE| Sí| -  
`mask`| Las áreas blancas se rellenan con contenido generado; las áreas negras se conservan. La máscara se binariza antes de enviarla con un umbral del 50%: solo las áreas pintadas con más del 50% de opacidad cuentan como blancas. Debe tener la misma relación de aspecto que la imagen.| MASK| Sí| -  
`prompt`| Descripción de lo que se debe generar dentro de la región enmascarada. Debe contener al menos 1 carácter. (predeterminado: "")| STRING| Sí| -  
`negative_prompt`| Un prompt que describe el contenido que se debe evitar en el resultado generado. Si se deja vacío, no se envía a la API. (predeterminado: "")| STRING| Sí| -  
`refine_prompt`| Ajusta automáticamente el prompt para obtener mejores resultados; desactívalo para usar el prompt exactamente como se escribió. (predeterminado: true)| BOOLEAN| Sí| true  
false  
`seed`| Semilla para el proceso de generación. (predeterminado: 42)| INT| Sí| 1 a 2147483647  
`moderación`| Configuración de moderación. Cuando se establece en “true”, se aplican las opciones de moderación a continuación. (predeterminado: “false”)| DYNAMIC_COMBO| Sí| ”false"  
"true”  
  
### 

​

Entradas de moderación (cuando `moderation` = “true”)

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt_content_moderation`| Aplica moderación de contenido al prompt. (predeterminado: false)| BOOLEAN| No| true  
false  
`visual_input_moderation`| Aplica moderación de contenido a la imagen de entrada. (predeterminado: false)| BOOLEAN| No| true  
false  
`visual_output_moderation`| Aplica moderación de contenido a la imagen de salida. (predeterminado: false)| BOOLEAN| No| true  
false  
  
**Nota:** El `prompt` no debe estar vacío. La `mask` debe tener la misma relación de aspecto que la `image`. La máscara se binariza al 50% de opacidad, por lo que las áreas pintadas con menos de la mitad de opacidad se ignoran; si la máscara no contiene áreas blancas después de la binarización, el nodo genera un error.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| La imagen resultante con la región enmascarada rellenada por el contenido generado.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/es.md)

* * *

**Source fingerprint (SHA-256):** `b23e29d4457f859181d68eaeb4b0238de28f4b18932d68438fa2954739cdc66a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BriaGenFill.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BriaGenFill)

[Ampliar imagen con Bria](https://docs.comfy.org/es/built-in-nodes/BriaExpandImage)[Bria FIBO 2.0 Image Edit](https://docs.comfy.org/es/built-in-nodes/BriaImageEditNode)
