---
url: https://docs.comfy.org/es/built-in-nodes/GetVideoComponents/
title: Obtener componentes de video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:51.241120+00:00
---

# Obtener componentes de video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/GetVideoComponents/

Video

# Obtener componentes de video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Get Video Components extrae todos los elementos principales de un archivo de video.

Copiar páginaCopiar página

El nodo Get Video Components extrae todos los elementos principales de un archivo de video. Separa el video en fotogramas individuales, extrae la pista de audio y proporciona la velocidad de fotogramas, la profundidad de bits y el espacio de color del video. Esto te permite trabajar con cada componente de forma independiente para su posterior procesamiento o análisis.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`video`| El video del que se extraerán los componentes.| VIDEO| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`images`| Los fotogramas individuales extraídos del video como imágenes separadas.| IMAGE  
`audio`| La pista de audio extraída del video.| AUDIO  
`fps`| La velocidad de fotogramas del video en fotogramas por segundo.| FLOAT  
`bit_depth`| La profundidad de bits del video.| COMBO  
`color_space`| El espacio de color del video.| COMBO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/es.md)

* * *

**Source fingerprint (SHA-256):** `b57dbf1120105885d17361f07ec96c078aac9ae9a84beb63319885df679e4f81`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/GetVideoComponents.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/GetVideoComponents)

[Interpolar fotogramas](https://docs.comfy.org/es/built-in-nodes/FrameInterpolate)[Cargar video](https://docs.comfy.org/es/built-in-nodes/LoadVideo)
