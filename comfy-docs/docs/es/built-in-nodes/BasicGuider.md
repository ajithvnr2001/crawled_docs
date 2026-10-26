---
url: https://docs.comfy.org/es/built-in-nodes/BasicGuider/
title: Gu\u00eda b\u00e1sica - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:31.590304+00:00
---

# Guía básica - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BasicGuider/

Guiadores

# Guía básica - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo BasicGuider crea un mecanismo de guía simple para el proceso de muestreo.

Copiar páginaCopiar página

El nodo BasicGuider crea un mecanismo de guía simple para el proceso de muestreo. Toma un modelo y datos de condicionamiento como entradas y produce un objeto guía que puede utilizarse para guiar el proceso de generación durante el muestreo. Este nodo proporciona la funcionalidad de guía fundamental necesaria para la generación controlada.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo que se utilizará para la guía| MODEL| Sí| -  
`acondicionamiento`| Los datos de condicionamiento que guían el proceso de generación| CONDITIONING| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`GUIDER`| Un objeto guía que puede utilizarse durante el proceso de muestreo para guiar la generación| GUIDER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/es.md)

* * *

**Source fingerprint (SHA-256):** `8ea6b56be58ae99baaf13a04c4fadbf8ad921801d8f2ce2aecce768cc34a3b20`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BasicGuider.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BasicGuider)

[Muestreador personalizado (avanzado)](https://docs.comfy.org/es/built-in-nodes/SamplerCustomAdvanced)[Guía CFG](https://docs.comfy.org/es/built-in-nodes/CFGGuider)
