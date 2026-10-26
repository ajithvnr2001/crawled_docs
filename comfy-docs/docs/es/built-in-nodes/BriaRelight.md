---
url: https://docs.comfy.org/es/built-in-nodes/BriaRelight/
title: Bria Reiluminar - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:33.212829+00:00
---

# Bria Reiluminar - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BriaRelight/

Bria

# Bria Reiluminar - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo cambia la atmósfera y la dirección de la iluminación de una imagen usando Bria.

Copiar páginaCopiar página

Este nodo cambia la atmósfera y la dirección de la iluminación de una imagen usando Bria. Bria vuelve a renderizar la imagen, por lo que el resultado no está alineado a nivel de píxel con la entrada; el fotograma completo se regenera a aproximadamente 1 megapíxel.

## 

​

Entradas

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen cuya iluminación se cambia. Cualquier canal alfa se descarta antes de subir la imagen.| IMAGE| Sí| -  
`light_type`| Atmósfera de iluminación que se aplicará.| COMBO| Sí| `"midday"`  
`"blue hour light"`  
`"low-angle sunlight"`  
`"sunrise light"`  
`"spotlight on subject"`  
`"overcast light"`  
`"soft overcast daylight lighting"`  
`"cloud-filtered lighting"`  
`"fog-diffused lighting"`  
`"moonlight lighting"`  
`"starlight nighttime"`  
`"soft bokeh lighting"`  
`"harsh studio lighting"`  
`light_direction`| De dónde viene la luz. Las atmósferas de luz dura, como midday, spotlight on subject y harsh studio lighting, son las que más reaccionan a ella.| COMBO| Sí| `"front"`  
`"side"`  
`"bottom"`  
`"top-down"`  
`moderación`| Ajustes de moderación. Seleccione `"true"` para mostrar las opciones de moderación, o `"false"` para ejecutar sin ellas.| DYNAMIC_COMBO| Sí| `"false"`  
`"true"`  
  
### 

​

Entradas de moderación

Estas opciones aparecen cuando `moderation` se establece en `"true"`.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`visual_input_moderation`| Activa la moderación de contenido en la imagen de entrada. Predeterminado: false.| BOOLEAN| No| `true`  
`false`  
`visual_output_moderation`| Activa la moderación de contenido en la imagen de salida generada. Predeterminado: false.| BOOLEAN| No| `true`  
`false`  
  
Nota: Bria vuelve a renderizar el fotograma completo a aproximadamente 1 megapíxel, por lo que el resultado no está alineado a nivel de píxel con la entrada.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| La imagen con la iluminación modificada devuelta por Bria.| IMAGE  
`structured_prompt`| Descripción estructurada de la imagen editada, para una edición posterior con Bria FIBO Image Edit.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/es.md)

* * *

**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BriaRelight.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BriaRelight)

[Aumentar resolución con Bria](https://docs.comfy.org/es/built-in-nodes/BriaIncreaseResolution)[Bria: Quitar fondo de imagen](https://docs.comfy.org/es/built-in-nodes/BriaRemoveImageBackground)
