---
url: https://docs.comfy.org/es/built-in-nodes/TextEncodeZImageOmni/
title: Codificar texto ZImage Omni - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:35.914119+00:00
---

# Codificar texto ZImage Omni - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TextEncodeZImageOmni/

Z Image

# Codificar texto ZImage Omni - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

TextEncodeZImageOmni codifica un prompt de texto junto con hasta tres imágenes de referencia opcionales en un formato de condicionamiento para modelos de

Copiar páginaCopiar página

TextEncodeZImageOmni codifica un prompt de texto junto con hasta tres imágenes de referencia opcionales en un formato de condicionamiento para modelos de generación de imágenes. El prompt se tokeniza y se codifica con el modelo CLIP, y cada imagen conectada puede procesarse opcionalmente mediante un codificador de visión y/o un VAE para que las referencias visuales se integren junto con el texto. Este nodo está marcado como experimental.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP utilizado para tokenizar y codificar el prompt de texto.| CLIP| Sí|   
`codificador_de_imagen`| Un modelo codificador de visión opcional. Si se proporciona, se utiliza para codificar las imágenes de entrada y los embeddings resultantes se añaden al condicionamiento.| CLIP_VISION| No|   
`instrucción`| El prompt de texto que se va a codificar. Admite entrada multilínea y prompts dinámicos.| STRING| Sí|   
`auto_redimensionar_imágenes`| Cuando está habilitado (predeterminado: True), las imágenes de entrada se redimensionan automáticamente antes de la codificación VAE para que su área total en píxeles se acerque a 1024x1024, con las dimensiones redondeadas a múltiplos de 8.| BOOLEAN| Sí| True  
False  
`vae`| Un modelo VAE opcional. Si se proporciona, se utiliza para codificar las imágenes de entrada en representaciones latentes, que se añaden al condicionamiento como latentes de referencia.| VAE| No|   
`imagen1`| La primera imagen de referencia opcional.| IMAGE| No|   
`imagen2`| La segunda imagen de referencia opcional.| IMAGE| No|   
`imagen3`| La tercera imagen de referencia opcional.| IMAGE| No|   
  
**Nota:** El nodo acepta un máximo de tres imágenes (`image1`, `image2`, `image3`). Las entradas `image_encoder` y `vae` solo se utilizan cuando se proporciona al menos una imagen; cuando ambas están conectadas, cada imagen es procesada por ambas. Cuando `auto_resize_images` es True y hay un `vae` conectado, las imágenes se redimensionan para tener un área total en píxeles cercana a 1024x1024 antes de la codificación. Si no se proporciona ninguna imagen, solo se codifica el prompt de texto.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`CONDITIONING`| La salida final de condicionamiento. Contiene el prompt de texto codificado y, cuando se proporcionan imágenes, puede incluir embeddings de imágenes codificados, latentes de referencia y embeddings de texto adicionales derivados de la plantilla de marcador de posición de imagen.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/es.md)

* * *

**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TextEncodeZImageOmni.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TextEncodeZImageOmni)

[YuE2 Generar música](https://docs.comfy.org/es/built-in-nodes/YuE2GenerateMusic)[Codificar con codificador de audio](https://docs.comfy.org/es/built-in-nodes/AudioEncoderEncode)
