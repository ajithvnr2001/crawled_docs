---
url: https://docs.comfy.org/es/built-in-nodes/ImageCompositeMasked/
title: Componer imagen con m\u00e1scara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:55.662033+00:00
---

# Componer imagen con máscara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageCompositeMasked/

Composición

# Componer imagen con máscara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageCompositeMasked está diseñado para la composición de imágenes

Copiar páginaCopiar página

El nodo `ImageCompositeMasked` está diseñado para la composición de imágenes, permitiendo superponer una imagen de origen sobre una imagen de destino en coordenadas específicas, con opciones de redimensionamiento y enmascaramiento.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`destino`| La imagen de destino sobre la cual se compondrá la imagen de origen. Actúa como fondo para la operación de composición.| `IMAGE`  
`fuente`| La imagen de origen que se va a componer sobre la imagen de destino. Esta imagen puede redimensionarse opcionalmente para ajustarse a las dimensiones de la imagen de destino.| `IMAGE`  
`x`| La coordenada x en la imagen de destino donde se colocará la esquina superior izquierda de la imagen de origen.| `INT`  
`y`| La coordenada y en la imagen de destino donde se colocará la esquina superior izquierda de la imagen de origen.| `INT`  
`redimensionar_fuente`| Un indicador booleano que especifica si la imagen de origen debe redimensionarse para coincidir con las dimensiones de la imagen de destino.| `BOOLEAN`  
`máscara`| Una máscara opcional que especifica qué partes de la imagen de origen deben componerse sobre la imagen de destino. Esto permite operaciones de composición más complejas, como fusiones o superposiciones parciales.| `MASK`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`image`| La imagen resultante después de la operación de composición, que combina elementos de ambas imágenes.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositeMasked/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageCompositeMasked.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageCompositeMasked)

[Normalizar imágenes](https://docs.comfy.org/es/built-in-nodes/NormalizeImages)[Unir imagen con alfa](https://docs.comfy.org/es/built-in-nodes/JoinImageWithAlpha)
