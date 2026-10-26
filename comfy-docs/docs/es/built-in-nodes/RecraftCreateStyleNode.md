---
url: https://docs.comfy.org/es/built-in-nodes/RecraftCreateStyleNode/
title: Recraft crear estilo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:21.090599+00:00
---

# Recraft crear estilo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RecraftCreateStyleNode/

Recraft

# Recraft crear estilo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo crea un estilo personalizado para la generación de imágenes mediante la carga de imágenes de referencia.

Copiar páginaCopiar página

Este nodo crea un estilo personalizado para la generación de imágenes mediante la carga de imágenes de referencia. Puedes cargar entre 1 y 5 imágenes para definir el nuevo estilo, y el nodo devolverá un ID de estilo único que se puede utilizar con otros nodos de Recraft. El tamaño total combinado de todos los archivos de imagen cargados no debe superar los 5 MB.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`estilo`| El estilo base de las imágenes generadas.| STRING| Sí| `"realistic_image"`  
`"digital_illustration"`  
`imágenes`| Un conjunto de 1 a 5 imágenes de referencia utilizadas para crear el estilo personalizado.| IMAGE| Sí| 1 a 5 imágenes  
  
**Nota:** El tamaño total de archivo de todas las imágenes en la entrada `images` debe ser inferior a 5 MB. El nodo fallará si se supera este límite.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`id_estilo`| El identificador único para el estilo personalizado recién creado.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreateStyleNode/es.md)

* * *

**Source fingerprint (SHA-256):** `36340e64d90b3edbbecedf15ac123adaabb5bc0c950183d2df6627dc873da61c`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RecraftCreateStyleNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RecraftCreateStyleNode)

[Controles de Recraft](https://docs.comfy.org/es/built-in-nodes/RecraftControls)[Recraft escalado creativo de imagen](https://docs.comfy.org/es/built-in-nodes/RecraftCreativeUpscaleNode)
