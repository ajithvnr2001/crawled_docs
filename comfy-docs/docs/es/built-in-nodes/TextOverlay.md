---
url: https://docs.comfy.org/es/built-in-nodes/TextOverlay/
title: Superponer texto - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:35.767938+00:00
---

# Superponer texto - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TextOverlay/

Texto

# Superponer texto - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo dibuja texto encima de una imagen o de un lote de imágenes.

Copiar páginaCopiar página

Este nodo dibuja texto encima de una imagen o de un lote de imágenes. Crea una superposición de texto usando un tamaño de fuente, color, posición vertical y alineación horizontal configurables, además de un contorno negro opcional, y luego combina la superposición con los píxeles de la imagen original.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`imágenes`| La imagen de entrada o el lote de imágenes sobre el que dibujar texto| IMAGE| Sí|   
`texto`| El texto que se superpondrá sobre la imagen (predeterminado: ""). Admite varias líneas: las secuencias de escape `\n` y `\t` se convierten en saltos de línea y tabulaciones, y las líneas largas se ajustan automáticamente para caber dentro del ancho de la imagen.| STRING| Sí|   
`tamaño de fuente`| Tamaño de fuente como porcentaje de la altura de la imagen (predeterminado: 5.0)| FLOAT| Sí| 0.5 a 50.0 (paso 0.5)  
`color`| Color del texto (predeterminado: “#ffffff”)| COLOR| Sí|   
`posición`| Posición vertical del texto en la imagen (predeterminado: “top”)| COMBO| Sí| ”top"  
"bottom”  
`alineación`| Alineación horizontal del texto (predeterminado: “left”)| COMBO| Sí| ”left"  
"center"  
"right”  
`contorno`| Dibujar un contorno negro alrededor del texto (predeterminado: True)| BOOLEAN| Sí|   
  
Nota: Si `text` está vacío o contiene solo espacios en blanco, el nodo devuelve las imágenes de entrada sin cambios. La superposición de texto se renderiza una vez y se aplica a cada imagen del lote. Si el bloque de texto renderizado es más alto que el área disponible de la imagen, el tamaño de fuente se reduce automáticamente hasta que encaje o alcance un tamaño mínimo.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`images`| Las imágenes de entrada con la superposición de texto compuesta encima| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/es.md)

* * *

**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TextOverlay.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TextOverlay)

[Generar prompt LTX2](https://docs.comfy.org/es/built-in-nodes/TextGenerateLTX2Prompt)[Convertir texto a minúsculas](https://docs.comfy.org/es/built-in-nodes/TextToLowercase)
