---
url: https://docs.comfy.org/es/built-in-nodes/LotusConditioning/
title: Acondicionamiento Lotus - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:07.329881+00:00
---

# Acondicionamiento Lotus - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LotusConditioning/

Lotus

# Acondicionamiento Lotus - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LotusConditioning proporciona embeddings de condicionamiento fijos y precalculados para el modelo Lotus.

Copiar páginaCopiar página

El nodo LotusConditioning proporciona embeddings de condicionamiento fijos y precalculados para el modelo Lotus. Debido a que Lotus utiliza un codificador congelado con condicionamiento nulo, el nodo incorpora directamente los embeddings de prompt resultantes en lugar de ejecutar inferencia o cargar archivos grandes de tensores, por lo que su salida nunca cambia. El condicionamiento devuelto se puede conectar directamente a un pipeline de generación que espera un condicionamiento compatible con Lotus.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
 _Sin entradas_|  Este nodo no acepta ningún parámetro de entrada.| -| -| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`conditioning`| Los embeddings de condicionamiento precalculados para el modelo Lotus. Se devuelven como una lista de condicionamiento que contiene los embeddings de prompt fijos junto con un diccionario vacío.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/es.md)

* * *

**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LotusConditioning.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LotusConditioning)

[Kandinsky 5 imagen a video](https://docs.comfy.org/es/built-in-nodes/Kandinsky5ImageToVideo)[Obtener parámetros IC-LoRA](https://docs.comfy.org/es/built-in-nodes/GetICLoRAParameters)
