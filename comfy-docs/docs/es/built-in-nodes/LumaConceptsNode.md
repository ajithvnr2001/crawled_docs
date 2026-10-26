---
url: https://docs.comfy.org/es/built-in-nodes/LumaConceptsNode/
title: Conceptos Luma - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:07.054628+00:00
---

# Conceptos Luma - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LumaConceptsNode/

Luma

# Conceptos Luma - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este documento fue generado por IA. Si encuentras algún error o tienes sugerencias de mejora

Copiar páginaCopiar página

Este documento fue generado por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/en.md) Almacena uno o más conceptos de cámara para usar con los nodos Luma Texto a Video y Luma Imagen a Video. Este nodo te permite seleccionar hasta cuatro conceptos de cámara y, opcionalmente, combinarlos con cadenas de conceptos existentes. **Nota:** Este nodo está marcado como obsoleto en el código fuente.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`concept1`| Primera selección de concepto de cámara de los conceptos Luma disponibles| STRING| Sí| Múltiples opciones disponibles  
Incluye opción “None”  
`concept2`| Segunda selección de concepto de cámara de los conceptos Luma disponibles| STRING| Sí| Múltiples opciones disponibles  
Incluye opción “None”  
`concept3`| Tercera selección de concepto de cámara de los conceptos Luma disponibles| STRING| Sí| Múltiples opciones disponibles  
Incluye opción “None”  
`concept4`| Cuarta selección de concepto de cámara de los conceptos Luma disponibles| STRING| Sí| Múltiples opciones disponibles  
Incluye opción “None”  
`luma_concepts`| Conceptos de cámara opcionales para agregar a los seleccionados aquí| LUMA_CONCEPTS| No| N/D  
  
**Nota:** Todos los parámetros de concepto (`concept1` a `concept4`) se pueden establecer en “None” si no deseas usar los cuatro espacios de concepto. El nodo fusionará cualquier `luma_concepts` proporcionado con los conceptos seleccionados para crear una cadena de conceptos combinada.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`luma_concepts`| Cadena de conceptos de cámara combinada que contiene todos los conceptos seleccionados| LUMA_CONCEPTS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/es.md)

* * *

**Source fingerprint (SHA-256):** `fc9da6288e29d89519f13e2412381ad8d689fc48353a80546a380dbe8f979037`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LumaConceptsNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LumaConceptsNode)

[LTX 2.5 Texto a Video](https://docs.comfy.org/es/built-in-nodes/LtxApi25TextToVideo)[Luma imagen a vídeo](https://docs.comfy.org/es/built-in-nodes/LumaImageToVideoNode)
