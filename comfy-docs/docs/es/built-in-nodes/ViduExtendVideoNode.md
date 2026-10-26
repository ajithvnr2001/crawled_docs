---
url: https://docs.comfy.org/es/built-in-nodes/ViduExtendVideoNode/
title: Extensi\u00f3n de video Vidu - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:43.291784+00:00
---

# Extensión de video Vidu - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ViduExtendVideoNode/

Vidu

# Extensión de video Vidu - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Vidu Video Extension genera fotogramas adicionales para extender la duración de un video existente.

Copiar páginaCopiar página

El nodo Vidu Video Extension genera fotogramas adicionales para extender la duración de un video existente. Utiliza un modelo de IA especificado para crear una continuación basada en el video de origen y un prompt de texto opcional.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| Modelo a usar para la extensión de video. Al seleccionar un modelo, se muestran sus ajustes específicos de duración y resolución.| DYNAMIC_COMBO| Sí| `"viduq2-pro"`  
`"viduq2-turbo"`  
`video`| El video de origen que se va a extender.| VIDEO| Sí| -  
`prompt`| Un prompt de texto opcional para el video extendido (máx. 2000 caracteres; predeterminado: vacío).| STRING| Sí| -  
`semilla`| Un valor de semilla para controlar la aleatoriedad de la generación (predeterminado: 1).| INT| Sí| 0 a 2147483647  
`fotograma_final`| Una imagen opcional para usar como fotograma final objetivo de la extensión.| IMAGE| No| -  
  
### 

​

Entradas de viduq2-pro y viduq2-turbo

Estos ajustes son compartidos por ambos modelos.

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`duration`| Duración del video extendido en segundos (predeterminado: 4). Este ajuste aparece después de seleccionar un modelo.| INT| Sí| 1 a 7  
`resolution`| Resolución del video de salida. Este ajuste aparece después de seleccionar un modelo.| COMBO| Sí| `"720p"`  
`"1080p"`  
  
**Nota:** El `video` de origen debe tener una duración entre 4 y 55 segundos. Si se proporciona `end_frame`, su relación de aspecto debe estar entre 1:4 y 4:1, y su ancho y alto deben ser de al menos 128 píxeles cada uno.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El archivo de video recién generado que contiene el metraje extendido.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `bfa79dd1aee8a3e56d95fe7a899454b5c5f93679e098f59fc3bf58d93d290819`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ViduExtendVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ViduExtendVideoNode)

[Generación de referencia a vídeo Vidu Q4](https://docs.comfy.org/es/built-in-nodes/Vidu4ReferenceVideoNode)[Generación de video a partir de imagen Vidu](https://docs.comfy.org/es/built-in-nodes/ViduImageToVideoNode)
