---
url: https://docs.comfy.org/es/built-in-nodes/HappyHorseVideoEditApi/
title: HappyHorse Edici\u00f3n de Video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:52.645988+00:00
---

# HappyHorse Edición de Video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HappyHorseVideoEditApi/

Wan

# HappyHorse Edición de Video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Edita un vídeo mediante instrucciones de texto o imágenes de referencia con el modelo HappyHorse.

Copiar páginaCopiar página

Edita un vídeo mediante instrucciones de texto o imágenes de referencia con el modelo HappyHorse. La duración de salida es de 3 a 15 segundos y coincide con el vídeo de entrada; los vídeos de más de 15 segundos se recortan.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo de edición de vídeo HappyHorse a utilizar. Esta selección determina qué opciones de prompt, resolución, relación de aspecto e imágenes de referencia están disponibles.| DYNAMIC_COMBO| Sí| ”happyhorse-1.0-video-edit”  
`video`| El vídeo a editar.| VIDEO| Sí| 3 a 60 segundos  
`semilla`| Semilla para la generación (predeterminada: 0).| INT| Sí| 0 a 2147483647  
`marca de agua`| Si se debe añadir una marca de agua generada por IA al resultado (predeterminado: False). Parámetro avanzado.| BOOLEAN| Sí| True  
False  
  
### 

​

Entradas de happyhorse-1.0-video-edit

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`prompt`| Instrucciones de edición o requisitos de transferencia de estilo. Debe tener al menos 1 carácter.| STRING| Sí| -  
`resolution`| La resolución de salida.| COMBO| Sí| ”720P"  
"1080P”  
`ratio`| Relación de aspecto. Si no se cambia, se aproxima a la relación de aspecto del vídeo de entrada.| COMBO| Sí| ”16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4”  
  
### 

​

Entradas de referencia

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`reference_images`| Ranura ampliable: conecta de 0 a 5 imágenes de referencia (`image1`…`image5`) para guiar la edición.| IMAGE| No| 0 a 5 imágenes  
  
**Nota:** El vídeo de entrada debe tener una duración de 3 a 60 segundos. La duración de salida es de 3 a 15 segundos y coincide con el vídeo de entrada; los vídeos de entrada de más de 15 segundos se recortan. El `prompt` debe tener al menos 1 carácter.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| El vídeo editado de salida.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/es.md)

* * *

**Source fingerprint (SHA-256):** `396cad4b5a06d457746a421050df98c892fa9db6019e3de983b4d0c417842b57`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HappyHorseVideoEditApi.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HappyHorseVideoEditApi)

[HappyHorse Texto a Video](https://docs.comfy.org/es/built-in-nodes/HappyHorseTextToVideoApi)[Wan 2.7 Imagen a Video](https://docs.comfy.org/es/built-in-nodes/Wan2ImageToVideoApi)
