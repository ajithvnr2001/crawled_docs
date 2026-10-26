---
url: https://docs.comfy.org/es/built-in-nodes/EmptyMiniMaxMusic3LatentAudio/
title: Audio latente vac\u00edo de MiniMax Music3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:46.185604+00:00
---

# Audio latente vacío de MiniMax Music3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyMiniMaxMusic3LatentAudio/

Minimax Music

# Audio latente vacío de MiniMax Music3 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo crea un latente de audio vacío (relleno de ceros) para el modelo MiniMax Music3.

Copiar páginaCopiar página

Este nodo crea un latente de audio vacío (relleno de ceros) para el modelo MiniMax Music3. Convierte la duración solicitada en segundos al número correspondiente de tramas de audio y produce un tensor latente en blanco del tamaño correcto, listo para usarse como punto de partida para la generación de música.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`seconds`| La duración del latente de audio en segundos (predeterminado: 120.0). El valor se convierte a tramas de audio y se recorta a los límites de duración admitidos por el modelo.| FLOAT| Sí| 0.04 to (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04  
`batch_size`| El número de latentes de audio a generar en un solo lote (predeterminado: 1).| INT| Sí| 1 a 4096  
  
Nota: El valor de `seconds` se redondea a la trama de audio más cercana y se recorta a un mínimo de 1 trama y un máximo de `MAX_AUDIO_FRAMES` tramas, por lo que la longitud real del latente puede diferir ligeramente del valor exacto introducido.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`LATENT`| Un tensor latente de audio relleno de ceros con forma (batch_size, 128, latent_length). Incluye metadatos que marcan la muestra como datos de audio con una relación de reducción temporal de 512.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyMiniMaxMusic3LatentAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyMiniMaxMusic3LatentAudio)

[Latente AV MiniMax H3 Vacío](https://docs.comfy.org/es/built-in-nodes/EmptyMiniMaxH3LatentAV)[Video latente Mochi vacío](https://docs.comfy.org/es/built-in-nodes/EmptyMochiLatentVideo)
