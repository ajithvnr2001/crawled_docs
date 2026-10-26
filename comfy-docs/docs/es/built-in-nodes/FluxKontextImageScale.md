---
url: https://docs.comfy.org/es/built-in-nodes/FluxKontextImageScale/
title: Escalar imagen Flux Kontext - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:48.898759+00:00
---

# Escalar imagen Flux Kontext - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/FluxKontextImageScale/

FLUX

# Escalar imagen Flux Kontext - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo escala la imagen de entrada a un tamaño óptimo utilizado durante el entrenamiento del modelo Flux Kontext

Copiar páginaCopiar página

Este nodo escala la imagen de entrada a un tamaño óptimo utilizado durante el entrenamiento del modelo Flux Kontext, empleando el algoritmo Lanczos y basándose en la relación de aspecto de la imagen de entrada. Este nodo es particularmente útil al ingresar imágenes de gran tamaño, ya que las entradas sobredimensionadas pueden provocar una degradación en la calidad de la salida del modelo o problemas como la aparición de múltiples sujetos en el resultado.

## 

​

Entradas

Nombre del Parámetro| Descripción| Tipo de Dato| Tipo de Entrada| Valor por Defecto| Rango de Valores  
---|---|---|---|---|---  
`imagen`| Imagen de entrada que se redimensionará| IMAGE| Requerido| -| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imagen`| Imagen redimensionada| IMAGE  
  
## 

​

Lista de Tamaños Predefinidos

A continuación se muestra una lista de tamaños estándar utilizados durante el entrenamiento del modelo. El nodo seleccionará el tamaño más cercano a la relación de aspecto de la imagen de entrada:

Ancho| Alto| Relación de Aspecto  
---|---|---  
672| 1568| 0.429  
688| 1504| 0.457  
720| 1456| 0.494  
752| 1392| 0.540  
800| 1328| 0.603  
832| 1248| 0.667  
880| 1184| 0.743  
944| 1104| 0.855  
1024| 1024| 1.000  
1104| 944| 1.170  
1184| 880| 1.345  
1248| 832| 1.500  
1328| 800| 1.660  
1392| 752| 1.851  
1456| 720| 2.022  
1504| 688| 2.186  
1568| 672| 2.333  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextImageScale/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/FluxKontextImageScale.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/FluxKontextImageScale)

[Guía Flux](https://docs.comfy.org/es/built-in-nodes/FluxGuidance)[Método de referencia del modelo de edición](https://docs.comfy.org/es/built-in-nodes/FluxKontextMultiReferenceLatentMethod)
