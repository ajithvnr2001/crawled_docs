---
url: https://docs.comfy.org/es/built-in-nodes/RegexMatch/
title: Coincidencia regex - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:22.630964+00:00
---

# Coincidencia regex - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RegexMatch/

Texto

# Coincidencia regex - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo RegexMatch verifica si una cadena de texto contiene una coincidencia con un patrón de expresión regular determinado.

Copiar páginaCopiar página

El nodo RegexMatch verifica si una cadena de texto contiene una coincidencia con un patrón de expresión regular determinado. Busca en la cadena de entrada y devuelve un resultado simple de sí/no que indica si el patrón se encontró en alguna parte del texto. Puedes ajustar cómo funciona la búsqueda habilitando opciones como la coincidencia sin distinción de mayúsculas/minúsculas o el modo multilínea.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`cadena`| La cadena de texto en la que buscar coincidencias| STRING| Sí| -  
`patrón_regex`| El patrón de expresión regular para comparar con la cadena| STRING| Sí| -  
`insensible_a_mayúsculas`| Si se debe ignorar mayúsculas/minúsculas al coincidir (valor predeterminado: True)| BOOLEAN| No| -  
`multilínea`| Si se debe habilitar el modo multilínea para la coincidencia de expresiones regulares (valor predeterminado: False)| BOOLEAN| No| -  
`dotall`| Si se debe habilitar el modo dotall para la coincidencia de expresiones regulares (valor predeterminado: False)| BOOLEAN| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`coincidencias`| Devuelve True si el patrón de expresión regular coincide con alguna parte de la cadena de entrada, False en caso contrario| BOOLEAN  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/es.md)

* * *

**Source fingerprint (SHA-256):** `b0ee05277edd8600d880051aa33a940c01abc170553515ab02960f25b1aec2be`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RegexMatch.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RegexMatch)

[Extracción regex](https://docs.comfy.org/es/built-in-nodes/RegexExtract)[Reemplazo regex](https://docs.comfy.org/es/built-in-nodes/RegexReplace)
