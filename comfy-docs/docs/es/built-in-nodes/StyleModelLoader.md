---
url: https://docs.comfy.org/es/built-in-nodes/StyleModelLoader/
title: Cargar modelo de estilo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:33.991991+00:00
---

# Cargar modelo de estilo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/StyleModelLoader/

Cargadores

# Cargar modelo de estilo - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detectará los modelos ubicados en la carpeta ComfyUI/models/stylemodels

Copiar páginaCopiar página

Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/style_models`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo desde la carpeta correspondiente. El nodo StyleModelLoader está diseñado para cargar un modelo de estilo desde una ruta especificada. Se enfoca en recuperar e inicializar modelos de estilo que pueden usarse para aplicar estilos artísticos específicos a las imágenes, permitiendo así la personalización de las salidas visuales según el modelo de estilo cargado.

## 

​

Entradas

Nombre del parámetro| Descripción| Tipo Comfy| Tipo Python  
---|---|---|---  
`nombre_del_modelo_de_estilo`| Especifica el nombre del modelo de estilo que se va a cargar. Este nombre se utiliza para localizar el archivo del modelo dentro de una estructura de directorios predefinida, lo que permite la carga dinámica de diferentes modelos de estilo según la entrada del usuario o las necesidades de la aplicación.| COMBO[STRING]| `str`  
  
## 

​

Salidas

Nombre del parámetro| Descripción| Tipo Comfy| Tipo Python  
---|---|---|---  
`style_model`| Devuelve el modelo de estilo cargado, listo para usar en la aplicación de estilos a las imágenes. Esto permite la personalización dinámica de las salidas visuales mediante la aplicación de diferentes estilos artísticos.| `STYLE_MODEL`| `StyleModel`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/StyleModelLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/StyleModelLoader)

[Cargar CLIP quad](https://docs.comfy.org/es/built-in-nodes/QuadrupleCLIPLoader)[Cargar CLIP triple](https://docs.comfy.org/es/built-in-nodes/TripleCLIPLoader)
