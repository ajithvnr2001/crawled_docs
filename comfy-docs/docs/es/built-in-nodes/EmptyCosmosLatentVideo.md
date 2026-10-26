---
url: https://docs.comfy.org/es/built-in-nodes/EmptyCosmosLatentVideo/
title: V\u00eddeo latente Cosmos vac\u00edo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:45.089673+00:00
---

# Vídeo latente Cosmos vacío - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyCosmosLatentVideo/

Cosmos

# Vídeo latente Cosmos vacío - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

EmptyCosmosLatentVideo crea un tensor de video latente vacío con las dimensiones especificadas.

Copiar páginaCopiar página

EmptyCosmosLatentVideo crea un tensor de video latente vacío con las dimensiones especificadas. Genera una representación latente rellena de ceros que puede utilizarse como punto de partida para flujos de trabajo de generación de video, con parámetros configurables de ancho, alto, duración y tamaño de lote.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`ancho`| El ancho del video latente en píxeles (predeterminado: 1280, incrementos de 16)| INT| Sí| 16 a MAX_RESOLUTION  
`altura`| El alto del video latente en píxeles (predeterminado: 704, incrementos de 16)| INT| Sí| 16 a MAX_RESOLUTION  
`longitud`| El número de fotogramas del video latente (predeterminado: 121, incrementos de 8)| INT| Sí| 1 a MAX_RESOLUTION  
`tamaño_del_lote`| El número de videos latentes a generar en un lote (predeterminado: 1)| INT| No| 1 a 4096  
  
Nota: El tensor latente se submuestrea espacialmente por un factor de 8 tanto en alto como en ancho, y contiene 16 canales. El número de fotogramas temporales latentes se calcula como `((length - 1) // 8) + 1`.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`samples`| El tensor de video latente vacío generado, con valores cero| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyCosmosLatentVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyCosmosLatentVideo)

[Imagen latente Chroma Radiance vacía](https://docs.comfy.org/es/built-in-nodes/EmptyChromaRadianceLatentImage)[Latente Flux 2 vacío](https://docs.comfy.org/es/built-in-nodes/EmptyFlux2LatentImage)
