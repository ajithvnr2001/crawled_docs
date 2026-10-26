---
url: https://docs.comfy.org/es/built-in-nodes/MinimaxTextToVideoNode/
title: MiniMax texto a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:12.404097+00:00
---

# MiniMax texto a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MinimaxTextToVideoNode/

Minimax

# MiniMax texto a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

Copiar páginaCopiar página

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento: Genera videos de forma síncrona basándose en un prompt y parámetros opcionales utilizando la API de MiniMax. Este nodo crea contenido de video a partir de descripciones de texto conectándose al servicio de texto a video de MiniMax.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`texto_de_indicación`| Prompt de texto para guiar la generación del video| STRING| Sí| -  
`modelo`| Modelo a utilizar para la generación de video (predeterminado: “T2V-01”)| COMBO| No| ”T2V-01"  
"T2V-01-Director”  
`semilla`| Semilla aleatoria utilizada para crear el ruido (predeterminado: 0)| INT| No| 0 a 18446744073709551615  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| El video generado basado en el prompt de entrada| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `bdbd8f9defc4c626f07b36c1ba9859155fa90a2d7ef9a491c30dac4d003d39be`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MinimaxTextToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MinimaxTextToVideoNode)

[MiniMax imagen a video](https://docs.comfy.org/es/built-in-nodes/MinimaxImageToVideoNode)[PixVerse imagen a video](https://docs.comfy.org/es/built-in-nodes/PixverseImageToVideoNode)
