---
url: https://docs.comfy.org/es/built-in-nodes/VAEComputeDtype/
title: VAEComputeDtype - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:33.990291+00:00
---

# VAEComputeDtype - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VAEComputeDtype/

Depuración

# VAEComputeDtype - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo establece el dtype de cómputo utilizado cuando un VAE codifica o decodifica, sin cambiar el resto del grafo del modelo.

Copiar páginaCopiar página

Este nodo establece el dtype de cómputo utilizado cuando un VAE codifica o decodifica, sin cambiar el resto del grafo del modelo. Devuelve una copia del VAE de entrada con la precisión solicitada, de modo que un flujo de trabajo puede ejecutar una rama con mayor precisión mientras las demás permanecen sin cambios. “default” conserva el dtype de cómputo que ya utiliza el VAE de entrada.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`vae`| VAE que se va a ajustar. El nodo trabaja sobre una copia, por lo que el VAE conectado no se modifica.| VAE| Sí| -  
`dtype`| Dtype de cómputo para la codificación y decodificación del VAE. “default” conserva el dtype de cómputo del VAE de entrada (predeterminado: “default”).| COMBO| Sí| ”default"  
"fp32"  
"fp16"  
"bf16”  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`vae`| La copia del VAE con el dtype de cómputo seleccionado aplicado.| VAE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEComputeDtype/es.md)

* * *

**Source fingerprint (SHA-256):** `239e5829d76b4bd43ec300fc2b7c8c408b5bd4a93918da417ecf43817aee3e12`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VAEComputeDtype.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VAEComputeDtype)

[Tipo de dato de cómputo del modelo](https://docs.comfy.org/es/built-in-nodes/ModelComputeDtype)[Normalización CFG](https://docs.comfy.org/es/built-in-nodes/CFGNorm)
