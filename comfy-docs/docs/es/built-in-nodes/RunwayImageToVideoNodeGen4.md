---
url: https://docs.comfy.org/es/built-in-nodes/RunwayImageToVideoNodeGen4/
title: Runway imagen a video (Gen4 turbo) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:25.115690+00:00
---

# Runway imagen a video (Gen4 turbo) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/RunwayImageToVideoNodeGen4/

Runway

# Runway imagen a video (Gen4 turbo) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Runway Image to Video (Gen4 Turbo) genera un video a partir de un único fotograma inicial utilizando el modelo Gen4 Turbo de Runway.

Copiar páginaCopiar página

El nodo Runway Image to Video (Gen4 Turbo) genera un video a partir de un único fotograma inicial utilizando el modelo Gen4 Turbo de Runway. Toma un mensaje de texto y una imagen de fotograma inicial, luego crea una secuencia de video basada en la duración y la configuración de relación de aspecto proporcionadas. El nodo se encarga de cargar el fotograma inicial a la API de Runway y devuelve el video generado.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Mensaje de texto para la generación (predeterminado: cadena vacía)| STRING| Sí| -  
`frame_inicial`| Fotograma inicial que se utilizará para el video| IMAGE| Sí| -  
`duración`| Duración del video en segundos (predeterminado: “5”)| COMBO| Sí| `"5"`  
`"10"`  
`proporción`| Relación de aspecto para el video generado (predeterminado: “1024:1024”)| COMBO| Sí| `"1024:1024"`  
`"1280:720"`  
`"720:1280"`  
`"1920:1080"`  
`"1080:1920"`  
`"2048:1080"`  
`"1080:2048"`  
`semilla`| Semilla aleatoria para la generación (predeterminado: 0)| INT| No| 0 a 4294967295  
  
**Restricciones de parámetros:**

  * La imagen `start_frame` debe tener dimensiones que no superen los 7999x7999 píxeles
  * La imagen `start_frame` debe tener una relación de aspecto entre 0.5 y 2.0
  * El `prompt` debe contener al menos un carácter



## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`output`| El video generado basado en el fotograma de entrada y el mensaje| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/es.md)

* * *

**Source fingerprint (SHA-256):** `ebb5f1cd5e6bf6e0fcfb4910c774c087980daf9a1987900ad966120608b924e7`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/RunwayImageToVideoNodeGen4.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/RunwayImageToVideoNodeGen4)

[Runway imagen a video (Gen3a turbo)](https://docs.comfy.org/es/built-in-nodes/RunwayImageToVideoNodeGen3a)[sync.so Lip Sync](https://docs.comfy.org/es/built-in-nodes/SyncLipSyncNode)
