---
url: https://docs.comfy.org/es/built-in-nodes/VAESave/
title: Guardar VAE - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:40.636954+00:00
---

# Guardar VAE - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VAESave/

Fusión

# Guardar VAE - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VAESave está diseñado para guardar modelos VAE junto con sus metadatos, incluyendo indicaciones e información adicional de PNG

Copiar páginaCopiar página

El nodo VAESave está diseñado para guardar modelos VAE junto con sus metadatos, incluyendo indicaciones e información adicional de PNG, en un directorio de salida especificado. Encapsula la funcionalidad de serializar el estado del modelo y la información asociada en un archivo, facilitando la preservación y el intercambio de modelos entrenados.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`vae`| El modelo VAE que se va a guardar. Este parámetro es crucial, ya que representa el modelo cuyo estado se serializará y almacenará.| VAE  
`prefijo_nombre_archivo`| Un prefijo para el nombre del archivo bajo el cual se guardarán el modelo y sus metadatos. Esto permite un almacenamiento organizado y una fácil recuperación de los modelos.| STRING  
  
## 

​

Salidas

El nodo no tiene tipos de salida.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAESave/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VAESave.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VAESave)

[Guardar pesos de LoRA](https://docs.comfy.org/es/built-in-nodes/SaveLoRA)[Aplicar Anima LLLite](https://docs.comfy.org/es/built-in-nodes/AnimaLLLiteApply)
