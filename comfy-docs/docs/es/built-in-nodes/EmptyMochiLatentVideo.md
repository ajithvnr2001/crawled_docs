---
url: https://docs.comfy.org/es/built-in-nodes/EmptyMochiLatentVideo/
title: Video latente Mochi vac\u00edo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:46.254125+00:00
---

# Video latente Mochi vacío - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyMochiLatentVideo/

Mochi

# Video latente Mochi vacío - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

EmptyMochiLatentVideo crea un tensor de video latente vacío con las dimensiones que especifiques.

Copiar páginaCopiar página

EmptyMochiLatentVideo crea un tensor de video latente vacío con las dimensiones que especifiques. Genera una representación latente llena de ceros que puede usarse como punto de partida para flujos de trabajo de generación de video. El nodo te permite definir el ancho, la altura, la longitud y el tamaño de lote del tensor de video latente.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`ancho`| El ancho del video latente en píxeles (predeterminado: 848, los valores aumentan en pasos de 16)| INT| Sí| 16 a MAX_RESOLUTION  
`altura`| La altura del video latente en píxeles (predeterminado: 480, los valores aumentan en pasos de 16)| INT| Sí| 16 a MAX_RESOLUTION  
`longitud`| El número de fotogramas en el video latente (predeterminado: 25, los valores aumentan en pasos de 6, comenzando en 7)| INT| Sí| 7 a MAX_RESOLUTION  
`tamaño_del_lote`| El número de videos latentes a generar en un lote (predeterminado: 1)| INT| No| 1 a 4096  
  
**Nota:** Las dimensiones latentes reales se calculan como width/8 y height/8, la dimensión temporal se calcula como `((length - 1) // 6) + 1`, y el tensor tiene 12 canales. Debido a que `length` avanza en pasos de 6 comenzando desde 7, los valores válidos son 7, 13, 19, 25, y así sucesivamente.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`samples`| Un tensor de video latente vacío con las dimensiones especificadas, que contiene todos ceros| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyMochiLatentVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyMochiLatentVideo)

[Audio latente vacío de MiniMax Music3](https://docs.comfy.org/es/built-in-nodes/EmptyMiniMaxMusic3LatentAudio)[Latente Qwen Image en capas vacío](https://docs.comfy.org/es/built-in-nodes/EmptyQwenImageLayeredLatentImage)
