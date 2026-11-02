---
url: https://docs.comfy.org/es/built-in-nodes/MinimaxHailuo03MaxLipSyncNode/
title: MinimaxHailuo03MaxLipSyncNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:33.901939+00:00
---

# MinimaxHailuo03MaxLipSyncNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MinimaxHailuo03MaxLipSyncNode/

Video

# MinimaxHailuo03MaxLipSyncNode - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo anima una imagen fija para que los movimientos de la boca sigan una pista de audio proporcionada.

Copiar páginaCopiar página

Este nodo anima una imagen fija para que los movimientos de la boca sigan una pista de audio proporcionada. La imagen y el audio se cargan, se consulta periódicamente el trabajo de sincronización labial de Hailuo 03 Max y el video de la persona hablando se devuelve con la resolución que elijas. El video de salida tiene la misma duración que el audio.

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
`image`| Imagen que se va a animar, de al menos 256x256 píxeles. La relación de aspecto debe estar entre 0.4 y 2.5.| IMAGE| Sí| Imagen única  
`audio`| Audio con el que se sincronizarán los labios, de 5 a 899 segundos de duración.| AUDIO| Sí| 5 a 899 segundos  
`resolution`| Resolución de salida (predeterminado: “768P”). La relación de aspecto será la soportada más cercana a la de la imagen.| COMBO| Sí| ”480P"  
"768P"  
"1080P"  
"2K”  
`transcription`| Transcribir el audio para guiar la sincronización labial (predeterminado: false).| BOOLEAN| No| true  
false  
`seed`| Semilla aleatoria. La misma solicitud con la misma semilla produce resultados similares, aunque no se garantiza que sean idénticos (predeterminado: 42).| INT| Sí| 0 a 2147483647  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| El video de la persona hablando, con la misma duración que el audio de entrada.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxLipSyncNode/es.md)

* * *

**Source fingerprint (SHA-256):** `0af4166f9f3237cacc3506d6c6544c0374a330cf998f8bd2ef1f4f7162e2f9ab`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MinimaxHailuo03MaxLipSyncNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MinimaxHailuo03MaxLipSyncNode)

[MinimaxHailuo03MaxInsertVideoNode](https://docs.comfy.org/es/built-in-nodes/MinimaxHailuo03MaxInsertVideoNode)[MinimaxHailuo03MaxRecastNode](https://docs.comfy.org/es/built-in-nodes/MinimaxHailuo03MaxRecastNode)
