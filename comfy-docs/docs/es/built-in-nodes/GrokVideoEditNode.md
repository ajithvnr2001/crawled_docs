---
url: https://docs.comfy.org/es/built-in-nodes/GrokVideoEditNode/
title: Edici\u00f3n de video Grok - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:51.772031+00:00
---

# Edición de video Grok - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/GrokVideoEditNode/

Grok

# Edición de video Grok - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo utiliza la API de Grok para editar un video existente a partir de un prompt de texto.

Copiar páginaCopiar página

Este nodo utiliza la API de Grok para editar un video existente a partir de un prompt de texto. Carga tu video, envía una solicitud al modelo de IA para modificarlo según tu descripción y devuelve el video recién generado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de IA que se utilizará para la edición de video (valor predeterminado: “grok-imagine-video”).| COMBO| Sí| ”grok-imagine-video”  
`indicación`| Descripción textual del video deseado.| STRING| Sí| N/A  
`video`| El video de entrada que se va a editar. La duración máxima admitida es de 8.7 segundos y el tamaño de archivo máximo es de 50 MB.| VIDEO| Sí| N/A  
`semilla`| Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales no son deterministas independientemente de la semilla (valor predeterminado: 0).| INT| No| 0 a 2147483647  
  
**Restricciones:**

  * El `prompt` no debe estar vacío.
  * El `video` de entrada debe tener una duración entre 1 y 8.7 segundos.
  * El tamaño del archivo del `video` de entrada no debe superar los 50 MB.

**Nota:** Este nodo es un nodo de API y requiere una cuenta de Comfy.org y una clave de API para ejecutarse. El uso se factura a aproximadamente $0.06 por segundo de video.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| El video editado generado por el modelo de IA.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/es.md)

* * *

**Source fingerprint (SHA-256):** `7ceedff2f858bc0849b5e0d92d10ed51e7fdccd1391c6a6966561cb05999b4b1`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/GrokVideoEditNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/GrokVideoEditNode)

[Google Gemini Omni (Vídeo)](https://docs.comfy.org/es/built-in-nodes/GeminiVideoOmniV2)[Extender video Grok](https://docs.comfy.org/es/built-in-nodes/GrokVideoExtendNode)
