---
url: https://docs.comfy.org/es/built-in-nodes/EmptyTrellis2LatentStructure/
title: Estructura latente Trellis2 vac\u00eda - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:46.547619+00:00
---

# Estructura latente Trellis2 vacía - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyTrellis2LatentStructure/

Trellis

# Estructura latente Trellis2 vacía - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo crea una estructura latente vacía para el modelo Trellis2, donde todos los valores se establecen en cero.

Copiar páginaCopiar página

Este nodo crea una estructura latente vacía para el modelo Trellis2, donde todos los valores se establecen en cero. Produce un tensor latente 3D en blanco con 32 canales y una resolución de 16×16×16, dimensionado para el número especificado de elementos en el lote.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`batch_size`| El número de imágenes latentes en el lote (por defecto: 1).| INT| Sí| 1 a 4096  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`LATENT`| Una estructura latente Trellis2 vacía. Las muestras son un tensor relleno de ceros con la forma (batch_size, 32, 16, 16, 16), y el tipo de latente se establece en “trellis2”.| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/es.md)

* * *

**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyTrellis2LatentStructure.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyTrellis2LatentStructure)

[Rotar latente](https://docs.comfy.org/es/built-in-nodes/LatentRotate)[Decodificación de forma VAE de Trellis2](https://docs.comfy.org/es/built-in-nodes/VaeDecodeShapeTrellis)
