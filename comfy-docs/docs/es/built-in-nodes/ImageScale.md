---
url: https://docs.comfy.org/es/built-in-nodes/ImageScale/
title: Ampliar imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:57.018323+00:00
---

# Ampliar imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageScale/

Escalado

# Ampliar imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageScale está diseñado para redimensionar imágenes a dimensiones específicas

Copiar páginaCopiar página

El nodo ImageScale está diseñado para redimensionar imágenes a dimensiones específicas, ofreciendo una selección de métodos de ampliación y la capacidad de recortar la imagen redimensionada. Abstrae la complejidad del escalado y recorte de imágenes, proporcionando una interfaz sencilla para modificar las dimensiones de la imagen según parámetros definidos por el usuario.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen de entrada que se va a ampliar. Este parámetro es central para el funcionamiento del nodo, ya que sirve como dato principal sobre el cual se aplican las transformaciones de redimensionamiento. La calidad y las dimensiones de la imagen de salida están directamente influenciadas por las propiedades de la imagen original.| `IMAGE`  
`metodo_ampliacion`| Especifica el método utilizado para ampliar la imagen. La elección del método puede afectar la calidad y las características de la imagen ampliada, influyendo en la fidelidad visual y los posibles artefactos en la salida redimensionada.| COMBO[STRING]  
`ancho`| El ancho objetivo para la imagen ampliada. Este parámetro influye directamente en las dimensiones de la imagen de salida, determinando la escala horizontal de la operación de redimensionamiento.| `INT`  
`altura`| La altura objetivo para la imagen ampliada. Este parámetro influye directamente en las dimensiones de la imagen de salida, determinando la escala vertical de la operación de redimensionamiento.| `INT`  
`recorte`| Determina si la imagen ampliada debe recortarse y de qué manera, ofreciendo opciones para deshabilitar el recorte o realizar un recorte centrado. Esto afecta la composición final de la imagen al eliminar potencialmente los bordes para ajustarse a las dimensiones especificadas.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`imagen`| La imagen ampliada (y opcionalmente recortada), lista para su posterior procesamiento o visualización.| `IMAGE`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScale/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageScale.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageScale)

[Rellenar imagen](https://docs.comfy.org/es/built-in-nodes/PadImageNode)[Ampliar imagen por](https://docs.comfy.org/es/built-in-nodes/ImageScaleBy)
