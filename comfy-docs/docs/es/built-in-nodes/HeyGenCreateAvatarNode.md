---
url: https://docs.comfy.org/es/built-in-nodes/HeyGenCreateAvatarNode/
title: Crear Avatar HeyGen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:52.469352+00:00
---

# Crear Avatar HeyGen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/HeyGenCreateAvatarNode/

Heygen

# Crear Avatar HeyGen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Crear un avatar HeyGen reutilizable a partir de una foto de una persona o de una descripción de texto que genere un personaje.

Copiar páginaCopiar página

Crear un avatar HeyGen reutilizable a partir de una foto de una persona o de una descripción de texto que genere un personaje. El `avatar_id` resultante puede usarse con el nodo HeyGen Avatar Video, y debe guardarse para reutilizar el avatar en flujos de trabajo futuros.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`fuente`| Genera un nuevo personaje a partir de una descripción de texto, o crea el avatar a partir de una foto conectada de una persona.| DYNAMIC_COMBO| Sí| `"prompt"`  
`"photo"`  
  
### 

​

Entradas de prompt

Disponible cuando `source` está configurado en `"prompt"`.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`prompt`| Descripción del avatar a generar (hasta 1000 caracteres). Debe contener al menos 1 carácter que no sea espacio en blanco. Valor predeterminado: cadena vacía.| STRING| Sí| De 1 a 1000 caracteres  
  
### 

​

Entradas de foto

Disponible cuando `source` está configurado en `"photo"`.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`identity_photo`| Foto de la persona para convertirla en avatar. Se reduce de escala automáticamente si es más grande que 2K.| IMAGE| Sí| Imagen única  
  
### 

​

Entradas de referencia

Disponible cuando `source` está configurado en `"prompt"`.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`reference_images`| Ranura ampliable: conecta hasta 3 imágenes (`ref_image_1`…`ref_image_3`) que guían el aspecto generado. Las imágenes se reducen de escala automáticamente si son más grandes que 2K.| IMAGE| No| De 0 a 3 imágenes  
  
**Nota:** El parámetro `source` alterna entre dos modos mutuamente excluyentes. En el modo `"prompt"`, se requiere `prompt` y opcionalmente se pueden conectar hasta 3 imágenes de referencia. En el modo `"photo"`, se requiere `identity_photo`. Las fotos y las imágenes de referencia se reducen de escala automáticamente cuando superan 2K; no se aceptan más de 3 imágenes de referencia.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`avatar_id`| Identificador del aspecto del avatar. Pásalo al `custom_avatar_id` de HeyGen Avatar Video; guárdalo para reutilizar el avatar más adelante.| STRING  
`vista previa`| Imagen de vista previa del avatar generado.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/es.md)

* * *

**Source fingerprint (SHA-256):** `3669686fc6d089909bd5d2d75292ceef05702ed3cc7b14e561bcb444c30a4e63`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/HeyGenCreateAvatarNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/HeyGenCreateAvatarNode)

[Video de Avatar HeyGen](https://docs.comfy.org/es/built-in-nodes/HeyGenAvatarVideoNode)[HeyGen Video 1.0 de imagen a vídeo](https://docs.comfy.org/es/built-in-nodes/HeyGenImageToVideoNode)
