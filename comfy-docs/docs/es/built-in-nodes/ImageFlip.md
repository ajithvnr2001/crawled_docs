---
url: https://docs.comfy.org/es/built-in-nodes/ImageFlip/
title: Voltear imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.290823+00:00
---

# Voltear imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageFlip/

Transformación

# Voltear imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageFlip invierte imágenes a lo largo de diferentes ejes.

Copiar páginaCopiar página

El nodo ImageFlip invierte imágenes a lo largo de diferentes ejes. Puede invertir imágenes verticalmente a lo largo del eje x u horizontalmente a lo largo del eje y. El nodo utiliza operaciones torch.flip para realizar la inversión según el método seleccionado.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada que se va a invertir| IMAGE| Sí| -  
`método_volteo`| La dirección de inversión a aplicar (predeterminado: “x-axis: vertically”)| STRING| Sí| ”x-axis: vertically"  
"y-axis: horizontally”  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen de salida invertida| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/es.md)

* * *

**Source fingerprint (SHA-256):** `5cb9949c53653192b1a696179351976c3a87e2e7afc4634624b4d827ad75b527`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageFlip.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageFlip)

[Recorte de imagen](https://docs.comfy.org/es/built-in-nodes/ImageCropV2)[Rellenar imagen para pintar fuera](https://docs.comfy.org/es/built-in-nodes/ImagePadForOutpaint)
