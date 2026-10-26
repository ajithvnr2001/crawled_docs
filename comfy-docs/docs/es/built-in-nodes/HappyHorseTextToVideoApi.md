---
url: https://docs.comfy.org/es/built-in-nodes/HappyHorseTextToVideoApi/
title: HappyHorse Texto a Video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:52.325269+00:00
---

# HappyHorse Texto a Video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HappyHorseTextToVideoApi/

Wan

# HappyHorse Texto a Video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera un video basado en un prompt de texto utilizando el modelo HappyHorse.

Copiar páginaCopiar página

Genera un video basado en un prompt de texto utilizando el modelo HappyHorse. Este nodo envía tu prompt y configuración a la API de HappyHorse, espera a que se genere el video y luego descarga el resultado.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo HappyHorse utilizado para la generación, junto con sus subparámetros. Seleccionar un modelo determina qué subparámetros están disponibles (consulta las secciones de modelos a continuación).| DYNAMIC_COMBO| Sí| ”happyhorse-1.1-t2v"  
"happyhorse-1.0-t2v”  
`semilla`| Semilla utilizada para la generación. Usar la misma semilla con las mismas entradas producirá el mismo resultado. (predeterminado: 0).| INT| Sí| 0 a 2147483647  
`marca de agua`| Si se añade una marca de agua generada por IA al resultado. (predeterminado: False).| BOOLEAN| Sí| True / False  
  
### 

​

Entradas de happyhorse-1.1-t2v

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Prompt que describe los elementos y las características visuales. Admite inglés y chino. (predeterminado: "").| STRING| Sí| -  
`resolution`| La resolución del video de salida.| COMBO| Sí| ”720P"  
"1080P”  
`ratio`| La relación de aspecto del video de salida.| COMBO| Sí| ”16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4"  
"21:9"  
"9:21"  
"5:4"  
"4:5”  
`duration`| La duración del video en segundos. (predeterminado: 5, mín.: 3, máx.: 15, paso: 1).| INT| Sí| 3 a 15  
  
### 

​

Entradas de happyhorse-1.0-t2v

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Prompt que describe los elementos y las características visuales. Admite inglés y chino. (predeterminado: "").| STRING| Sí| -  
`resolution`| La resolución del video de salida.| COMBO| Sí| ”720P"  
"1080P”  
`ratio`| La relación de aspecto del video de salida.| COMBO| Sí| ”16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4”  
`duration`| La duración del video en segundos. (predeterminado: 5, mín.: 3, máx.: 15, paso: 1).| INT| Sí| 3 a 15  
  
Nota: el prompt no debe estar vacío; se genera un error si no se proporciona ningún prompt. Ambos modelos admiten duraciones de video de 3 a 15 segundos. El modelo `happyhorse-1.1-t2v` ofrece relaciones de aspecto adicionales (`21:9`, `9:21`, `5:4`, `4:5`) que no están disponibles con `happyhorse-1.0-t2v`.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`VIDEO`| El archivo de video generado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/es.md)

* * *

**Source fingerprint (SHA-256):** `b60cfc3ce4935d7eb36bb28f9bd268446c4df5b437e06278b7e6d91d349d0238`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HappyHorseTextToVideoApi.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HappyHorseTextToVideoApi)

[HappyHorse Referencia a Video](https://docs.comfy.org/es/built-in-nodes/HappyHorseReferenceVideoApi)[HappyHorse Edición de Video](https://docs.comfy.org/es/built-in-nodes/HappyHorseVideoEditApi)
