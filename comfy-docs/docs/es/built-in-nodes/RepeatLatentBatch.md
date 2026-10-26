---
url: https://docs.comfy.org/es/built-in-nodes/RepeatLatentBatch/
title: Repetir lote latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:23.528197+00:00
---

# Repetir lote latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RepeatLatentBatch/

Lote

# Repetir lote latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo RepeatLatentBatch está diseñado para replicar un lote determinado de representaciones latentes un número específico de veces

Copiar páginaCopiar página

El nodo RepeatLatentBatch está diseñado para replicar un lote determinado de representaciones latentes un número específico de veces, incluyendo potencialmente datos adicionales como máscaras de ruido e índices de lote. Esta funcionalidad es crucial para operaciones que requieren múltiples instancias de los mismos datos latentes, como el aumento de datos o tareas generativas específicas.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras`| El parámetro ‘samples’ representa las representaciones latentes que se replicarán. Es esencial para definir los datos que se someterán a repetición.| `LATENT`  
`cantidad`| El parámetro ‘amount’ especifica el número de veces que se deben repetir las muestras de entrada. Influye directamente en el tamaño del lote de salida, afectando así la carga computacional y la diversidad de los datos generados.| `INT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La salida es una versión modificada de las representaciones latentes de entrada, replicadas según el ‘amount’ especificado. Puede incluir máscaras de ruido replicadas e índices de lote ajustados, si corresponde.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RepeatLatentBatch.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RepeatLatentBatch)

[Reagrupar latentes](https://docs.comfy.org/es/built-in-nodes/RebatchLatents)[Reemplazar fotogramas de latente de video](https://docs.comfy.org/es/built-in-nodes/ReplaceVideoLatentFrames)
