---
url: https://docs.comfy.org/es/built-in-nodes/TextEncodeAceStepAudio/
title: Codificar texto Ace Step audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:34.821909+00:00
---

# Codificar texto Ace Step audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TextEncodeAceStepAudio/

Ace

# Codificar texto Ace Step audio - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo TextEncodeAceStepAudio procesa entradas de texto para el acondicionamiento de audio combinando etiquetas y letras en tokens y, a continuación

Copiar páginaCopiar página

El nodo TextEncodeAceStepAudio procesa entradas de texto para el acondicionamiento de audio combinando etiquetas y letras en tokens y, a continuación, codificándolos con una fuerza de letras ajustable. Toma un modelo CLIP junto con descripciones de texto y letras, los tokeniza conjuntamente y genera datos de acondicionamiento adecuados para tareas de generación de audio. El nodo permite ajustar finamente la influencia de las letras mediante un parámetro de fuerza que controla su impacto en la salida final.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP utilizado para la tokenización y codificación| CLIP| Sí| -  
`etiquetas`| Etiquetas o descripciones de texto para el acondicionamiento de audio (admite entrada multilínea e indicaciones dinámicas)| STRING| Sí| -  
`letras`| Texto de letras para el acondicionamiento de audio (admite entrada multilínea e indicaciones dinámicas)| STRING| Sí| -  
`intensidad_letras`| Controla la fuerza de la influencia de las letras en la salida de acondicionamiento (valor por defecto: 1.0, paso: 0.01)| FLOAT| Sí| 0.0 - 10.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`conditioning`| Los datos de acondicionamiento codificados que contienen los tokens de texto procesados con la fuerza de letras aplicada| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/es.md)

* * *

**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TextEncodeAceStepAudio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TextEncodeAceStepAudio)

[Cargar modelo ControlNet](https://docs.comfy.org/es/built-in-nodes/ControlNetLoader)[TextEncodeAceStepAudio1.5](https://docs.comfy.org/es/built-in-nodes/TextEncodeAceStepAudio1.5)
