---
url: https://docs.comfy.org/es/custom-nodes/backend/images_and_masks/
title: Im\u00e1genes, latentes y m\u00e1scaras - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:49.644024+00:00
---

# Imágenes, latentes y máscaras - ComfyUI

> Source: https://docs.comfy.org/es/custom-nodes/backend/images_and_masks/

## En esta página

Volver arriba

  * Imágenes
    * Trabajar con PIL.Image
  * Máscaras
    * Máscaras desde el nodo Load Image
    * Entender las formas de las máscaras
  * Latents



Python (backend)

# Imágenes, latentes y máscaras

Copiar páginaCopiar página

Domina datos backend para imágenes, máscaras y latentes en nodos personalizados de Comfy. Aprende formas de tensores y conversiones PIL en la documentación.

Copiar páginaCopiar página

Cuando trabajes con estos tipos de datos, necesitarás conocer la clase `torch.Tensor`. La documentación completa está [aquí](https://pytorch.org/docs/stable/tensors.html), o una introducción a los conceptos clave requeridos para Comfy [aquí](https://docs.comfy.org/es/custom-nodes/backend/tensors).

Si tu nodo tiene una sola salida que es un tensor, recuerda devolver `(image,)` no `(image)`

La mayoría de los conceptos a continuación se ilustran en los [fragmentos de código de ejemplo](https://docs.comfy.org/es/custom-nodes/backend/snippets).

## 

​

Imágenes

Un IMAGE es un `torch.Tensor` con forma `[B,H,W,C]`, `C=3`. Si vas a guardar o cargar imágenes, necesitarás convertir desde y hacia el formato `PIL.Image`; ¡consulta los fragmentos de código a continuación! Ten en cuenta que algunas operaciones de `pytorch` ofrecen (o esperan) `[B,C,H,W]`, conocido como ‘channel first’, por razones de eficiencia computacional. Solo ten cuidado.

### 

​

Trabajar con PIL.Image

Si quieres cargar y guardar imágenes, querrás usar PIL:
    
    
    from PIL import Image, ImageOps
    

## 

​

Máscaras

Una MASK es un `torch.Tensor` con forma `[B,H,W]`. En muchos contextos, las máscaras tienen valores binarios (0 o 1), que se usan para indicar qué píxeles deben someterse a operaciones específicas. En algunos casos, se usan valores entre 0 y 1 para indicar un grado de enmascaramiento (por ejemplo, para alterar la transparencia, ajustar filtros o componer capas).

### 

​

Máscaras desde el nodo Load Image

El nodo `LoadImage` usa el canal alfa de una imagen (la “A” de “RGBA”) para crear MASKs. Los valores del canal alfa se normalizan al rango [0,1] (torch.float32) y luego se invierten. El nodo `LoadImage` siempre produce una salida MASK al cargar una imagen. Muchas imágenes (como las JPEG) no tienen canal alfa. En estos casos, `LoadImage` crea una máscara predeterminada con la forma `[1, 64, 64]`.

### 

​

Entender las formas de las máscaras

En bibliotecas como `numpy`, `PIL` y muchas otras, las imágenes de un solo canal (como las máscaras) suelen representarse como arreglos 2D, con forma `[H,W]`. Esto significa que la dimensión `C` (canal) es implícita y, por lo tanto, a diferencia de los tipos IMAGE, los lotes de MASK tienen solo tres dimensiones: `[B, H, W]`. No es raro encontrar una máscara a la que se le ha quitado implícitamente la dimensión `B`, dando como resultado un tensor `[H,W]`. Para usar una MASK, a menudo tendrás que igualar las formas añadiendo dimensiones para producir una forma `[B,H,W,C]` con `C=1`. Para añadir la dimensión `C`, debes usar `unsqueeze(-1)`; para añadir `B`, usas `unsqueeze(0)`. Si tu nodo recibe una MASK como entrada, sería prudente que siempre revises `len(mask.shape)`.

## 

​

Latents

Un LATENT es un `dict`; la muestra de latent se referencia con la clave `samples` y tiene forma `[B,C,H,W]`, con `C=4`.

LATENT tiene el canal primero, IMAGE tiene el canal al final

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/custom-nodes/backend/images_and_masks.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/custom-nodes/backend/images_and_masks)

[Tipos de datos](https://docs.comfy.org/es/custom-nodes/backend/datatypes)[Entradas ocultas y flexibles](https://docs.comfy.org/es/custom-nodes/backend/more_on_inputs)
