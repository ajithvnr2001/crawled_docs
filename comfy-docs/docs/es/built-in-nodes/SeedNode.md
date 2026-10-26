---
url: https://docs.comfy.org/es/built-in-nodes/SeedNode/
title: Semilla - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:30.013679+00:00
---

# Semilla - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SeedNode/

Utilidades

# Semilla - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Seed proporciona un valor entero que se puede usar como semilla para controlar la reproducibilidad de operaciones aleatorias en otros nodos.

Copiar páginaCopiar página

El nodo Seed proporciona un valor entero que se puede usar como semilla para controlar la reproducibilidad de operaciones aleatorias en otros nodos. Al proporcionar un valor inicial consistente, ayuda a mantener repetibles los resultados generados cuando sea necesario.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`semilla`| El valor de semilla que se va a usar. La opción control after generate determina si el valor permanece fijo o cambia después de cada generación; en este nodo, está establecido en fixed.| INT| Sí| 0 a 9223372036854775807  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`seed`| El valor de semilla generado.| INT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedNode/es.md)

* * *

**Source fingerprint (SHA-256):** `19f9b22945bb152ff5066195067f1b6b4c006589f26c7533fad905044ac3b7fa`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SeedNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SeedNode)

[Selector de resolución](https://docs.comfy.org/es/built-in-nodes/ResolutionSelector)[MarkdownNote](https://docs.comfy.org/es/built-in-nodes/MarkdownNote)
