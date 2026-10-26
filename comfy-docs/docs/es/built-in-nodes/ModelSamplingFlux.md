---
url: https://docs.comfy.org/es/built-in-nodes/ModelSamplingFlux/
title: Muestreo de modelo Flux - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:15.215110+00:00
---

# Muestreo de modelo Flux - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelSamplingFlux/

FLUX

# Muestreo de modelo Flux - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ModelSamplingFlux aplica el muestreo del modelo Flux a un modelo dado calculando un parámetro de desplazamiento basado en las dimensiones de la imagen.

Copiar páginaCopiar página

El nodo ModelSamplingFlux aplica el muestreo del modelo Flux a un modelo dado calculando un parámetro de desplazamiento basado en las dimensiones de la imagen. Crea una configuración de muestreo especializada que ajusta el comportamiento del modelo según el ancho, la altura y los parámetros de desplazamiento especificados, y luego devuelve el modelo modificado con la nueva configuración de muestreo aplicada.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo al que aplicar el muestreo de Flux| MODEL| Sí| -  
`desplazamiento_max`| Valor máximo de desplazamiento para el cálculo del muestreo (valor predeterminado: 1.15)| FLOAT| Sí| 0.0 - 100.0 (paso 0.01)  
`desplazamiento_base`| Valor base de desplazamiento para el cálculo del muestreo (valor predeterminado: 0.5)| FLOAT| Sí| 0.0 - 100.0 (paso 0.01)  
`ancho`| Ancho de la imagen objetivo en píxeles (valor predeterminado: 1024)| INT| Sí| 16 - MAX_RESOLUTION (paso 8)  
`altura`| Altura de la imagen objetivo en píxeles (valor predeterminado: 1024)| INT| Sí| 16 - MAX_RESOLUTION (paso 8)  
  
`max_shift` y `base_shift` son parámetros avanzados. El desplazamiento aplicado a la configuración de muestreo se calcula a partir de las dimensiones de la imagen: la resolución latente se calcula como `width × height / 256`, y el valor de desplazamiento se interpola entre `base_shift` en una resolución latente de 256 y `max_shift` en una resolución latente de 4096.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo modificado con la configuración de muestreo de Flux aplicada| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/es.md)

* * *

**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelSamplingFlux.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelSamplingFlux)

[Opciones Chroma Radiance](https://docs.comfy.org/es/built-in-nodes/ChromaRadianceOptions)[Referencia de estilo USO](https://docs.comfy.org/es/built-in-nodes/USOStyleReference)
