---
url: https://docs.comfy.org/es/built-in-nodes/EmptyHunyuanImageLatent/
title: Imagen latente Hunyuan vac\u00eda - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:45.269756+00:00
---

# Imagen latente Hunyuan vacía - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyHunyuanImageLatent/

Hunyuan Image

# Imagen latente Hunyuan vacía - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo EmptyHunyuanImageLatent crea un espacio latente en blanco, con todos los valores en cero, para los modelos de generación de imágenes Hunyuan.

Copiar páginaCopiar página

El nodo EmptyHunyuanImageLatent crea un espacio latente en blanco, con todos los valores en cero, para los modelos de generación de imágenes Hunyuan. Produce un latente inicial vacío usando el `width`, `height` y `batch_size` proporcionados, que luego puede pasarse a los nodos posteriores del flujo de trabajo. El tensor latente contiene 64 canales, y cada dimensión espacial es igual a la dimensión de píxeles correspondiente dividida por 32.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`ancho`| El ancho de la imagen latente generada en píxeles (predeterminado: 2048, paso: 32)| INT| Sí| 64 a MAX_RESOLUTION  
`alto`| El alto de la imagen latente generada en píxeles (predeterminado: 2048, paso: 32)| INT| Sí| 64 a MAX_RESOLUTION  
`tamaño_lote`| El número de muestras latentes que se generarán en un lote (predeterminado: 1)| INT| Sí| 1 a 4096  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`LATENT`| Un tensor latente vacío con 64 canales y dimensiones de alto ÷ 32 por ancho ÷ 32, listo para el procesamiento de imágenes de Hunyuan| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/es.md)

* * *

**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyHunyuanImageLatent.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyHunyuanImageLatent)

[Decodificación VAE de Hunyuan 3D](https://docs.comfy.org/es/built-in-nodes/VAEDecodeHunyuan3D)[Vídeo latente Hunyuan Video 1.0 vacío](https://docs.comfy.org/es/built-in-nodes/EmptyHunyuanLatentVideo)
