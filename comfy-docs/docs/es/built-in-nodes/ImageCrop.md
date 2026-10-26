---
url: https://docs.comfy.org/es/built-in-nodes/ImageCrop/
title: Recorte de imagen (obsoleto) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:55.865787+00:00
---

# Recorte de imagen (obsoleto) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageCrop/

Transformación

# Recorte de imagen (obsoleto) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageCrop está diseñado para recortar imágenes a un ancho y alto específicos, comenzando desde una coordenada x e y determinada.

Copiar páginaCopiar página

El nodo `ImageCrop` está diseñado para recortar imágenes a un ancho y alto específicos, comenzando desde una coordenada x e y determinada. Esta funcionalidad es esencial para enfocarse en regiones específicas de una imagen o para ajustar el tamaño de la imagen a ciertos requisitos.

## 

​

Entradas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen de entrada que se va a recortar. Este parámetro es crucial, ya que define la imagen fuente de la cual se extraerá una región según las dimensiones y coordenadas especificadas.| `IMAGE`  
`ancho`| Especifica el ancho de la imagen recortada. Este parámetro determina qué tan ancha será la imagen recortada resultante.| `INT`  
`altura`| Especifica el alto de la imagen recortada. Este parámetro determina la altura de la imagen recortada resultante.| `INT`  
`x`| La coordenada x de la esquina superior izquierda del área de recorte. Este parámetro establece el punto de inicio para la dimensión de ancho del recorte.| `INT`  
`y`| La coordenada y de la esquina superior izquierda del área de recorte. Este parámetro establece el punto de inicio para la dimensión de alto del recorte.| `INT`  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen recortada como resultado de la operación de recorte. Esta salida es importante para el procesamiento o análisis posterior de la región de imagen especificada.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCrop/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageCrop.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageCrop)

[Recortar por cajas delimitadoras](https://docs.comfy.org/es/built-in-nodes/CropByBBoxes)[Recortar imagen a máscara](https://docs.comfy.org/es/built-in-nodes/ImageCropToMask)
