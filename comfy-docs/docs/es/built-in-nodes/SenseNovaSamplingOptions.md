---
url: https://docs.comfy.org/es/built-in-nodes/SenseNovaSamplingOptions/
title: Opciones de muestreo de SenseNova - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:30.656191+00:00
---

# Opciones de muestreo de SenseNova - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SenseNovaSamplingOptions/

Sensenova

# Opciones de muestreo de SenseNova - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

SenseNova Sampling Options establece el desplazamiento de flujo (flow shift) de SenseNova en un modelo.

Copiar páginaCopiar página

SenseNova Sampling Options establece el desplazamiento de flujo (flow shift) de SenseNova en un modelo. Clona el modelo de entrada, adjunta una configuración de muestreo del modelo SenseNova usando el valor de desplazamiento de flujo elegido y devuelve el modelo parcheado para usarlo durante el muestreo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`model`| El modelo al que se aplica la configuración de muestreo con desplazamiento de flujo de SenseNova.| MODEL| Sí| -  
`shift`| El valor de desplazamiento de flujo que se establecerá en el muestreo del modelo SenseNova (predeterminado: 3.0; paso de la UI: 0.01).| FLOAT| Sí| Sin mínimo ni máximo definidos  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`MODEL`| Una copia del modelo de entrada con el desplazamiento de flujo de SenseNova aplicado a su configuración de muestreo.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/es.md)

* * *

**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SenseNovaSamplingOptions.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SenseNovaSamplingOptions)

[Aplicar ControlNet DiffSynth para Qwen Image](https://docs.comfy.org/es/built-in-nodes/QwenImageDiffsynthControlnet)[Muestreo de modelo Stable Cascade](https://docs.comfy.org/es/built-in-nodes/ModelSamplingStableCascade)
