---
url: https://docs.comfy.org/es/built-in-nodes/StringCompare/
title: Comparar - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:33.060676+00:00
---

# Comparar - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/StringCompare/

Texto

# Comparar - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo StringCompare compara dos cadenas de texto utilizando diferentes métodos de comparación.

Copiar páginaCopiar página

El nodo StringCompare compara dos cadenas de texto utilizando diferentes métodos de comparación. Puede verificar si una cadena comienza con otra, termina con otra, o si ambas cadenas son exactamente iguales. La comparación puede realizarse considerando o ignorando las diferencias entre mayúsculas y minúsculas.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`cadena_a`| La primera cadena a comparar| STRING| Sí| -  
`cadena_b`| La segunda cadena contra la que se compara| STRING| Sí| -  
`modo`| El método de comparación a utilizar (predeterminado: “Comienza Con”)| COMBO| Sí| ”Comienza Con"  
"Termina Con"  
"Igual”  
`distingue mayúsculas y minúsculas`| Si se deben considerar las diferencias entre mayúsculas y minúsculas durante la comparación (predeterminado: verdadero)| BOOLEAN| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| Devuelve verdadero si se cumple la condición de comparación, falso en caso contrario| BOOLEAN  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/es.md)

* * *

**Source fingerprint (SHA-256):** `4491e4acd2c1881e9c924c6ae51d764dec5f46279094d173fe551e9ee9256597`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/StringCompare.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/StringCompare)

[Guardar Texto](https://docs.comfy.org/es/built-in-nodes/SaveText)[Concatenar](https://docs.comfy.org/es/built-in-nodes/StringConcatenate)
