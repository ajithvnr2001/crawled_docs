---
url: https://docs.comfy.org/es/built-in-nodes/TextEncodeJoyImageEdit/
title: TextEncodeJoyImageEdit - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:35.140811+00:00
---

# TextEncodeJoyImageEdit - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/TextEncodeJoyImageEdit/

Joyimage

# TextEncodeJoyImageEdit - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo codifica un mensaje de texto e imágenes opcionales en datos de condicionamiento para su uso con modelos JoyImage.

Copiar páginaCopiar página

Este nodo codifica un mensaje de texto e imágenes opcionales en datos de condicionamiento para su uso con modelos JoyImage. Combina un codificador de texto CLIP con entradas de imagen opcionales para crear un condicionamiento enriquecido que puede guiar tareas de generación o edición de imágenes.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`clip`| El modelo CLIP utilizado para codificar el mensaje de texto| CLIP| Sí| -  
`prompt`| El mensaje de texto a codificar, compatible con entrada multilínea y mensajes dinámicos| STRING| Sí| -  
`vae`| Un modelo VAE para codificar imágenes en el espacio latente| VAE| No| -  
`imágenes`| Imágenes opcionales para incluir en el condicionamiento, hasta un máximo de 6 imágenes. Cada imagen se conecta como una entrada separada (image_0 a image_5)| IMAGE| No| 0 a 6 imágenes  
  
## 

​

Salidas

La entrada `images` es un grupo de autoexpansión que acepta entre 0 y 6 imágenes. Cuando no se conecta ninguna imagen, el condicionamiento se basa únicamente en el mensaje de texto.

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`CONDITIONING`| Los datos de condicionamiento codificados que combinan el mensaje de texto y cualquier imagen proporcionada| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeJoyImageEdit/es.md)

* * *

**Source fingerprint (SHA-256):** `ef48523aa9fc990b2839d755cef272bcdfbacef5af8d961736fde5200c6f082d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/TextEncodeJoyImageEdit.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/TextEncodeJoyImageEdit)

[Acondicionamiento InstructPix2Pix](https://docs.comfy.org/es/built-in-nodes/InstructPixToPixConditioning)[Codificar texto CLIP para Kandinsky 5](https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeKandinsky5)
