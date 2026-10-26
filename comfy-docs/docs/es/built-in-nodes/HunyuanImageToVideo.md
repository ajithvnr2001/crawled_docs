---
url: https://docs.comfy.org/es/built-in-nodes/HunyuanImageToVideo/
title: Hunyuan imagen a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:53.807559+00:00
---

# Hunyuan imagen a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HunyuanImageToVideo/

Hunyuan Video

# Hunyuan imagen a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo HunyuanImageToVideo convierte imágenes en representaciones latentes de video usando el modelo de video Hunyuan.

Copiar páginaCopiar página

El nodo HunyuanImageToVideo convierte imágenes en representaciones latentes de video usando el modelo de video Hunyuan. Toma entradas de condicionamiento e imágenes iniciales opcionales para generar latentes de video que pueden ser procesados posteriormente por modelos de generación de video. El nodo admite diferentes tipos de guía para controlar cómo la imagen inicial influye en el proceso de generación de video.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`positivo`| Entrada de condicionamiento positivo para guiar la generación de video| CONDITIONING| Sí| -  
`vae`| Modelo VAE utilizado para codificar imágenes en el espacio latente| VAE| Sí| -  
`ancho`| Ancho del video de salida en píxeles (predeterminado: 848, paso: 16)| INT| Sí| 16 a MAX_RESOLUTION  
`altura`| Alto del video de salida en píxeles (predeterminado: 480, paso: 16)| INT| Sí| 16 a MAX_RESOLUTION  
`longitud`| Número de fotogramas del video de salida (predeterminado: 53, paso: 4)| INT| Sí| 1 a MAX_RESOLUTION  
`tamaño_del_lote`| Número de videos a generar simultáneamente (predeterminado: 1)| INT| Sí| 1 a 4096  
`tipo_de_orientación`| Método para incorporar la imagen inicial en la generación de video (predeterminado: “v1 (concat)”). Opción avanzada| COMBO| Sí| ”v1 (concat)"  
"v2 (replace)"  
"custom”  
`imagen_inicial`| Imagen inicial opcional (o secuencia de imágenes) para inicializar la generación de video. Solo se utilizan los primeros `length` fotogramas y los primeros 3 canales de color| IMAGE| No| -  
  
**Nota:** Cuando se proporciona `start_image`, el nodo utiliza diferentes métodos de guía según el `guidance_type` seleccionado:

  * “v1 (concat)”: Concatena el latente de la imagen con el latente del video y aplica una máscara para mezclar la imagen en el video
  * “v2 (replace)”: Reemplaza los fotogramas iniciales del video con el latente de la imagen y aplica una máscara de ruido
  * “custom”: Utiliza la imagen como un latente de referencia para la guía

Si no se proporciona `start_image`, no se agrega condicionamiento de guía y el latente se devuelve como un bloque simple de ceros.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positive`| Condicionamiento positivo modificado con guía de imagen aplicada cuando se proporciona `start_image`| CONDITIONING  
`latent`| Representación latente de video lista para su posterior procesamiento por modelos de generación de video| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HunyuanImageToVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HunyuanImageToVideo)

[Codificar texto CLIP para Hunyuan Image](https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeHunyuanDiT)[Refinador de latentes Hunyuan](https://docs.comfy.org/es/built-in-nodes/HunyuanRefinerLatent)
