---
url: https://docs.comfy.org/es/built-in-nodes/MinimaxHailuoVideoNode/
title: MiniMax Hailuo Video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:11.759657+00:00
---

# MiniMax Hailuo Video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MinimaxHailuoVideoNode/

Minimax

# MiniMax Hailuo Video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera videos a partir de prompts de texto utilizando el modelo MiniMax Hailuo-02.

Copiar páginaCopiar página

Genera videos a partir de prompts de texto utilizando el modelo MiniMax Hailuo-02. De manera opcional, puedes proporcionar una imagen inicial para usarla como primer fotograma, lo que crea un video que continúa a partir de esa imagen.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`texto_del_prompt`| Prompt de texto para guiar la generación del video (predeterminado: vacío).| STRING| Sí| -  
`semilla`| La semilla aleatoria utilizada para crear el ruido (predeterminado: 0).| INT| No| 0 a 18446744073709551615  
`imagen_primer_fotograma`| Imagen opcional para usar como primer fotograma al generar un video.| IMAGE| No| -  
`optimizador_de_prompt`| Optimiza el prompt para mejorar la calidad de la generación cuando sea necesario (predeterminado: True).| BOOLEAN| No| True  
False  
`duración`| La duración del video de salida en segundos (predeterminado: 6).| COMBO| No| 6  
10  
`resolución`| Las dimensiones de visualización del video. 1080p es 1920x1080, 768p es 1366x768 (predeterminado: “768P”).| COMBO| No| ”768P"  
"1080P”  
  
**Nota:** Cuando `resolution` se establece en “1080P”, `duration` se limita a 6 segundos. Cuando no se proporciona `first_frame_image`, `prompt_text` no debe estar vacío.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El archivo de video generado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MinimaxHailuoVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MinimaxHailuoVideoNode)

[MiniMax H3 Texto a Video](https://docs.comfy.org/es/built-in-nodes/MinimaxHailuo03TextToVideoNode)[MiniMax imagen a video](https://docs.comfy.org/es/built-in-nodes/MinimaxImageToVideoNode)
