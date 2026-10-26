---
url: https://docs.comfy.org/es/built-in-nodes/SavePointCloud/
title: Guardar Nube de Puntos - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:29.235131+00:00
---

# Guardar Nube de Puntos - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SavePointCloud/

3D

# Guardar Nube de Puntos - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Guardar Nube de Puntos guarda un archivo de nube de puntos 3D en el directorio de salida y, opcionalmente

Copiar páginaCopiar página

El nodo Guardar Nube de Puntos guarda un archivo de nube de puntos 3D en el directorio de salida y, opcionalmente, proporciona datos de vista previa para el visor 3D. Gestiona la asignación de nombres y el guardado de archivos, al mismo tiempo que transfiere información de cámara y modelo para fines de visualización.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`model_3d`| Archivo de nube de puntos (.ply)| FILE3D_POINT_CLOUD_ANY o FILE3D_PLY| Sí| -  
`filename_prefix`| Prefijo para el nombre del archivo guardado (predeterminado: “3d/ComfyUI”)| STRING| Sí| -  
`viewport_state`| Estado actual del viewport que contiene información de cámara y modelo| LOAD3D| Sí| -  
`model_3d_info`| Información adicional del modelo para el visor 3D| LOAD3D_MODEL_INFO| No| -  
`camera_info`| Información de la cámara para el visor 3D| LOAD3D_CAMERA| No| -  
`width`| Ancho de la visualización de vista previa en píxeles (predeterminado: 1024)| INT| Sí| 1 a 4096  
`height`| Alto de la visualización de vista previa en píxeles (predeterminado: 1024)| INT| Sí| 1 a 4096  
El archivo guardado se escribe en el directorio de salida usando `filename_prefix` con un contador de 5 dígitos añadido (por ejemplo, `3d/ComfyUI_00001.ply`). Cuando la entrada opcional `camera_info` no está conectada, la información de cámara se toma de `viewport_state`; de manera similar, cuando `model_3d_info` no está conectada, la información del modelo se toma de `viewport_state` (o una lista vacía si no hay ninguna disponible).| | | |   
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`model_3d`| El archivo de nube de puntos guardado| FILE3D_POINT_CLOUD_ANY  
`model_3d_info`| Información del modelo para el visor 3D| LOAD3D_MODEL_INFO  
`camera_info`| Información de la cámara para el visor 3D| LOAD3D_CAMERA  
`width`| Ancho de la visualización de vista previa| INT  
`height`| Alto de la visualización de vista previa| INT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/es.md)

* * *

**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SavePointCloud.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SavePointCloud)

[Guardar GLB](https://docs.comfy.org/es/built-in-nodes/SaveGLB)[Voxel a malla](https://docs.comfy.org/es/built-in-nodes/VoxelToMesh)
