---
url: https://docs.comfy.org/es/built-in-nodes/RandomCropImages/
title: Recorte aleatorio de im\u00e1genes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:20.585512+00:00
---

# Recorte aleatorio de imágenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RandomCropImages/

Transformación

# Recorte aleatorio de imágenes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Recorte Aleatorio de Imágenes selecciona aleatoriamente una sección rectangular de cada imagen de entrada y la recorta a un ancho y alto especificados.

Copiar páginaCopiar página

El nodo Recorte Aleatorio de Imágenes selecciona aleatoriamente una sección rectangular de cada imagen de entrada y la recorta a un ancho y alto especificados. Se usa comúnmente para aumento de datos con el fin de crear variaciones de imágenes de entrenamiento. La posición aleatoria del recorte se determina mediante un valor de semilla, lo que garantiza que se pueda reproducir el mismo recorte.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`image`| La imagen que se va a recortar.| IMAGE| Sí| -  
`width`| El ancho del área de recorte (predeterminado: 512).| INT| No| 1 - 8192  
`height`| La altura del área de recorte (predeterminado: 512).| INT| No| 1 - 8192  
`seed`| Número utilizado para controlar la posición aleatoria del recorte (predeterminado: 0).| INT| No| 0 - 18446744073709551615  
  
**Nota:** Los parámetros `width` y `height` deben ser menores o iguales a las dimensiones de la imagen de entrada. Si una dimensión especificada es mayor que la imagen, el recorte se limitará al borde de la imagen.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`images`| La imagen resultante después de aplicar el recorte aleatorio.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/es.md)

* * *

**Source fingerprint (SHA-256):** `bc4aca8cc63bde28fee906a92463b73436ba48ba69d7c1ff13881ac900e252a8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RandomCropImages.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RandomCropImages)

[Unión de imágenes](https://docs.comfy.org/es/built-in-nodes/ImageStitch)[Redimensionar y rellenar imagen](https://docs.comfy.org/es/built-in-nodes/ResizeAndPadImage)
