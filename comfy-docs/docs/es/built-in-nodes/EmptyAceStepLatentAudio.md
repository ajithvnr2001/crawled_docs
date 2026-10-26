---
url: https://docs.comfy.org/es/built-in-nodes/EmptyAceStepLatentAudio/
title: Audio latente Ace Step 1.0 vac\u00edo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:44.875899+00:00
---

# Audio latente Ace Step 1.0 vacío - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyAceStepLatentAudio/

Ace

# Audio latente Ace Step 1.0 vacío - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Empty Ace Step 1.0 Latent Audio crea muestras de audio latente vacías para una duración elegida.

Copiar páginaCopiar página

El nodo Empty Ace Step 1.0 Latent Audio crea muestras de audio latente vacías para una duración elegida. Rellena un lote de latentes de audio silenciosos (todos en cero), donde la longitud se calcula a partir de la entrada `seconds` usando parámetros de procesamiento de audio. Esto se usa típicamente para inicializar flujos de trabajo de audio que necesitan una representación latente como punto de partida.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`segundos`| La duración del audio en segundos (predeterminado: 120.0, paso: 0.1)| FLOAT| Sí| 1.0 - 1000.0  
`tamaño_del_lote`| El número de imágenes latentes en el lote (predeterminado: 1)| INT| Sí| 1 - 4096  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| Devuelve muestras de audio latente vacías rellenas con ceros. La salida contiene un tensor `samples` y un campo `type` establecido en “audio”.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyAceStepLatentAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyAceStepLatentAudio)

[EmptyAceStep1.5LatentAudio](https://docs.comfy.org/es/built-in-nodes/EmptyAceStep1.5LatentAudio)[Aplicar operación a latente](https://docs.comfy.org/es/built-in-nodes/LatentApplyOperation)
