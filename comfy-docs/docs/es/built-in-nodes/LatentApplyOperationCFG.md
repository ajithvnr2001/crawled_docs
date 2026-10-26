---
url: https://docs.comfy.org/es/built-in-nodes/LatentApplyOperationCFG/
title: Aplicar operaci\u00f3n CFG a latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:02.577822+00:00
---

# Aplicar operación CFG a latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentApplyOperationCFG/

Operaciones

# Aplicar operación CFG a latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentApplyOperationCFG aplica una operación latente dentro del paso de guía libre de clasificador (CFG) del proceso de muestreo de un modelo.

Copiar páginaCopiar página

El nodo LatentApplyOperationCFG aplica una operación latente dentro del paso de guía libre de clasificador (CFG) del proceso de muestreo de un modelo. Intercepta las salidas de condicionamiento producidas antes de CFG, aplica la operación conectada a los valores latentes y devuelve el modelo con este comportamiento de muestreo modificado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo al que se aplicará la operación CFG| MODEL| Sí| -  
`operación`| La operación latente que se aplicará durante el proceso de muestreo CFG| LATENT_OPERATION| Sí| -  
`start_percent`| Fracción de la programación de eliminación de ruido en la que la operación empieza a aplicarse; 0 es el inicio de la programación (predeterminado: 0.0)| FLOAT| No| 0.0 a 1.0 (paso 0.001)  
`end_percent`| Fracción de la programación de eliminación de ruido en la que la operación deja de aplicarse; 1 es el final de la programación (predeterminado: 1.0)| FLOAT| No| 0.0 a 1.0 (paso 0.001)  
  
Nota: Este nodo está marcado como experimental. La operación se aplica a las salidas de condicionamiento del modelo durante el proceso de muestreo CFG. Cuando hay dos salidas de condicionamiento, la operación se aplica a la diferencia entre la primera y la segunda salida, y la segunda salida se vuelve a sumar al resultado. Cuando solo hay una salida de condicionamiento, la operación se aplica directamente a ella. La operación solo se ejecuta entre los puntos `start_percent` y `end_percent` de la programación de eliminación de ruido, por lo que puede limitarse a una parte de la programación; fuera de esa ventana, las salidas de condicionamiento se devuelven sin cambios.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo modificado con la operación CFG aplicada a su proceso de muestreo| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/es.md)

* * *

**Source fingerprint (SHA-256):** `6a5f59f02eaec38334c63d871e48e89aa983a5ac2ca10801161cdc9e13cacdf2`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentApplyOperationCFG.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentApplyOperationCFG)

[Aplicar operación a latente](https://docs.comfy.org/es/built-in-nodes/LatentApplyOperation)[Mezcla de operación latent](https://docs.comfy.org/es/built-in-nodes/LatentOperationBlend)
