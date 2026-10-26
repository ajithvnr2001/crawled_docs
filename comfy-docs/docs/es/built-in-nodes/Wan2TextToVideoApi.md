---
url: https://docs.comfy.org/es/built-in-nodes/Wan2TextToVideoApi/
title: Wan 2.7 Texto a Video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:44.536034+00:00
---

# Wan 2.7 Texto a Video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Wan2TextToVideoApi/

Wan

# Wan 2.7 Texto a Video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo genera un video a partir de una descripción de texto utilizando el modelo Wan 2.7.

Copiar páginaCopiar página

Este nodo genera un video a partir de una descripción de texto utilizando el modelo Wan 2.7. Envía tu prompt a la API de generación de video de Wan, espera a que la tarea finalice y devuelve el video resultante. Opcionalmente, puedes conectar un clip de audio para influir en el movimiento y la sincronización del video; si no se proporciona audio, el modelo genera automáticamente audio coincidente.

## 

​

Entradas

### 

​

Entradas comunes

Estas entradas están siempre disponibles en el nivel superior del nodo.

Parámetro| Descripción| Tipo de datos| Obligatoria| Rango  
---|---|---|---|---  
`modelo`| El modelo específico a utilizar para la generación de video.| DYNAMIC_COMBO| Sí| `"wan2.7-t2v"`  
`audio`| Audio para impulsar la generación de video (por ejemplo, sincronización de labios, movimiento sincronizado con el ritmo). Duración: 3s-30s. Si no se proporciona, el modelo genera automáticamente música de fondo o efectos de sonido coincidentes.| AUDIO| No| -  
`semilla`| Semilla a utilizar para la generación (predeterminado: 0).| INT| Sí| 0 a 2147483647  
`extender_prompt`| Si se debe mejorar el prompt con asistencia de IA (predeterminado: True).| BOOLEAN| Sí| True  
False  
`marca de agua`| Si se debe añadir una marca de agua generada por IA al resultado (predeterminado: False).| BOOLEAN| Sí| True  
False  
  
### 

​

Entradas de wan2.7-t2v

Estos ajustes aparecen cuando se selecciona el modelo `wan2.7-t2v`.

Parámetro| Descripción| Tipo de datos| Obligatoria| Rango  
---|---|---|---|---  
`prompt`| Prompt que describe los elementos y las características visuales. Admite inglés y chino.| STRING| Sí| -  
`negative_prompt`| Prompt negativo que describe lo que se debe evitar. El valor predeterminado es una cadena vacía.| STRING| No| -  
`resolution`| La resolución del video de salida.| COMBO| Sí| `"720P"`  
`"1080P"`  
`ratio`| La relación de aspecto del video de salida.| COMBO| Sí| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`duration`| La duración del video en segundos (predeterminado: 5).| INT| Sí| 2 a 15  
  
**Nota:** La entrada `prompt` no debe estar vacía. La entrada `audio` es opcional; si se proporciona, el nodo acepta audio de entre 1.5 y 60 segundos, aunque la información emergente recomiende 3s-30s. Si no se suministra audio, el modelo genera automáticamente audio coincidente. Cuando `negative_prompt` se deja vacío, no se envía a la API. `prompt_extend` y `watermark` son opciones avanzadas.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El archivo de video generado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/es.md)

* * *

**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Wan2TextToVideoApi.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Wan2TextToVideoApi)

[Wan 2.7 Referencia a Video](https://docs.comfy.org/es/built-in-nodes/Wan2ReferenceVideoApi)[Wan 2.7 Continuación de Video](https://docs.comfy.org/es/built-in-nodes/Wan2VideoContinuationApi)
