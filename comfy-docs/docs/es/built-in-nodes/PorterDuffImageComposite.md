---
url: https://docs.comfy.org/es/built-in-nodes/PorterDuffImageComposite/
title: Composici\u00f3n de imagen Porter-Duff - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:18.596215+00:00
---

# Composición de imagen Porter-Duff - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PorterDuffImageComposite/

Composición

# Composición de imagen Porter-Duff - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo PorterDuffImageComposite está diseñado para realizar composición de imágenes utilizando los operadores de composición Porter-Duff.

Copiar páginaCopiar página

El nodo PorterDuffImageComposite está diseñado para realizar composición de imágenes utilizando los operadores de composición Porter-Duff. Permite la combinación de imágenes de origen y destino según varios modos de fusión, facilitando la creación de efectos visuales complejos al manipular la transparencia de las imágenes y superponerlas de formas creativas.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`fuente`| El tensor de la imagen de origen que se compondrá sobre la imagen de destino. Desempeña un papel crucial en la determinación del resultado visual final según el modo de composición seleccionado.| `IMAGE`  
`alfa_fuente`| El canal alfa de la imagen de origen, que especifica la transparencia de cada píxel en la imagen de origen. Afecta cómo se fusiona la imagen de origen con la imagen de destino.| `MASK`  
`destino`| El tensor de la imagen de destino que sirve como fondo sobre el cual se compone la imagen de origen. Contribuye a la imagen compuesta final según el modo de fusión.| `IMAGE`  
`alfa_destino`| El canal alfa de la imagen de destino, que define la transparencia de los píxeles de la imagen de destino. Influye en la fusión de las imágenes de origen y destino.| `MASK`  
`modo`| El modo de composición Porter-Duff a aplicar, que determina cómo se fusionan las imágenes de origen y destino. Cada modo crea diferentes efectos visuales.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`image`| La imagen compuesta resultante de la aplicación del modo Porter-Duff especificado.| `IMAGE`  
`mask`| El canal alfa de la imagen compuesta, que indica la transparencia de cada píxel.| `MASK`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PorterDuffImageComposite.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PorterDuffImageComposite)

[Unir imagen con alfa](https://docs.comfy.org/es/built-in-nodes/JoinImageWithAlpha)[Dividir imagen con alfa](https://docs.comfy.org/es/built-in-nodes/SplitImageWithAlpha)
