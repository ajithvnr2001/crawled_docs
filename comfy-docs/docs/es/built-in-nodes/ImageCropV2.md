---
url: https://docs.comfy.org/es/built-in-nodes/ImageCropV2/
title: Recorte de imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.022716+00:00
---

# Recorte de imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageCropV2/

Transformación

# Recorte de imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo de Recorte de Imagen extrae una sección rectangular de una imagen de entrada.

Copiar páginaCopiar página

El nodo de Recorte de Imagen extrae una sección rectangular de una imagen de entrada. Se define la región a conservar especificando las coordenadas de su esquina superior izquierda, así como su ancho y alto. El nodo devuelve la porción recortada de la imagen original.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`image`| La imagen de entrada que se va a recortar.| IMAGE| Sí| N/A  
`crop_region`| Define el área rectangular que se extraerá de la imagen. Se especifica mediante `x` (inicio horizontal), `y` (inicio vertical), `ancho` y `alto`. Si la región definida se extiende más allá de los bordes de la imagen, se ajustará automáticamente para que quepa dentro de las dimensiones de la imagen.| BOUNDINGBOX| Sí| N/A  
  
**Nota sobre restricciones de la región:** La región de recorte se limita automáticamente para mantenerse dentro de los límites de la imagen de entrada. Si la coordenada `x` o `y` especificada es mayor que el ancho o alto de la imagen, se establecerá en la posición máxima válida. El ancho y alto del recorte resultante se ajustarán para que la región no exceda los bordes de la imagen.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`image`| La sección recortada de la imagen de entrada original.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/es.md)

* * *

**Source fingerprint (SHA-256):** `9d3543aa8396ae2ab0353accc3c89ae6be6495f6fdcefbb5439fa865a5d3059f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageCropV2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageCropV2)

[Recortar imagen a máscara](https://docs.comfy.org/es/built-in-nodes/ImageCropToMask)[Voltear imagen](https://docs.comfy.org/es/built-in-nodes/ImageFlip)
