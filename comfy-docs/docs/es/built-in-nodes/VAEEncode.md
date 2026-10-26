---
url: https://docs.comfy.org/es/built-in-nodes/VAEEncode/
title: Codificaci\u00f3n VAE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:40.503198+00:00
---

# Codificación VAE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VAEEncode/

Latente

# Codificación VAE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para codificar imágenes en una representación de espacio latente utilizando un modelo VAE específico.

Copiar páginaCopiar página

Este nodo está diseñado para codificar imágenes en una representación de espacio latente utilizando un modelo VAE específico. Abstrae la complejidad del proceso de codificación, proporcionando una forma directa de transformar imágenes en sus representaciones latentes.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`píxeles`| El parámetro ‘pixels’ representa los datos de la imagen que se codificarán en el espacio latente. Desempeña un papel crucial en la determinación de la representación latente de salida al servir como entrada directa para el proceso de codificación.| `IMAGE`  
`vae`| El parámetro ‘vae’ especifica el modelo de Autoencoder Variacional que se utilizará para codificar los datos de la imagen en el espacio latente. Es esencial para definir el mecanismo de codificación y las características de la representación latente generada.| VAE  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La salida es una representación del espacio latente de la imagen de entrada, que encapsula sus características esenciales en una forma comprimida.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncode/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VAEEncode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VAEEncode)

[Decodificación VAE (Mosaico)](https://docs.comfy.org/es/built-in-nodes/VAEDecodeTiled)[Codificación de audio con VAE](https://docs.comfy.org/es/built-in-nodes/VAEEncodeAudio)
