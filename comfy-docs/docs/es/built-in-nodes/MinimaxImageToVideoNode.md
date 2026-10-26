---
url: https://docs.comfy.org/es/built-in-nodes/MinimaxImageToVideoNode/
title: MiniMax imagen a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:11.923983+00:00
---

# MiniMax imagen a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MinimaxImageToVideoNode/

Minimax

# MiniMax imagen a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

Copiar páginaCopiar página

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento: Genera videos de forma síncrona basándose en una imagen y un prompt, y parámetros opcionales utilizando la API de MiniMax. Este nodo toma una imagen de entrada y una descripción de texto para crear una secuencia de video, con varias opciones de modelo y configuraciones disponibles.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| Imagen a utilizar como primer fotograma de la generación de video| IMAGE| Sí| -  
`texto de prompt`| Prompt de texto para guiar la generación del video (predeterminado: cadena vacía)| STRING| Sí| -  
`modelo`| Modelo a utilizar para la generación de video (predeterminado: “I2V-01”)| COMBO| Sí| ”I2V-01-Director"  
"I2V-01"  
"I2V-01-live”  
`semilla`| Semilla aleatoria utilizada para crear el ruido (predeterminado: 0)| INT| No| 0 a 18446744073709551615  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| El video generado como salida| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `9ad1659352e363361f09d6a7a0e24835056b20cc84532247251f516b0ac284e8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MinimaxImageToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MinimaxImageToVideoNode)

[MiniMax Hailuo Video](https://docs.comfy.org/es/built-in-nodes/MinimaxHailuoVideoNode)[MiniMax texto a video](https://docs.comfy.org/es/built-in-nodes/MinimaxTextToVideoNode)
