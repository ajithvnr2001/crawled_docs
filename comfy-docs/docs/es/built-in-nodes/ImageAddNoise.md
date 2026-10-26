---
url: https://docs.comfy.org/es/built-in-nodes/ImageAddNoise/
title: A\u00f1adir ruido a imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:55.188268+00:00
---

# Añadir ruido a imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageAddNoise/

Filtros

# Añadir ruido a imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageAddNoise añade ruido aleatorio a una imagen de entrada.

Copiar páginaCopiar página

El nodo ImageAddNoise añade ruido aleatorio a una imagen de entrada. Utiliza una semilla aleatoria especificada para generar patrones de ruido consistentes y permite controlar la intensidad del efecto de ruido. La imagen resultante mantiene las mismas dimensiones que la entrada, pero con textura visual añadida.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada a la que se añadirá ruido| IMAGE| Sí| -  
`semilla`| La semilla aleatoria utilizada para crear el ruido (predeterminado: 0). Este parámetro admite la funcionalidad «control después de generar».| INT| Sí| 0 a 18446744073709551615  
`intensidad`| Controla la intensidad del efecto de ruido (predeterminado: 0.5, paso: 0.01)| FLOAT| Sí| 0.0 a 1.0  
  
**Nota:** Los valores de ruido se añaden a la imagen y el resultado se recorta al rango 0.0–1.0. Si la imagen de entrada tiene un canal alfa (4 canales), el canal alfa original se conserva sin cambios; el ruido solo se aplica a los canales de color.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| La imagen de salida con el ruido añadido aplicado| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/es.md)

* * *

**Source fingerprint (SHA-256):** `e6b9815e7c075c7ee97c924c22a92dfef6d9c65b97b6e65b0f9e1c96628f39f2`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageAddNoise.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageAddNoise)

[ColorTransfer](https://docs.comfy.org/es/built-in-nodes/ColorTransfer)[Mezcla de imágenes](https://docs.comfy.org/es/built-in-nodes/ImageBlend)
