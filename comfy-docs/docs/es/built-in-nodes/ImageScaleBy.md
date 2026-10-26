---
url: https://docs.comfy.org/es/built-in-nodes/ImageScaleBy/
title: Ampliar imagen por - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.098127+00:00
---

# Ampliar imagen por - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageScaleBy/

Escalado

# Ampliar imagen por - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageScaleBy está diseñado para escalar imágenes mediante un factor de escala específico utilizando diversos métodos de interpolación.

Copiar páginaCopiar página

El nodo ImageScaleBy está diseñado para escalar imágenes mediante un factor de escala específico utilizando diversos métodos de interpolación. Permite ajustar el tamaño de la imagen de manera flexible, adaptándose a diferentes necesidades de escalado.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen de entrada que se va a escalar. Este parámetro es fundamental, ya que proporciona la imagen base que se someterá al proceso de escalado.| `IMAGE`  
`metodo_ampliacion`| Especifica el método de interpolación que se utilizará para el escalado. La elección del método puede afectar la calidad y las características de la imagen escalada.| COMBO[STRING]  
`escalar_por`| El factor por el cual se escalará la imagen. Esto determina el aumento de tamaño de la imagen de salida en relación con la imagen de entrada.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen escalada, que es más grande que la imagen de entrada según el factor de escala y el método de interpolación especificados.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleBy/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageScaleBy.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageScaleBy)

[Ampliar imagen](https://docs.comfy.org/es/built-in-nodes/ImageScale)[Escalar imagen a dimensión máxima](https://docs.comfy.org/es/built-in-nodes/ImageScaleToMaxDimension)
