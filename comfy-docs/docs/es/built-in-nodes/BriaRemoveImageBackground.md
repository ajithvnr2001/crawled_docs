---
url: https://docs.comfy.org/es/built-in-nodes/BriaRemoveImageBackground/
title: Bria: Quitar fondo de imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:33.293329+00:00
---

# Bria: Quitar fondo de imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/BriaRemoveImageBackground/

Bria

# Bria: Quitar fondo de imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo elimina el fondo de una imagen utilizando el servicio Bria RMBG 2.0.

Copiar páginaCopiar página

Este nodo elimina el fondo de una imagen utilizando el servicio Bria RMBG 2.0. Envía la imagen a una API externa para su procesamiento y devuelve el resultado con el fondo eliminado.

## 

​

Entradas

El selector `moderation` revela opciones de moderación adicionales cuando se establece en `"true"`.

### 

​

Entradas comunes

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada a la que se le eliminará el fondo.| IMAGE| Sí| -  
`moderación`| Configuración de moderación. Cuando se establece en `"true"`, se habilitan opciones de moderación adicionales.| DYNAMIC_COMBO| Sí| `"false"`  
`"true"`  
`semilla`| La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Predeterminado: `0`.| INT| Sí| 0 a 2147483647  
  
### 

​

Entradas de moderación “true”

Estos parámetros solo aparecen cuando `moderation` se establece en `"true"`. La opción `"false"` no agrega entradas adicionales.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`visual_input_moderation`| Habilita la moderación de contenido visual en la imagen de entrada. Predeterminado: `False`.| BOOLEAN| No| -  
`visual_output_moderation`| Habilita la moderación de contenido visual en la imagen de salida. Predeterminado: `True`.| BOOLEAN| No| -  
  
**Nota:** Los parámetros `visual_input_moderation` y `visual_output_moderation` dependen del parámetro `moderation`. Solo están activos cuando `moderation` se establece en `"true"`.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| La imagen procesada con su fondo eliminado.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/es.md)

* * *

**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/BriaRemoveImageBackground.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/BriaRemoveImageBackground)

[Bria Reiluminar](https://docs.comfy.org/es/built-in-nodes/BriaRelight)[Bria Reemplazar fondo de imagen](https://docs.comfy.org/es/built-in-nodes/BriaReplaceImageBackground)
