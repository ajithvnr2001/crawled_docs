---
url: https://docs.comfy.org/es/built-in-nodes/LTXVAudioVAEDecode/
title: Decodificar LTXV audio VAE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:00.457220+00:00
---

# Decodificar LTXV audio VAE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LTXVAudioVAEDecode/

Ltxv

# Decodificar LTXV audio VAE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LTXV Audio VAE Decode convierte una representación latente de audio de vuelta a una forma de onda de audio.

Copiar páginaCopiar página

El nodo LTXV Audio VAE Decode convierte una representación latente de audio de vuelta a una forma de onda de audio. Utiliza un modelo Audio VAE especializado para realizar este proceso de decodificación, produciendo una salida de audio con su frecuencia de muestreo asociada.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`samples`| El latente a decodificar.| LATENT| Sí| N/A  
`audio_vae`| El modelo Audio VAE utilizado para decodificar el latente.| VAE| Sí| N/A  
  
**Nota:** Si el latente proporcionado está anidado (contiene múltiples latentes), el nodo utiliza automáticamente el último latente de la secuencia para la decodificación.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`Audio`| La forma de onda de audio decodificada y su frecuencia de muestreo asociada. La forma de onda se coloca en el mismo dispositivo que el latente de entrada, y la frecuencia de muestreo está determinada por el modelo Audio VAE.| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/es.md)

* * *

**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LTXVAudioVAEDecode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LTXVAudioVAEDecode)

[Vídeo latente LTXV vacío](https://docs.comfy.org/es/built-in-nodes/EmptyLTXVLatentVideo)[Codificar LTXV audio VAE](https://docs.comfy.org/es/built-in-nodes/LTXVAudioVAEEncode)
