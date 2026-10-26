---
url: https://docs.comfy.org/es/built-in-nodes/StringSubstring/
title: Subcadena - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:33.597818+00:00
---

# Subcadena - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/StringSubstring/

Texto

# Subcadena - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo StringSubstring extrae una porción de texto de una cadena más grande.

Copiar páginaCopiar página

El nodo StringSubstring extrae una porción de texto de una cadena más grande. Toma una posición inicial y una posición final para definir la sección que se desea extraer, y luego devuelve el texto comprendido entre esas dos posiciones.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`cadena`| La cadena de texto de entrada de la que se extraerá. Admite texto de varias líneas.| STRING| Sí| -  
`inicio`| El índice de la posición inicial para la subcadena. El primer carácter se encuentra en el índice 0.| INT| Sí| -  
`fin`| El índice de la posición final para la subcadena. El carácter en este índice no se incluye en el resultado.| INT| Sí| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| La subcadena extraída del texto de entrada, que contiene todos los caracteres desde la posición `inicio` hasta (sin incluir) la posición `fin`.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/es.md)

* * *

**Source fingerprint (SHA-256):** `962d0b19af88b6c95b5c9d374081ecd55ee8cffbfb638de7ed38e6e378b220c5`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/StringSubstring.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/StringSubstring)

[Reemplazar](https://docs.comfy.org/es/built-in-nodes/StringReplace)[Recortar](https://docs.comfy.org/es/built-in-nodes/StringTrim)
