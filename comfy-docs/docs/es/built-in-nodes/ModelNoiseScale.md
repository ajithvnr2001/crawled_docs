---
url: https://docs.comfy.org/es/built-in-nodes/ModelNoiseScale/
title: Escala de Ruido del Modelo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:14.605130+00:00
---

# Escala de Ruido del Modelo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ModelNoiseScale/

Parches

# Escala de Ruido del Modelo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo ajusta la escala de ruido utilizada durante el muestreo del modelo.

Copiar páginaCopiar página

Este nodo ajusta la escala de ruido utilizada durante el muestreo del modelo. Crea una copia del modelo de entrada, aplica la escala de ruido especificada a su configuración de muestreo y devuelve el modelo modificado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo al que se aplicará el ajuste de escala de ruido.| MODEL| Sí| -  
`escala_ruido`| Escala de ruido absoluta de entrenamiento. Por ejemplo, HiDream-O1 base: 8.0, dev: 7.5. (predeterminado: 1.0)| FLOAT| Sí| 0.0 a 64.0 (paso: 0.01)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`MODEL`| El modelo modificado con la nueva escala de ruido aplicada.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/es.md)

* * *

**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ModelNoiseScale.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ModelNoiseScale)

[Backend de atención del modelo](https://docs.comfy.org/es/built-in-nodes/ModelAttentionBackend)[Muestreo de modelo AuraFlow](https://docs.comfy.org/es/built-in-nodes/ModelSamplingAuraFlow)
