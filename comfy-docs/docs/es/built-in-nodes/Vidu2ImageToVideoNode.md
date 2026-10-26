---
url: https://docs.comfy.org/es/built-in-nodes/Vidu2ImageToVideoNode/
title: Vidu2 generaci\u00f3n de imagen a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:42.720393+00:00
---

# Vidu2 generación de imagen a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Vidu2ImageToVideoNode/

Vidu

# Vidu2 generación de imagen a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo de Generación de Video a partir de Imagen Vidu2 crea una secuencia de video a partir de una única imagen de entrada.

Copiar páginaCopiar página

El nodo de Generación de Video a partir de Imagen Vidu2 crea una secuencia de video a partir de una única imagen de entrada. Utiliza un modelo Vidu2 específico para animar la escena basándose en un mensaje de texto opcional, controlando la duración, resolución e intensidad del movimiento del video.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo Vidu2 a utilizar para la generación de video. Diferentes modelos ofrecen distintas compensaciones entre velocidad y calidad.| COMBO| Sí| `"viduq2-pro-fast"`  
`"viduq2-pro"`  
`"viduq2-turbo"`  
`imagen`| Una imagen que se usará como fotograma inicial del video generado. Solo se permite una imagen.| IMAGE| Sí| -  
`prompt`| Un mensaje de texto opcional para la generación del video (máximo 2000 caracteres). El valor predeterminado es una cadena vacía.| STRING| No| -  
`duración`| La duración del video generado en segundos. El valor predeterminado es 5.| INT| Sí| 1 a 10  
`semilla`| Un valor de semilla para la generación de números aleatorios, con el fin de garantizar resultados reproducibles. El valor predeterminado es 1.| INT| No| 0 a 2147483647  
`resolución`| La resolución de salida del video generado. Este parámetro es avanzado.| COMBO| Sí| `"720p"`  
`"1080p"`  
`amplitud_de_movimiento`| La amplitud de movimiento de los objetos en el fotograma. Este parámetro es avanzado.| COMBO| Sí| `"auto"`  
`"small"`  
`"medium"`  
`"large"`  
  
**Restricciones:**

  * La entrada `image` debe contener exactamente una imagen.
  * La relación de aspecto de la imagen de entrada debe estar entre 1:4 y 4:1.
  * El texto de `prompt` está limitado a un máximo de 2000 caracteres.



## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| El archivo de video generado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ImageToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `204f8d2b9edf17c2c180480f98a852718416a54725d92e5fec574b8517ada398`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Vidu2ImageToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Vidu2ImageToVideoNode)

[Generación de video Google Veo 3](https://docs.comfy.org/es/built-in-nodes/Veo3VideoGenerationNode)[Vidu2 generación de video con referencias](https://docs.comfy.org/es/built-in-nodes/Vidu2ReferenceVideoNode)
