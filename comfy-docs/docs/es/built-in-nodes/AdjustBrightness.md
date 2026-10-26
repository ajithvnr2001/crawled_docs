---
url: https://docs.comfy.org/es/built-in-nodes/AdjustBrightness/
title: Ajustar brillo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:30.516381+00:00
---

# Ajustar brillo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/AdjustBrightness/

Ajustes

# Ajustar brillo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Adjust Brightness cambia el brillo de una imagen.

Copiar páginaCopiar página

El nodo Adjust Brightness cambia el brillo de una imagen. Multiplica los valores de color de la imagen por un `factor` y mantiene los resultados dentro del rango válido de 0.0 a 1.0. Un factor de 1.0 deja la imagen sin cambios, los valores inferiores a 1.0 la oscurecen y los valores superiores a 1.0 la hacen más brillante.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`image`| La imagen de entrada a ajustar. Acepta una sola imagen o un lote de imágenes.| IMAGE| Sí| -  
`factor`| Factor de brillo. 1.0 = sin cambios, <1.0 = más oscuro, >1.0 = más brillante. (predeterminado: 1.0)| FLOAT| No| 0.0 - 2.0  
  
Nota: Si la imagen de entrada tiene un canal alfa (RGBA), solo se ajustan los canales de color. El canal alfa se copia de la entrada sin cambios porque almacena transparencia, no color.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`imágenes`| La imagen de salida con el brillo ajustado. Si la entrada tiene un canal alfa, los valores alfa permanecen sin cambios.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/es.md)

* * *

**Source fingerprint (SHA-256):** `64c1499d16deb5922fa63538182cd227e8f2ba9ded5962064ce9f228a0f4a163`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/AdjustBrightness.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/AdjustBrightness)

[Compilar modelo con Torch](https://docs.comfy.org/es/built-in-nodes/TorchCompileModel)[Ajustar contraste](https://docs.comfy.org/es/built-in-nodes/AdjustContrast)
