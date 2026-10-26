---
url: https://docs.comfy.org/es/built-in-nodes/ImageRGBToYUV/
title: Imagen RGB a YUV - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.952677+00:00
---

# Imagen RGB a YUV - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageRGBToYUV/

Color

# Imagen RGB a YUV - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageRGBToYUV convierte una imagen RGB en componentes de color de estilo YUV mediante una conversión de color de RGB a YCbCr.

Copiar páginaCopiar página

El nodo ImageRGBToYUV convierte una imagen RGB en componentes de color de estilo YUV mediante una conversión de color de RGB a YCbCr. Divide el resultado en tres imágenes separadas — Y (luminancia o brillo), U (croma de diferencia de azul) y V (croma de diferencia de rojo) — y devuelve cada componente con el mismo ancho y alto que la entrada.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen RGB de entrada que se va a convertir en los componentes Y, U y V. Si la imagen contiene un canal alfa, solo se utilizan los tres primeros canales (RGB).| IMAGE| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`Y`| El componente de luminancia (brillo) del espacio de color YUV, devuelto como una imagen de tres canales| IMAGE  
`U`| El componente de croma de diferencia de azul del espacio de color YUV, devuelto como una imagen de tres canales| IMAGE  
`V`| El componente de croma de diferencia de rojo del espacio de color YUV, devuelto como una imagen de tres canales| IMAGE  
  
Cada salida tiene el mismo ancho y alto que la imagen de entrada. El componente Y, U o V correspondiente se repite en los tres canales para que cada salida se devuelva como una imagen estándar de tres canales.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/es.md)

* * *

**Source fingerprint (SHA-256):** `1a75ce64dfaec316a8f4b3a210cede388c9ba12d3ab3ec5ec14b0027be383744`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageRGBToYUV.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageRGBToYUV)

[Convertir espacio de color de imagen](https://docs.comfy.org/es/built-in-nodes/ImageColorSpace)[Convertir SDR a HDR](https://docs.comfy.org/es/built-in-nodes/ImageSDRToHDR)
