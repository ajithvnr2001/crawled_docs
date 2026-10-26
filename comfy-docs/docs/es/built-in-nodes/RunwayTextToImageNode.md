---
url: https://docs.comfy.org/es/built-in-nodes/RunwayTextToImageNode/
title: Runway texto a imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:25.361803+00:00
---

# Runway texto a imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RunwayTextToImageNode/

Runway

# Runway texto a imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Runway Text to Image genera imágenes a partir de indicaciones de texto utilizando el modelo Gen 4 de Runway.

Copiar páginaCopiar página

El nodo **Runway Text to Image** genera imágenes a partir de indicaciones de texto utilizando el modelo Gen 4 de Runway. Puedes proporcionar una descripción textual y, opcionalmente, incluir una imagen de referencia para guiar el proceso de generación. El nodo gestiona la comunicación con la API y devuelve la imagen generada.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`texto_descriptivo`| Indicación de texto para la generación (predeterminado: "")| STRING| Sí| -  
`proporción`| Relación de aspecto para la imagen generada| COMBO| Sí| ”16:9"  
"1:1"  
"21:9"  
"2:3"  
"3:2"  
"4:5"  
"5:4"  
"9:16"  
"9:21”  
`imagen_referencia`| Imagen de referencia opcional para guiar la generación| IMAGE| No| -  
  
**Nota:** La imagen de referencia debe tener dimensiones que no superen los 7999x7999 píxeles y una relación de aspecto entre 0.5 y 2.0. Cuando se proporciona una imagen de referencia, esta guía el proceso de generación de la imagen.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`output`| La imagen generada basada en la indicación de texto y la imagen de referencia opcional| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/es.md)

* * *

**Source fingerprint (SHA-256):** `140f8e6b07216892d84f2d7fbc3afaf1c390e98ddedf27d4926032066a783f67`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RunwayTextToImageNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RunwayTextToImageNode)

[Reve mezclar imagen](https://docs.comfy.org/es/built-in-nodes/ReveImageRemixNode)[Tencent HY Image: Editar](https://docs.comfy.org/es/built-in-nodes/HunyuanImageEditApi)
