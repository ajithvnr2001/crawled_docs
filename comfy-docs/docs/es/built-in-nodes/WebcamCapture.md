---
url: https://docs.comfy.org/es/built-in-nodes/WebcamCapture/
title: Captura de Webcam - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:47.595036+00:00
---

# Captura de Webcam - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WebcamCapture/

Imagen

# Captura de Webcam - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo WebcamCapture captura imágenes desde un dispositivo de cámara web y las convierte a un formato que puede utilizarse dentro de los flujos de trabajo de

Copiar páginaCopiar página

El nodo WebcamCapture captura imágenes desde un dispositivo de cámara web y las convierte a un formato que puede utilizarse dentro de los flujos de trabajo de ComfyUI. Hereda del nodo LoadImage y proporciona opciones para controlar las dimensiones y el momento de la captura. Cuando está habilitado, el nodo puede capturar nuevas imágenes cada vez que se procesa la cola del flujo de trabajo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`imagen`| La fuente de entrada de la cámara web desde la cual capturar imágenes| WEBCAM| Sí| -  
`ancho`| El ancho deseado para la imagen capturada (predeterminado: 0, usa la resolución nativa de la cámara web)| INT| Sí| 0 a MAX_RESOLUTION  
`altura`| La altura deseada para la imagen capturada (predeterminado: 0, usa la resolución nativa de la cámara web)| INT| Sí| 0 a MAX_RESOLUTION  
`captura_en_cola`| Cuando está habilitado, captura una nueva imagen cada vez que se procesa la cola del flujo de trabajo (predeterminado: True)| BOOLEAN| Sí| -  
  
**Nota:** Cuando tanto `width` como `height` se establecen en 0, el nodo utiliza la resolución nativa de la cámara web. Establecer cualquiera de las dimensiones a un valor distinto de cero redimensionará la imagen capturada en consecuencia.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`IMAGE`| La imagen capturada de la cámara web convertida al formato de imagen de ComfyUI| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/es.md)

* * *

**Source fingerprint (SHA-256):** `551368150fc293309f917eabaa066f223b1fa1a016ffd3643b57b80c83f812cc`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WebcamCapture.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WebcamCapture)

[Guardar SVG](https://docs.comfy.org/es/built-in-nodes/SaveSVGNode)[Obtener tamaño del latent de imagen/vídeo](https://docs.comfy.org/es/built-in-nodes/GetLatentSize)
