---
url: https://docs.comfy.org/es/built-in-nodes/LatentUpscale/
title: Escalar latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:03.952796+00:00
---

# Escalar latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentUpscale/

Latente

# Escalar latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentUpscale está diseñado para escalar representaciones latentes de imágenes.

Copiar páginaCopiar página

El nodo LatentUpscale está diseñado para escalar representaciones latentes de imágenes. Permite ajustar las dimensiones de la imagen de salida y el método de escalado, ofreciendo flexibilidad para mejorar la resolución de imágenes latentes.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`muestras`| La representación latente de una imagen que se va a escalar. Este parámetro es crucial para determinar el punto de partida del proceso de escalado.| `LATENT`  
`método_escala`| Especifica el método utilizado para escalar la imagen latente. Diferentes métodos pueden afectar la calidad y las características de la imagen escalada.| COMBO[STRING]  
`ancho`| El ancho deseado de la imagen escalada. Si se establece en 0, se calculará en función de la altura para mantener la relación de aspecto.| `INT`  
`altura`| La altura deseada de la imagen escalada. Si se establece en 0, se calculará en función del ancho para mantener la relación de aspecto.| `INT`  
`recorte`| Determina cómo se debe recortar la imagen escalada, afectando la apariencia final y las dimensiones de la salida.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`latent`| La representación latente escalada de la imagen, lista para su posterior procesamiento o generación.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscale/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentUpscale.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentUpscale)

[Componer latente con máscara](https://docs.comfy.org/es/built-in-nodes/LatentCompositeMasked)[Escalar latente por](https://docs.comfy.org/es/built-in-nodes/LatentUpscaleBy)
