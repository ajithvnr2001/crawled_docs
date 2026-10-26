---
url: https://docs.comfy.org/es/built-in-nodes/RegexExtract/
title: Extracci\u00f3n regex - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:22.809761+00:00
---

# Extracción regex - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RegexExtract/

Texto

# Extracción regex - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo RegexExtract busca patrones en texto utilizando expresiones regulares.

Copiar páginaCopiar página

El nodo RegexExtract busca patrones en texto utilizando expresiones regulares. Puede encontrar la primera coincidencia, todas las coincidencias, grupos específicos de las coincidencias, o todos los grupos en múltiples coincidencias. El nodo admite varias flags de expresiones regulares para sensibilidad a mayúsculas/minúsculas, coincidencia multilínea y comportamiento dotall.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`cadena`| El texto de entrada en el que buscar patrones| STRING| Sí| -  
`patrón_regex`| El patrón de expresión regular a buscar| STRING| Sí| -  
`modo`| El modo de extracción determina qué partes de las coincidencias se devuelven (predeterminado: “First Match”)| COMBO| Sí| ”First Match"  
"All Matches"  
"First Group"  
"All Groups”  
`insensible_a_mayúsculas`| Si se ignora mayúsculas/minúsculas al coincidir (predeterminado: True)| BOOLEAN| No| -  
`multilínea`| Si se trata la cadena como múltiples líneas (predeterminado: False)| BOOLEAN| No| -  
`dotall`| Si el punto (.) coincide con saltos de línea (predeterminado: False)| BOOLEAN| No| -  
`índice_de_grupo`| El índice del grupo de captura a extraer al usar modos de grupo (predeterminado: 1)| INT| No| 0-100  
  
**Nota:** Al usar los modos “First Group” o “All Groups”, el parámetro `group_index` especifica qué grupo de captura extraer. El grupo 0 representa la coincidencia completa, mientras que los grupos 1+ representan los grupos de captura numerados en tu patrón de expresión regular.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| El texto extraído según el modo y los parámetros seleccionados| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/es.md)

* * *

**Source fingerprint (SHA-256):** `38e365d21bea966ed65bc78c184766330924fe75392cdb88c6978052037f5d5f`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RegexExtract.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RegexExtract)

[Unir listas de textos](https://docs.comfy.org/es/built-in-nodes/MergeTextLists)[Coincidencia regex](https://docs.comfy.org/es/built-in-nodes/RegexMatch)
