---
url: https://docs.comfy.org/es/built-in-nodes/SetUnionControlNetType/
title: Establecer tipo Union ControlNet - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:31.091102+00:00
---

# Establecer tipo Union ControlNet - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SetUnionControlNetType/

Controlnet

# Establecer tipo Union ControlNet - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SetUnionControlNetType permite elegir qué tipo de control utiliza una red de control.

Copiar páginaCopiar página

El nodo SetUnionControlNetType permite elegir qué tipo de control utiliza una red de control. Toma una red de control existente y crea una copia modificada con el tipo de control seleccionado, sin modificar la red de control original. Cuando se selecciona `"auto"`, se borra el tipo de control almacenado para que el tipo pueda detectarse automáticamente.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`controlnet`| La red de control que se modificará con una nueva configuración de tipo| CONTROL_NET| Sí| -  
`tipo`| El tipo de red de control que se aplicará. Use `"auto"` para la detección automática de tipo o seleccione un tipo de red de control específico entre las opciones disponibles (predeterminado: `"auto"`)| COMBO| Sí| `"auto"`  
`"openpose"`  
`"depth"`  
`"hed/pidi/softedge"`  
`"canny"`  
`"scribble"`  
`"seg"`  
`"tile"`  
`"inpaint"`  
`"lineart"`  
`"blur"`  
`"mlsd"`  
`"normalbae"`  
`"mask"`  
  
Cuando `type` se establece en `"auto"`, el nodo borra el tipo de control almacenado para que el tipo pueda detectarse automáticamente. Cuando se selecciona un tipo específico, el nodo almacena el tipo de control correspondiente en la red de control copiada. La red de control de entrada nunca se modifica en el lugar; en su lugar, se devuelve una copia modificada.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`control_net`| La red de control modificada con la configuración de tipo especificada aplicada| CONTROL_NET  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/es.md)

* * *

**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SetUnionControlNetType.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SetUnionControlNetType)

[Aplicar ControlNet inpainting AliMama](https://docs.comfy.org/es/built-in-nodes/ControlNetInpaintingAliMamaApply)[Cosmos imagen a latente de video](https://docs.comfy.org/es/built-in-nodes/CosmosImageToVideoLatent)
