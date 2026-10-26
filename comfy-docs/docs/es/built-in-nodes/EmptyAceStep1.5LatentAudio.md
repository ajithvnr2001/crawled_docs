---
url: https://docs.comfy.org/es/built-in-nodes/EmptyAceStep1.5LatentAudio
title: EmptyAceStep1.5LatentAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:44.962154+00:00
---

# EmptyAceStep1.5LatentAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyAceStep1.5LatentAudio

Ace

# EmptyAceStep1.5LatentAudio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Empty Ace Step 1.5 Latent Audio crea un tensor latente de audio vacío (silencioso) para flujos de trabajo de generación de audio.

Copiar páginaCopiar página

El nodo Empty Ace Step 1.5 Latent Audio crea un tensor latente de audio vacío (silencioso) para flujos de trabajo de generación de audio. Construye un latente con 64 canales cuya longitud temporal se calcula a partir de la duración solicitada y lo etiqueta como datos de audio para que lo usen los nodos de audio posteriores.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`seconds`| La duración del audio a generar, en segundos (predeterminado: 120.0). La longitud del latente se calcula como `seconds * 48000 / 1920`, redondeada al número entero más cercano.| FLOAT| Sí| 1.0 - 1000.0 (paso: 0.01)  
`batch_size`| El número de imágenes latentes en el lote (predeterminado: 1).| INT| Sí| 1 - 4096  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`LATENT`| Un tensor latente vacío que representa audio silencioso. El tensor tiene la forma [batch_size, 64, length], donde length se deriva de `seconds`. La salida también incluye un identificador de tipo “audio” y un valor `downscale_ratio_temporal` de 1764, que se utiliza para el submuestreo temporal en el procesamiento de audio.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyAceStep1.5LatentAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyAceStep1.5LatentAudio)

[Codificar texto para edición de MOSS-Image](https://docs.comfy.org/es/built-in-nodes/TextEncodeMOSSImageEdit)[Audio latente Ace Step 1.0 vacío](https://docs.comfy.org/es/built-in-nodes/EmptyAceStepLatentAudio)
