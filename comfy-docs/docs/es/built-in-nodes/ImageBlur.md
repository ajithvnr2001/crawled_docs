---
url: https://docs.comfy.org/es/built-in-nodes/ImageBlur/
title: Desenfoque de imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:55.504768+00:00
---

# Desenfoque de imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageBlur/

Filtros

# Desenfoque de imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageBlur aplica un desenfoque gaussiano a una imagen, permitiendo suavizar bordes y reducir detalles y ruido.

Copiar páginaCopiar página

El nodo `ImageBlur` aplica un desenfoque gaussiano a una imagen, permitiendo suavizar bordes y reducir detalles y ruido. Proporciona control sobre la intensidad y propagación del desenfoque mediante parámetros.

## 

​

Entradas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen de entrada que se va a desenfocar. Este es el objetivo principal del efecto de desenfoque.| `IMAGE`  
`radio_de_desenfoque`| Determina el radio del efecto de desenfoque. Un radio mayor produce un desenfoque más pronunciado.| `INT`  
`sigma`| Controla la propagación del desenfoque. Un valor de sigma más alto significa que el desenfoque afectará un área más amplia alrededor de cada píxel.| `FLOAT`  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La salida es la versión desenfocada de la imagen de entrada, con el grado de desenfoque determinado por los parámetros de entrada.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageBlur.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageBlur)

[Mezcla de imágenes](https://docs.comfy.org/es/built-in-nodes/ImageBlend)[Cuantizar imagen](https://docs.comfy.org/es/built-in-nodes/ImageQuantize)
