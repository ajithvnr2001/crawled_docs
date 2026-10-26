---
url: https://docs.comfy.org/es/built-in-nodes/EmptyARVideoLatent/
title: EmptyARVideoLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:44.735026+00:00
---

# EmptyARVideoLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyARVideoLatent/

Autorregresivo

# EmptyARVideoLatent - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo EmptyARVideoLatent crea una representación latente vacía para la generación de video.

Copiar páginaCopiar página

El nodo EmptyARVideoLatent crea una representación latente vacía para la generación de video. Construye un tensor de ceros usando el ancho, la altura, la cantidad de fotogramas y el tamaño de lote solicitados, que luego puede usarse para inicializar un proceso de generación de video.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`width`| El ancho de los fotogramas de video en píxeles (predeterminado: 832)| INT| Sí| 16 a 8192 (paso: 16)  
`height`| La altura de los fotogramas de video en píxeles (predeterminado: 480)| INT| Sí| 16 a 8192 (paso: 16)  
`length`| La cantidad de fotogramas en el video (predeterminado: 81)| INT| Sí| 1 a 1024 (paso: 4)  
`batch_size`| La cantidad de videos a generar en un solo lote (predeterminado: 1)| INT| Sí| 1 a 64  
  
Nota: El tamaño latente interno se deriva de estas entradas. `width` y `height` se dividen entre 8, y la cantidad de pasos de tiempo latentes se calcula como `((length - 1) // 4) + 1`.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`LATENT`| Un tensor latente lleno de ceros, que representa un espacio latente de video vacío con las dimensiones, longitud y tamaño de lote especificados. La forma del tensor es [batch_size, 16, lat_t, height/8, width/8], donde lat_t = ((length - 1) // 4) + 1 es la cantidad de pasos de tiempo latentes derivados de la longitud solicitada.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/es.md)

* * *

**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyARVideoLatent.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyARVideoLatent)

[Restar latentes](https://docs.comfy.org/es/built-in-nodes/LatentSubtract)[Procesar latentes por lotes](https://docs.comfy.org/es/built-in-nodes/BatchLatentsNode)
