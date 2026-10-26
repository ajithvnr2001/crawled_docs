---
url: https://docs.comfy.org/es/built-in-nodes/InvertMask/
title: Invertir m\u00e1scara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.808520+00:00
---

# Invertir máscara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/InvertMask/

Máscara

# Invertir máscara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo InvertMask está diseñado para invertir los valores de una máscara dada, intercambiando efectivamente las áreas enmascaradas y no enmascaradas.

Copiar páginaCopiar página

El nodo InvertMask está diseñado para invertir los valores de una máscara dada, intercambiando efectivamente las áreas enmascaradas y no enmascaradas. Esta operación es fundamental en tareas de procesamiento de imágenes donde es necesario cambiar el foco de interés entre el primer plano y el fondo.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`máscara`| El parámetro `máscara` representa la máscara de entrada que se va a invertir. Es crucial para determinar las áreas que se intercambiarán en el proceso de inversión.| MASK  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`máscara`| La salida es una versión invertida de la máscara de entrada, donde las áreas previamente enmascaradas pasan a ser no enmascaradas y viceversa.| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InvertMask/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/InvertMask.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/InvertMask)

[Convertir imagen a máscara](https://docs.comfy.org/es/built-in-nodes/ImageToMask)[Componer máscara](https://docs.comfy.org/es/built-in-nodes/MaskComposite)
