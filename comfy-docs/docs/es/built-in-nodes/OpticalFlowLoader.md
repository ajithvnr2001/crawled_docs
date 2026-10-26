---
url: https://docs.comfy.org/es/built-in-nodes/OpticalFlowLoader/
title: Cargar modelo de flujo \u00f3ptico - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:16.282929+00:00
---

# Cargar modelo de flujo óptico - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/OpticalFlowLoader/

Cargadores

# Cargar modelo de flujo óptico - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Carga un modelo de flujo óptico desde la carpeta models/opticalflow/.

Copiar páginaCopiar página

Carga un modelo de flujo óptico desde la carpeta `models/optical_flow/`. Actualmente, solo se admite el formato RAFT-large de torchvision, que es el modelo utilizado por el nodo VOIDWarpedNoise. ComfyUI no descarga los pesos del flujo óptico automáticamente; debe colocar el archivo de checkpoint manualmente en el directorio `models/optical_flow/`.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`model_name`| Modelo de flujo óptico a cargar. Los archivos deben colocarse en la carpeta `optical_flow`. Actualmente solo se admite `raft_large.pth` de torchvision.| COMBO| Sí| Lista de archivos en la carpeta `models/optical_flow/`  
  
Nota: El checkpoint seleccionado debe ser un state dict de torchvision RAFT-large que contenga claves con los prefijos `feature_encoder.`, `context_encoder.` y `update_block.`. Si el archivo no coincide con este formato, el nodo lanza un ValueError.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`OPTICAL_FLOW`| El modelo de flujo óptico cargado, configurado en modo de evaluación y precisión float32, envuelto en un ModelPatcher para usarlo con otros nodos.| OPTICAL_FLOW  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/es.md)

* * *

**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/OpticalFlowLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/OpticalFlowLoader)

[Cargar parche de modelo](https://docs.comfy.org/es/built-in-nodes/ModelPatchLoader)[Cargar PhotoMaker](https://docs.comfy.org/es/built-in-nodes/PhotoMakerLoader)
