---
url: https://docs.comfy.org/es/built-in-nodes/LoadImageMask/
title: Cargar imagen (como m\u00e1scara) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:05.098952+00:00
---

# Cargar imagen (como máscara) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadImageMask/

Imagen

# Cargar imagen (como máscara) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LoadImageMask está diseñado para cargar imágenes y sus máscaras asociadas desde una ruta especificada

Copiar páginaCopiar página

El nodo LoadImageMask está diseñado para cargar imágenes y sus máscaras asociadas desde una ruta especificada, procesándolas para garantizar la compatibilidad con tareas posteriores de manipulación o análisis de imágenes. Se enfoca en manejar varios formatos de imagen y condiciones, como la presencia de un canal alfa para las máscaras, y prepara las imágenes y máscaras para el procesamiento posterior convirtiéndolas a un formato estandarizado.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen`| El parámetro `imagen` especifica el archivo de imagen que se cargará y procesará. Desempeña un papel crucial en la determinación de la salida al proporcionar la imagen de origen para la extracción de la máscara y la conversión de formato.| COMBO[STRING]  
`canal`| El parámetro `canal` especifica el canal de color de la imagen que se utilizará para generar la máscara. Esto permite flexibilidad en la creación de máscaras basadas en diferentes canales de color, mejorando la utilidad del nodo en diversos escenarios de procesamiento de imágenes.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`mask`| Este nodo genera la máscara producida a partir de la imagen y el canal especificados, preparada en un formato estandarizado adecuado para su posterior procesamiento en tareas de manipulación de imágenes.| `MASK`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageMask/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadImageMask.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadImageMask)

[Cargar conjunto de imágenes desde carpeta](https://docs.comfy.org/es/built-in-nodes/LoadImageDataSetFromFolder)[Cargar imagen (desde salidas)](https://docs.comfy.org/es/built-in-nodes/LoadImageOutput)
