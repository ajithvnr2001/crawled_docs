---
url: https://docs.comfy.org/es/built-in-nodes/LoadMoGeModel/
title: Cargar modelo MoGe - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:06.036607+00:00
---

# Cargar modelo MoGe - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadMoGeModel/

Cargadores

# Cargar modelo MoGe - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Carga un modelo MoGe (Geometría Monocular) desde un archivo y lo prepara para su uso en tareas de estimación de geometría.

Copiar páginaCopiar página

Carga un modelo MoGe (Geometría Monocular) desde un archivo y lo prepara para su uso en tareas de estimación de geometría. El nodo lee el archivo de modelo seleccionado desde la carpeta `geometry_estimation` e inicializa el modelo MoGe con sus pesos almacenados.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model_name`| El nombre del archivo de modelo MoGe que se va a cargar. Seleccione entre los archivos de modelo disponibles en la carpeta `geometry_estimation` de su instalación de ComfyUI.| COMBO| Sí| Lista de archivos de modelo disponibles en la carpeta `geometry_estimation`  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`MOGE_MODEL`| La instancia del modelo MoGe cargada, lista para su uso en flujos de trabajo de estimación de geometría.| MOGE_MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/es.md)

* * *

**Source fingerprint (SHA-256):** `b5b55f94d3762852d5a1480c0b00d15da4e534adbeb544bf7c47da012e5a6353`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadMoGeModel.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadMoGeModel)

[Cargar MediaPipe Face Landmarker](https://docs.comfy.org/es/built-in-nodes/LoadMediaPipeFaceLandmarker)[Cargar LoRA (Bypass) (Para depuración)](https://docs.comfy.org/es/built-in-nodes/LoraLoaderBypass)
