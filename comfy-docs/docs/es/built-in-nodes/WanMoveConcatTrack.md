---
url: https://docs.comfy.org/es/built-in-nodes/WanMoveConcatTrack/
title: Wan concatenar pista de movimiento - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:46.053208+00:00
---

# Wan concatenar pista de movimiento - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WanMoveConcatTrack/

Mover

# Wan concatenar pista de movimiento - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo WanMoveConcatTrack combina dos conjuntos de datos de seguimiento de movimiento en una única secuencia más larga.

Copiar páginaCopiar página

El nodo WanMoveConcatTrack combina dos conjuntos de datos de seguimiento de movimiento en una única secuencia más larga. Funciona uniendo las rutas de seguimiento y las máscaras de visibilidad de las pistas de entrada a lo largo de sus dimensiones respectivas. Si solo se proporciona una entrada de pista, simplemente pasa esos datos sin cambios.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`pistas_1`| El primer conjunto de datos de seguimiento de movimiento que se va a concatenar.| TRACKS| Sí|   
`pistas_2`| Un segundo conjunto opcional de datos de seguimiento de movimiento. Si no se proporciona, `tracks_1` se pasa directamente a la salida.| TRACKS| No|   
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`tracks`| Los datos de seguimiento de movimiento concatenados, que contienen los `track_path` y `track_visibility` combinados de las entradas. Devuelve `tracks_1` sin cambios cuando `tracks_2` no está conectado.| TRACKS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/es.md)

* * *

**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WanMoveConcatTrack.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WanMoveConcatTrack)

[Generar pistas de video](https://docs.comfy.org/es/built-in-nodes/GenerateTracks)[Wan pistas de movimiento desde coordenadas](https://docs.comfy.org/es/built-in-nodes/WanMoveTracksFromCoords)
