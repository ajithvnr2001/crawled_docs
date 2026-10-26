---
url: https://docs.comfy.org/es/built-in-nodes/CropMask/
title: Recortar m\u00e1scara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:42.971683+00:00
---

# Recortar máscara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CropMask/

Máscara

# Recortar máscara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo CropMask está diseñado para recortar un área específica de una máscara determinada.

Copiar páginaCopiar página

El nodo CropMask está diseñado para recortar un área específica de una máscara determinada. Permite a los usuarios definir la región de interés especificando coordenadas y dimensiones, extrayendo eficazmente una porción de la máscara para su posterior procesamiento o análisis.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`máscara`| La entrada de máscara representa la imagen de máscara que se va a recortar. Es esencial para definir el área a extraer según las coordenadas y dimensiones especificadas.| MASK  
`x`| La coordenada x especifica el punto de inicio en el eje horizontal desde el cual debe comenzar el recorte.| INT  
`y`| La coordenada y determina el punto de inicio en el eje vertical para la operación de recorte.| INT  
`ancho`| El ancho define la extensión horizontal del área de recorte desde el punto de inicio.| INT  
`altura`| La altura especifica la extensión vertical del área de recorte desde el punto de inicio.| INT  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`máscara`| La salida es una máscara recortada, que es una porción de la máscara original definida por las coordenadas y dimensiones especificadas.| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropMask/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CropMask.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CropMask)

[Procesar máscaras por lotes](https://docs.comfy.org/es/built-in-nodes/BatchMasksNode)[Difuminar máscara](https://docs.comfy.org/es/built-in-nodes/FeatherMask)
