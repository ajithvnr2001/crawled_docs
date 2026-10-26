---
url: https://docs.comfy.org/es/built-in-nodes/ImageQuantize/
title: Cuantizar imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.746569+00:00
---

# Cuantizar imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageQuantize/

Filtros

# Cuantizar imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageQuantize está diseñado para reducir la cantidad de colores en una imagen a un número específico

Copiar páginaCopiar página

El nodo ImageQuantize está diseñado para reducir la cantidad de colores en una imagen a un número específico, aplicando opcionalmente técnicas de tramado para mantener la calidad visual. Este proceso es útil para crear imágenes basadas en paletas o reducir la complejidad cromática para ciertas aplicaciones.

## 

​

Entradas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen`| El tensor de imagen de entrada que se va a cuantizar. Afecta la ejecución del nodo al ser los datos principales sobre los cuales se realiza la reducción de color.| `IMAGE`  
`colores`| Especifica la cantidad de colores a los que se reducirá la imagen. Influye directamente en el proceso de cuantización al determinar el tamaño de la paleta de colores.| `INT`  
`difuminado`| Determina la técnica de tramado que se aplicará durante la cuantización, afectando la calidad visual y la apariencia de la imagen de salida.| COMBO[STRING]  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La versión cuantizada de la imagen de entrada, con complejidad cromática reducida y opcionalmente tramada para mantener la calidad visual.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageQuantize.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageQuantize)

[Desenfoque de imagen](https://docs.comfy.org/es/built-in-nodes/ImageBlur)[Enfocar imagen](https://docs.comfy.org/es/built-in-nodes/ImageSharpen)
