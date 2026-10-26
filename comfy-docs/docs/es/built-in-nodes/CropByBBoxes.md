---
url: https://docs.comfy.org/es/built-in-nodes/CropByBBoxes/
title: Recortar por cajas delimitadoras - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:42.695459+00:00
---

# Recortar por cajas delimitadoras - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CropByBBoxes/

Transformación

# Recortar por cajas delimitadoras - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CropByBBoxes extrae y redimensiona regiones rectangulares específicas de un lote de imágenes de entrada.

Copiar páginaCopiar página

El nodo CropByBBoxes extrae y redimensiona regiones rectangulares específicas de un lote de imágenes de entrada. Utiliza las coordenadas de cuadros delimitadores proporcionadas para definir el área a recortar de cada imagen. Las regiones recortadas se redimensionan luego a una dimensión de salida especificada, con opciones para estirar el recorte o rellenarlo para preservar su relación de aspecto original.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| El lote de imágenes de entrada a recortar.| IMAGE| Sí| -  
`cajas delimitadoras`| La lista de cuadros delimitadores que definen las regiones a recortar. Esta entrada es forzada, lo que significa que debe estar conectada.| BOUNDINGBOX| Sí| -  
`ancho de salida`| El ancho al que se redimensiona cada recorte (predeterminado: 512).| INT| No| 64 - 4096  
`alto de salida`| La altura a la que se redimensiona cada recorte (predeterminado: 512).| INT| No| 64 - 4096  
`relleno`| Relleno adicional en píxeles añadido a cada lado del cuadro delimitador antes de recortar (predeterminado: 0).| INT| No| 0 - 1024  
`mantener_proporción`| Si estirar el recorte para que se ajuste al tamaño de salida, o rellenarlo con píxeles negros para preservar su relación de aspecto (predeterminado: “stretch”).| COMBO| No| `"stretch"`  
`"pad"`  
  
**Nota:** El nodo procesa un fotograma de imagen a la vez. Si se proporcionan múltiples cuadros delimitadores para un solo fotograma, calcula una única región de recorte que es la unión (el rectángulo más pequeño que contiene todos los cuadros) de todos los cuadros proporcionados. Si una región de recorte calculada no es válida (por ejemplo, ancho o altura cero), el nodo creará un recorte alternativo desde el centro-superior de la imagen.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imagen`| Todas las regiones recortadas y redimensionadas, apiladas en un solo lote de imágenes.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/es.md)

* * *

**Source fingerprint (SHA-256):** `9c0b3078405567911731c42e1873c57c77363e21ef6805769730667c811b0a0b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CropByBBoxes.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CropByBBoxes)

[Recorte central de imágenes](https://docs.comfy.org/es/built-in-nodes/CenterCropImages)[Recorte de imagen (obsoleto)](https://docs.comfy.org/es/built-in-nodes/ImageCrop)
