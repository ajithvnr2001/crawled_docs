---
url: https://docs.comfy.org/es/built-in-nodes/VAEDecodeAudio/
title: Decodificaci\u00f3n de audio con VAE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:40.141302+00:00
---

# Decodificación de audio con VAE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VAEDecodeAudio/

Latente

# Decodificación de audio con VAE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo convierte una representación latente de audio de vuelta en una forma de onda de audio reproducible usando un autoencoder variacional (VAE).

Copiar páginaCopiar página

Este nodo convierte una representación latente de audio de vuelta en una forma de onda de audio reproducible usando un autoencoder variacional (VAE). Toma las muestras codificadas, las decodifica a través del VAE seleccionado y luego normaliza la forma de onda resultante para que el nivel de volumen general se mantenga constante. El audio de salida usa la frecuencia de muestreo de audio del VAE (44100 Hz por defecto), o la frecuencia de muestreo almacenada en las muestras de entrada cuando está presente.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`muestras`| Las muestras de audio codificadas en el espacio latente que se decodificarán de nuevo en una forma de onda de audio. Si las muestras tienen su propia frecuencia de muestreo, se usa ese valor para la salida.| LATENT| Sí| -  
`vae`| El modelo de autoencoder variacional (VAE) que se usa para decodificar las muestras latentes en audio. Su frecuencia de muestreo de salida de audio (44100 Hz por defecto) determina la frecuencia de muestreo de la forma de onda resultante cuando las muestras de entrada no especifican una.| VAE| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`AUDIO`| La forma de onda de audio decodificada con volumen normalizado, devuelta junto con su frecuencia de muestreo (la frecuencia de muestreo de las `samples` de entrada si está presente; de lo contrario, la frecuencia de muestreo de audio del VAE, 44100 Hz por defecto).| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VAEDecodeAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VAEDecodeAudio)

[Decodificación VAE](https://docs.comfy.org/es/built-in-nodes/VAEDecode)[Decodificación de audio con VAE (Mosaico)](https://docs.comfy.org/es/built-in-nodes/VAEDecodeAudioTiled)
