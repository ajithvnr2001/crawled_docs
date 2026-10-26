---
url: https://docs.comfy.org/es/built-in-nodes/TextEncodeBooguEdit/
title: TextEncodeBooguEdit - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:34.897497+00:00
---

# TextEncodeBooguEdit - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TextEncodeBooguEdit/

Boogu

# TextEncodeBooguEdit - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo prepara el condicionamiento para la edición de imágenes con Boogu.

Copiar páginaCopiar página

Este nodo prepara el condicionamiento para la edición de imágenes con Boogu. Procesa imágenes de referencia para generar salidas de condicionamiento tanto positivas como negativas. La imagen de referencia se usa dos veces: los tokens de visión de la imagen se agregan solo al condicionamiento positivo para amplificar la instrucción de edición, mientras que un latente de referencia del VAE se agrega tanto al condicionamiento positivo como al negativo para que se cancele bajo CFG, preservando la identidad de la imagen original; el tokenizador selecciona automáticamente el prompt del sistema apropiado según la presencia de imágenes y prompts negativos vacíos.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP utilizado para la codificación de texto| CLIP| Sí|   
`prompt`| El prompt de texto que describe la edición deseada. Admite texto multilínea y prompts dinámicos.| STRING| Sí|   
`negative_prompt`| El prompt de texto que describe lo que se debe evitar en la edición. Puede dejarse vacío para eliminar el condicionamiento negativo. Parámetro avanzado.| STRING| Sí|   
`vae`| El modelo VAE utilizado para codificar imágenes de referencia en el espacio latente. Necesario para agregar latentes de referencia a las salidas de condicionamiento.| VAE| No|   
`imágenes`| Imagen(es) de referencia a editar. Boogu se enfoca en una referencia por muestra; se permiten más.| IMAGE| No| Hasta 16 imágenes  
Los latentes de referencia se agregan a ambas salidas de condicionamiento solo cuando se proporciona `vae` junto con al menos una `image` de referencia. Si se omite `vae`, la salida positiva aún recibe tokens de visión de las imágenes de referencia, pero ninguna salida incluye latentes de referencia.| | | |   
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`positivo`| Condicionamiento que contiene tanto el prompt de texto con tokens visuales como los latentes de referencia| CONDITIONING  
`negativo`| Condicionamiento que contiene el prompt de texto negativo y los latentes de referencia| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/es.md)

* * *

**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TextEncodeBooguEdit.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TextEncodeBooguEdit)

[Bernini Conditioning](https://docs.comfy.org/es/built-in-nodes/BerniniConditioning)[Aplicar ControlNet (ANTIGUO)](https://docs.comfy.org/es/built-in-nodes/ControlNetApply)
