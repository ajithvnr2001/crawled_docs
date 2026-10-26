---
url: https://docs.comfy.org/es/built-in-nodes/SelfAttentionGuidance/
title: Orientaci\u00f3n de Auto-Atenci\u00f3n - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:30.943989+00:00
---

# Orientación de Auto-Atención - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SelfAttentionGuidance/

Experimental

# Orientación de Auto-Atención - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

Copiar páginaCopiar página

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento: El nodo de Guía de Autoatención aplica guía a modelos de difusión modificando el mecanismo de atención durante el proceso de muestreo. Captura las puntuaciones de atención de los pasos de eliminación de ruido incondicionales y las utiliza para crear mapas de guía borrosos que influyen en la salida final. Esta técnica ayuda a guiar el proceso de generación aprovechando los propios patrones de atención del modelo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo de difusión al que se aplicará la guía de autoatención| MODEL| Sí| -  
`escala`| La intensidad del efecto de guía de autoatención (predeterminado: 0.5)| FLOAT| No| -2.0 a 5.0  
`blur_sigma`| La cantidad de desenfoque aplicada para crear el mapa de guía (predeterminado: 2.0)| FLOAT| No| 0.0 a 10.0  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`modelo`| El modelo modificado con la guía de autoatención aplicada| MODEL  
  
**Nota:** Este nodo es actualmente experimental y tiene limitaciones con lotes fragmentados. Solo puede guardar puntuaciones de atención de una llamada UNet y puede no funcionar correctamente con tamaños de lote más grandes.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/es.md)

* * *

**Source fingerprint (SHA-256):** `5f16ecd8f74bfd71073c6e3a65be08e54e4f5b9c56fe08deb48f35df381e82fa`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SelfAttentionGuidance.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SelfAttentionGuidance)

[SamplerEulerCFG++](https://docs.comfy.org/es/built-in-nodes/SamplerEulerCFGpp)[Compilar modelo con Torch](https://docs.comfy.org/es/built-in-nodes/TorchCompileModel)
