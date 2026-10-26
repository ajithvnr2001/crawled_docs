---
url: https://docs.comfy.org/es/built-in-nodes/Vidu3ImageToVideoNode/
title: Generaci\u00f3n de video de imagen a video Vidu Q3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:43.209949+00:00
---

# Generación de video de imagen a video Vidu Q3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Vidu3ImageToVideoNode/

Vidu

# Generación de video de imagen a video Vidu Q3 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo de generación de video a partir de imagen Vidu Q3 crea una secuencia de video a partir de una imagen de entrada.

Copiar páginaCopiar página

El nodo de generación de video a partir de imagen Vidu Q3 crea una secuencia de video a partir de una imagen de entrada. Utiliza un modelo Vidu Q3 para animar la imagen, opcionalmente guiado por un prompt de texto, y genera como salida un archivo de video.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| Modelo que se usará para la generación de video.| DYNAMIC_COMBO| Sí| `"viduq3-pro"`  
`"viduq3-turbo"`  
`imagen`| Una imagen que se usará como fotograma inicial del video generado.| IMAGE| Sí| -  
`prompt`| Un prompt de texto opcional para la generación de video (máx. 2000 caracteres) (predeterminado: vacío).| STRING| Sí| -  
`semilla`| El valor de semilla utilizado para controlar la aleatoriedad de la generación (predeterminado: 1).| INT| Sí| 0 a 2147483647  
  
### 

​

Entradas de viduq3-pro

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`resolution`| Resolución del video de salida.| COMBO| Sí| `"720p"`  
`"1080p"`  
`"2K"`  
`duration`| Duración del video de salida en segundos (predeterminado: 5).| INT| Sí| 1 a 16  
`audio`| Cuando está habilitado, genera video con sonido (incluidos diálogos y efectos de sonido) (predeterminado: False).| BOOLEAN| Sí| `True`  
`False`  
  
### 

​

Entradas de viduq3-turbo

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`resolution`| Resolución del video de salida.| COMBO| Sí| `"720p"`  
`"1080p"`  
`duration`| Duración del video de salida en segundos (predeterminado: 5).| INT| Sí| 1 a 16  
`audio`| Cuando está habilitado, genera video con sonido (incluidos diálogos y efectos de sonido) (predeterminado: False).| BOOLEAN| Sí| `True`  
`False`  
  
**Nota:** La `image` debe tener una relación de aspecto entre 1:4 y 4:1 (vertical a horizontal). El `prompt` es opcional, pero no puede superar los 2000 caracteres. Las opciones de `resolution` disponibles dependen del modelo seleccionado: `"viduq3-pro"` admite `"720p"`, `"1080p"` y `"2K"`; `"viduq3-turbo"` admite `"720p"` y `"1080p"`.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El archivo de video generado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `77500d1e19928128decc010540670e311cd8ec4fcad913412517f47f0e27e15f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Vidu3ImageToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Vidu3ImageToVideoNode)

[Generación de video de Vidu2 desde texto](https://docs.comfy.org/es/built-in-nodes/Vidu2TextToVideoNode)[Generación de video de inicio/fin de Vidu Q3](https://docs.comfy.org/es/built-in-nodes/Vidu3StartEndToVideoNode)
