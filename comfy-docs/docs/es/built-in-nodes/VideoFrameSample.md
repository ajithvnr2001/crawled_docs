---
url: https://docs.comfy.org/es/built-in-nodes/VideoFrameSample/
title: Muestrear fotograma de video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:42.356929+00:00
---

# Muestrear fotograma de video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VideoFrameSample/

Video

# Muestrear fotograma de video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VideoFrameSample extrae un número fijo de fotogramas de un video utilizando una de cuatro estrategias.

Copiar páginaCopiar página

El nodo `VideoFrameSample` extrae un número fijo de fotogramas de un video utilizando una de cuatro estrategias. Para las estrategias contiguas “head” y “tail”, la salida es una referencia de video diferida (los fotogramas no se decodifican); para las estrategias no contiguas “uniform” y “random”, solo se decodifican los fotogramas seleccionados.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`video`| Video de entrada.| VIDEO| Sí| –  
`num_frames`| Número de fotogramas a muestrear (por defecto: 16).| INT| Sí| 1 – 9999  
`estrategia`| uniform: espaciados uniformemente, head: primeros N, tail: últimos N, random: orden aleatorio (predeterminado: “uniform”).| COMBO| Sí| ”uniform"  
"head"  
"tail"  
"random”  
`semilla`| Semilla aleatoria, solo se usa con la estrategia “random” (por defecto: 0).| INT| Sí| 0 – 18446744073709551615  
  
  * `num_frames` se ajusta automáticamente al número total de fotogramas del video de entrada.
  * El parámetro `seed` no tiene efecto a menos que `strategy` esté configurado como `"random"`.
  * Cuando `strategy` es `"uniform"` y `num_frames` es 1, se selecciona el fotograma central del video.
  * Un valor de `strategy` no reconocido genera un error.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`video`| Video muestreado.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoFrameSample/es.md)

* * *

**Source fingerprint (SHA-256):** `727504a9cf7fe5505c33da071cb8f21a38e1b7c0f964c5da172d9cedfc2f2300`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VideoFrameSample.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VideoFrameSample)

[Recortar vídeo](https://docs.comfy.org/es/built-in-nodes/VideoCrop)[Recortar vídeo (avanzado)](https://docs.comfy.org/es/built-in-nodes/VideoTrim)
