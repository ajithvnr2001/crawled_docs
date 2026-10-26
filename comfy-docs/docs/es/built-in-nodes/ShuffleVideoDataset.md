---
url: https://docs.comfy.org/es/built-in-nodes/ShuffleVideoDataset/
title: Mezclar Lista de Videos - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:31.354510+00:00
---

# Mezclar Lista de Videos - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ShuffleVideoDataset/

Lote

# Mezclar Lista de Videos - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo toma una lista de videos y los reordena aleatoriamente.

Copiar páginaCopiar página

Este nodo toma una lista de videos y los reordena aleatoriamente. Utiliza una semilla aleatoria para que la mezcla sea reproducible, por lo que la misma semilla siempre produce el mismo orden de salida.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`videos`| Lista de videos para mezclar.| VIDEO| Sí| Lista de entradas de video  
`seed`| Semilla aleatoria para la mezcla (predeterminado: 0).| INT| No| 0 a 18446744073709551615  
Nota: el valor de la semilla se reduce módulo 4294967295 (2^32 - 1) antes de usarse. Como resultado, las semillas que difieren en un múltiplo de 4294967295 producen el mismo orden de salida.| | | |   
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`videos`| Lista de videos mezclados en orden aleatorio.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleVideoDataset/es.md)

* * *

**Source fingerprint (SHA-256):** `0bd32b664197d3bbd4c53f65e29ef38fba836579f07f05cb7fb85f3b8a1024ac`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ShuffleVideoDataset.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ShuffleVideoDataset)

[Wan intercambio de bloques](https://docs.comfy.org/es/built-in-nodes/wanBlockSwap)[Mezclar Pares de Video-Texto](https://docs.comfy.org/es/built-in-nodes/ShuffleVideoTextDataset)
