---
url: https://docs.comfy.org/es/built-in-nodes/FluxEraseNode/
title: Flux Borrar imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:48.181016+00:00
---

# Flux Borrar imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/FluxEraseNode/

BFL

# Flux Borrar imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Elimina el objeto enmascarado de una imagen y reconstruye el fondo.

Copiar páginaCopiar página

Elimina el objeto enmascarado de una imagen y reconstruye el fondo. Pinte la máscara sobre lo que desee borrar y el nodo rellenará el área con contenido de fondo plausible.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada a procesar| IMAGE| Sí| -  
`máscara`| Las áreas blancas se eliminan; las áreas negras se conservan| MASK| Sí| -  
`dilatar_pixeles`| Expande los límites de la máscara para asegurar una cobertura limpia de los bordes del objeto (predeterminado: 10)| INT| Sí| 0 a 25  
`seed`| La semilla aleatoria utilizada para generar el ruido (predeterminado: 0)| INT| No| 0 a 2147483647  
  
**Nota:** La imagen de entrada debe tener al menos 256x256 píxeles en ambas dimensiones. La máscara se redimensiona automáticamente para coincidir con las dimensiones de la imagen, y el canal alfa de la imagen se elimina antes del procesamiento.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`IMAGE`| La imagen resultante con el objeto enmascarado eliminado y el fondo reconstruido| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxEraseNode/es.md)

* * *

**Source fingerprint (SHA-256):** `124be59b9829aa9f865d7ec76cd68f7978e2010cd3a84f25742a1c17f2d70b76`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/FluxEraseNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/FluxEraseNode)

[FLUX 3 Image](https://docs.comfy.org/es/built-in-nodes/Flux3ImageNode)[Flux.1 expandir imagen](https://docs.comfy.org/es/built-in-nodes/FluxProExpandNode)
