---
url: https://docs.comfy.org/es/built-in-nodes/StringFormat/
title: Formatear Texto - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:33.334295+00:00
---

# Formatear Texto - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/StringFormat/

Texto

# Formatear Texto - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo da formato a un texto con el método format de cadenas de Python.

Copiar páginaCopiar página

## 

​

Descripción general

Este nodo formatea texto utilizando el método de formato de cadenas de Python. Funciona como una plantilla donde se define un patrón de texto con marcadores de posición, y luego se proporcionan valores para completar dichos marcadores. Soporta todas las opciones y características de formato de Python.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`f_string`| La plantilla de cadena de formato con marcadores de posición (predeterminado: `{a}`). Admite entrada multilínea.| STRING| Sí| N/D  
`values`| Entrada dinámica para proporcionar valores que completan los marcadores de posición en la cadena de formato. Se pueden agregar múltiples entradas de valor según sea necesario.| STRING| Sí| N/D  
  
**Nota sobre la entrada`values`:** Esta entrada es dinámica y se puede expandir para incluir múltiples valores con nombre. Cada entrada de valor está etiquetada con una letra (a, b, c, etc.) y corresponde a un marcador de posición en la cadena de formato (por ejemplo, `{a}`, `{b}`, `{c}`). Puede agregar o eliminar entradas de valor según sea necesario.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`STRING`| La cadena de texto formateada con todos los marcadores de posición reemplazados por sus valores correspondientes.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringFormat/es.md)

* * *

**Source fingerprint (SHA-256):** `72625287533829a8087687bb47f39bc265aced3d5f43066f615326d729725122`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/StringFormat.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/StringFormat)

[Contiene](https://docs.comfy.org/es/built-in-nodes/StringContains)[Longitud](https://docs.comfy.org/es/built-in-nodes/StringLength)
