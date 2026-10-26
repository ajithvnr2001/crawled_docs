---
url: https://docs.comfy.org/es/built-in-nodes/PrimitiveBoundingBox/
title: Caja delimitadora - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:19.085359+00:00
---

# Caja delimitadora - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PrimitiveBoundingBox/

Primitivos

# Caja delimitadora - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo PrimitiveBoundingBox crea un área rectangular simple definida por su posición y tamaño.

Copiar páginaCopiar página

El nodo PrimitiveBoundingBox crea un área rectangular simple definida por su posición y tamaño. Toma coordenadas X e Y para la esquina superior izquierda, junto con valores de ancho y alto, y genera una estructura de datos de cuadro delimitador que puede ser utilizada por otros nodos en un flujo de trabajo.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`x`| La coordenada X de la esquina superior izquierda del cuadro delimitador (por defecto: 0).| INT| Sí| 0 a 16384  
`y`| La coordenada Y de la esquina superior izquierda del cuadro delimitador (por defecto: 0).| INT| Sí| 0 a 16384  
`width`| El ancho del cuadro delimitador (por defecto: 512).| INT| Sí| 1 a 16384  
`height`| La altura del cuadro delimitador (por defecto: 512).| INT| Sí| 1 a 16384  
  
Nota: Todos los valores máximos siguen la constante MAX_RESOLUTION de ComfyUI, que define la dimensión de imagen más grande que el nodo acepta.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`bounding_box`| Una estructura de datos que contiene las propiedades `x`, `y`, `width` y `height` del rectángulo definido.| BOUNDING_BOX  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/es.md)

* * *

**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PrimitiveBoundingBox.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PrimitiveBoundingBox)

[Booleano](https://docs.comfy.org/es/built-in-nodes/PrimitiveBoolean)[Flotante](https://docs.comfy.org/es/built-in-nodes/PrimitiveFloat)
