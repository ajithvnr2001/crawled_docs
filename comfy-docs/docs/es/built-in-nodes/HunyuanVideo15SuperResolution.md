---
url: https://docs.comfy.org/es/built-in-nodes/HunyuanVideo15SuperResolution/
title: HunyuanVideo 1.5 super resoluci\u00f3n - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:54.110480+00:00
---

# HunyuanVideo 1.5 super resolución - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HunyuanVideo15SuperResolution/

Hunyuan Video

# HunyuanVideo 1.5 super resolución - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo HunyuanVideo15SuperResolution prepara datos de condicionamiento para un proceso de superresolución de video.

Copiar páginaCopiar página

El nodo HunyuanVideo15SuperResolution prepara datos de condicionamiento para un proceso de superresolución de video. Toma una representación latente de un video y, opcionalmente, una imagen inicial, y los empaqueta junto con aumento de ruido y datos de visión CLIP en un formato que puede ser utilizado por un modelo para generar una salida de mayor resolución.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`positivo`| La entrada de condicionamiento positivo que se modificará con datos latentes y de aumento.| CONDITIONING| Sí| N/A  
`negativo`| La entrada de condicionamiento negativo que se modificará con datos latentes y de aumento.| CONDITIONING| Sí| N/A  
`vae`| El VAE utilizado para codificar la `start_image` opcional. Requerido si se proporciona `start_image`.| VAE| No| N/A  
`imagen_inicial`| Una imagen inicial opcional para guiar la superresolución. Si se proporciona, se amplía y se codifica en el latente de condicionamiento.| IMAGE| No| N/A  
`clip_vision_output`| Incrustaciones de visión CLIP opcionales para añadir al condicionamiento.| CLIP_VISION_OUTPUT| No| N/A  
`latente`| La representación latente de video de entrada que se incorpora al condicionamiento.| LATENT| Sí| N/A  
`aumento_de_ruido`| La fuerza del aumento de ruido a aplicar al condicionamiento (predeterminado: 0.70). Este es un parámetro avanzado.| FLOAT| Sí| 0.0 - 1.0 (step 0.01)  
  
**Nota:** Si se proporciona una `start_image`, también debe conectarse un `vae` para que pueda codificarse. La `start_image` se amplía automáticamente a 16 veces las dimensiones espaciales (ancho y alto) del `latent` de entrada, luego se codifica y se coloca en el latente de condicionamiento. Solo se utilizan los canales RGB de la `start_image` para la codificación.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positive`| El condicionamiento positivo modificado, que ahora contiene el latente concatenado, el aumento de ruido y los datos opcionales de visión CLIP.| CONDITIONING  
`negative`| El condicionamiento negativo modificado, que ahora contiene el latente concatenado, el aumento de ruido y los datos opcionales de visión CLIP.| CONDITIONING  
`latente`| El latente de entrada se pasa sin cambios.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/es.md)

* * *

**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HunyuanVideo15SuperResolution.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HunyuanVideo15SuperResolution)

[HunyuanVideo 1.5 imagen a video](https://docs.comfy.org/es/built-in-nodes/HunyuanVideo15ImageToVideo)[Codificar texto HunyuanVideo imagen a video](https://docs.comfy.org/es/built-in-nodes/TextEncodeHunyuanVideo_ImageToVideo)
