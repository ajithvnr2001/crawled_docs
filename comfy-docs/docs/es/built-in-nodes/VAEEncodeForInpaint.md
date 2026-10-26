---
url: https://docs.comfy.org/es/built-in-nodes/VAEEncodeForInpaint/
title: Codificaci\u00f3n VAE (para inpainting) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:40.858705+00:00
---

# Codificación VAE (para inpainting) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VAEEncodeForInpaint/

Latente

# Codificación VAE (para inpainting) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para codificar imágenes en una representación latente adecuada para tareas de inpainting

Copiar páginaCopiar página

Este nodo está diseñado para codificar imágenes en una representación latente adecuada para tareas de inpainting, incorporando pasos de preprocesamiento adicionales para ajustar la imagen de entrada y la máscara, logrando una codificación óptima por parte del modelo VAE.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`píxeles`| La imagen de entrada que se va a codificar. Esta imagen se somete a un preprocesamiento y redimensionamiento para que coincida con las dimensiones de entrada esperadas por el modelo VAE antes de la codificación.| `IMAGE`  
`vae`| El modelo VAE utilizado para codificar la imagen en su representación latente. Desempeña un papel crucial en el proceso de transformación, determinando la calidad y las características del espacio latente de salida.| VAE  
`máscara`| Una máscara que indica las regiones de la imagen de entrada que se van a inpaint. Se utiliza para modificar la imagen antes de la codificación, asegurando que el VAE se centre en las áreas relevantes.| `MASK`  
`crecer_máscara_por`| Especifica cuánto expandir la máscara de inpainting para garantizar transiciones sin fisuras en el espacio latente. Un valor mayor aumenta el área afectada por el inpainting.| `INT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`latent`| La salida incluye la representación latente codificada de la imagen y una máscara de ruido, ambas cruciales para las tareas posteriores de inpainting.| `LATENT`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeForInpaint/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VAEEncodeForInpaint.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VAEEncodeForInpaint)

[Codificación de audio con VAE](https://docs.comfy.org/es/built-in-nodes/VAEEncodeAudio)[Codificación VAE (Mosaico)](https://docs.comfy.org/es/built-in-nodes/VAEEncodeTiled)
