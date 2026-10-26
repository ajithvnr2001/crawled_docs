---
url: https://docs.comfy.org/es/built-in-nodes/ReplaceText/
title: Reemplazar texto - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:23.340066+00:00
---

# Reemplazar texto - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ReplaceText/

Texto

# Reemplazar texto - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Reemplazar Texto realiza una sustitución de texto simple.

Copiar páginaCopiar página

El nodo Reemplazar Texto realiza una sustitución de texto simple. Busca un fragmento de texto específico dentro de la entrada y reemplaza cada aparición con un nuevo fragmento de texto. La operación se aplica a todas las entradas de texto proporcionadas al nodo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`text`| El texto a procesar.| STRING| Sí| -  
`find`| Texto a buscar (predeterminado: cadena vacía).| STRING| Sí| -  
`replace`| Texto con el que reemplazar (predeterminado: cadena vacía).| STRING| Sí| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`texts`| El texto procesado con todas las apariciones del texto `find` reemplazadas por el texto `replace`.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/es.md)

* * *

**Source fingerprint (SHA-256):** `e9d4681e638c5ca2732ec254282243e9e9cdd01cc985af8bbfa41dea208cb7dd`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ReplaceText.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ReplaceText)

[Reemplazo regex](https://docs.comfy.org/es/built-in-nodes/RegexReplace)[Guardar Texto](https://docs.comfy.org/es/built-in-nodes/SaveText)
