---
url: https://docs.comfy.org/es/built-in-nodes/LtxApiVideoAlphaGen/
title: LTX Video AlphaGen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:54.756471+00:00
---

# LTX Video AlphaGen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LtxApiVideoAlphaGen/

Video

# LTX Video AlphaGen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Extrae un mate alfa en escala de grises, blanco para el primer plano, que coincide con el video de entrada fotograma por fotograma.

Copiar páginaCopiar página

Extrae un mate alfa en escala de grises, blanco para el primer plano, que coincide con el video de entrada fotograma por fotograma. Pasa el mate a Get Video Components e Image To Mask para convertirlo en una máscara. El audio no se conserva.

## Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`video`| Video al que aplicar el mate, de hasta 10 segundos y 3840x2160 en cualquiera de las dos orientaciones.| VIDEO| Sí| -  
`seed`| Controla si el nodo se vuelve a ejecutar; los resultados no son deterministas independientemente de la semilla. Predeterminado: 42.| INT| No| 0 a 4294967295  
  
## Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`matte`| El mate alfa como video, un fotograma por cada fotograma de entrada y sin audio.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApiVideoAlphaGen/es.md)

* * *

**Source fingerprint (SHA-256):** `54a8304c2d092a736ad7fb86c8497aceda6340886beb81b6068a3de5a387a746`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LtxApiVideoAlphaGen.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LtxApiVideoAlphaGen)

[FLUX 3 Max de texto a vídeo](https://docs.comfy.org/es/built-in-nodes/Flux3MaxTextToVideoNode)[LTX Video Reframe](https://docs.comfy.org/es/built-in-nodes/LtxApiVideoReframe)
