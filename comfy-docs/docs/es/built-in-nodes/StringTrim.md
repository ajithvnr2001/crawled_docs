---
url: https://docs.comfy.org/es/built-in-nodes/StringTrim/
title: Recortar - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:33.685624+00:00
---

# Recortar - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/StringTrim/

Texto

# Recortar - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo StringTrim elimina los caracteres de espacio en blanco del inicio, final o ambos lados de una cadena de texto.

Copiar páginaCopiar página

El nodo `StringTrim` elimina los caracteres de espacio en blanco del inicio, final o ambos lados de una cadena de texto. Puedes elegir recortar desde el lado izquierdo, el lado derecho o ambos lados de la cadena. Esto es útil para limpiar entradas de texto eliminando espacios no deseados, tabulaciones o saltos de línea.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`cadena`| La cadena de texto a procesar. Admite entrada multilínea.| STRING| Sí| -  
`modo`| Especifica qué lado(s) de la cadena recortar. “Both” elimina espacios en blanco de ambos extremos, “Left” solo del inicio, “Right” solo del final.| COMBO| Sí| ”Both"  
"Left"  
"Right”  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| La cadena de texto recortada, con los espacios en blanco eliminados según el modo seleccionado.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/es.md)

* * *

**Source fingerprint (SHA-256):** `29b4da100373585af8a672ccfbd4c0b597705c1d8c176b2f88f3e878c1192460`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/StringTrim.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/StringTrim)

[Subcadena](https://docs.comfy.org/es/built-in-nodes/StringSubstring)[Eliminar espacios en blanco](https://docs.comfy.org/es/built-in-nodes/StripWhitespace)
