---
url: https://docs.comfy.org/es/built-in-nodes/EmptyLatentAudio/
title: Audio latente vac\u00edo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:45.806678+00:00
---

# Audio latente vacío - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyLatentAudio/

Latente

# Audio latente vacío - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Empty Latent Audio crea un tensor latente vacío para el procesamiento de audio.

Copiar páginaCopiar página

Empty Latent Audio crea un tensor latente vacío para el procesamiento de audio. Genera una representación latente de audio en blanco con una duración y un tamaño de lote especificados, que puede utilizarse como punto de partida para flujos de trabajo de generación o procesamiento de audio. El nodo calcula automáticamente las dimensiones latentes adecuadas basándose en la duración del audio y la frecuencia de muestreo.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`segundos`| La duración del audio en segundos (por defecto: 47.6)| FLOAT| Sí| 1.0 - 1000.0  
`tamaño_del_lote`| El número de imágenes latentes en el lote (por defecto: 1)| INT| Sí| 1 - 4096  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`LATENT`| Devuelve un tensor latente vacío para el procesamiento de audio con la duración y el tamaño de lote especificados. El tensor tiene una forma de [batch_size, 64, length], donde length se calcula a partir de la duración del audio y la frecuencia de muestreo. La salida también incluye metadatos que indican que el tipo es “audio” y una relación de reducción temporal de 2048.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `6ca63d26febe2d87ff751a57044eb81b553b19756f4b3f9478ecb5a733ec0041`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyLatentAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyLatentAudio)

[Audio latent vacío de YuE2](https://docs.comfy.org/es/built-in-nodes/EmptyYuE2LatentAudio)[Imagen latente vacía](https://docs.comfy.org/es/built-in-nodes/EmptyLatentImage)
