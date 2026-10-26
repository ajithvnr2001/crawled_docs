---
url: https://docs.comfy.org/es/built-in-nodes/Flux2Scheduler/
title: Programador Flux 2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:47.672701+00:00
---

# Programador Flux 2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Flux2Scheduler/

Programadores

# Programador Flux 2 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Flux2Scheduler genera una secuencia de niveles de ruido (sigmas) para el proceso de eliminación de ruido, específicamente adaptada para el modelo Flux.

Copiar páginaCopiar página

Flux2Scheduler genera una secuencia de niveles de ruido (sigmas) para el proceso de eliminación de ruido, específicamente adaptada para el modelo Flux. Calcula un programa basado en el número de pasos de eliminación de ruido y las dimensiones de la imagen objetivo, lo que influye en la progresión de la eliminación de ruido durante la generación de imágenes.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`pasos`| El número de pasos de eliminación de ruido a realizar. Un valor más alto generalmente produce resultados más detallados, pero tarda más en procesarse (predeterminado: 20).| INT| Sí| 1 a 4096  
`ancho`| El ancho de la imagen a generar, en píxeles. Este valor influye en el cálculo del programa de ruido (predeterminado: 1024).| INT| Sí| 16 a 16384  
`alto`| El alto de la imagen a generar, en píxeles. Este valor influye en el cálculo del programa de ruido (predeterminado: 1024).| INT| Sí| 16 a 16384  
  
Nota: El programa se calcula a partir de la longitud de la secuencia de la imagen, que se deriva de `width` y `height` como `(width * height) / 256`, reflejando el submuestreo latente de 16x del modelo. Las imágenes más grandes producen secuencias más largas, lo que desplaza el programa de ruido en consecuencia.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`sigmas`| Una secuencia de valores de nivel de ruido (sigmas) que definen el programa de eliminación de ruido para el muestreador.| SIGMAS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/es.md)

* * *

**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Flux2Scheduler.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Flux2Scheduler)

[Programador exponencial](https://docs.comfy.org/es/built-in-nodes/ExponentialScheduler)[Programador GITS](https://docs.comfy.org/es/built-in-nodes/GITSScheduler)
