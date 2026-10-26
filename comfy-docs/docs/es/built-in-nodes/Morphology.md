---
url: https://docs.comfy.org/es/built-in-nodes/Morphology/
title: MorfologiaDeImagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:15.542000+00:00
---

# MorfologiaDeImagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Morphology/

Filtros

# MorfologiaDeImagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Morfología aplica diversas operaciones morfológicas a las imágenes

Copiar páginaCopiar página

El nodo Morfología aplica diversas operaciones morfológicas a las imágenes, las cuales son operaciones matemáticas utilizadas para procesar y analizar formas en imágenes. Puede realizar operaciones como erosión, dilatación, apertura, cierre y más, utilizando un tamaño de kernel personalizable para controlar la intensidad del efecto.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada a procesar| IMAGE| Sí| -  
`operacion`| La operación morfológica a aplicar (predeterminado: “erode”)| STRING| Sí| `"erode"`  
`"dilate"`  
`"open"`  
`"close"`  
`"gradient"`  
`"bottom_hat"`  
`"top_hat"`  
`tamaño_kernel`| El tamaño del kernel del elemento estructurante (predeterminado: 3). Debe ser un número impar.| INT| Sí| 3-999  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen procesada después de aplicar la operación morfológica| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/es.md)

* * *

**Source fingerprint (SHA-256):** `7f6224a0e58fbb7263267b377394e119c6f8d65d16af4ce492ca9504654af7b4`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Morphology.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Morphology)

[Enfocar imagen](https://docs.comfy.org/es/built-in-nodes/ImageSharpen)[Convertir geometría DA3 a malla](https://docs.comfy.org/es/built-in-nodes/DA3GeometryToMesh)
