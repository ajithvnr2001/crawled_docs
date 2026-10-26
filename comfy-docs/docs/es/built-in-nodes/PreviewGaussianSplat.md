---
url: https://docs.comfy.org/es/built-in-nodes/PreviewGaussianSplat/
title: Vista previa de Splat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:18.796601+00:00
---

# Vista previa de Splat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PreviewGaussianSplat/

3D

# Vista previa de Splat - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo PreviewGaussianSplat muestra un archivo de gaussian splat 3D en una ventana de vista previa sin guardarlo en el directorio de salida de ComfyUI.

Copiar páginaCopiar página

El nodo PreviewGaussianSplat muestra un archivo de gaussian splat 3D en una ventana de vista previa sin guardarlo en el directorio de salida de ComfyUI. Acepta un archivo de modelo 3D en varios formatos de gaussian splat, guarda una copia temporal para la vista previa y pasa los datos del modelo para su procesamiento posterior en el flujo de trabajo. Este nodo está marcado como experimental y actúa como un nodo de salida.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo_3d`| Un archivo de gaussian splat 3D.| FILE3D| Sí| splat  
ply  
spz  
ksplat  
`info_modelo_3d`| Información de metadatos opcional sobre el modelo 3D. Cuando no está conectado, el nodo usa la información del modelo de `viewport_state`.| LOAD3DMODELINFO| No| -  
`estado_de_vista`| El estado actual del viewport 3D, incluida la información de la cámara y del modelo.| LOAD3D| Sí| -  
`info_cámara`| Información de cámara opcional para la vista previa. Cuando no está conectado, el nodo usa la información de cámara de `viewport_state`.| LOAD3DCAMERA| No| -  
`ancho`| El ancho del renderizado de la vista previa en píxeles (predeterminado: 1024).| INT| Sí| 1 a 4096  
`alto`| La altura del renderizado de la vista previa en píxeles (predeterminado: 1024).| INT| Sí| 1 a 4096  
  
Nota: Cuando no se proporcionan `camera_info` o `model_3d_info`, el nodo recurre a la información de cámara y modelo almacenada en `viewport_state`. Si `viewport_state` no es un objeto de estado de viewport válido, se trata como vacío.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model_3d`| El archivo de gaussian splat 3D de entrada, pasado sin cambios.| FILE3D  
`model_3d_info`| Información de metadatos sobre el modelo 3D, ya sea desde la entrada o derivada del estado del viewport.| LOAD3DMODELINFO  
`camera_info`| Información de cámara para la vista previa, ya sea desde la entrada o derivada del estado del viewport.| LOAD3DCAMERA  
`width`| El ancho del renderizado de la vista previa.| INT  
`height`| La altura del renderizado de la vista previa.| INT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/es.md)

* * *

**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PreviewGaussianSplat.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PreviewGaussianSplat)

[Vista previa 3D (Avanzado)](https://docs.comfy.org/es/built-in-nodes/Preview3DAdvanced)[Vista previa de nube de puntos](https://docs.comfy.org/es/built-in-nodes/PreviewPointCloud)
