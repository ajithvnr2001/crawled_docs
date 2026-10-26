---
url: https://docs.comfy.org/es/built-in-nodes/EmptyHiDreamO1LatentImage/
title: Imagen Latente Vac\u00eda HiDream-O1 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:45.511202+00:00
---

# Imagen Latente Vacía HiDream-O1 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/EmptyHiDreamO1LatentImage/

Hidream

# Imagen Latente Vacía HiDream-O1 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo crea una imagen latente vacía en el espacio de píxeles para el modelo HiDream-O1-Image.

Copiar páginaCopiar página

Este nodo crea una imagen latente vacía en el espacio de píxeles para el modelo HiDream-O1-Image. Genera un tensor en blanco de ceros que actúa como punto de partida para la generación de imágenes, con dimensiones definidas por las entradas `width`, `height` y `batch_size`.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`ancho`| El ancho de la imagen latente en píxeles. Valor predeterminado: 2048. El valor debe ser un múltiplo de 32. El modelo fue entrenado a aproximadamente 4 megapíxeles; las resoluciones más bajas pueden reducir la calidad de forma notable.| INT| Sí| 64 a 4096 (paso: 32)  
`alto`| La altura de la imagen latente en píxeles. Valor predeterminado: 2048. El valor debe ser un múltiplo de 32. El modelo fue entrenado a aproximadamente 4 megapíxeles; las resoluciones más bajas pueden reducir la calidad de forma notable.| INT| Sí| 64 a 4096 (paso: 32)  
`tamaño_lote`| El número de imágenes latentes que se generarán en un solo lote. Valor predeterminado: 1.| INT| Sí| 1 a 64  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`samples`| Un tensor lleno de ceros que representa la imagen latente vacía, con forma (batch_size, 3, height, width).| LATENT  
  
## 

​

Notas

  * El modelo HiDream-O1-Image fue entrenado a aproximadamente 4 megapíxeles. Usar resoluciones significativamente más bajas puede provocar una reducción notable en la calidad de la imagen.
  * Las resoluciones de entrenamiento incluyen: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.



> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/es.md)

* * *

**Source fingerprint (SHA-256):** `7412639e261512d9174e60009143c8c06c354e2a20ada7271837d72053426be5`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/EmptyHiDreamO1LatentImage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/EmptyHiDreamO1LatentImage)

[Latente Flux 2 vacío](https://docs.comfy.org/es/built-in-nodes/EmptyFlux2LatentImage)[Latente Hunyuan 3D v2 vacío](https://docs.comfy.org/es/built-in-nodes/EmptyLatentHunyuan3Dv2)
