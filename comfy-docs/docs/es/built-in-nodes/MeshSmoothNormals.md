---
url: https://docs.comfy.org/es/built-in-nodes/MeshSmoothNormals/
title: Suavizar normales de malla - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:10.140647+00:00
---

# Suavizar normales de malla - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MeshSmoothNormals/

Mallas

# Suavizar normales de malla - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Calcula normales suaves por vértice para una malla y las adjunta.

Copiar páginaCopiar página

Calcula normales suaves por vértice para una malla y las adjunta. Los visores glTF sombrean las mallas sin normales de forma plana (por cara); este nodo hace que se sombreen suavemente. Con un ángulo de pliegue inferior a 180, los bordes más afilados que el umbral se mantienen duros dividiendo los vértices a lo largo de ellos.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`malla`| La malla de entrada que se va a procesar.| MESH| Sí| -  
`crease_angle`| Los bordes cuyo ángulo diedro supera este valor (en grados) permanecen duros (los vértices se dividen). 180 = totalmente suave; un valor menor conserva los bordes afilados (p. ej., ~30-60 para superficies duras). Predeterminado: 180.0.| FLOAT| Sí| 0.0 a 180.0 (paso: 1.0)  
  
Cuando `crease_angle` es 180 o superior, la topología de la malla no cambia. Cuando se establece por debajo de 180, los vértices se dividen a lo largo de los bordes duros, lo que puede aumentar el recuento de vértices. Cuando se dividen los vértices, los datos por vértice (colores, UVs y tangentes) se duplican para coincidir con la nueva disposición de vértices, y la malla resultante se reconstruye como un lote de tamaño variable.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`mesh`| La malla de entrada con datos de normales suaves adjuntos, o con vértices divididos y normales cuando se establece un ángulo de pliegue.| MESH  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/es.md)

* * *

**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MeshSmoothNormals.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MeshSmoothNormals)

[Combinar mallas](https://docs.comfy.org/es/built-in-nodes/MergeMeshes)[Pintar malla](https://docs.comfy.org/es/built-in-nodes/PaintMesh)
