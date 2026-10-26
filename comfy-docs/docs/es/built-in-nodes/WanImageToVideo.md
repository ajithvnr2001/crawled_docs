---
url: https://docs.comfy.org/es/built-in-nodes/WanImageToVideo/
title: Wan imagen a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:46.144502+00:00
---

# Wan imagen a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WanImageToVideo/

Wan

# Wan imagen a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo WanImageToVideo prepara representaciones de condicionamiento y latentes para la generación de video.

Copiar páginaCopiar página

El nodo WanImageToVideo prepara representaciones de condicionamiento y latentes para la generación de video. Crea un espacio latente vacío para el video y puede incorporar opcionalmente una imagen inicial y una salida de visión CLIP para guiar la generación. Tanto las entradas de condicionamiento `positive` como `negative` se actualizan con la imagen y los datos de visión proporcionados.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`positivo`| Entrada de condicionamiento positiva utilizada para guiar la generación| CONDITIONING| Sí| -  
`negativo`| Entrada de condicionamiento negativa utilizada para guiar la generación| CONDITIONING| Sí| -  
`vae`| Modelo VAE utilizado para codificar imágenes en el espacio latente| VAE| Sí| -  
`ancho`| Ancho del video generado (predeterminado: 832, paso: 16)| INT| Sí| 16 a MAX_RESOLUTION  
`altura`| Alto del video generado (predeterminado: 480, paso: 16)| INT| Sí| 16 a MAX_RESOLUTION  
`longitud`| Número de fotogramas del video (predeterminado: 81, paso: 4)| INT| Sí| 1 a MAX_RESOLUTION  
`tamaño_del_lote`| Número de videos que se generarán en un lote (predeterminado: 1)| INT| Sí| 1 a 4096  
`salida_de_vision_clip`| Salida de visión CLIP opcional añadida como condicionamiento adicional tanto a las entradas positiva como negativa| CLIP_VISION_OUTPUT| No| -  
`imagen_inicial`| Imagen inicial opcional utilizada para inicializar el video. Cuando se proporciona, se redimensiona al `width` y `height` especificados y se coloca al principio de la secuencia de fotogramas; los fotogramas más allá de `length` se ignoran. Los fotogramas restantes se rellenan con valores de gris neutro (0.5), a menos que se proporcione `ref_pad_image`.| IMAGE| No| -  
`ref_pad_image`| Imagen de referencia opcional cuyo primer fotograma sustituye el relleno de gris neutro de la secuencia de fotogramas. Se redimensiona al `width` y `height` especificados y solo se utiliza la primera imagen del lote. Solo tiene efecto cuando también se proporciona `start_image`.| IMAGE| No| -  
  
**Nota:** Cuando se proporciona `start_image`, la secuencia de fotogramas se codifica con el VAE y se aplica una máscara al condicionamiento. La máscara se establece en 0 para los fotogramas cubiertos por la imagen inicial y en 1 para los fotogramas restantes, de modo que la generación continúa desde la imagen proporcionada. Durante la codificación solo se utilizan los primeros tres canales de color (RGB) de la imagen. Tanto el condicionamiento positivo como el negativo reciben la misma imagen latente concatenada, la máscara y (si se proporciona) la salida de visión CLIP. Cuando se proporciona `ref_pad_image` junto con `start_image`, su primer fotograma se redimensiona al `width` y `height` y se escribe en los canales RGB de los fotogramas de relleno antes de colocar encima la imagen inicial, de modo que el relleno lleva la imagen de referencia en lugar de gris plano. Se trata de un relleno anti-deriva estilo SVI, utilizado por modelos como ID-V2V.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`positive`| Condicionamiento positivo, actualizado con la imagen y los datos de visión| CONDITIONING  
`negative`| Condicionamiento negativo, actualizado con la imagen y los datos de visión| CONDITIONING  
`latent`| Tensor latente vacío listo para la generación de video, con forma [batch_size, 16, ((length-1)//4)+1, height//8, width//8]| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `3000c1c816d2c123fc5bc46ea1f193c52c0f81a2f8c4a9110d8a4fa909185aea`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WanImageToVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WanImageToVideo)

[Wan primer-último fotograma a video](https://docs.comfy.org/es/built-in-nodes/WanFirstLastFrameToVideo)[SheetSage2 Audio a ABC](https://docs.comfy.org/es/built-in-nodes/SheetSage2AudioToABC)
