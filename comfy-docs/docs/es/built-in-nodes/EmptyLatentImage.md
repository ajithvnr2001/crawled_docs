---
url: https://docs.comfy.org/es/built-in-nodes/EmptyLatentImage/
title: Imagen latente vac\u00eda - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:45.742442+00:00
---

# Imagen latente vacía - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyLatentImage/

Latente

# Imagen latente vacía - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo EmptyLatentImage está diseñado para generar una representación de espacio latente en blanco con dimensiones y tamaño de lote especificados.

Copiar páginaCopiar página

El nodo `EmptyLatentImage` está diseñado para generar una representación de espacio latente en blanco con dimensiones y tamaño de lote especificados. Este nodo sirve como paso fundamental en la generación o manipulación de imágenes en el espacio latente, proporcionando un punto de partida para procesos posteriores de síntesis o modificación de imágenes.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`ancho`| Especifica el ancho de la imagen latente a generar. Este parámetro influye directamente en las dimensiones espaciales de la representación latente resultante.| `INT`  
`altura`| Determina la altura de la imagen latente a generar. Este parámetro es crucial para definir las dimensiones espaciales de la representación del espacio latente.| `INT`  
`tamaño_del_lote`| Controla la cantidad de imágenes latentes a generar en un solo lote. Esto permite la generación simultánea de múltiples representaciones latentes, facilitando el procesamiento por lotes.| `INT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`latent`| La salida es un tensor que representa un lote de imágenes latentes en blanco, que sirve como base para la generación o manipulación adicional de imágenes en el espacio latente.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentImage/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyLatentImage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyLatentImage)

[Audio latente vacío](https://docs.comfy.org/es/built-in-nodes/EmptyLatentAudio)[Obtener tamaño del latent de audio](https://docs.comfy.org/es/built-in-nodes/GetAudioLatentSize)
