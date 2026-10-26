---
url: https://docs.comfy.org/es/built-in-nodes/StringContains/
title: Contiene - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:33.273723+00:00
---

# Contiene - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/StringContains/

Texto

# Contiene - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo StringContains verifica si una cadena de texto determinada contiene una subcadena especificada.

Copiar páginaCopiar página

El nodo StringContains verifica si una cadena de texto determinada contiene una subcadena especificada. Puede realizar esta verificación con coincidencia sensible a mayúsculas/minúsculas o insensible, devolviendo un resultado booleano que indica si la subcadena fue encontrada dentro de la cadena principal.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`cadena`| La cadena de texto principal en la que buscar| STRING| Sí| -  
`subcadena`| El texto a buscar dentro de la cadena principal| STRING| Sí| -  
`distingue mayúsculas y minúsculas`| Determina si la búsqueda debe ser sensible a mayúsculas/minúsculas (valor predeterminado: true)| BOOLEAN| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`contiene`| Devuelve true si la subcadena se encuentra en la cadena, false en caso contrario| BOOLEAN  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/es.md)

* * *

**Source fingerprint (SHA-256):** `ef7329ca8586e0f894306d93835490edb948a346db1e0cb011e4da5a6fe44202`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/StringContains.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/StringContains)

[Concatenar](https://docs.comfy.org/es/built-in-nodes/StringConcatenate)[Formatear Texto](https://docs.comfy.org/es/built-in-nodes/StringFormat)
