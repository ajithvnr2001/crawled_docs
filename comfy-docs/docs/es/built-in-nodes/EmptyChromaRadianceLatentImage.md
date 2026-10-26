---
url: https://docs.comfy.org/es/built-in-nodes/EmptyChromaRadianceLatentImage/
title: Imagen latente Chroma Radiance vac\u00eda - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:45.193669+00:00
---

# Imagen latente Chroma Radiance vacía - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyChromaRadianceLatentImage/

Chroma Radiance

# Imagen latente Chroma Radiance vacía - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo EmptyChromaRadianceLatentImage crea una imagen latente en blanco con las dimensiones que especifiques

Copiar páginaCopiar página

El nodo EmptyChromaRadianceLatentImage crea una imagen latente en blanco con las dimensiones que especifiques, para usarla en flujos de trabajo de chroma radiance. Produce un tensor lleno de ceros que actúa como punto de partida para operaciones en el espacio latente, permitiéndote definir el ancho, la altura y el tamaño de lote de la imagen latente vacía.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`ancho`| El ancho de la imagen latente en píxeles (predeterminado: 1024)| INT| Sí| 16 a MAX_RESOLUTION  
`alto`| La altura de la imagen latente en píxeles (predeterminado: 1024)| INT| Sí| 16 a MAX_RESOLUTION  
`tamaño_lote`| El número de imágenes latentes a generar en un lote (predeterminado: 1)| INT| Sí| 1 a 4096  
  
Nota: `width` y `height` se definen con un paso de 16, por lo que los valores se ajustan en múltiplos de 16.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`samples`| El tensor de imagen latente vacía generado, relleno de ceros, con la forma batch_size x 3 x height x width| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/es.md)

* * *

**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyChromaRadianceLatentImage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyChromaRadianceLatentImage)

[Reemplazar fotogramas de latente de video](https://docs.comfy.org/es/built-in-nodes/ReplaceVideoLatentFrames)[Vídeo latente Cosmos vacío](https://docs.comfy.org/es/built-in-nodes/EmptyCosmosLatentVideo)
