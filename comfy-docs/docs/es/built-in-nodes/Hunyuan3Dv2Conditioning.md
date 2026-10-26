---
url: https://docs.comfy.org/es/built-in-nodes/Hunyuan3Dv2Conditioning/
title: Acondicionamiento Hunyuan 3D v2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:53.882725+00:00
---

# Acondicionamiento Hunyuan 3D v2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Hunyuan3Dv2Conditioning/

Hunyuan 3d

# Acondicionamiento Hunyuan 3D v2 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Hunyuan3Dv2Conditioning procesa la salida de visión CLIP para generar datos de acondicionamiento para modelos 3D.

Copiar páginaCopiar página

El nodo Hunyuan3Dv2Conditioning procesa la salida de visión CLIP para generar datos de acondicionamiento para modelos 3D. Extrae las incrustaciones del último estado oculto de la salida de visión y crea pares de acondicionamiento tanto positivos como negativos. El acondicionamiento positivo utiliza las incrustaciones reales, mientras que el acondicionamiento negativo utiliza incrustaciones con valor cero de la misma forma.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`salida_vision_clip`| La salida de un modelo de visión CLIP que contiene incrustaciones visuales| CLIP_VISION_OUTPUT| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positive`| Datos de acondicionamiento positivos que contienen las incrustaciones de visión CLIP| CONDITIONING  
`negative`| Datos de acondicionamiento negativos que contienen incrustaciones con valor cero que coinciden con la forma de las incrustaciones positivas| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/es.md)

* * *

**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Hunyuan3Dv2Conditioning.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Hunyuan3Dv2Conditioning)

[Imágenes de Referencia HiDream-O1](https://docs.comfy.org/es/built-in-nodes/HiDreamO1ReferenceImages)[Acondicionamiento Hunyuan 3D v2 (multi-vista)](https://docs.comfy.org/es/built-in-nodes/Hunyuan3Dv2ConditioningMultiView)
