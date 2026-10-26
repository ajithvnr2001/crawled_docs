---
url: https://docs.comfy.org/es/built-in-nodes/PixverseTextToVideoNode/
title: PixVerse texto a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:17.793641+00:00
---

# PixVerse texto a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PixverseTextToVideoNode/

Pixverse

# PixVerse texto a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Genera videos a partir de un prompt de texto usando la API de PixVerse.

Copiar páginaCopiar página

Genera videos a partir de un prompt de texto usando la API de PixVerse. El nodo permite controlar la forma, la calidad, la duración y el estilo de movimiento del video, y opcionalmente puede aplicar una plantilla de estilo guardada. Envía la solicitud, espera a que finalice la generación y devuelve el video terminado.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Prompt para la generación del video (predeterminado: "")| STRING| Sí| Debe contener al menos 1 carácter  
`relación_de_aspecto`| Relación de aspecto para el video generado| COMBO| Sí| `"16:9"`  
`"9:16"`  
`"1:1"`  
`calidad`| Configuración de calidad del video (predeterminado: “540p”)| COMBO| Sí| `"540p"`  
`"1080p"`  
`duración_segundos`| Duración del video generado en segundos| COMBO| Sí| `"5"`  
`"10"`  
`modo_de_movimiento`| Estilo de movimiento para la generación del video| COMBO| Sí| `"normal"`  
`"fast"`  
`semilla`| Semilla para la generación del video (predeterminado: 0)| INT| Sí| 0 a 2147483647  
`prompt_negativo`| Descripción de texto opcional de elementos no deseados en una imagen (predeterminado: "")| STRING| No| -  
`plantilla_pixverse`| Plantilla opcional para influir en el estilo de la generación, creada por el nodo PixVerse Template| CUSTOM| No| -  
  
**Nota:** El `prompt` debe contener al menos 1 carácter. Cuando se selecciona la calidad 1080p, el modo de movimiento se establece automáticamente en `normal` y la duración se limita a 5 segundos. Para cualquier duración distinta de 5 segundos, el modo de movimiento también se establece automáticamente en `normal`.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| El archivo de video generado| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/es.md)

* * *

**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PixverseTextToVideoNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PixverseTextToVideoNode)

[Plantilla de PixVerse](https://docs.comfy.org/es/built-in-nodes/PixverseTemplateNode)[Video de transición PixVerse](https://docs.comfy.org/es/built-in-nodes/PixverseTransitionVideoNode)
