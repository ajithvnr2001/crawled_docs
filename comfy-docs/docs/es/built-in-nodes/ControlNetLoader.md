---
url: https://docs.comfy.org/es/built-in-nodes/ControlNetLoader/
title: Cargar modelo ControlNet - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:41.693551+00:00
---

# Cargar modelo ControlNet - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ControlNetLoader/

Cargador

# Cargar modelo ControlNet - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo detecta los modelos ubicados en la carpeta ComfyUI/models/controlnet

Copiar páginaCopiar página

Este nodo detecta los modelos ubicados en la carpeta `ComfyUI/models/controlnet`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, puede ser necesario **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo desde la carpeta correspondiente. El nodo ControlNetLoader está diseñado para cargar un modelo ControlNet desde una ruta específica. Desempeña un papel fundamental en la inicialización de modelos ControlNet, los cuales son esenciales para aplicar mecanismos de control sobre el contenido generado o modificar contenido existente basándose en señales de control.

## 

​

Entradas

Campo| Descripción| Tipo Comfy  
---|---|---  
`nombre_control_net`| Especifica el nombre del modelo ControlNet a cargar, utilizado para localizar el archivo del modelo dentro de una estructura de directorios predefinida.| `COMBO[STRING]`  
  
## 

​

Salidas

Campo| Descripción| Tipo Comfy  
---|---|---  
`control_net`| Devuelve el modelo ControlNet cargado, listo para usarse en el control o modificación de procesos de generación de contenido.| `CONTROL_NET`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetLoader/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ControlNetLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ControlNetLoader)

[Obtener tamaño del latent de imagen/vídeo](https://docs.comfy.org/es/built-in-nodes/GetLatentSize)[Codificar texto Ace Step audio](https://docs.comfy.org/es/built-in-nodes/TextEncodeAceStepAudio)
