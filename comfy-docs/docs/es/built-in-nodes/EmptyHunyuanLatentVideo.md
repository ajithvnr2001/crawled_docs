---
url: https://docs.comfy.org/es/built-in-nodes/EmptyHunyuanLatentVideo/
title: V\u00eddeo latente Hunyuan Video 1.0 vac\u00edo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:45.415079+00:00
---

# Vídeo latente Hunyuan Video 1.0 vacío - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyHunyuanLatentVideo/

Hunyuan Video

# Vídeo latente Hunyuan Video 1.0 vacío - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo EmptyHunyuanLatentVideo es similar al nodo EmptyLatentImage.

Copiar páginaCopiar página

El nodo `EmptyHunyuanLatentVideo` es similar al nodo `EmptyLatentImage`. Puede considerarse como un lienzo en blanco para la generación de video, donde el ancho, la altura y la longitud definen las propiedades del lienzo, y el tamaño del lote determina la cantidad de lienzos a crear. Este nodo crea lienzos vacíos listos para tareas posteriores de generación de video.

## 

​

Entradas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`ancho`| Ancho del video, valor predeterminado 848, mínimo 16, máximo `nodes.MAX_RESOLUTION`, tamaño de paso 16.| `INT`  
`altura`| Altura del video, valor predeterminado 480, mínimo 16, máximo `nodes.MAX_RESOLUTION`, tamaño de paso 16.| `INT`  
`longitud`| Longitud del video, valor predeterminado 25, mínimo 1, máximo `nodes.MAX_RESOLUTION`, tamaño de paso 4.| `INT`  
`tamaño_del_lote`| Tamaño del lote, valor predeterminado 1, mínimo 1, máximo 4096.| `INT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`samples`| Muestras de video latente generadas que contienen tensores cero, listas para tareas de procesamiento y generación.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyHunyuanLatentVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyHunyuanLatentVideo)

[Imagen latente Hunyuan vacía](https://docs.comfy.org/es/built-in-nodes/EmptyHunyuanImageLatent)[Vídeo latente Hunyuan Video 1.5 vacío](https://docs.comfy.org/es/built-in-nodes/EmptyHunyuanVideo15Latent)
