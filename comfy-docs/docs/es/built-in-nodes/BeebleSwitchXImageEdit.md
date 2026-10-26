---
url: https://docs.comfy.org/es/built-in-nodes/BeebleSwitchXImageEdit/
title: Beeble SwitchX Edici\u00f3n de Imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:31.801575+00:00
---

# Beeble SwitchX Edición de Imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BeebleSwitchXImageEdit/

Beeble

# Beeble SwitchX Edición de Imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Edita una sola imagen con Beeble SwitchX.

Copiar páginaCopiar página

## 

​

Resumen

Edita una sola imagen con Beeble SwitchX. Este nodo puede cambiar cualquier elemento de la escena (fondo, iluminación, vestimenta) mientras preserva los píxeles del sujeto original. Proporciona una imagen de referencia y/o un prompt de texto para describir el nuevo aspecto. La resolución máxima es de aproximadamente 2,77 megapíxeles.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen de origen a editar.| IMAGE| Sí| -  
`prompt`| Una descripción textual del nuevo aspecto deseado (ej., “un caballero con armadura brillante”).| STRING| Sí| -  
`modo_alpha`| Cómo manejar el matte alfa. “select” usa un fotograma clave para seleccionar el sujeto, “fill” reemplaza toda la imagen sin un matte separado, “custom” usa una máscara proporcionada por el usuario.| COMBO| Sí| `"select"`  
`"fill"`  
`"custom"`  
`resolución_máxima`| La resolución máxima para la imagen de salida. Una resolución más alta consume más créditos.| COMBO| Sí| `"1080p"`  
`"720p"`  
`semilla`| Un valor de semilla para reproducibilidad.| INT| Sí| -  
`imagen_de_referencia`| Una imagen de referencia opcional para guiar el estilo o la apariencia de los nuevos elementos de la escena.| IMAGE| No| -  
  
**Nota sobre`alpha_mode`:** Cuando `alpha_mode` está configurado en `"select"`, también debes proporcionar un `alpha_keyframe` (una imagen de fotograma clave usada para seleccionar el sujeto). Cuando está configurado en `"custom"`, debes proporcionar un `alpha_mask` (una máscara creada por el usuario). Cuando está configurado en `"fill"`, no se necesita entrada alfa.

## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen editada con los elementos de la escena cambiados.| IMAGE  
`alfa`| El matte alfa utilizado por Beeble. Vacío para el modo “fill”, que no tiene matte separado.| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/es.md)

* * *

**Source fingerprint (SHA-256):** `41f23435686626e3ade28708fcb1da192ded347b210080ee9b17834ea8b727fb`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BeebleSwitchXImageEdit.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BeebleSwitchXImageEdit)

[VEED Clean Audio](https://docs.comfy.org/es/built-in-nodes/VeedCleanAudioNode)[Flux.2 Image](https://docs.comfy.org/es/built-in-nodes/Flux2ImageNode)
