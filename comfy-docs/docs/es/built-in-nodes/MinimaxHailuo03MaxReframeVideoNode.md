---
url: https://docs.comfy.org/es/built-in-nodes/MinimaxHailuo03MaxReframeVideoNode/
title: MiniMax H3 Max Reencuadrar v\u00eddeo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-06T14:52:02.290287+00:00
---

# MiniMax H3 Max Reencuadrar vídeo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MinimaxHailuo03MaxReframeVideoNode/

Video

# MiniMax H3 Max Reencuadrar vídeo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo adapta un video a una nueva relación de aspecto ajustándolo en un nuevo lienzo y generando las áreas circundantes.

Copiar páginaCopiar página

Este nodo adapta un video a una nueva relación de aspecto ajustándolo en un nuevo lienzo y generando las áreas circundantes. Se conservan la sincronización y el sonido del video de origen. Úselo para convertir un clip horizontal en uno vertical, o viceversa, sin recortar el sujeto fuera del encuadre.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| Modelo que se usará para la generación de video.| DYNAMIC_COMBO| Sí| ”MiniMax H3 Max”  
  
### 

​

Entradas de MiniMax H3 Max

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`video`| Video de origen al que se le cambiará el encuadre, de 0.5 a 300 segundos de duración.| VIDEO| Sí| 0.5 a 300 segundos  
`aspect_ratio`| Relación de aspecto del lienzo de salida (predeterminado: “9:16”).| COMBO| Sí| ”16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4"  
"21:9"  
"9:21”  
`resolution`| Resolución del video de salida (predeterminado: “768P”).| COMBO| Sí| ”480P"  
"768P"  
"1080P”  
`prompt`| Guía opcional para las áreas circundantes generadas.| STRING| Sí| 0 a 50000 caracteres  
`seed`| Semilla aleatoria. La misma solicitud con la misma semilla produce resultados similares, pero no necesariamente idénticos (predeterminado: 42).| INT| Sí| 0 a 4294967295  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| El video con el nuevo encuadre en la relación de aspecto seleccionada.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxReframeVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `83d780c2fe8c42475d4ad25ad5b318f2a4c135edef9c0ca1ff0d1fd07d90c1c6`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MinimaxHailuo03MaxReframeVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MinimaxHailuo03MaxReframeVideoNode)

[MiniMax H3 Max Recast](https://docs.comfy.org/es/built-in-nodes/MinimaxHailuo03MaxRecastNode)[Pruna P-Video Upscale](https://docs.comfy.org/es/built-in-nodes/PrunaPVideoUpscaleNode)
