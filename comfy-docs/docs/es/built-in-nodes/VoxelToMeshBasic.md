---
url: https://docs.comfy.org/es/built-in-nodes/VoxelToMeshBasic/
title: Voxel a malla (b\u00e1sico) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:44.390694+00:00
---

# Voxel a malla (básico) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VoxelToMeshBasic/

3D

# Voxel a malla (básico) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VoxelToMeshBasic convierte datos de vóxeles 3D en geometría de malla.

Copiar páginaCopiar página

El nodo VoxelToMeshBasic convierte datos de vóxeles 3D en geometría de malla. Procesa volúmenes de vóxeles aplicando un valor de umbral para determinar qué partes del volumen se convierten en superficies sólidas en la malla resultante. El nodo genera una estructura de malla completa con vértices y caras que puede utilizarse para renderizado y modelado 3D.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`voxel`| Los datos de vóxeles 3D que se convertirán en una malla| VOXEL| Sí| -  
`umbral`| El valor de umbral utilizado para determinar qué vóxeles forman parte de la superficie de la malla (predeterminado: 0.6)| FLOAT| Sí| -1.0 a 1.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`MESH`| La malla 3D generada que contiene vértices y caras| MESH  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/es.md)

* * *

**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VoxelToMeshBasic.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VoxelToMeshBasic)

[Voxel a malla](https://docs.comfy.org/es/built-in-nodes/VoxelToMesh)[EasyCache](https://docs.comfy.org/es/built-in-nodes/EasyCache)
