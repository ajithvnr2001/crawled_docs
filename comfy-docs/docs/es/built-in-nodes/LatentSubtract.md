---
url: https://docs.comfy.org/es/built-in-nodes/LatentSubtract/
title: Restar latentes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:04.228613+00:00
---

# Restar latentes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentSubtract/

Avanzado

# Restar latentes - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentSubtract está diseñado para restar una representación latente de otra.

Copiar páginaCopiar página

El nodo LatentSubtract está diseñado para restar una representación latente de otra. Esta operación puede utilizarse para manipular o modificar las características de las salidas de modelos generativos, eliminando eficazmente rasgos o atributos representados en un espacio latente de otro.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras1`| El primer conjunto de muestras latentes del cual se restará. Sirve como base para la operación de resta.| `LATENT`  
`muestras2`| El segundo conjunto de muestras latentes que se restará del primer conjunto. Esta operación puede alterar la salida del modelo generativo resultante al eliminar atributos o rasgos.| `LATENT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| El resultado de restar el segundo conjunto de muestras latentes del primero. Esta representación latente modificada puede utilizarse para tareas generativas posteriores.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentSubtract/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentSubtract.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentSubtract)

[Multiplicar latente](https://docs.comfy.org/es/built-in-nodes/LatentMultiply)[EmptyARVideoLatent](https://docs.comfy.org/es/built-in-nodes/EmptyARVideoLatent)
