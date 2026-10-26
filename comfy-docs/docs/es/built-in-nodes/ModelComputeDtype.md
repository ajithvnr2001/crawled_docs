---
url: https://docs.comfy.org/es/built-in-nodes/ModelComputeDtype/
title: Tipo de dato de c\u00f3mputo del modelo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:12.847603+00:00
---

# Tipo de dato de cómputo del modelo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelComputeDtype/

Depuración

# Tipo de dato de cómputo del modelo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ModelComputeDtype cambia el tipo de datos computacional (precisión) utilizado por un modelo durante el procesamiento.

Copiar páginaCopiar página

El nodo ModelComputeDtype cambia el tipo de datos computacional (precisión) utilizado por un modelo durante el procesamiento. Crea una copia del modelo de entrada y aplica la configuración de precisión seleccionada, lo que puede ayudar a optimizar el uso de memoria y el rendimiento según su hardware. Esto es útil para depurar y probar diferentes configuraciones de precisión.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo de entrada para modificar con un nuevo tipo de datos computacional| MODEL| Sí| -  
`dtype`| El tipo de datos computacional que se aplicará al modelo (predeterminado: “default”). Este parámetro está marcado como una opción avanzada.| COMBO| Sí| ”default"  
"fp32"  
"fp16"  
"bf16”  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo modificado con el nuevo tipo de datos computacional aplicado| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/es.md)

* * *

**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelComputeDtype.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelComputeDtype)

[LazyCache](https://docs.comfy.org/es/built-in-nodes/LazyCache)[Normalización CFG](https://docs.comfy.org/es/built-in-nodes/CFGNorm)
