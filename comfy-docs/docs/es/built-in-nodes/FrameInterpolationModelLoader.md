---
url: https://docs.comfy.org/es/built-in-nodes/FrameInterpolationModelLoader/
title: Cargar modelo de interpolaci\u00f3n de fotogramas - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:49.498800+00:00
---

# Cargar modelo de interpolación de fotogramas - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/FrameInterpolationModelLoader/

Cargadores

# Cargar modelo de interpolación de fotogramas - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo carga un archivo de modelo de interpolación de fotogramas y lo prepara para su uso en el flujo de trabajo.

Copiar páginaCopiar página

Este nodo carga un archivo de modelo de interpolación de fotogramas y lo prepara para su uso en el flujo de trabajo. Detecta automáticamente si el archivo es un modelo FILM o RIFE y configura el modelo para el hardware disponible.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`nombre del modelo`| Selecciona un modelo de interpolación de fotogramas para cargar. Los modelos deben colocarse en la carpeta `frame_interpolation`.| COMBO| Sí| Lista de archivos de modelo en la carpeta `frame_interpolation`  
  
Nota: El nodo admite formatos de modelo FILM y RIFE. Si el archivo seleccionado no es un formato reconocido, se genera un error.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`FRAME_INTERPOLATION_MODEL`| El modelo de interpolación de fotogramas cargado y configurado, listo para usarse en otros nodos.| INTERP_MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolationModelLoader/es.md)

* * *

**Source fingerprint (SHA-256):** `21f470ee2852dbd1b332ac4a506eaa20dc8578c04b63c4fe1a072878b57beaba`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/FrameInterpolationModelLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/FrameInterpolationModelLoader)

[Cargar CLIP dual](https://docs.comfy.org/es/built-in-nodes/DualCLIPLoader)[Cargar GLIGEN](https://docs.comfy.org/es/built-in-nodes/GLIGENLoader)
