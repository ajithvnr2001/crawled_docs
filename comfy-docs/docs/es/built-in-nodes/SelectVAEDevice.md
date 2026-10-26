---
url: https://docs.comfy.org/es/built-in-nodes/SelectVAEDevice/
title: Seleccionar dispositivo VAE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:30.597471+00:00
---

# Seleccionar dispositivo VAE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SelectVAEDevice/

Multi-GPU

# Seleccionar dispositivo VAE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora

Copiar páginaCopiar página

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectVAEDevice/en.md)

## 

​

Resumen

Este nodo permite seleccionar manualmente en qué dispositivo GPU debe colocarse el modelo VAE. De forma predeterminada, el VAE se coloca en el dispositivo asignado por el cargador de modelos, pero puedes fijarlo a una GPU específica (por ejemplo, `gpu:0`, `gpu:1`). Si el dispositivo seleccionado no está disponible en tu máquina, el nodo pasará el VAE sin cambios y registrará un mensaje en lugar de fallar.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`vae`| El modelo VAE que se asignará a un dispositivo específico.| VAE| Sí|   
`dispositivo`| El dispositivo de destino para el VAE. `"default"` restaura el dispositivo asignado por el cargador. `"gpu:N"` fija el VAE a la N-ésima GPU disponible. La CPU no es una opción compatible y será ignorada si se proporciona. (predeterminado: `"default"`)| COMBO| Sí| `"default"`  
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
`vae`| El modelo VAE, ahora asignado al dispositivo seleccionado. Si el dispositivo solicitado no está disponible o no es válido, el VAE se pasa sin cambios.| VAE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectVAEDevice/es.md)

* * *

**Source fingerprint (SHA-256):** `011154043fc02f930b0074de656bb24baf4dfe74bcfd2e89ea76284f0a5b7d8e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SelectVAEDevice.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SelectVAEDevice)

[Seleccionar Dispositivo del Modelo](https://docs.comfy.org/es/built-in-nodes/SelectModelDevice)[Comfy Cloud Flux 2 Texto a imagen [BETA]](https://docs.comfy.org/es/built-in-nodes/ComfyCloudFlux2TextToImageNode)
