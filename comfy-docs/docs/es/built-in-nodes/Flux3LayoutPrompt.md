---
url: https://docs.comfy.org/es/built-in-nodes/Flux3LayoutPrompt/
title: Prompt de dise\u00f1o de FLUX 3 Image - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:48.249601+00:00
---

# Prompt de diseño de FLUX 3 Image - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Flux3LayoutPrompt/

FLUX

# Prompt de diseño de FLUX 3 Image - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Construye la tabla de diseño que FLUX 3 Image lee desde un prompt.

Copiar páginaCopiar página

Construye la tabla de diseño que FLUX 3 Image lee desde un prompt. Toma los elementos dibujados en el nodo Create Bounding Boxes y los añade a tu prompt como una lista de cuadros, cada uno con un id, sus coordenadas y su descripción. Haz referencia a un cuadro en el prompt como `<obj_N>` para vincular palabras a esa región; luego conecta la salida a la entrada `prompt` del nodo FLUX 3 Image. Si no hay elementos conectados, el prompt se devuelve sin cambios.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| El texto del prompt. Haz referencia al cuadro N como `<obj_N>` para vincular palabras a él.| STRING| Sí| -  
`element`| Los elementos que se colocarán en el diseño, tomados del nodo Create Bounding Boxes. No se usan paletas de colores, por lo que describe los colores en la descripción.| ARRAY| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`prompt`| El prompt con la tabla de diseño de cuadros añadida, listo para alimentar el nodo FLUX 3 Image.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3LayoutPrompt/es.md)

* * *

**Source fingerprint (SHA-256):** `ac8f61701c8da0a6fc8361aeebf7fc5e7aa338ce6ad8689718904caa9c53e3b8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Flux3LayoutPrompt.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Flux3LayoutPrompt)

[Codificar texto CLIP para Flux](https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeFlux)[Desactivar guía Flux](https://docs.comfy.org/es/built-in-nodes/FluxDisableGuidance)
