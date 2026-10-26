---
url: https://docs.comfy.org/es/built-in-nodes/ViduTextToVideoNode/
title: Generaci\u00f3n de video Vidu de texto a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:43.749572+00:00
---

# Generación de video Vidu de texto a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ViduTextToVideoNode/

Vidu

# Generación de video Vidu de texto a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias para mejorar

Copiar páginaCopiar página

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias para mejorar, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/en.md) El nodo de Generación de Video a partir de Texto de Vidu crea videos a partir de descripciones textuales. Utiliza el modelo de generación de video Vidu para transformar tus indicaciones de texto en contenido de video con configuraciones personalizables para duración, relación de aspecto y estilo visual.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| Nombre del modelo| COMBO| Sí| `viduq1`  
`prompt`| Descripción textual para la generación del video| STRING| Sí| -  
`duración`| Duración del video de salida en segundos (predeterminado: 5)| INT| No| 5-5  
`semilla`| Semilla para la generación del video (0 para aleatorio) (predeterminado: 0)| INT| No| 0-2147483647  
`relación_de_aspecto`| Relación de aspecto del video de salida| COMBO| No| `16:9`  
`9:16`  
`1:1`  
`resolución`| Los valores compatibles pueden variar según el modelo y la duración| COMBO| No| `1080p`  
`amplitud_movimiento`| Amplitud de movimiento de los objetos en el encuadre| COMBO| No| `auto`  
`small`  
`medium`  
`large`  
  
**Nota:** El campo `prompt` es obligatorio y no puede estar vacío. El parámetro `duration` actualmente está fijado en 5 segundos.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| El video generado a partir de la indicación de texto| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `0d331d3eab8a4af9c90831f3f8fd8ae34aa0c393142cb6f89404edc94024d95f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ViduTextToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ViduTextToVideoNode)

[Generación de video Vidu de inicio a fin](https://docs.comfy.org/es/built-in-nodes/ViduStartEndToVideoNode)[HappyHorse Imagen a Video](https://docs.comfy.org/es/built-in-nodes/HappyHorseImageToVideoApi)
