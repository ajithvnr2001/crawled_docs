---
url: https://docs.comfy.org/es/built-in-nodes/DiffusersLoader/
title: Cargar modelo Diffusers (obsoleto) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:43.567672+00:00
---

# Cargar modelo Diffusers (obsoleto) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/DiffusersLoader/

Cargadores

# Cargar modelo Diffusers (obsoleto) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo DiffusersLoader carga modelos preentrenados guardados en el formato diffusers.

Copiar páginaCopiar página

El nodo DiffusersLoader carga modelos preentrenados guardados en el formato diffusers. Busca en las carpetas `diffusers` configuradas los directorios que contengan un archivo `model_index.json`, te permite seleccionar uno y lo carga como los componentes MODEL, CLIP y VAE utilizados en el pipeline. Este nodo está obsoleto, pero sigue disponible para compatibilidad con modelos diffusers de Hugging Face.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`ruta_del_modelo`| La ruta al directorio del modelo diffusers que se va a cargar. El nodo escanea automáticamente las carpetas diffusers configuradas para buscar modelos válidos y muestra las opciones disponibles.| COMBO| Sí| Múltiples opciones disponibles  
(autocompletadas desde las carpetas diffusers)  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`MODEL`| El componente de modelo cargado desde el formato diffusers.| MODEL  
`CLIP`| El componente de modelo CLIP cargado desde el formato diffusers.| CLIP  
`VAE`| El componente VAE (Autoencoder Variacional) cargado desde el formato diffusers.| VAE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/es.md)

* * *

**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/DiffusersLoader.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/DiffusersLoader)

[Cargar modelo ControlNet (diff)](https://docs.comfy.org/es/built-in-nodes/DiffControlNetLoader)[Cargar CLIP dual](https://docs.comfy.org/es/built-in-nodes/DualCLIPLoader)
