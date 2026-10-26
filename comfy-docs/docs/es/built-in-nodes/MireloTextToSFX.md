---
url: https://docs.comfy.org/es/built-in-nodes/MireloTextToSFX/
title: Mirelo de texto a SFX - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:12.251115+00:00
---

# Mirelo de texto a SFX - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MireloTextToSFX/

Audio

# Mirelo de texto a SFX - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera un efecto de sonido a partir de una descripción textual con Mirelo SFX.

Copiar páginaCopiar página

Genera un efecto de sonido a partir de una descripción textual con Mirelo SFX. Describe el sonido en sí, no la imagen a la que pertenece, y el nodo devuelve una única pista de audio de la duración solicitada. Úsalo para foley, ambientes, impactos y texturas musicales breves sin grabar ni subir vídeo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| Modelo a utilizar. Al seleccionar un modelo se muestran los parámetros específicos de este: `prompt`, `negative_prompt`, `duration` y `seed`.| DYNAMIC_COMBO| Sí| `"sfx-2.0"`  
`prompt`| Describe el sonido, no la imagen. De 1 a 2000 caracteres.| STRING| Sí| 1 a 2000 caracteres  
`negative_prompt`| Sonidos que se deben evitar, como una lista breve separada por comas. Puede dejarse vacío (predeterminado: vacío). Máximo 1000 caracteres.| STRING| Sí| Hasta 1000 caracteres  
`duration`| Duración del sonido en segundos. (predeterminado: 5.0)| FLOAT| Sí| 0.1 a 600.0 (paso 0.1)  
`seed`| La semilla para la solicitud. Los resultados no son deterministas, por lo que la misma semilla no repite un sonido. (predeterminado: 42)| INT| Sí| 0 a 4294967295  
  
El nodo se detiene con un error cuando `prompt` está vacío o tiene más de 2000 caracteres, y cuando `negative_prompt` tiene más de 1000 caracteres.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`AUDIO`| El efecto de sonido generado, con la duración de `duration`.| AUDIO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MireloTextToSFX/es.md)

* * *

**Source fingerprint (SHA-256):** `b09a9562cea636702acd9fc50feb38b272a558f8b8509da21f5fada2abd9fd48`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MireloTextToSFX.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MireloTextToSFX)

[Texto a voz de HeyGen Voice 1.0](https://docs.comfy.org/es/built-in-nodes/HeyGenVoiceTextToSpeechNode)[Mirelo de vídeo a SFX](https://docs.comfy.org/es/built-in-nodes/MireloVideoToSFX)
