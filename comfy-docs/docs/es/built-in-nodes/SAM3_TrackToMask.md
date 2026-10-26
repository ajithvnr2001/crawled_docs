---
url: https://docs.comfy.org/es/built-in-nodes/SAM3_TrackToMask/
title: Seguimiento a m\u00e1scara SAM3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:26.065981+00:00
---

# Seguimiento a máscara SAM3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SAM3_TrackToMask/

Detección

# Seguimiento a máscara SAM3 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Selecciona objetos rastreados concretos de una sesión de seguimiento de SAM3 por su número de índice y los combina en una sola máscara de salida.

Copiar páginaCopiar página

## 

​

Descripción general

Selecciona objetos rastreados específicos de una sesión de seguimiento SAM3 mediante sus números de índice y los combina en una única máscara de salida. Esto permite elegir qué objetos conservar y cuáles ignorar de los resultados del seguimiento.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`datos_de_rastreo`| Datos de seguimiento provenientes de un nodo rastreador SAM3, que contienen las máscaras empaquetadas y el tamaño original de la imagen.| SAM3TRACKDATA| Sí| N/A  
`índices_de_objeto`| Índices de objetos separados por comas para incluir en la máscara de salida (ej. ‘0,2,3’). Si se deja vacío, se incluyen todos los objetos rastreados.| STRING| No| Cualquier lista de enteros separados por comas  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`máscaras`| Una única máscara binaria por cada fotograma, donde los objetos seleccionados se combinan en una sola máscara. Si no se selecciona ningún objeto o no existen datos de seguimiento, devuelve una máscara de ceros.| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackToMask/es.md)

* * *

**Source fingerprint (SHA-256):** `2da82effc4cdc6655d0d37e281858bf33f7b62d9056629ec810e3ff9b2e7b5a6`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SAM3_TrackToMask.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SAM3_TrackToMask)

[Previsualizar seguimiento SAM3](https://docs.comfy.org/es/built-in-nodes/SAM3_TrackPreview)[Seguimiento de vídeo SAM3](https://docs.comfy.org/es/built-in-nodes/SAM3_VideoTrack)
