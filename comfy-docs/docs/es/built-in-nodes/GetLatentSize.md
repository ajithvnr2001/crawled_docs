---
url: https://docs.comfy.org/es/built-in-nodes/GetLatentSize/
title: Obtener tama\u00f1o del latent de imagen/v\u00eddeo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:51.299525+00:00
---

# Obtener tamaño del latent de imagen/vídeo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/GetLatentSize/

Latente

# Obtener tamaño del latent de imagen/vídeo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Lee un latente de imagen o video y devuelve su ancho, alto, número de fotogramas y tamaño de lote

Copiar páginaCopiar página

Lee un latente de imagen o video y devuelve su ancho, alto, número de fotogramas y tamaño de lote, de modo que la geometría pueda reutilizarse sin decodificar el latente. Úsalo para dimensionar máscaras de ruido, alinear resoluciones o calcular solapamientos al dividir un sampler en mosaicos. Los valores medidos también se muestran en el propio nodo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`latent`| El latente de imagen o video que se va a inspeccionar. Cuando el latente contiene varios flujos, se mide el primero.| LATENT| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`width`| El ancho del latente, en celdas de latente en lugar de píxeles.| INT  
`height`| El alto del latente, en celdas de latente en lugar de píxeles.| INT  
`frames`| El número de fotogramas del latente. Los latentes de imagen tienen un solo fotograma.| INT  
`batch_size`| El número de latentes en el lote.| INT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetLatentSize/es.md)

* * *

**Source fingerprint (SHA-256):** `f75b3347cb1853b035b0bb283d5487ab1532d561d66d3cae3c67f54bf693d31a`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/GetLatentSize.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/GetLatentSize)

[Captura de Webcam](https://docs.comfy.org/es/built-in-nodes/WebcamCapture)[Cargar modelo ControlNet](https://docs.comfy.org/es/built-in-nodes/ControlNetLoader)
