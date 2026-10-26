---
url: https://docs.comfy.org/es/built-in-nodes/NormalizeImages/
title: Normalizar im\u00e1genes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:15.756676+00:00
---

# Normalizar imágenes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/NormalizeImages/

Color

# Normalizar imágenes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo normaliza los colores de una imagen de entrada ajustando sus valores de píxel según una media y una desviación estándar especificadas.

Copiar páginaCopiar página

Este nodo normaliza los colores de una imagen de entrada ajustando sus valores de píxel según una media y una desviación estándar especificadas. A cada píxel se le resta la media y luego se divide por la desviación estándar, lo cual es un paso común para estandarizar los datos de imagen antes de otro procesamiento.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`image`| La imagen de entrada que se va a normalizar.| IMAGE| Sí| -  
`media`| Valor de la media para la normalización (predeterminado: 0.5).| FLOAT| No| 0.0 - 1.0  
`desviación estándar`| Desviación estándar para la normalización (predeterminado: 0.5).| FLOAT| No| 0.001 - 1.0  
  
Los parámetros `mean` y `std` controlan la normalización aplicada a la imagen de entrada. El valor predeterminado para ambos parámetros es 0.5. Nota: Si la imagen de entrada tiene un canal alfa (transparencia), ese canal no se normaliza. Se copia sin cambios a la salida porque el alfa almacena transparencia en lugar de color. Nota: El nodo funciona con cualquier tamaño de lote, por lo que se pueden procesar varias imágenes a la vez.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| La imagen resultante después de aplicar el proceso de normalización. Los valores de píxel se ajustan usando la media y la desviación estándar especificadas, y el canal alfa (si está presente) se conserva.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/es.md)

* * *

**Source fingerprint (SHA-256):** `30c0587265754842ff7d1e5f339fc934b58d59bb3ba18716c2a1f9679f2d561d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/NormalizeImages.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/NormalizeImages)

[Imagen YUV a RGB](https://docs.comfy.org/es/built-in-nodes/ImageYUVToRGB)[Componer imagen con máscara](https://docs.comfy.org/es/built-in-nodes/ImageCompositeMasked)
