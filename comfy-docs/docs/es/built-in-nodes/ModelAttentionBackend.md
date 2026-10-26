---
url: https://docs.comfy.org/es/built-in-nodes/ModelAttentionBackend/
title: Backend de atenci\u00f3n del modelo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:12.690450+00:00
---

# Backend de atención del modelo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelAttentionBackend/

Parches

# Backend de atención del modelo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo selecciona la implementación de atención densa para un modelo, clona el modelo, aplica el backend elegido y devuelve el clon parcheado.

Copiar páginaCopiar página

Este nodo selecciona la implementación de atención densa para un modelo, clona el modelo, aplica el backend elegido y devuelve el clon parcheado. Cuando se usa con Block Sparse Attention, este backend se utiliza siempre que la atención dispersa esté inactiva o no sea compatible. Si el backend seleccionado no está disponible, el nodo recurre automáticamente a la atención de PyTorch.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo al que se aplicará el parche.| MODEL| Sí|   
`atención`| El backend de atención densa que se aplicará. La atención de Comfy Kitchen usa atención INT8 cuantizada y solo está disponible en GPU de Nvidia y AMD. Predeterminado: “pytorch attention”. Si el backend seleccionado no está disponible, se usa la atención de PyTorch como respaldo.| COMBO| Sí| ”pytorch attention"  
"comfy kitchen attention”  
  
Nota: La opción “comfy kitchen attention” solo se muestra cuando el módulo de atención INT8 de Comfy Kitchen está disponible en el entorno actual.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| Un clon del modelo de entrada al que se ha aplicado el backend de atención seleccionado.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/es.md)

* * *

**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelAttentionBackend.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelAttentionBackend)

[Ventanas de contexto (Manual)](https://docs.comfy.org/es/built-in-nodes/ContextWindowsManual)[Escala de Ruido del Modelo](https://docs.comfy.org/es/built-in-nodes/ModelNoiseScale)
