---
url: https://docs.comfy.org/es/built-in-nodes/ImageRotate/
title: RotarImagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.180308+00:00
---

# RotarImagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageRotate/

Transformación

# RotarImagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageRotate rota una imagen de entrada según ángulos especificados.

Copiar páginaCopiar página

El nodo ImageRotate rota una imagen de entrada según ángulos especificados. Admite cuatro opciones de rotación: sin rotación, 90 grados en sentido horario, 180 grados y 270 grados en sentido horario. La rotación se realiza mediante operaciones eficientes con tensores que mantienen la integridad de los datos de la imagen.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada que se va a rotar| IMAGE| Sí| -  
`rotación`| El ángulo de rotación que se aplicará a la imagen (predeterminado: “none”)| STRING| Sí| ”none"  
"90 degrees"  
"180 degrees"  
"270 degrees”  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`imagen`| La imagen de salida rotada| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRotate/es.md)

* * *

**Source fingerprint (SHA-256):** `068946b31ebe87b2524a1e628b5bc0a3da7367d7252fa7afafe96bcbb174747d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageRotate.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageRotate)

[Rellenar imagen para pintar fuera](https://docs.comfy.org/es/built-in-nodes/ImagePadForOutpaint)[Unión de imágenes](https://docs.comfy.org/es/built-in-nodes/ImageStitch)
