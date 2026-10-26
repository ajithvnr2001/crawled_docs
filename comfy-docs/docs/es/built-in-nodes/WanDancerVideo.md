---
url: https://docs.comfy.org/es/built-in-nodes/WanDancerVideo/
title: WanDancerVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:45.424320+00:00
---

# WanDancerVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WanDancerVideo/

Dancer

# WanDancerVideo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo WanDancerVideo prepara datos de condicionamiento y un tensor latente vacío para la generación de video con el modelo WanDancer.

Copiar páginaCopiar página

El nodo WanDancerVideo prepara datos de condicionamiento y un tensor latente vacío para la generación de video con el modelo WanDancer. Adjunta imágenes iniciales opcionales, máscaras, incrustaciones de visión CLIP y características de audio al condicionamiento positivo y negativo para que puedan guiar el video generado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`positivo`| El condicionamiento positivo para guiar la generación de video.| CONDITIONING| Sí|   
`negativo`| El condicionamiento negativo para guiar la generación de video.| CONDITIONING| Sí|   
`vae`| El VAE utilizado para codificar la imagen inicial en el espacio latente.| VAE| Sí|   
`ancho`| El ancho del video generado en píxeles (predeterminado: 480).| INT| Sí| 16 to MAX_RESOLUTION (step: 16)  
`alto`| La altura del video generado en píxeles (predeterminado: 832).| INT| Sí| 16 to MAX_RESOLUTION (step: 16)  
`longitud`| El número de fotogramas en el video generado. Debe permanecer en 149 para WanDancer (predeterminado: 149).| INT| Sí| 1 to MAX_RESOLUTION (step: 4)  
`clip_vision_output`| Las incrustaciones de visión CLIP para el primer fotograma.| CLIP_VISION_OUTPUT| No|   
`clip_vision_output_ref`| Las incrustaciones de visión CLIP para la imagen de referencia.| CLIP_VISION_OUTPUT| No|   
`imagen_inicial`| La(s) imagen(es) inicial(es) a codificar; puede ser cualquier número de fotogramas.| IMAGE| No|   
`máscara`| Máscara de condicionamiento de imagen para la(s) imagen(es) inicial(es). El blanco se conserva, el negro se genera. Se usa para las generaciones locales.| MASK| No|   
`audio_encoder_output`| Una salida del codificador de audio que proporciona características de audio, frecuencia de fotogramas y valores de escala de inyección, que se adjuntan al condicionamiento cuando se proporcionan.| AUDIO_ENCODER_OUTPUT| No|   
  
### 

​

Notas sobre el comportamiento de los parámetros

  * `start_image` es opcional. Cuando se proporciona, se redimensiona a `width` y `height`, se codifica con el `vae` y se adjunta tanto al condicionamiento positivo como al negativo. Si `start_image` tiene más fotogramas que `length`, los fotogramas adicionales se descartan. Si tiene menos fotogramas, los faltantes se rellenan con valores cero.
  * `mask` solo tiene efecto cuando también se proporciona `start_image`. Las áreas blancas se conservan y las áreas negras se generan.
  * `clip_vision_output_ref` solo tiene efecto cuando también se proporciona `clip_vision_output`.
  * `audio_encoder_output`, cuando se proporciona, adjunta incrustaciones de audio, frecuencia de fotogramas y escala de inyección tanto al condicionamiento positivo como al negativo.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positivo`| El condicionamiento positivo con cualquier latente de imagen inicial, máscara, visión CLIP o datos de audio adjuntos.| CONDITIONING  
`negativo`| El condicionamiento negativo con cualquier latente de imagen inicial, máscara, visión CLIP o datos de audio adjuntos.| CONDITIONING  
`latente`| Un tensor latente vacío dimensionado para la longitud, altura y ancho de video solicitados.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WanDancerVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WanDancerVideo)

[WanDancerEncodeAudio](https://docs.comfy.org/es/built-in-nodes/WanDancerEncodeAudio)[Wan 2.2 FunControl a video](https://docs.comfy.org/es/built-in-nodes/Wan22FunControlToVideo)
