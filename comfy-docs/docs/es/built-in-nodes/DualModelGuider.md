---
url: https://docs.comfy.org/es/built-in-nodes/DualModelGuider/
title: Gu\u00eda CFG de Doble Modelo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:43.826280+00:00
---

# Guía CFG de Doble Modelo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/DualModelGuider/

Guiadores

# Guía CFG de Doble Modelo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo permite utilizar dos modelos diferentes durante el proceso de muestreo CFG guiado: un modelo para el paso positivo (condicional) y un modelo separado

Copiar páginaCopiar página

Este nodo permite utilizar dos modelos diferentes durante el proceso de muestreo CFG guiado: un modelo para el paso positivo (condicional) y un modelo separado para el paso negativo (incondicional). Cuando no se proporciona un modelo negativo, funciona como una guía CFG estándar que utiliza un solo modelo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`modelo`| Modelo utilizado para el paso positivo (condicional).| MODEL| Sí|   
`modelo_negativo`| Modelo utilizado para el paso negativo (incondicional). Use el mismo modelo para CFG ordinario.| MODEL| No|   
`positivo`| La entrada de condicionamiento positivo.| CONDITIONING| Sí|   
`cfg`| El valor de escala CFG (predeterminado: 4.0).| FLOAT| Sí| 0.0 a 100.0 (paso: 0.1)  
`negativo`| Condicionamiento negativo ejecutado en el modelo negativo. Déjelo desconectado para un paso incondicional sin texto (solo imagen).| CONDITIONING| No|   
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`GUIDER`| Un objeto guía configurado con los modelos y condicionamientos especificados para usar en el muestreo.| GUIDER  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualModelGuider/es.md)

* * *

**Source fingerprint (SHA-256):** `a60803156e98d2ffe975d39922dfbeacafd1a2155d88dd2e285ac1426a1e7a33`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/DualModelGuider.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/DualModelGuider)

[Guía CFG dual](https://docs.comfy.org/es/built-in-nodes/DualCFGGuider)[LTXV Dual CFG Guider](https://docs.comfy.org/es/built-in-nodes/LTXVDualCFGGuider)
