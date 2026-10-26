---
url: https://docs.comfy.org/es/built-in-nodes/ModelSamplingStableCascade/
title: Muestreo de modelo Stable Cascade - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:15.360255+00:00
---

# Muestreo de modelo Stable Cascade - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelSamplingStableCascade/

Stable Cascade

# Muestreo de modelo Stable Cascade - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ModelSamplingStableCascade aplica la configuración de muestreo de Stable Cascade a un modelo mediante la aplicación de un valor de desplazamiento a los

Copiar páginaCopiar página

El nodo ModelSamplingStableCascade aplica la configuración de muestreo de Stable Cascade a un modelo mediante la aplicación de un valor de desplazamiento a los parámetros de muestreo. Devuelve una copia parcheada del modelo de entrada con la configuración personalizada de muestreo de Stable Cascade, dejando el modelo original sin cambios.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de entrada al que se aplicará el muestreo de Stable Cascade| MODEL| Sí| -  
`desplazamiento`| El valor de desplazamiento aplicado a los parámetros de muestreo (predeterminado: 2.0)| FLOAT| Sí| 0.0 - 100.0 (paso 0.01)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo modificado con el muestreo de Stable Cascade aplicado| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/es.md)

* * *

**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelSamplingStableCascade.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelSamplingStableCascade)

[Opciones de muestreo de SenseNova](https://docs.comfy.org/es/built-in-nodes/SenseNovaSamplingOptions)[Muestreo de modelo SD3](https://docs.comfy.org/es/built-in-nodes/ModelSamplingSD3)
