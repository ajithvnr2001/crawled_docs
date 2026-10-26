---
url: https://docs.comfy.org/es/built-in-nodes/ImageStitch/
title: Uni\u00f3n de im\u00e1genes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.326484+00:00
---

# Unión de imágenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageStitch/

Transformación

# Unión de imágenes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo te permite unir dos imágenes en una dirección especificada (arriba, abajo, izquierda, derecha)

Copiar páginaCopiar página

Este nodo te permite unir dos imágenes en una dirección especificada (arriba, abajo, izquierda, derecha), con soporte para ajuste de tamaño y espaciado entre imágenes.

## 

​

Entradas

Nombre del Parámetro| Descripción| Tipo de Dato| Tipo de Entrada| Valor por Defecto| Rango  
---|---|---|---|---|---  
`imagen1`| La primera imagen que se va a unir| IMAGE| Requerida| -| -  
`imagen2`| La segunda imagen que se va a unir; si no se proporciona, devuelve solo la primera imagen| IMAGE| Opcional| None| -  
`dirección`| La dirección para unir la segunda imagen: derecha, abajo, izquierda o arriba| STRING| Requerida| right| right/down/left/up  
`coincidir_tamaño_imagen`| Si se debe redimensionar la segunda imagen para que coincida con las dimensiones de la primera imagen| BOOLEAN| Requerida| True| True/False  
`ancho_espaciado`| Ancho del espacio entre imágenes, debe ser un número par| INT| Requerida| 0| 0-1024  
`color_espaciado`| Color del espacio entre las imágenes unidas| STRING| Requerida| white| white/black/red/green/blue  
  
> Para `spacing_color`, al usar colores distintos a “white/black”, si `match_image_size` está configurado como `false`, el área de relleno se completará con negro

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`IMAGE`| La imagen unida| IMAGE  
  
## 

​

Ejemplo de Flujo de Trabajo

En el flujo de trabajo a continuación, usamos 3 imágenes de entrada de diferentes tamaños como ejemplo:

  * image1: 500x300
  * image2: 400x250
  * image3: 300x300

![workflow](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/ImageStitch/workflow.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=d7fc26a57f9cfe0d2f6dfa1a3cad2ab6) **Primer Nodo de Unión de Imágenes**

  * `match_image_size`: false, las imágenes se unirán en sus tamaños originales
  * `direction`: up, `image2` se colocará encima de `image1`
  * `spacing_width`: 20
  * `spacing_color`: black

Imagen de salida 1: ![output1](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/ImageStitch/output-1.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=671f720ee4cca028cc03d8abe9aecac0) **Segundo Nodo de Unión de Imágenes**

  * `match_image_size`: true, la segunda imagen se escalará para que coincida con la altura o el ancho de la primera imagen
  * `direction`: right, `image3` aparecerá en el lado derecho
  * `spacing_width`: 20
  * `spacing_color`: white

Imagen de salida 2: ![output2](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/ImageStitch/output-2.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=4ed7e7cbfcc3f1f35866b4472b2e517d)

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageStitch.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageStitch)

[RotarImagen](https://docs.comfy.org/es/built-in-nodes/ImageRotate)[Recorte aleatorio de imágenes](https://docs.comfy.org/es/built-in-nodes/RandomCropImages)
