---
url: https://docs.comfy.org/es/built-in-nodes/CustomCombo/
title: Combinaci\u00f3n personalizada - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:42.850215+00:00
---

# Combinación personalizada - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CustomCombo/

Utilidades

# Combinación personalizada - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Custom Combo te permite definir tu propia lista de opciones de texto para un menú desplegable en lugar de elegir entre valores fijos.

Copiar páginaCopiar página

El nodo Custom Combo te permite definir tu propia lista de opciones de texto para un menú desplegable en lugar de elegir entre valores fijos. Es un nodo enfocado en el frontend que también tiene una representación en el backend, por lo que los flujos de trabajo que lo contienen siguen siendo compatibles. Cuando seleccionas una opción, el nodo genera como salida el texto seleccionado y su posición de índice.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`elección`| La opción de texto seleccionada del menú desplegable personalizado. La lista de opciones disponibles la define el usuario en la interfaz frontend del nodo.| COMBO| Sí| Definido por el usuario  
`index`| Un valor entero que se puede usar para especificar un índice. Predeterminado: 0.| INT| No| Cualquier entero (predeterminado: 0)  
  
**Nota:** La validación de las entradas de este nodo está deshabilitada intencionalmente. Esto te permite escribir cualquier opción de texto personalizada en el frontend sin que el backend verifique si tu selección coincide con una lista predefinida. Los widgets distintos del menú desplegable combo están totalmente definidos en el frontend. Este nodo está marcado como experimental.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`STRING`| La cadena de texto de la opción seleccionada del cuadro combo personalizado.| STRING  
`INDEX`| La posición de índice de la opción seleccionada en la lista desplegable.| INT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/es.md)

* * *

**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CustomCombo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CustomCombo)

[Editor de curvas](https://docs.comfy.org/es/built-in-nodes/CurveEditor)[Obtener elemento de la lista](https://docs.comfy.org/es/built-in-nodes/GetItemFromList)
