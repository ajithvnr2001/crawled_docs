---
url: https://docs.comfy.org/es/built-in-nodes/RunwayAleph2KeyframeNode/
title: Runway Aleph2 Fotograma Clave - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:24.983995+00:00
---

# Runway Aleph2 Fotograma Clave - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RunwayAleph2KeyframeNode/

Runway

# Runway Aleph2 Fotograma Clave - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Runway Aleph2 Keyframe ancla una imagen de guía a un momento específico

Copiar páginaCopiar página

El nodo Runway Aleph2 Keyframe ancla una imagen de guía a un momento específico

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen de guía para aplicar en el momento elegido del video de entrada.| IMAGE| Sí| -  
`sincronización`| Cómo ubicar esta imagen en la línea de tiempo del video de entrada.| COMBO| Sí| Ver abajo  
`fotogramas_clave`| Fotogramas clave anteriores opcionales para encadenar con este.| KEYFRAME| No| -  
  
### 

​

Opciones del Parámetro Timing

El parámetro `timing` tiene dos modos:

Modo| Subparámetro| Descripción| Rango  
---|---|---|---  
”Segundos absolutos”| `seconds`| Tiempo en segundos desde el inicio del video de entrada donde se aplica esta imagen (predeterminado: 0.0)| 0.0 a 30.0, paso 0.1  
”Fracción de duración”| `fraction`| Dónde en el video de entrada se aplica esta imagen, como fracción de su duración (0.0 = inicio, 1.0 = final) (predeterminado: 0.0)| 0.0 a 1.0, paso 0.01  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`fotogramas_clave`| Una cadena de fotogramas clave que incluye este y cualquier fotograma clave previamente conectado.| KEYFRAME  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2KeyframeNode/es.md)

* * *

**Source fingerprint (SHA-256):** `b5ac6553166b7366fd35f97740861be163f91bc2353f5f83bdc2f04bf40f8478`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RunwayAleph2KeyframeNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RunwayAleph2KeyframeNode)

[Pruna P-Video-2 de texto a vídeo](https://docs.comfy.org/es/built-in-nodes/PrunaTextToVideoNode)[Runway Aleph2 Imagen de Guía](https://docs.comfy.org/es/built-in-nodes/RunwayAleph2PromptImageNode)
