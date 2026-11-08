---
url: https://docs.comfy.org/es/built-in-nodes/OpenAIGPTImageSVGNode/
title: OpenAIGPTImageSVGNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-08T14:09:41.743993+00:00
---

# OpenAIGPTImageSVGNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/OpenAIGPTImageSVGNode/

Openai

# OpenAIGPTImageSVGNode - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

OpenAI GPT Image 2.6 SVG generates an editable SVG from a prompt with OpenAI’s GPT Image models.

Copiar páginaCopiar página

## 

​

Descripción general

OpenAI GPT Image 2.6 SVG genera un SVG editable a partir de un prompt con los modelos GPT Image de OpenAI. El resultado es marcado vectorial, por lo que las formas y el texto permanecen editables en un editor vectorial. Hay dos modelos disponibles: `gpt-image-2.6-flare` y `gpt-image-2.6-sunburst`.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| El modelo GPT Image que se usará para el SVG.| DYNAMIC_COMBO| Sí| `"gpt-image-2.6-flare"`  
`"gpt-image-2.6-sunburst"`  
  
### 

​

Entradas de gpt-image-2.6-flare y gpt-image-2.6-sunburst

Ambos modelos comparten los mismos parámetros.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model.prompt`| Descripción del SVG que se va a dibujar. (predeterminado: `""`)| STRING| Sí| N/A  
`model.size`| Tamaño de la imagen de referencia a partir de la cual se dibuja el SVG. (predeterminado: `"1024x1024"`)| COMBO| Sí| `"1024x1024"`  
`"1024x1536"`  
`"1536x1024"`  
`model.background`| Fondo de la imagen de referencia. (predeterminado: `"auto"`)| COMBO| Sí| `"auto"`  
`"opaque"`  
`"transparent"`  
`model.quality`| Calidad de la imagen de referencia a partir de la cual se dibuja el SVG. (predeterminado: `"low"`)| COMBO| Sí| `"low"`  
`"medium"`  
`"high"`  
`"xhigh"`  
`"max"`  
`model.complexity`| Cuánto planifica el modelo la imagen de referencia antes de renderizarla. (predeterminado: `"high"`)| COMBO| Sí| `"low"`  
`"medium"`  
`"high"`  
`model.seed`| Controla si el nodo se vuelve a ejecutar; los resultados no son deterministas independientemente de la semilla. (predeterminado: `42`)| INT| Sí| 0 a 2147483647  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`svg`| La imagen vectorial generada como marcado SVG.| SVG  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageSVGNode/es.md)

* * *

**Source fingerprint (SHA-256):** `8ac2f473b265d3b6857e6280a1c017301b124fc6d671ec83a59c677218062c90`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/OpenAIGPTImageSVGNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/OpenAIGPTImageSVGNode)

[OpenAIGPTImageGIFNode](https://docs.comfy.org/es/built-in-nodes/OpenAIGPTImageGIFNode)[Imagen de OpenRouter](https://docs.comfy.org/es/built-in-nodes/OpenRouterImageNode)
