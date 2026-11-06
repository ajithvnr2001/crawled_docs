---
url: https://docs.comfy.org/es/built-in-nodes/PikaSoundtrackNode/
title: PikaSoundtrackNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-06T14:51:54.435766+00:00
---

# PikaSoundtrackNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PikaSoundtrackNode/

Video

# PikaSoundtrackNode - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo genera una banda sonora sincronizada para un video con Pika.

Copiar páginaCopiar página

Este nodo genera una banda sonora sincronizada para un video con Pika. Se conservan la imagen y la duración; solo se reemplaza el audio. Describe el sonido que deseas o deja la instrucción vacía para derivarlo de la imagen.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`video`| El clip para el que se escribirá una banda sonora. Hasta 10 minutos.| VIDEO| Sí| -  
`instruction`| Qué debe ser el audio: efectos de sonido, ambiente, música o estilo. Déjalo vacío para derivarlo de la imagen. Predeterminado: "" (cadena vacía).| STRING| Sí| 0 a 10000 caracteres  
`seed`| Semilla para el muestreo. Predeterminado: 42.| INT| Sí| 0 a 2147483647  
  
**Restricciones:**

  * El video de entrada debe durar 10 minutos o menos.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`VIDEO`| El clip de entrada con la banda sonora generada en lugar del audio original.| VIDEO  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaSoundtrackNode/es.md)

* * *

**Source fingerprint (SHA-256):** `9820efec607ba52dbabe5e4fb0862240fb0f0215ce7e72914451823b7e75120b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PikaSoundtrackNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PikaSoundtrackNode)

[PikaH3FlexVideoNode](https://docs.comfy.org/es/built-in-nodes/PikaH3FlexVideoNode)[Doblaje de VEED](https://docs.comfy.org/es/built-in-nodes/VeedDubbingNode)
