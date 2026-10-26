---
url: https://docs.comfy.org/es/built-in-nodes/RecraftColorRGB/
title: Recraft color RGB - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:20.728075+00:00
---

# Recraft color RGB - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RecraftColorRGB/

Recraft

# Recraft color RGB - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Crea un color Recraft especificando valores individuales de rojo, verde y azul.

Copiar páginaCopiar página

Crea un color Recraft especificando valores individuales de rojo, verde y azul. Este nodo toma valores enteros RGB (0-255) y los convierte en un formato de color Recraft que puede utilizarse en otras operaciones Recraft. También puedes proporcionar opcionalmente una cadena de color Recraft existente para extenderla con el nuevo color.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`r`| Valor rojo del color (predeterminado: 0)| INT| Sí| 0-255  
`g`| Valor verde del color (predeterminado: 0)| INT| Sí| 0-255  
`b`| Valor azul del color (predeterminado: 0)| INT| Sí| 0-255  
`recraft_color`| Cadena de color Recraft existente opcional para extender con el nuevo color RGB| COLOR| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`recraft_color`| El objeto de color Recraft creado que contiene los valores RGB especificados, o la cadena de color extendida si se proporcionó una existente| COLOR  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/es.md)

* * *

**Source fingerprint (SHA-256):** `8c3503632d085fa4c1771f92f17008b7b051e9604d9e7d1e7d352cbbbd22dddc`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RecraftColorRGB.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RecraftColorRGB)

[Qwen Image 3 Text to Image](https://docs.comfy.org/es/built-in-nodes/QwenImageTextToImageApi)[Controles de Recraft](https://docs.comfy.org/es/built-in-nodes/RecraftControls)
