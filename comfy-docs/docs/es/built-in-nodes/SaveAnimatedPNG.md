---
url: https://docs.comfy.org/es/built-in-nodes/SaveAnimatedPNG/
title: Guardar PNG animado - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:28.157329+00:00
---

# Guardar PNG animado - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveAnimatedPNG/

Imagen

# Guardar PNG animado - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SaveAnimatedPNG está diseñado para crear y guardar imágenes PNG animadas a partir de una secuencia de fotogramas.

Copiar páginaCopiar página

El nodo SaveAnimatedPNG está diseñado para crear y guardar imágenes PNG animadas a partir de una secuencia de fotogramas. Gestiona el ensamblaje de fotogramas de imagen individuales en una animación cohesiva, permitiendo la personalización de la duración de los fotogramas, el bucle y la inclusión de metadatos.

## 

​

Entradas

Campo| Descripción| Tipo de Dato  
---|---|---  
`imágenes`| Una lista de imágenes que se procesarán y guardarán como un PNG animado. Cada imagen en la lista representa un fotograma de la animación.| `IMAGE`  
`prefijo_nombre_archivo`| Especifica el nombre base del archivo de salida, que se utilizará como prefijo para los archivos PNG animados generados.| `STRING`  
`fps`| La velocidad de fotogramas por segundo de la animación, que controla la rapidez con la que se muestran los fotogramas.| `FLOAT`  
`nivel_compresión`| El nivel de compresión aplicado a los archivos PNG animados, que afecta el tamaño del archivo y la claridad de la imagen.| `INT`  
  
## 

​

Salidas

Campo| Descripción| Tipo de Dato  
---|---|---  
`images`| Proporciona un componente de interfaz de usuario que muestra las imágenes PNG animadas generadas e indica si la animación es de un solo fotograma o de múltiples fotogramas.| N/A  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveAnimatedPNG.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveAnimatedPNG)

[Redimensionar imagen/máscara](https://docs.comfy.org/es/built-in-nodes/ResizeImageMaskNode)[Guardar WEBP animado](https://docs.comfy.org/es/built-in-nodes/SaveAnimatedWEBP)
