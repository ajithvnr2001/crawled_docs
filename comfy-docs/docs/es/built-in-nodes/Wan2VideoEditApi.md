---
url: https://docs.comfy.org/es/built-in-nodes/Wan2VideoEditApi/
title: Wan 2.7 Edici\u00f3n de Video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:44.780241+00:00
---

# Wan 2.7 Edición de Video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Wan2VideoEditApi/

Wan

# Wan 2.7 Edición de Video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Wan 2.7 Video Edit edita un video usando instrucciones de texto, imágenes de referencia o transferencia de estilo.

Copiar páginaCopiar página

El nodo Wan 2.7 Video Edit edita un video usando instrucciones de texto, imágenes de referencia o transferencia de estilo. Envía el video de entrada (más cualquier imagen de referencia) al servicio de edición de video Wan 2.7 y devuelve un video recién generado según la resolución, relación de aspecto y duración elegidas.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo que se usará para la edición de video. Cada opción expone su propio conjunto de subparámetros.| DYNAMIC_COMBO| Sí| `"wan2.7-videoedit"`  
`video`| El video que se va a editar.| VIDEO| Sí| -  
`semilla`| Semilla que se usará para la generación. (predeterminado: 0)| INT| Sí| 0 a 2147483647  
`configuración_de_audio`| ’auto’: el modelo decide si regenerar el audio según el prompt. ‘origin’: conserva el audio original del video de entrada. (predeterminado: “auto”)| COMBO| Sí| `"auto"`  
`"origin"`  
`marca de agua`| Si se debe agregar una marca de agua generada por IA al resultado. (predeterminado: False)| BOOLEAN| Sí| -  
  
### 

​

Entradas de wan2.7-videoedit

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Instrucciones de edición o requisitos de transferencia de estilo. (predeterminado: cadena vacía)| STRING| Sí| -  
`resolution`| La resolución del video de salida.| COMBO| Sí| `"720P"`  
`"1080P"`  
`ratio`| Relación de aspecto. Si no se cambia, se aproxima a la relación de aspecto del video de entrada.| COMBO| Sí| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`duration`| Duración de salida en segundos. ‘auto’ coincide con la duración del video de entrada. Un valor específico recorta desde el inicio del video. (predeterminado: “auto”)| COMBO| Sí| `"auto"`  
`"2"`  
`"3"`  
`"4"`  
`"5"`  
`"6"`  
`"7"`  
`"8"`  
`"9"`  
`"10"`  
  
### 

​

Entradas de referencia

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`reference_images`| Ranura ampliable: conecta de 0 a 4 imágenes (`image1`…`image4`) para guiar la edición. El límite de cantidad es 4 para el modelo wan2.7-videoedit.| IMAGE| No| 0 a 4 items  
  
**Restricciones:**

  * `audio_setting` y `watermark` son opciones avanzadas.
  * El `prompt` debe contener al menos 1 carácter.
  * El `video` de entrada debe tener una duración de entre 2 y 10 segundos.
  * La ranura ampliable `reference_images` acepta un máximo de 4 imágenes.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El video editado generado por el modelo.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/es.md)

* * *

**Source fingerprint (SHA-256):** `27283273ee56c90903db103a3e9bc17dc4df0914676c9aedd2a115b07937dc10`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Wan2VideoEditApi.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Wan2VideoEditApi)

[Wan 2.7 Continuación de Video](https://docs.comfy.org/es/built-in-nodes/Wan2VideoContinuationApi)[Imagen a vídeo de Wan 3.0](https://docs.comfy.org/es/built-in-nodes/Wan3ImageToVideoApi)
