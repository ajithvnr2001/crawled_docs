---
url: https://docs.comfy.org/es/built-in-nodes/LTXVCropGuides/
title: Recortar gu\u00edas LTXV - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:01.517899+00:00
---

# Recortar guías LTXV - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LTXVCropGuides/

Ltxv

# Recortar guías LTXV - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LTXVCropGuides elimina los datos de guía de fotogramas clave de un flujo de trabajo de generación de video.

Copiar páginaCopiar página

El nodo LTXVCropGuides elimina los datos de guía de fotogramas clave de un flujo de trabajo de generación de video. Cuenta los fotogramas clave registrados en el condicionamiento positivo, recorta esa cantidad de fotogramas del final de las muestras latentes y la máscara de ruido, y borra las entradas de índice de fotogramas clave y de atención de guía de ambas entradas de condicionamiento. Cuando no se encuentran fotogramas clave, las entradas de condicionamiento se devuelven sin cambios y el latente se pasa con un tensor de muestras clonado y su máscara de ruido.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`positivo`| La entrada de condicionamiento positivo que contiene información de guía para la generación. La cantidad de fotogramas clave que contiene determina cuántos fotogramas se recortan del latente.| CONDITIONING| Sí| -  
`negativo`| La entrada de condicionamiento negativo que contiene información de guía sobre qué evitar en la generación. Sus datos de fotogramas clave se borran junto con el condicionamiento positivo.| CONDITIONING| Sí| -  
`latente`| La representación latente que contiene muestras de imagen y datos de máscara de ruido. Cuando hay fotogramas clave presentes, los fotogramas de los fotogramas clave finales se eliminan tanto de las muestras como de la máscara de ruido.| LATENT| Sí| -  
  
Nota: El recorte solo ocurre cuando se detectan índices de fotogramas clave en el condicionamiento positivo. Si no se detectan fotogramas clave, el condicionamiento positivo y negativo se devuelven sin cambios, mientras que el latente aún se devuelve con un tensor de muestras clonado y una máscara de ruido explícita (se crea una máscara de todos unos si el latente de entrada no tiene ninguna).

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positive`| El condicionamiento positivo procesado con los índices de fotogramas clave y las entradas de atención de guía borrados| CONDITIONING  
`negative`| El condicionamiento negativo procesado con los índices de fotogramas clave y las entradas de atención de guía borrados| CONDITIONING  
`latent`| La representación latente recortada con muestras y máscara de ruido ajustadas, donde se han eliminado las secciones de fotogramas clave| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/es.md)

* * *

**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LTXVCropGuides.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LTXVCropGuides)

[Acondicionamiento LTXV](https://docs.comfy.org/es/built-in-nodes/LTXVConditioning)[LTXV Duration Predictor](https://docs.comfy.org/es/built-in-nodes/LTXVDurationPredictor)
