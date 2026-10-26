---
url: https://docs.comfy.org/es/built-in-nodes/ImageColorToMask/
title: Color de imagen a m\u00e1scara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:55.581923+00:00
---

# Color de imagen a máscara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageColorToMask/

Máscara

# Color de imagen a máscara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageColorToMask está diseñado para convertir un color específico de una imagen en una máscara.

Copiar páginaCopiar página

El nodo `ImageColorToMask` está diseñado para convertir un color específico de una imagen en una máscara. Procesa una imagen y un color objetivo, generando una máscara donde se resalta el color especificado, facilitando operaciones como la segmentación basada en color o el aislamiento de objetos.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`imagen`| El parámetro `imagen` representa la imagen de entrada que se va a procesar. Es fundamental para determinar las áreas de la imagen que coinciden con el color especificado y que se convertirán en una máscara.| `IMAGE`  
`color`| El parámetro `color` especifica el color objetivo en la imagen que se convertirá en una máscara. Desempeña un papel clave en la identificación de las áreas de color específicas que se resaltarán en la máscara resultante.| `INT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`mask`| La salida es una máscara que resalta las áreas de la imagen de entrada que coinciden con el color especificado. Esta máscara se puede utilizar para tareas posteriores de procesamiento de imágenes, como segmentación o aislamiento de objetos.| `MASK`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorToMask/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageColorToMask.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageColorToMask)

[Expandir máscara](https://docs.comfy.org/es/built-in-nodes/GrowMask)[Convertir imagen a máscara](https://docs.comfy.org/es/built-in-nodes/ImageToMask)
