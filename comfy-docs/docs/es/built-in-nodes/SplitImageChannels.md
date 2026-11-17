---
url: https://docs.comfy.org/es/built-in-nodes/SplitImageChannels/
title: Separar canales de imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-17T16:46:37.791050+00:00
---

# Separar canales de imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SplitImageChannels/

Compositing

# Separar canales de imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Divide una imagen en sus canales rojo, verde y azul, y devuelve el canal alfa como una máscara.

Copiar páginaCopiar página

Divide una imagen en sus canales rojo, verde y azul, y devuelve el canal alfa como una máscara. Cada salida de color es una imagen en escala de grises de tres canales, por lo que se previsualiza y se guarda como una imagen normal. Úselo para inspeccionar o editar un solo canal, o para extraer la transparencia de una imagen que tenga un canal alfa: las imágenes cargadas con Load Image no tienen canal alfa, ya que su alfa se expone como una salida `MASK` separada.

## Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`image`| La imagen que se va a dividir. Una entrada de un solo canal (escala de grises) se expande para que las tres salidas de color contengan los mismos datos.| IMAGE| Sí| -  
  
## Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`red`| El canal rojo, como una imagen en escala de grises de tres canales.| IMAGE  
`green`| El canal verde, como una imagen en escala de grises de tres canales.| IMAGE  
`blue`| El canal azul, como una imagen en escala de grises de tres canales.| IMAGE  
`alpha`| El alfa como una máscara, invertido de la misma manera que en Load Image, por lo que 1 marca los píxeles totalmente transparentes. Una imagen sin canal alfa devuelve una máscara con todos los valores en cero.| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageChannels/es.md)

* * *

**Source fingerprint (SHA-256):** `0f300d2e86c74e856001eb82da26c871c94c1dae5ec73a4504ca258420fbcf52`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SplitImageChannels.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SplitImageChannels)

[Captura de Webcam](https://docs.comfy.org/es/built-in-nodes/WebcamCapture)[Obtener tamaño del latent de imagen/vídeo](https://docs.comfy.org/es/built-in-nodes/GetLatentSize)
