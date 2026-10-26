---
url: https://docs.comfy.org/es/built-in-nodes/SelectCLIPDevice/
title: Seleccionar Dispositivo CLIP - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:30.281445+00:00
---

# Seleccionar Dispositivo CLIP - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SelectCLIPDevice/

Multi-GPU

# Seleccionar Dispositivo CLIP - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Select CLIP Device te permite elegir en qué dispositivo (CPU o una GPU concreta) se ejecuta el codificador de texto CLIP.

Copiar páginaCopiar página

## 

​

Descripción general

El nodo Seleccionar Dispositivo CLIP permite elegir en qué dispositivo (CPU o una GPU específica) se ejecuta el codificador de texto CLIP. Por defecto, el dispositivo es asignado por el cargador del modelo, pero puedes sobrescribirlo para usar la CPU o una GPU en particular. Si el dispositivo solicitado no existe en tu máquina, el nodo simplemente pasa el CLIP sin cambios y registra un mensaje en lugar de generar un error.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`clip`| El codificador de texto CLIP a asignar a un dispositivo específico.| CLIP| Sí|   
`device`| El dispositivo donde colocar el codificador de texto CLIP. `"default"` restaura el dispositivo asignado por el cargador. `"cpu"` fija tanto el dispositivo de carga como el de descarga a la CPU. `"gpu:N"` fija el dispositivo de carga a la N-ésima GPU disponible (predeterminado: `"default"`).| COMBO| Sí| `"default"`  
`"cpu"`  
`"gpu:0"`  
`"gpu:1"`  
`"gpu:2"`  
`"gpu:3"`  
`"gpu:4"`  
`"gpu:5"`  
`"gpu:6"`  
`"gpu:7"`  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`clip`| El codificador de texto CLIP asignado al dispositivo seleccionado, o el CLIP original pasado sin cambios si el dispositivo solicitado no está disponible.| CLIP  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectCLIPDevice/es.md)

* * *

**Source fingerprint (SHA-256):** `92af94d9f5eea27095cc008debdf7339d26888a0e2cc8bd71ae9c9ba8718eb01`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SelectCLIPDevice.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SelectCLIPDevice)

[División CFG MultiGPU](https://docs.comfy.org/es/built-in-nodes/MultiGPU_WorkUnits)[Seleccionar Dispositivo del Modelo](https://docs.comfy.org/es/built-in-nodes/SelectModelDevice)
