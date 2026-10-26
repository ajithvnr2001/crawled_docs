---
url: https://docs.comfy.org/es/built-in-nodes/SaveGaussianSplat/
title: Guardar Splat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:29.040169+00:00
---

# Guardar Splat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveGaussianSplat/

3D

# Guardar Splat - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo guarda un archivo 3D de salpicadura gaussiana en el directorio de salida.

Copiar páginaCopiar página

Este nodo guarda un archivo 3D de salpicadura gaussiana en el directorio de salida. Maneja el proceso de guardado del archivo y proporciona datos de vista previa para el visor 3D.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`model_3d`| Un archivo 3D de salpicadura gaussiana.| FILE3D| Sí| SplatAny  
PLY  
SPLAT  
SPZ  
KSPLAT  
`filename_prefix`| El prefijo para el nombre del archivo guardado (predeterminado: “3d/ComfyUI”).| STRING| Sí| Cualquier prefijo de nombre de archivo válido  
`viewport_state`| El estado actual del visor que contiene información de la cámara y del modelo.| LOAD3D| Sí| -  
`model_3d_info`| Información adicional del modelo 3D para el visor.| LOAD3DMODELINFO| No| -  
`camera_info`| Información de la cámara para la vista previa del visor.| LOAD3DCAMERA| No| -  
`width`| El ancho de la vista previa (predeterminado: 1024).| INT| Sí| 1 a 4096  
`height`| La altura de la vista previa (predeterminado: 1024).| INT| Sí| 1 a 4096  
  
Nota: Si no se proporcionan `camera_info` o `model_3d_info`, el nodo usa los valores correspondientes de `viewport_state` cuando están disponibles.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`model_3d`| El archivo 3D de salpicadura gaussiana guardado.| FILE3D  
`model_3d_info`| Información del modelo 3D para el visor.| LOAD3DMODELINFO  
`camera_info`| Información de la cámara para la vista previa del visor.| LOAD3DCAMERA  
`width`| El ancho de la vista previa.| INT  
`height`| La altura de la vista previa.| INT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/es.md)

* * *

**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveGaussianSplat.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveGaussianSplat)

[Guardar 3D (Avanzado)](https://docs.comfy.org/es/built-in-nodes/Save3DAdvanced)[Guardar GLB](https://docs.comfy.org/es/built-in-nodes/SaveGLB)
