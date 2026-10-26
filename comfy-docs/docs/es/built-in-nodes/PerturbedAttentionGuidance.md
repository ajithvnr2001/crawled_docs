---
url: https://docs.comfy.org/es/built-in-nodes/PerturbedAttentionGuidance/
title: Gu\u00eda de atenci\u00f3n perturbada - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:17.352954+00:00
---

# Guía de atención perturbada - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PerturbedAttentionGuidance/

Unet

# Guía de atención perturbada - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo PerturbedAttentionGuidance aplica guía de atención perturbada a un modelo de difusión para mejorar la calidad de generación.

Copiar páginaCopiar página

El nodo PerturbedAttentionGuidance aplica guía de atención perturbada a un modelo de difusión para mejorar la calidad de generación. Durante el muestreo, realiza una predicción adicional en la que la autoatención del bloque intermedio se reemplaza por una versión simplificada que deja pasar directamente las proyecciones de valor; luego, añade al resultado desruidificado la diferencia escalada entre la predicción condicional normal y esta predicción perturbada. Establecer `scale` en 0 desactiva por completo el efecto.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de difusión al que se aplica la guía de atención perturbada| MODEL| Sí| -  
`escala`| La intensidad del efecto de guía de atención perturbada (predeterminado: 3.0). Cuando se establece en 0, el nodo no tiene efecto y devuelve el resultado desruidificado original sin cambios.| FLOAT| Sí| 0.0 - 100.0 (paso: 0.01)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| El modelo modificado con el parche de guía de atención perturbada adjunto a su proceso de muestreo| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/es.md)

* * *

**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PerturbedAttentionGuidance.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PerturbedAttentionGuidance)

[Reducir modelo (Kohya Deep Shrink)](https://docs.comfy.org/es/built-in-nodes/PatchModelAddDownscale)[TSR - reajuste de puntuación temporal](https://docs.comfy.org/es/built-in-nodes/TemporalScoreRescaling)
