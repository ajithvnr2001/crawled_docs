---
url: https://docs.comfy.org/es/built-in-nodes/VoxelToMesh/
title: Voxel a malla - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:43.972779+00:00
---

# Voxel a malla - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VoxelToMesh/

3D

# Voxel a malla - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VoxelToMesh convierte datos de vóxeles 3D en una geometría de malla mediante la extracción de una superficie en un valor de umbral especificado.

Copiar páginaCopiar página

El nodo VoxelToMesh convierte datos de vóxeles 3D en una geometría de malla mediante la extracción de una superficie en un valor de umbral especificado. Ofrece dos algoritmos para la extracción de superficie: un método básico que crea caras simples similares a cajas, y un método de red de superficie que produce mallas más suaves y detalladas. El nodo procesa cada cuadrícula de vóxeles en la entrada y genera vértices y caras que forman una representación de malla 3D.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`voxel`| Los datos de vóxeles de entrada que se convertirán en geometría de malla| VOXEL| Sí| -  
`algoritmo`| El algoritmo utilizado para la extracción de superficie. “surface net” produce mallas más suaves, mientras que “basic” crea caras simples similares a cajas (predeterminado: “surface net”)| COMBO| Sí| `"surface net"`  
`"basic"`  
`umbral`| El valor de umbral para la extracción de superficie. Los vóxeles con valores por encima de este umbral se consideran sólidos (predeterminado: 0.6)| FLOAT| Sí| -1.0 a 1.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`MESH`| La malla 3D generada que contiene vértices y caras de todas las cuadrículas de vóxeles de entrada. Si todas las cuadrículas de vóxeles producen mallas con formas idénticas, la salida es un tensor apilado; de lo contrario, se devuelve un lote de longitud variable| MESH  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/es.md)

* * *

**Source fingerprint (SHA-256):** `b600be13f1a484d8c0cc1f9c3918630d00c15d35008bcac0f677b21ef64b5d98`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VoxelToMesh.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VoxelToMesh)

[Guardar Nube de Puntos](https://docs.comfy.org/es/built-in-nodes/SavePointCloud)[Voxel a malla (básico)](https://docs.comfy.org/es/built-in-nodes/VoxelToMeshBasic)
