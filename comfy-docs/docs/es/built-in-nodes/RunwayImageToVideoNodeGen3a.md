---
url: https://docs.comfy.org/es/built-in-nodes/RunwayImageToVideoNodeGen3a/
title: Runway imagen a video (Gen3a turbo) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:25.177663+00:00
---

# Runway imagen a video (Gen3a turbo) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RunwayImageToVideoNodeGen3a/

Runway

# Runway imagen a video (Gen3a turbo) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Runway Image to Video (Gen3a Turbo) genera un video a partir de un único fotograma inicial utilizando el modelo Gen3a Turbo de Runway.

Copiar páginaCopiar página

El nodo Runway Image to Video (Gen3a Turbo) genera un video a partir de un único fotograma inicial utilizando el modelo Gen3a Turbo de Runway. Toma un prompt de texto y un fotograma de imagen inicial, y luego crea una secuencia de video basada en la duración y la relación de aspecto especificadas. La generación se procesa de forma remota a través de la API de Runway. Este nodo está marcado como obsoleto.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Prompt de texto para la generación (predeterminado: "")| STRING| Sí| N/A  
`fotograma_inicial`| Fotograma inicial que se utilizará para el video| IMAGE| Sí| N/A  
`duración`| Duración del video generado, en segundos (predeterminado: “5”)| COMBO| Sí| `"5"`  
`"10"`  
`relación`| Relación de aspecto del video generado (predeterminado: “768:1280”)| COMBO| Sí| `"768:1280"`  
`"1280:768"`  
`semilla`| Semilla aleatoria para la generación (predeterminado: 0)| INT| Sí| 0 a 4294967295  
  
**Restricciones de los parámetros:**

  * El `prompt` debe contener al menos un carácter (no puede estar vacío).
  * El `start_frame` acepta una sola imagen (máximo de 1).
  * El `start_frame` no debe exceder las dimensiones de 7999 x 7999 píxeles.
  * El `start_frame` debe tener una relación de aspecto entre 1:2 y 2:1 (0.5 a 2.0).



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| La secuencia de video generada| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/es.md)

* * *

**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RunwayImageToVideoNodeGen3a.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RunwayImageToVideoNodeGen3a)

[Runway Primer-Fotograma-Último a video](https://docs.comfy.org/es/built-in-nodes/RunwayFirstLastFrameNode)[Runway imagen a video (Gen4 turbo)](https://docs.comfy.org/es/built-in-nodes/RunwayImageToVideoNodeGen4)
