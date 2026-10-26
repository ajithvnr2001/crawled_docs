---
url: https://docs.comfy.org/es/built-in-nodes/ImageGrid/
title: Cuadr\u00edcula de im\u00e1genes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.510691+00:00
---

# Cuadrícula de imágenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageGrid/

Lote

# Cuadrícula de imágenes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Cuadrícula de Imágenes combina múltiples imágenes en una única cuadrícula o collage organizado.

Copiar páginaCopiar página

El nodo **Cuadrícula de Imágenes** combina múltiples imágenes en una única cuadrícula o collage organizado. Toma una lista de imágenes y las dispone en un número específico de columnas, redimensionando cada imagen para que se ajuste a un tamaño de celda definido y añadiendo relleno opcional entre ellas. El resultado es una única imagen nueva que contiene todas las imágenes de entrada en un diseño de cuadrícula.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imágenes`| Lista de imágenes que se organizarán en la cuadrícula. El nodo requiere al menos una imagen para funcionar.| IMAGE| Sí| -  
`columnas`| Número de columnas en la cuadrícula (valor predeterminado: 4).| INT| No| 1 - 20  
`ancho_de_celda`| Ancho, en píxeles, de cada celda en la cuadrícula (valor predeterminado: 256).| INT| No| 32 - 2048  
`alto_de_celda`| Alto, en píxeles, de cada celda en la cuadrícula (valor predeterminado: 256).| INT| No| 32 - 2048  
`espaciado`| Cantidad de relleno, en píxeles, que se colocará entre las imágenes en la cuadrícula (valor predeterminado: 4).| INT| No| 0 - 50  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imágenes`| La única imagen de salida que contiene todas las imágenes de entrada dispuestas en una cuadrícula.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/es.md)

* * *

**Source fingerprint (SHA-256):** `79d0942c79d3966d06fe804f839c1d677764cef90265bd621bf915fe6de0ad46`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageGrid.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageGrid)

[Imagen desde lote](https://docs.comfy.org/es/built-in-nodes/ImageFromBatch)[Unir lista de mosaicos en imagen](https://docs.comfy.org/es/built-in-nodes/ImageMergeTileList)
