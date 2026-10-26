---
url: https://docs.comfy.org/es/built-in-nodes/ImageBlend/
title: Mezcla de im\u00e1genes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:55.260121+00:00
---

# Mezcla de imágenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageBlend/

Filtros

# Mezcla de imágenes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageBlend está diseñado para fusionar dos imágenes según un modo de fusión y un factor de mezcla especificados.

Copiar páginaCopiar página

El nodo `ImageBlend` está diseñado para fusionar dos imágenes según un modo de fusión y un factor de mezcla especificados. Admite varios modos de fusión como normal, multiplicar, pantalla, superposición, luz suave y diferencia, lo que permite técnicas versátiles de manipulación y composición de imágenes. Este nodo es esencial para crear imágenes compuestas ajustando la interacción visual entre dos capas de imagen.

## 

​

Entradas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen1`| La primera imagen a fusionar. Actúa como capa base para la operación de fusión.| `IMAGE`  
`imagen2`| La segunda imagen a fusionar. Dependiendo del modo de fusión, modifica la apariencia de la primera imagen.| `IMAGE`  
`factor_de_mezcla`| Determina el peso de la segunda imagen en la mezcla. Un factor de mezcla más alto otorga mayor prominencia a la segunda imagen en el resultado final.| `FLOAT`  
`modo_de_mezcla`| Especifica el método de fusión de las dos imágenes. Admite modos como normal, multiplicar, pantalla, superposición, luz suave y diferencia, cada uno produciendo un efecto visual único.| COMBO[STRING]  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`image`| La imagen resultante tras fusionar las dos imágenes de entrada según el modo de fusión y el factor especificados.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlend/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageBlend.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageBlend)

[Añadir ruido a imagen](https://docs.comfy.org/es/built-in-nodes/ImageAddNoise)[Desenfoque de imagen](https://docs.comfy.org/es/built-in-nodes/ImageBlur)
