---
url: https://docs.comfy.org/es/built-in-nodes/IdeogramV4/
title: Ideogram V4 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:54.852754+00:00
---

# Ideogram V4 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/IdeogramV4/

Ideogram

# Ideogram V4 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera imágenes utilizando el modelo Ideogram 4.0 a partir de una descripción textual.

Copiar páginaCopiar página

Genera imágenes utilizando el modelo Ideogram 4.0 a partir de una descripción textual. Este nodo envía tu descripción de texto a la API de Ideogram y devuelve la imagen generada como un tensor de salida.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Descripción textual para la generación de la imagen.| STRING| Sí| Sin restricciones  
`resolución`| La resolución de la imagen generada. Valor predeterminado: “Auto” que permite al modelo elegir la mejor resolución.| COMBO| Sí| `"Auto"`  
`"2048x2048 (1:1)"`  
`"1440x2880 (1:2)"`  
`"2880x1440 (2:1)"`  
`"1664x2496 (2:3)"`  
`"2496x1664 (3:2)"`  
`"1792x2240 (4:5)"`  
`"2240x1792 (5:4)"`  
`"1440x2560 (9:16)"`  
`"2560x1440 (16:9)"`  
`"1600x2560 (5:8)"`  
`"2560x1600 (8:5)"`  
`"1728x2304 (3:4)"`  
`"2304x1728 (4:3)"`  
`"1296x3168 (9:22)"`  
`"3168x1296 (22:9)"`  
`"1152x2944 (9:23)"`  
`"2944x1152 (23:9)"`  
`"1248x3328 (3:8)"`  
`"3328x1248 (8:3)"`  
`"1280x3072 (5:12)"`  
`"3072x1280 (12:5)"`  
`velocidad_de_renderizado`| Controla el equilibrio entre velocidad de generación y calidad. Valor predeterminado: “DEFAULT”.| COMBO| Sí| `"DEFAULT"`  
`"TURBO"`  
`"QUALITY"`  
`semilla`| Semilla para generación reproducible. Valor predeterminado: 0.| INT| Sí| Mín: 0  
Máx: 2147483647  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`IMAGE`| La imagen generada como un tensor.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV4/es.md)

* * *

**Source fingerprint (SHA-256):** `47a486824211d34b9109c5038b0b094d192c4e243c0a6c4ceab13af3bdabe6e4`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/IdeogramV4.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/IdeogramV4)

[Ideogram V3](https://docs.comfy.org/es/built-in-nodes/IdeogramV3)[Generación de imágenes Kling](https://docs.comfy.org/es/built-in-nodes/KlingImageGenerationNode)
