---
url: https://docs.comfy.org/es/built-in-nodes/FluxVideoUpscaleNode/
title: Ampliaci\u00f3n de v\u00eddeo Flux - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:49.255772+00:00
---

# Ampliación de vídeo Flux - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/FluxVideoUpscaleNode/

BFL

# Ampliación de vídeo Flux - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Flux Video Upscale aumenta la escala de un clip de video entre 1.5 y 3 veces mediante superresolución de FLUX.

Copiar páginaCopiar página

Flux Video Upscale aumenta la escala de un clip de video entre 1.5 y 3 veces mediante superresolución de FLUX. En el modo creativo restaura e inventa detalles finos; en el modo preciso mejora la nitidez de la fuente sin modificarla.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`vídeo`| Clip de origen de 1 a 20 segundos con una relación de aspecto entre 1:4 y 4:1. La salida se renderiza a 24 fps y se limita a aproximadamente 14.4 megapíxeles por fotograma.| VIDEO| Sí| 1 a 20 segundos de duración; relación de aspecto entre 1:4 y 4:1; mínimo 64x64 píxeles  
`upscale_factor`| Tamaño de salida relativo a la fuente. Las fuentes muy grandes se amplían menos que el factor solicitado debido al límite por fotograma. (predeterminado: 2.0)| FLOAT| Sí| 1.5 a 3.0 (paso 0.1)  
`modo`| ’creative’ restaura e inventa detalles finos, ideal para metraje generado, texturas y paisajes. ‘precise’ mejora la nitidez de la fuente sin modificarla, para rostros, productos y metraje real. (predeterminado: “creative”)| COMBO| Sí| ”creative"  
"precise”  
`prompt`| Descripción opcional del clip que guía el detalle mejorado. Déjelo vacío para un aumento de escala neutro. (predeterminado: vacío)| STRING| Sí| Texto multilínea  
`auto_downscale`| Reduce automáticamente la escala de fuentes con un área mayor a 3840x2160 píxeles para ajustarse al límite de entrada. Se conserva la relación de aspecto; los videos más pequeños no se modifican. (predeterminado: true)| BOOLEAN| Sí| true  
false  
`safety_tolerance`| Tolerancia de moderación; 0 es la más estricta. (predeterminado: 2, parámetro avanzado)| INT| Sí| 0 a 4  
`seed`| Semilla para determinar si el nodo debe volver a ejecutarse; FLUX elige su propia semilla, por lo que los resultados reales son no deterministas independientemente de este valor. (predeterminado: 42)| INT| Sí| 0 a 4294967295  
  
Nota: El video de origen debe durar entre 1 y 20 segundos, tener al menos 64x64 píxeles de tamaño y una relación de aspecto entre 1:4 y 4:1. Si `auto_downscale` está deshabilitado y el área del video supera los 3840x2160 píxeles, el nodo genera un error. El video de salida se renderiza a 24 fps y se limita a aproximadamente 14.4 megapíxeles por fotograma, por lo que las fuentes muy grandes pueden ampliarse menos que el factor solicitado.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| El clip de video con escala aumentada.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/es.md)

* * *

**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/FluxVideoUpscaleNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/FluxVideoUpscaleNode)

[Edición de vídeo Flux](https://docs.comfy.org/es/built-in-nodes/FluxVideoEditNode)[Bria: Quitar fondo de video](https://docs.comfy.org/es/built-in-nodes/BriaRemoveVideoBackground)
