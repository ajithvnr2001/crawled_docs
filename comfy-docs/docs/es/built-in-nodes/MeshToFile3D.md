---
url: https://docs.comfy.org/es/built-in-nodes/MeshToFile3D/
title: Crear archivo 3D (desde malla) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:10.080895+00:00
---

# Crear archivo 3D (desde malla) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MeshToFile3D/

3D

# Crear archivo 3D (desde malla) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo serializa una malla en un objeto de archivo GLB que puede pasarse a los nodos Save 3D o Preview 3D.

Copiar páginaCopiar página

Este nodo serializa una malla en un objeto de archivo GLB que puede pasarse a los nodos Save 3D o Preview 3D. Conserva todos los datos de la malla, incluidos UVs, colores, normales, textura, mapas de normales/oclusión/emisión y configuración del material. Solo se utiliza el primer elemento de un lote con varios elementos.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`malla`| La malla que se convertirá en un archivo GLB, incluidos UVs, colores, normales, textura, mapas de normales/oclusión/emisión y material. Solo se admite un elemento por lote; si un lote contiene varios elementos, se utiliza el primero.| MESH| Sí| Malla única  
  
Nota: El nodo admite solo un elemento por lote. Si la malla de entrada contiene más de un elemento en su lote, se registra una advertencia y se utiliza el primer elemento. La malla debe contener al menos un vértice y una cara; una malla vacía genera un error.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model_3d`| Un objeto de archivo GLB (glTF Binary) que contiene la malla serializada, listo para guardarse o previsualizarse mediante otros nodos 3D.| FILE3D  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshToFile3D/es.md)

* * *

**Source fingerprint (SHA-256):** `f004c2907c0df2e0127e49b4767d1624bf89c72665fc7028347a0b8a63a5772e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MeshToFile3D.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MeshToFile3D)

[Cargar 3D (Avanzado)](https://docs.comfy.org/es/built-in-nodes/Load3DAdvanced)[Vista previa 3D y animación (OBSOLETO)](https://docs.comfy.org/es/built-in-nodes/Preview3D)
