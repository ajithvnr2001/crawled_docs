---
url: https://docs.comfy.org/es/built-in-nodes/ModelSamplingDiscrete/
title: Muestreo de modelo discreto - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:14.964869+00:00
---

# Muestreo de modelo discreto - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelSamplingDiscrete/

Parches

# Muestreo de modelo discreto - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para modificar el comportamiento de muestreo de un modelo aplicando una estrategia de muestreo discreto.

Copiar páginaCopiar página

Este nodo está diseñado para modificar el comportamiento de muestreo de un modelo aplicando una estrategia de muestreo discreto. Permite seleccionar diferentes métodos de muestreo, como epsilon, v_prediction, lcm o x0, y opcionalmente ajusta la estrategia de reducción de ruido del modelo según la configuración de la relación de ruido cero-shot (zsnr).

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Python dtype  
---|---|---|---  
`modelo`| El modelo al que se aplicará la estrategia de muestreo discreto. Este parámetro es crucial ya que define el modelo base que será modificado.| MODEL| `torch.nn.Module`  
`muestreo`| Especifica el método de muestreo discreto que se aplicará al modelo. La elección del método afecta la forma en que el modelo genera muestras, ofreciendo diferentes estrategias de muestreo.| COMBO[STRING]| `str`  
`zsnr`| Una bandera booleana que, cuando está habilitada, ajusta la estrategia de reducción de ruido del modelo según la relación de ruido cero-shot. Esto puede influir en la calidad y las características de las muestras generadas.| `BOOLEAN`| `bool`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato| Python dtype  
---|---|---|---  
`modelo`| El modelo modificado con la estrategia de muestreo discreto aplicada. Este modelo ahora está preparado para generar muestras utilizando el método y los ajustes especificados.| MODEL| `torch.nn.Module`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingDiscrete/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelSamplingDiscrete.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelSamplingDiscrete)

[Muestreo de modelo V continuo](https://docs.comfy.org/es/built-in-nodes/ModelSamplingContinuousV)[Renormalizar CFG](https://docs.comfy.org/es/built-in-nodes/RenormCFG)
