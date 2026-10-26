---
url: https://docs.comfy.org/es/built-in-nodes/Vidu2TextToVideoNode/
title: Generaci\u00f3n de video de Vidu2 desde texto - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:43.142344+00:00
---

# Generación de video de Vidu2 desde texto - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Vidu2TextToVideoNode/

Vidu

# Generación de video de Vidu2 desde texto - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Vidu2 Text-to-Video Generation crea un video a partir de una descripción de texto.

Copiar páginaCopiar página

El nodo Vidu2 Text-to-Video Generation crea un video a partir de una descripción de texto. Se conecta a una API externa para generar contenido de video basado en tu prompt, lo que permite controlar la duración, el estilo visual y el formato del video.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de IA que se utilizará para la generación de video. Actualmente, solo hay un modelo disponible.| COMBO| Sí| `"viduq2"`  
`prompt`| Una descripción textual para la generación de video, con una longitud máxima de 2000 caracteres.| STRING| Sí| -  
`duración`| La duración del video generado en segundos. El valor se puede ajustar mediante un control deslizante (predeterminado: 5).| INT| No| 1 a 10  
`semilla`| Un número que se utiliza para controlar la aleatoriedad de la generación y permitir resultados reproducibles. Se puede controlar después de la generación (predeterminado: 1).| INT| No| 0 a 2147483647  
`relación_de_aspecto`| La relación proporcional entre el ancho y el alto del video.| COMBO| No| `"16:9"`  
`"9:16"`  
`"3:4"`  
`"4:3"`  
`"1:1"`  
`resolución`| Las dimensiones en píxeles del video generado. Este es un parámetro avanzado.| COMBO| No| `"720p"`  
`"1080p"`  
`música_de_fondo`| Indica si se debe añadir música de fondo al video generado (predeterminado: False). Este es un parámetro avanzado.| BOOLEAN| No| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El archivo de video generado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `27b7c05ae1b3b23d07e775f67474ecef1ffc0bd8240f4aa2219e15949d854f27`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Vidu2TextToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Vidu2TextToVideoNode)

[Generación de video de Vidu2 desde fotogramas inicial/final](https://docs.comfy.org/es/built-in-nodes/Vidu2StartEndToVideoNode)[Generación de video de imagen a video Vidu Q3](https://docs.comfy.org/es/built-in-nodes/Vidu3ImageToVideoNode)
