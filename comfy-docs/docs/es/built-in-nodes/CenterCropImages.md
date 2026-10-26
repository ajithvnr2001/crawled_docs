---
url: https://docs.comfy.org/es/built-in-nodes/CenterCropImages/
title: Recorte central de im\u00e1genes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:37.597600+00:00
---

# Recorte central de imágenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CenterCropImages/

Transformación

# Recorte central de imágenes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Center Crop Images recorta una imagen desde su centro hasta un ancho y alto especificados.

Copiar páginaCopiar página

El nodo **Center Crop Images** recorta una imagen desde su centro hasta un ancho y alto especificados. Calcula la región central de la imagen de entrada y extrae un área rectangular con las dimensiones definidas. Si el tamaño de recorte solicitado es mayor que la imagen, el recorte se limitará a los bordes de la imagen.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`image`| La imagen de entrada que se va a recortar.| IMAGE| Sí| -  
`ancho`| El ancho del área de recorte (predeterminado: 512).| INT| Sí| 1 a 8192  
`alto`| El alto del área de recorte (predeterminado: 512).| INT| Sí| 1 a 8192  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imágenes`| La imagen resultante después de la operación de recorte centrado.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/es.md)

* * *

**Source fingerprint (SHA-256):** `4361b6630ab1833e035d6ab04a130fb36fff33cddc36b54ff5a2d8e04534a555`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CenterCropImages.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CenterCropImages)

[GLSL Shader](https://docs.comfy.org/es/built-in-nodes/GLSLShader)[Recortar por cajas delimitadoras](https://docs.comfy.org/es/built-in-nodes/CropByBBoxes)
