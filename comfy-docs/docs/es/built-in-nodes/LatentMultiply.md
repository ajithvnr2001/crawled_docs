---
url: https://docs.comfy.org/es/built-in-nodes/LatentMultiply/
title: Multiplicar latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:03.611027+00:00
---

# Multiplicar latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentMultiply/

Avanzado

# Multiplicar latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentMultiply está diseñado para escalar la representación latente de muestras mediante un multiplicador específico.

Copiar páginaCopiar página

El nodo LatentMultiply está diseñado para escalar la representación latente de muestras mediante un multiplicador específico. Esta operación permite ajustar la intensidad o magnitud de las características dentro del espacio latente, posibilitando el refinamiento del contenido generado o la exploración de variaciones en una dirección latente determinada.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`muestras`| El parámetro ‘samples’ representa las representaciones latentes que se escalarán. Es fundamental para definir los datos de entrada sobre los cuales se realizará la operación de multiplicación.| `LATENT`  
`multiplicador`| El parámetro ‘multiplier’ especifica el factor de escala que se aplicará a las muestras latentes. Desempeña un papel clave en el ajuste de la magnitud de las características latentes, permitiendo un control preciso sobre la salida generada.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La salida es una versión modificada de las muestras latentes de entrada, escaladas por el multiplicador especificado. Esto permite explorar variaciones dentro del espacio latente ajustando la intensidad de sus características.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentMultiply/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentMultiply.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentMultiply)

[Interpolar latentes](https://docs.comfy.org/es/built-in-nodes/LatentInterpolate)[Restar latentes](https://docs.comfy.org/es/built-in-nodes/LatentSubtract)
