---
url: https://docs.comfy.org/es/built-in-nodes/ResizeAndPadImage/
title: Redimensionar y rellenar imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:23.928810+00:00
---

# Redimensionar y rellenar imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ResizeAndPadImage/

Transformación

# Redimensionar y rellenar imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ResizeAndPadImage redimensiona una imagen para que se ajuste a unas dimensiones específicas, manteniendo su relación de aspecto original.

Copiar páginaCopiar página

El nodo ResizeAndPadImage redimensiona una imagen para que se ajuste a unas dimensiones específicas, manteniendo su relación de aspecto original. Escala la imagen proporcionalmente para que quepa dentro del ancho y alto objetivo, y luego añade relleno alrededor de los bordes para llenar el espacio restante. El color de relleno y el método de interpolación se pueden personalizar para controlar la apariencia de las áreas rellenas y la calidad del redimensionamiento.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada que se redimensionará y rellenará| IMAGE| Sí| -  
`ancho_objetivo`| El ancho deseado de la imagen de salida (predeterminado: 512)| INT| Sí| 1 a MAX_RESOLUTION  
`alto_objetivo`| La altura deseada de la imagen de salida (predeterminado: 512)| INT| Sí| 1 a MAX_RESOLUTION  
`color_relleno`| El color que se usará para las áreas de relleno alrededor de la imagen redimensionada (predeterminado: “white”)| COMBO| Sí| ”white"  
"black”  
`interpolación`| El método de interpolación utilizado para redimensionar la imagen (predeterminado: “area”)| COMBO| Sí| ”area"  
"bicubic"  
"nearest-exact"  
"bilinear"  
"lanczos”  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen de salida redimensionada y rellenada| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/es.md)

* * *

**Source fingerprint (SHA-256):** `01566327d46043d1ff9ce404b4df8f49e853d0b01d07cc189fb843157dac1cac`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ResizeAndPadImage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ResizeAndPadImage)

[Recorte aleatorio de imágenes](https://docs.comfy.org/es/built-in-nodes/RandomCropImages)[Redimensionar imágenes por el borde más largo](https://docs.comfy.org/es/built-in-nodes/ResizeImagesByLongerEdge)
