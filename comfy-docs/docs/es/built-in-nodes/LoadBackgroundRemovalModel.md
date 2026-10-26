---
url: https://docs.comfy.org/es/built-in-nodes/LoadBackgroundRemovalModel/
title: Cargar modelo de eliminaci\u00f3n de fondo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:04.612871+00:00
---

# Cargar modelo de eliminación de fondo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadBackgroundRemovalModel/

Cargadores

# Cargar modelo de eliminación de fondo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Carga un modelo de eliminación de fondos desde un archivo.

Copiar páginaCopiar página

Carga un modelo de eliminación de fondos desde un archivo. Este nodo prepara el modelo para que pueda ser usado por otros nodos y así eliminar fondos de las imágenes.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`nombre_del_modelo_de_eliminación_de_fondo`| El modelo utilizado para eliminar fondos de las imágenes. Seleccione de la lista de archivos de modelos de eliminación de fondos disponibles.| COMBO| Sí| Lista de archivos de modelos disponibles (ordenados alfabéticamente)  
  
Nota: Si el archivo seleccionado no contiene un modelo de eliminación de fondos válido, el nodo genera un RuntimeError.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`bg_model`| El modelo de eliminación de fondos cargado, listo para ser usado por otros nodos para procesar imágenes.| BACKGROUND_REMOVAL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/es.md)

* * *

**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadBackgroundRemovalModel.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadBackgroundRemovalModel)

[Cargar modelo de escalado latent](https://docs.comfy.org/es/built-in-nodes/LatentUpscaleModelLoader)[Cargar Depth Anything 3](https://docs.comfy.org/es/built-in-nodes/LoadDA3Model)
