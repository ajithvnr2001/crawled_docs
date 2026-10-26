---
url: https://docs.comfy.org/es/built-in-nodes/LatentBatch/
title: Lote de latentes (obsoleto) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:02.942010+00:00
---

# Lote de latentes (obsoleto) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentBatch/

Lote

# Lote de latentes (obsoleto) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentBatch está diseñado para fusionar dos conjuntos de muestras latentes en un solo lote

Copiar páginaCopiar página

El nodo LatentBatch está diseñado para fusionar dos conjuntos de muestras latentes en un solo lote, redimensionando potencialmente un conjunto para que coincida con las dimensiones del otro antes de la concatenación. Esta operación facilita la combinación de diferentes representaciones latentes para tareas de procesamiento o generación posteriores.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras1`| El primer conjunto de muestras latentes que se fusionarán. Desempeña un papel crucial en la determinación de la forma final del lote fusionado.| `LATENT`  
`muestras2`| El segundo conjunto de muestras latentes que se fusionarán. Si sus dimensiones difieren del primer conjunto, se redimensiona para garantizar la compatibilidad antes de la fusión.| `LATENT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| El conjunto fusionado de muestras latentes, ahora combinado en un solo lote para su posterior procesamiento.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentBatch.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentBatch)

[Procesar latentes por lotes](https://docs.comfy.org/es/built-in-nodes/BatchLatentsNode)[Latente de lote](https://docs.comfy.org/es/built-in-nodes/LatentFromBatch)
