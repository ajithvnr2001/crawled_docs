---
url: https://docs.comfy.org/es/built-in-nodes/VideoTrim/
title: Recortar v\u00eddeo (avanzado) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:42.491085+00:00
---

# Recortar vídeo (avanzado) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VideoTrim/

Video

# Recortar vídeo (avanzado) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo recorta un video a una ventana de tiempo elegida estableciendo un tiempo de inicio y una duración.

Copiar páginaCopiar página

Este nodo recorta un video a una ventana de tiempo elegida estableciendo un tiempo de inicio y una duración. También ofrece un modo estricto que genera un error cuando no se puede alcanzar la duración solicitada.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Requerido| Rango  
---|---|---|---|---  
`video`| El video a recortar.| VIDEO| Sí| —  
`trim`| Ventana de recorte usando fotogramas de inicio/fin. La ventana se convierte en un tiempo de inicio (en segundos desde el comienzo del video) y una duración (en segundos). Cuando tanto el tiempo de inicio como la duración son 0, se devuelve el video sin ningún recorte.| VIDEO_EDIT| Sí| start_time: >= 0, predeterminado 0  
duration: >= 0, predeterminado 0  
`strict_duration`| Si es True, cuando la duración especificada no sea posible, se generará un error. (predeterminado: False)| BOOLEAN| No| true  
false  
  
Nota: La duración del recorte debe ser >= 0; los valores negativos generan un error. La ventana de recorte solicitada debe caber dentro del video de origen. Si el recorte no se puede aplicar, se genera un error que informa la duración de origen, el tiempo de inicio y la duración objetivo.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`video`| El video recortado. Cuando la ventana de recorte está vacía (tiempo de inicio y duración ambos 0), se devuelve el video original sin cambios.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTrim/es.md)

* * *

**Source fingerprint (SHA-256):** `ba8f8ccbae7e8aebda553810b81ccaa427d45523142bd00746c4e2f4e5b41a1b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VideoTrim.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VideoTrim)

[Muestrear fotograma de video](https://docs.comfy.org/es/built-in-nodes/VideoFrameSample)
