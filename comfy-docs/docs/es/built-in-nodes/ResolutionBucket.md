---
url: https://docs.comfy.org/es/built-in-nodes/ResolutionBucket/
title: Agrupaci\u00f3n por resoluci\u00f3n - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:23.689476+00:00
---

# Agrupación por resolución - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ResolutionBucket/

Entrenamiento

# Agrupación por resolución - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo organiza una lista de imágenes latentes y sus datos de condicionamiento correspondientes por su resolución.

Copiar páginaCopiar página

Este nodo organiza una lista de imágenes latentes y sus datos de condicionamiento correspondientes por su resolución. Agrupa los elementos que comparten la misma altura y anchura, creando lotes separados para cada resolución única. Este proceso es útil para preparar datos para un entrenamiento eficiente, ya que permite a los modelos procesar múltiples elementos del mismo tamaño juntos.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`latentes`| Lista de diccionarios de latentes para agrupar por resolución.| LATENT| Sí| N/A  
`condicionamiento`| Lista de listas de condicionamiento (debe coincidir con la longitud de `latents`).| CONDITIONING| Sí| N/A  
  
**Nota:** Ambas entradas son entradas de tipo lista, lo que significa que el nodo recibe una lista de elementos para cada una. El número de elementos de la lista `latents` debe coincidir exactamente con el número de elementos de la lista `conditioning`; si las cantidades no coinciden, el nodo genera un error. Cada diccionario latente puede contener un lote de muestras, y la lista de condicionamiento correspondiente debe contener un número coincidente de elementos de condicionamiento para ese lote, ya que cada muestra del lote está emparejada con su propia entrada de condicionamiento. Las muestras latentes pueden tener una forma de (B, C, H, W) para imágenes o (B, T, C, H, W) para videos; el nodo las agrupa solo por altura y anchura.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`latents`| Lista de diccionarios de latentes por lotes, uno por cada grupo de resolución.| LATENT  
`conditioning`| Lista de listas de condicionamiento, una por cada grupo de resolución.| CONDITIONING  
  
**Nota:** Ambas salidas son salidas de tipo lista. Cada lista de salida contiene una entrada por cada resolución única (altura y anchura) encontrada en la entrada, en el orden en que se encontraron por primera vez las resoluciones. Los latentes dentro de cada grupo se apilan a lo largo de una nueva dimensión de lote.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/es.md)

* * *

**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ResolutionBucket.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ResolutionBucket)

[Crear conjunto de datos de entrenamiento](https://docs.comfy.org/es/built-in-nodes/MakeTrainingDataset)[Guardar conjunto de datos de entrenamiento](https://docs.comfy.org/es/built-in-nodes/SaveTrainingDataset)
