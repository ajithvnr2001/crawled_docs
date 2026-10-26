---
url: https://docs.comfy.org/es/built-in-nodes/RebatchLatents/
title: Reagrupar latentes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:20.894949+00:00
---

# Reagrupar latentes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RebatchLatents/

Lote

# Reagrupar latentes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo RebatchLatents está diseñado para reorganizar un lote de representaciones latentes en una nueva configuración de lote

Copiar páginaCopiar página

El nodo RebatchLatents está diseñado para reorganizar un lote de representaciones latentes en una nueva configuración de lote, basada en un tamaño de lote especificado. Garantiza que las muestras latentes se agrupen adecuadamente, manejando variaciones en dimensiones y tamaños, para facilitar el procesamiento posterior o la inferencia del modelo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latentes`| El parámetro ‘latents’ representa las representaciones latentes de entrada que se reorganizarán en lotes. Es crucial para determinar la estructura y el contenido del lote de salida.| `LATENT`  
`tamaño_lote`| El parámetro ‘batch_size’ especifica la cantidad deseada de muestras por lote en la salida. Influye directamente en la agrupación y división de las latentes de entrada en nuevos lotes.| `INT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La salida es un lote reorganizado de representaciones latentes, ajustado según el tamaño de lote especificado. Facilita el procesamiento o análisis posterior.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RebatchLatents.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RebatchLatents)

[Latente de lote](https://docs.comfy.org/es/built-in-nodes/LatentFromBatch)[Repetir lote latente](https://docs.comfy.org/es/built-in-nodes/RepeatLatentBatch)
