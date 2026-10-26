---
url: https://docs.comfy.org/es/built-in-nodes/SaveLoRANode/
title: SaveLoRANode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:29.325579+00:00
---

# SaveLoRANode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveLoRANode/

Fusión de modelos

# SaveLoRANode - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SaveLoRA guarda modelos LoRA (Adaptación de Bajo Rango) en tu directorio de salida.

Copiar páginaCopiar página

El nodo SaveLoRA guarda modelos LoRA (Adaptación de Bajo Rango) en tu directorio de salida. Toma un modelo LoRA como entrada y crea un archivo safetensors con un nombre de archivo generado automáticamente. Puedes personalizar el prefijo del nombre de archivo y, opcionalmente, incluir el número de pasos de entrenamiento en el nombre para una mejor organización.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`lora`| El modelo LoRA a guardar. No uses el modelo con capas LoRA.| LORA_MODEL| Sí| -  
`prefix`| El prefijo a utilizar para el archivo LoRA guardado (predeterminado: “loras/ComfyUI_trained_lora”).| STRING| Sí| -  
`steps`| Opcional: El número de pasos con los que se ha entrenado el LoRA, utilizado para nombrar el archivo guardado.| INT| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
 _Ninguno_|  Este nodo no devuelve ninguna salida, pero guarda el modelo LoRA en el directorio de salida.| -  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/es.md)

* * *

**Source fingerprint (SHA-256):** `06a1067433aa4b720b51050b09fbad4870caf12c5e92f788d44ea022a39efef4`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveLoRANode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveLoRANode)

[DeprecatedDiffusersLoader](https://docs.comfy.org/es/built-in-nodes/DeprecatedDiffusersLoader)[División CFG MultiGPU](https://docs.comfy.org/es/built-in-nodes/MultiGPU_WorkUnits)
