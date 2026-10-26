---
url: https://docs.comfy.org/es/built-in-nodes/AdjustContrast/
title: Ajustar contraste - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:30.454613+00:00
---

# Ajustar contraste - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/AdjustContrast/

Ajustes

# Ajustar contraste - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Adjust Contrast ajusta el contraste de una imagen de entrada escalando la diferencia entre las áreas claras y oscuras alrededor del punto medio del

Copiar páginaCopiar página

El nodo Adjust Contrast ajusta el contraste de una imagen de entrada escalando la diferencia entre las áreas claras y oscuras alrededor del punto medio del rango de color. Un factor de 1.0 deja la imagen sin cambios, los valores inferiores a 1.0 reducen el contraste y los valores superiores a 1.0 lo aumentan.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`image`| La imagen de entrada cuyo contraste se ajustará.| IMAGE| Sí| -  
`factor`| Factor de contraste. 1.0 = sin cambios, <1.0 = menos contraste, >1.0 = más contraste. (por defecto: 1.0)| FLOAT| No| 0.0 - 2.0  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`imágenes`| La imagen resultante con el contraste ajustado. Los valores de píxeles se limitan al rango de 0.0 a 1.0. Si la imagen de entrada tiene un canal alfa, ese canal se conserva sin cambios.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/es.md)

* * *

**Source fingerprint (SHA-256):** `489f840cc3d98339a5cf7b55e9179c60878c58b2f992740796c7d49642e05932`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/AdjustContrast.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/AdjustContrast)

[Ajustar brillo](https://docs.comfy.org/es/built-in-nodes/AdjustBrightness)[Eliminar fondo](https://docs.comfy.org/es/built-in-nodes/RemoveBackground)
