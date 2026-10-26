---
url: https://docs.comfy.org/es/built-in-nodes/EmptyLTXVLatentVideo/
title: V\u00eddeo latente LTXV vac\u00edo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:45.586514+00:00
---

# Vídeo latente LTXV vacío - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyLTXVLatentVideo/

Ltxv

# Vídeo latente LTXV vacío - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo EmptyLTXVLatentVideo crea un tensor de video latente vacío (relleno de ceros) utilizando el ancho, alto, longitud y tamaño de lote que especifiques.

Copiar páginaCopiar página

El nodo EmptyLTXVLatentVideo crea un tensor de video latente vacío (relleno de ceros) utilizando el ancho, alto, longitud y tamaño de lote que especifiques. Proporciona un punto de partida en blanco para flujos de trabajo de generación de video LTXV, con las dimensiones latentes comprimidas automáticamente en relación con el tamaño de video solicitado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`ancho`| El ancho del tensor de video latente (predeterminado: 768, paso: 32)| INT| Sí| 64 a MAX_RESOLUTION  
`altura`| La altura del tensor de video latente (predeterminado: 512, paso: 32)| INT| Sí| 64 a MAX_RESOLUTION  
`longitud`| El número de fotogramas en el video latente (predeterminado: 97, paso: 8)| INT| Sí| 1 a MAX_RESOLUTION  
`tamaño_del_lote`| El número de videos latentes a generar en un lote (predeterminado: 1)| INT| Sí| 1 a 4096  
  
Nota: El video latente está comprimido en comparación con las dimensiones solicitadas: las dimensiones espaciales (ancho y alto) se dividen entre 32, y el recuento de fotogramas (length) se divide entre 8 y se redondea hacia arriba al número entero más cercano. Los valores de paso para width, height y length ayudan a que estas divisiones sean exactas.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`samples`| El tensor latente vacío generado con valores cero en las dimensiones especificadas, junto con una relación de reducción espacial de 32| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyLTXVLatentVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyLTXVLatentVideo)

[Reescalado de latente Hunyuan Video 1.5 con modelo](https://docs.comfy.org/es/built-in-nodes/HunyuanVideo15LatentUpscaleWithModel)[Decodificar LTXV audio VAE](https://docs.comfy.org/es/built-in-nodes/LTXVAudioVAEDecode)
