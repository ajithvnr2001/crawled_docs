---
url: https://docs.comfy.org/es/built-in-nodes/TorchCompileModel/
title: Compilar modelo con Torch - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:36.609884+00:00
---

# Compilar modelo con Torch - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TorchCompileModel/

Experimental

# Compilar modelo con Torch - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo TorchCompileModel aplica compilación de PyTorch a un modelo para optimizar su rendimiento.

Copiar páginaCopiar página

El nodo TorchCompileModel aplica compilación de PyTorch a un modelo para optimizar su rendimiento. Crea una copia del modelo de entrada y la envuelve con la funcionalidad de compilación de PyTorch utilizando el backend especificado. Esto puede mejorar la velocidad de ejecución del modelo durante la inferencia.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo que se va a compilar y optimizar| MODEL| Sí| -  
`backend`| El backend de compilación de PyTorch a utilizar para la optimización (predeterminado: “inductor”)| STRING| Sí| ”inductor"  
"cudagraphs”  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`modelo`| El modelo compilado con la compilación de PyTorch aplicada| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/es.md)

* * *

**Source fingerprint (SHA-256):** `923e71b528e6e53468916f74c2a02924bf51738f29e36638312c6da6357fcedb`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TorchCompileModel.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TorchCompileModel)

[Orientación de Auto-Atención](https://docs.comfy.org/es/built-in-nodes/SelfAttentionGuidance)[Ajustar brillo](https://docs.comfy.org/es/built-in-nodes/AdjustBrightness)
