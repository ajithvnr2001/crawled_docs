---
url: https://docs.comfy.org/es/built-in-nodes/RescaleCFG/
title: Reescalar CFG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:23.460170+00:00
---

# Reescalar CFG - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RescaleCFG/

Parches

# Reescalar CFG - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo RescaleCFG está diseñado para ajustar las escalas de condicionamiento y no condicionamiento de la salida de un modelo en función de un multiplicador

Copiar páginaCopiar página

El nodo RescaleCFG está diseñado para ajustar las escalas de condicionamiento y no condicionamiento de la salida de un modelo en función de un multiplicador especificado, con el objetivo de lograr un proceso de generación más equilibrado y controlado. Funciona reescalando la salida del modelo para modificar la influencia de los componentes condicionados y no condicionados, mejorando potencialmente el rendimiento o la calidad de la salida del modelo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`modelo`| El parámetro `modelo` representa el modelo generativo que se va a ajustar. Es crucial, ya que el nodo aplica una función de reescalado a la salida del modelo, influyendo directamente en el proceso de generación.| MODEL  
`multiplicador`| El parámetro `multiplicador` controla el grado de reescalado aplicado a la salida del modelo. Determina el equilibrio entre los componentes originales y reescalados, afectando las características finales de la salida.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`modelo`| El modelo modificado con escalas de condicionamiento y no condicionamiento ajustadas. Se espera que este modelo produzca salidas con características potencialmente mejoradas debido al reescalado aplicado.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RescaleCFG/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RescaleCFG.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RescaleCFG)

[Renormalizar CFG](https://docs.comfy.org/es/built-in-nodes/RenormCFG)[Escalar ROPE](https://docs.comfy.org/es/built-in-nodes/ScaleROPE)
