---
url: https://docs.comfy.org/es/built-in-nodes/ImageYUVToRGB/
title: Imagen YUV a RGB - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.702989+00:00
---

# Imagen YUV a RGB - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageYUVToRGB/

Color

# Imagen YUV a RGB - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageYUVToRGB convierte imágenes del espacio de color YUV al espacio de color RGB.

Copiar páginaCopiar página

El nodo ImageYUVToRGB convierte imágenes del espacio de color YUV al espacio de color RGB. Toma tres imágenes de entrada separadas que representan los componentes Y (luma), U (proyección azul) y V (proyección roja), y las combina en una sola imagen RGB.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`Y`| La imagen de entrada del componente Y (luminancia). Si la imagen tiene más de tres canales, solo se usan los primeros tres y se promedian en un único canal.| IMAGE| Sí| -  
`U`| La imagen de entrada del componente U (proyección azul). Si la imagen tiene más de tres canales, solo se usan los primeros tres y se promedian en un único canal.| IMAGE| Sí| -  
`V`| La imagen de entrada del componente V (proyección roja). Si la imagen tiene más de tres canales, solo se usan los primeros tres y se promedian en un único canal.| IMAGE| Sí| -  
  
**Nota:** Las tres imágenes de entrada (Y, U y V) deben proporcionarse juntas y deben tener dimensiones compatibles (altura, anchura y tamaño de lote coincidentes) para que la conversión se realice correctamente.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| La imagen RGB convertida| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageYUVToRGB/es.md)

* * *

**Source fingerprint (SHA-256):** `47e90b1a9aeb5ddfccea4493021b83e06faad3f84d40c8b0f2b3cec59b192c2e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageYUVToRGB.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageYUVToRGB)

[Convertir SDR a HDR](https://docs.comfy.org/es/built-in-nodes/ImageSDRToHDR)[Normalizar imágenes](https://docs.comfy.org/es/built-in-nodes/NormalizeImages)
