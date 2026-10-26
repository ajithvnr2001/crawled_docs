---
url: https://docs.comfy.org/es/built-in-nodes/LTXVFreezeLatent/
title: LTXV Congelar latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:01.346155+00:00
---

# LTXV Congelar latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LTXVFreezeLatent/

Ltxv

# LTXV Congelar latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LTXV Freeze Latent establece en cero la máscara de ruido de un latente

Copiar páginaCopiar página

El nodo LTXV Freeze Latent establece en cero la máscara de ruido de un latente, lo que mantiene ese latente limpio y sin cambios mientras se ejecuta el muestreo. Funciona tanto con latentes de video como de audio, por lo que un latente se puede congelar antes de concatenarlo con otros o cuando no deba someterse a eliminación de ruido en absoluto.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`latent`| Latente de video o audio que se va a congelar. El audio es 4D; el video es 5D.| LATENT| Sí| N/A  
  
### 

​

Restricciones

  * El latente debe contener un tensor simple. No se acepta un latente concatenado de audio y video; primero debe separarse con el nodo Separate AV Latent.
  * Solo se admiten latentes 4D (audio) y 5D (video). Cualquier otra forma provoca un error.
  * La máscara de ruido generada se crea con ceros usando el mismo dispositivo que el tensor de entrada. Para latentes de video, la máscara tiene forma (batch, 1, frames, 1, 1); para latentes de audio, tiene forma (batch, 1, frames, 1).



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`latent`| El latente de entrada con una máscara de ruido de ceros añadida, por lo que permanece limpio durante el muestreo.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVFreezeLatent/es.md)

* * *

**Source fingerprint (SHA-256):** `d5d228687f0a124644323c0448dcce53ed6eb2224d3f44d1756079b2a71539ca`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LTXVFreezeLatent.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LTXVFreezeLatent)

[Audio latente LTXV vacío](https://docs.comfy.org/es/built-in-nodes/LTXVEmptyLatentAudio)[Ampliar latente LTXV](https://docs.comfy.org/es/built-in-nodes/LTXVLatentUpsampler)
