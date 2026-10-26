---
url: https://docs.comfy.org/es/built-in-nodes/VideoTriangleCFGGuidance/
title: Gu\u00eda CFG triangular para video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:42.815283+00:00
---

# Guía CFG triangular para video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VideoTriangleCFGGuidance/

Guiadores

# Guía CFG triangular para video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VideoTriangleCFGGuidance aplica un patrón de escalado de guía libre de clasificador (CFG) triangular a un modelo de video.

Copiar páginaCopiar página

El nodo VideoTriangleCFGGuidance aplica un patrón de escalado de guía libre de clasificador (CFG) triangular a un modelo de video. Varía la escala de condicionamiento usando una onda triangular que oscila entre `min_cfg` y la escala de condicionamiento original del modelo. Esto crea un patrón de guía dinámico que puede ayudar a mejorar la consistencia y la calidad de la generación de video.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de video al que se aplicará la guía CFG triangular.| MODEL| Sí| -  
`min_cfg`| El valor mínimo de escala CFG para el patrón triangular. Este parámetro se muestra en la sección avanzada de la interfaz del nodo (predeterminado: 1.0).| FLOAT| Sí| 0.0 - 100.0 (paso: 0.5, redondeo: 0.01)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo modificado con la guía CFG triangular aplicada.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/es.md)

* * *

**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VideoTriangleCFGGuidance.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VideoTriangleCFGGuidance)

[Guía CFG lineal para video](https://docs.comfy.org/es/built-in-nodes/VideoLinearCFGGuidance)[Agregar ruido](https://docs.comfy.org/es/built-in-nodes/AddNoise)
