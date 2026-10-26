---
url: https://docs.comfy.org/es/built-in-nodes/LatentUpscaleBy/
title: Escalar latente por - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:04.165601+00:00
---

# Escalar latente por - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentUpscaleBy/

Latente

# Escalar latente por - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentUpscaleBy está diseñado para escalar representaciones latentes de imágenes.

Copiar páginaCopiar página

El nodo LatentUpscaleBy está diseñado para escalar representaciones latentes de imágenes. Permite ajustar el factor de escala y el método de escalado, ofreciendo flexibilidad para mejorar la resolución de muestras latentes.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras`| La representación latente de las imágenes que se escalarán. Este parámetro es crucial para determinar los datos de entrada que se someterán al proceso de escalado.| `LATENT`  
`método_escala`| Especifica el método utilizado para escalar las muestras latentes. La elección del método puede afectar significativamente la calidad y las características del resultado escalado.| COMBO[STRING]  
`escalar_por`| Determina el factor por el cual se escalan las muestras latentes. Este parámetro influye directamente en la resolución de la salida, permitiendo un control preciso sobre el proceso de escalado.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La representación latente escalada, lista para procesos posteriores o tareas de generación. Esta salida es esencial para mejorar la resolución de imágenes generadas o para operaciones posteriores del modelo.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleBy/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentUpscaleBy.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentUpscaleBy)

[Escalar latente](https://docs.comfy.org/es/built-in-nodes/LatentUpscale)[Cargar latente](https://docs.comfy.org/es/built-in-nodes/LoadLatent)
