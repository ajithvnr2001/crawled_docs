---
url: https://docs.comfy.org/es/built-in-nodes/RegexReplace/
title: Reemplazo regex - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:22.569007+00:00
---

# Reemplazo regex - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RegexReplace/

Texto

# Reemplazo regex - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo RegexReplace busca y reemplaza texto en cadenas utilizando patrones de expresiones regulares.

Copiar páginaCopiar página

El nodo RegexReplace busca y reemplaza texto en cadenas utilizando patrones de expresiones regulares. Permite buscar patrones de texto y reemplazarlos con texto nuevo, con opciones para controlar cómo funciona la coincidencia de patrones, incluyendo sensibilidad a mayúsculas/minúsculas, coincidencia multilínea y limitación del número de reemplazos.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`cadena`| La cadena de texto de entrada en la que buscar y reemplazar| STRING| Sí| -  
`patron_regex`| El patrón de expresión regular para buscar en la cadena de entrada| STRING| Sí| -  
`reemplazar`| El texto de reemplazo para sustituir los patrones coincidentes| STRING| Sí| -  
`insensible_a_mayusculas`| Cuando está habilitado, hace que la coincidencia de patrones ignore diferencias de mayúsculas/minúsculas (predeterminado: Verdadero)| BOOLEAN| No| -  
`multilínea`| Cuando está habilitado, cambia el comportamiento de ^ y $ para que coincidan al inicio/final de cada línea en lugar de solo al inicio/final de toda la cadena (predeterminado: Falso)| BOOLEAN| No| -  
`dotall`| Cuando está habilitado, el carácter punto (.) coincidirá con cualquier carácter, incluidos los caracteres de nueva línea. Cuando está deshabilitado, los puntos no coincidirán con nuevas líneas (predeterminado: Falso)| BOOLEAN| No| -  
`contador`| Número máximo de reemplazos a realizar. Establecer en 0 para reemplazar todas las ocurrencias (predeterminado). Establecer en 1 para reemplazar solo la primera coincidencia, 2 para las dos primeras coincidencias, etc. (predeterminado: 0)| INT| No| 0-100  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| La cadena modificada con los reemplazos especificados aplicados| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/es.md)

* * *

**Source fingerprint (SHA-256):** `4a4d4b317ee23314a4ac26cf3b58a2cc904bfb8111608f88345c1014b801ea00`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RegexReplace.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RegexReplace)

[Coincidencia regex](https://docs.comfy.org/es/built-in-nodes/RegexMatch)[Reemplazar texto](https://docs.comfy.org/es/built-in-nodes/ReplaceText)
