---
url: https://docs.comfy.org/es/built-in-nodes/VAEDecode/
title: Decodificaci\u00f3n VAE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:40.051309+00:00
---

# Decodificación VAE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VAEDecode/

Latente

# Decodificación VAE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VAEDecode está diseñado para decodificar representaciones latentes en imágenes utilizando un Autoencoder Variacional (VAE) específico.

Copiar páginaCopiar página

El nodo VAEDecode está diseñado para decodificar representaciones latentes en imágenes utilizando un Autoencoder Variacional (VAE) específico. Su propósito es generar imágenes a partir de representaciones de datos comprimidos, facilitando la reconstrucción de imágenes desde sus codificaciones en el espacio latente.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras`| El parámetro ‘samples’ representa las representaciones latentes que se decodificarán en imágenes. Es crucial para el proceso de decodificación, ya que proporciona los datos comprimidos a partir de los cuales se reconstruyen las imágenes.| `LATENT`  
`vae`| El parámetro ‘vae’ especifica el modelo de Autoencoder Variacional que se utilizará para decodificar las representaciones latentes en imágenes. Es esencial para determinar el mecanismo de decodificación y la calidad de las imágenes reconstruidas.| VAE  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`image`| La salida es una imagen reconstruida a partir de la representación latente proporcionada, utilizando el modelo VAE especificado.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VAEDecode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VAEDecode)

[Recortar latente de video](https://docs.comfy.org/es/built-in-nodes/TrimVideoLatent)[Decodificación de audio con VAE](https://docs.comfy.org/es/built-in-nodes/VAEDecodeAudio)
