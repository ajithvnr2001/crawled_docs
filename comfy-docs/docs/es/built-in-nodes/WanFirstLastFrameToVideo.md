---
url: https://docs.comfy.org/es/built-in-nodes/WanFirstLastFrameToVideo/
title: Wan primer-\u00faltimo fotograma a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:45.777682+00:00
---

# Wan primer-último fotograma a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WanFirstLastFrameToVideo/

Wan

# Wan primer-último fotograma a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo WanFirstLastFrameToVideo prepara el condicionamiento para la generación de vídeo combinando un fotograma inicial y un fotograma final con indicaciones

Copiar páginaCopiar página

El nodo WanFirstLastFrameToVideo prepara el condicionamiento para la generación de vídeo combinando un fotograma inicial y un fotograma final con indicaciones de texto. Codifica las imágenes de los fotogramas en el espacio latente, crea una máscara que indica al modelo de vídeo qué fotogramas ya se conocen y adjunta las características CLIP vision cuando se proporcionan. El nodo genera un condicionamiento positivo y negativo actualizado, además de un latente vacío que define el tamaño y la duración del vídeo a generar.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`positivo`| Condicionamiento de texto positivo utilizado para guiar la generación del vídeo.| CONDITIONING| Sí| -  
`negativo`| Condicionamiento de texto negativo utilizado para guiar la generación del vídeo.| CONDITIONING| Sí| -  
`vae`| Modelo VAE utilizado para codificar las imágenes combinadas de los fotogramas en el espacio latente.| VAE| Sí| -  
`ancho`| Anchura del vídeo generado en píxeles (predeterminado: 832, paso: 16).| INT| Sí| 16 a MAX_RESOLUTION  
`alto`| Altura del vídeo generado en píxeles (predeterminado: 480, paso: 16).| INT| Sí| 16 a MAX_RESOLUTION  
`longitud`| Número de fotogramas en la secuencia de vídeo (predeterminado: 81, paso: 4).| INT| Sí| 1 a MAX_RESOLUTION  
`tamaño_lote`| Número de vídeos a generar a la vez (predeterminado: 1).| INT| Sí| 1 a 4096  
`clip_vision_start_image`| Características CLIP vision extraídas de la imagen inicial. Si se proporcionan tanto las entradas CLIP vision inicial como final, sus características se combinan.| CLIP_VISION_OUTPUT| No| -  
`clip_vision_end_image`| Características CLIP vision extraídas de la imagen final. Si se proporcionan tanto las entradas CLIP vision inicial como final, sus características se combinan.| CLIP_VISION_OUTPUT| No| -  
`imagen_inicial`| Imagen del fotograma inicial para la secuencia de vídeo. Se utilizan sus primeros `length` fotogramas y se redimensionan a `width` × `height`.| IMAGE| No| -  
`imagen_final`| Imagen del fotograma final para la secuencia de vídeo. Se utilizan sus últimos `length` fotogramas y se redimensionan a `width` × `height`.| IMAGE| No| -  
  
**Nota:** Cuando se proporciona al menos una de las imágenes `start_image` o `end_image`, el nodo construye una secuencia de fotogramas combinada donde los fotogramas inicial y final se rellenan y los fotogramas restantes utilizan un marcador gris neutro (0.5). Una máscara marca las regiones rellenas como conocidas y las regiones del marcador como desconocidas, lo que permite al modelo de vídeo generar los fotogramas intermedios. Cuando se proporciona una imagen inicial, la región conocida también se extiende 3 fotogramas adicionales más allá de la imagen. La misma imagen de fotograma codificada y máscara se adjuntan tanto al condicionamiento `positive` como al `negative`. Si se proporcionan ambas entradas CLIP vision, sus estados ocultos se concatenan; si solo se proporciona una, se utiliza por sí sola. La duración latente del vídeo se deriva de `length` después de la compresión temporal: `((length - 1) // 4) + 1`.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positivo`| Condicionamiento positivo con la imagen de fotograma codificada, la máscara y, si se proporcionan, las características CLIP vision adjuntas.| CONDITIONING  
`negativo`| Condicionamiento negativo con la imagen de fotograma codificada, la máscara y, si se proporcionan, las características CLIP vision adjuntas.| CONDITIONING  
`latente`| Tensor latente vacío (todo ceros) con forma para el tamaño de lote, la duración del vídeo y la resolución dados.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WanFirstLastFrameToVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WanFirstLastFrameToVideo)

[Wan 2.2 imagen a latente de video](https://docs.comfy.org/es/built-in-nodes/Wan22ImageToVideoLatent)[Wan imagen a video](https://docs.comfy.org/es/built-in-nodes/WanImageToVideo)
