---
url: https://docs.comfy.org/es/built-in-nodes/FluxVTONode/
title: Flux Prueba virtual de ropa - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:49.129308+00:00
---

# Flux Prueba virtual de ropa - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/FluxVTONode/

BFL

# Flux Prueba virtual de ropa - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo realiza una prueba virtual de ropa al vestir a una persona con una imagen de prenda proporcionada.

Copiar páginaCopiar página

Este nodo realiza una prueba virtual de ropa al vestir a una persona con una imagen de prenda proporcionada. Envía las imágenes de la persona y de la prenda al servicio BFL Flux VTO, que genera una imagen realista de la persona usando la prenda. Se puede usar una instrucción de texto opcional para describir cómo debería quedar o verse la prenda.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`person`| Imagen de la persona a vestir.| IMAGE| Sí| -  
`garment`| Imagen de la prenda a aplicar.| IMAGE| Sí| -  
`prompt`| Instrucción opcional de estilo en lenguaje natural (p. ej., cómo debería quedar la prenda). El valor predeterminado es una cadena vacía.| STRING| No| -  
`seed`| La semilla aleatoria utilizada para crear el ruido. Predeterminado: 0.| INT| No| 0 a 18446744073709551615  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`image`| La imagen resultante que muestra a la persona usando la prenda proporcionada.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/es.md)

* * *

**Source fingerprint (SHA-256):** `5e0777dedcbd6275e31a16f6f5d78f4166147266c0c88531c5843a027702e594`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/FluxVTONode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/FluxVTONode)

[Flux 1.1 [pro] Ultra imagen](https://docs.comfy.org/es/built-in-nodes/FluxProUltraImageNode)[Bria Añadir objeto](https://docs.comfy.org/es/built-in-nodes/BriaAddObject)
