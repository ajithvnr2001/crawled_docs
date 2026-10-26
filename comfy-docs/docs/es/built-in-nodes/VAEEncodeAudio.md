---
url: https://docs.comfy.org/es/built-in-nodes/VAEEncodeAudio/
title: Codificaci\u00f3n de audio con VAE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:40.922122+00:00
---

# Codificación de audio con VAE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VAEEncodeAudio/

Latente

# Codificación de audio con VAE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VAE Encode Audio convierte datos de audio en una representación latente utilizando un autoencoder variacional (VAE).

Copiar páginaCopiar página

El nodo VAE Encode Audio convierte datos de audio en una representación latente utilizando un autoencoder variacional (VAE). Procesa el audio de entrada a través del VAE para producir muestras latentes comprimidas que pueden usarse para tareas posteriores de generación o manipulación de audio. Si la frecuencia de muestreo del audio difiere de la frecuencia de muestreo esperada por el VAE, el audio se remuestrea automáticamente antes de la codificación.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`audio`| Los datos de audio a codificar, que contienen la forma de onda y la información de frecuencia de muestreo| AUDIO| Sí| -  
`vae`| El modelo de autoencoder variacional utilizado para codificar el audio en el espacio latente| VAE| Sí| -  
  
**Nota:** La entrada de audio se remuestrea automáticamente para coincidir con la frecuencia de muestreo esperada por el VAE (predeterminada: 44100 Hz) si la frecuencia de muestreo original difiere de este valor. Si el audio de entrada es None (por ejemplo, cuando el video de origen no tiene pista de audio), el nodo generará un error.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`LATENT`| La representación de audio codificada en el espacio latente, que contiene muestras comprimidas| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `224563af40a377a37209b26ec8becf035560da273b18293634f684e18c5e63ed`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VAEEncodeAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VAEEncodeAudio)

[Codificación VAE](https://docs.comfy.org/es/built-in-nodes/VAEEncode)[Codificación VAE (para inpainting)](https://docs.comfy.org/es/built-in-nodes/VAEEncodeForInpaint)
