---
url: https://docs.comfy.org/es/built-in-nodes/CreateHookLoraModelOnly/
title: Crear hook LoRA (MO) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:42.395902+00:00
---

# Crear hook LoRA (MO) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/CreateHookLoraModelOnly/

Crear

# Crear hook LoRA (MO) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo crea un hook LoRA (Adaptación de Bajo Rango) que se aplica únicamente al componente del modelo, dejando el componente CLIP completamente sin cambios.

Copiar páginaCopiar página

Este nodo crea un hook LoRA (Adaptación de Bajo Rango) que se aplica únicamente al componente del modelo, dejando el componente CLIP completamente sin cambios. Carga un archivo LoRA y lo aplica con una intensidad específica al modelo, mientras establece la intensidad CLIP en cero. El nodo puede encadenarse con hooks anteriores para construir pipelines de modificación complejas.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Requerido| Rango  
---|---|---|---|---  
`lora_name`| El nombre del archivo LoRA a cargar desde la carpeta loras| STRING| Sí| Múltiples opciones disponibles  
`strength_model`| El multiplicador de intensidad para aplicar el LoRA al componente del modelo (predeterminado: 1.0)| FLOAT| Sí| -20.0 a 20.0  
`prev_hooks`| Hooks anteriores opcionales para encadenar con este hook| HOOKS| No| -  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`hooks`| El hook LoRA creado que puede aplicarse al procesamiento del modelo| HOOKS  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/es.md)

* * *

**Source fingerprint (SHA-256):** `10adbdfc2e37fcf317e93130f87d9a7038d00b091cb6d1b45f4658c81632ef80`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/CreateHookLoraModelOnly.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/CreateHookLoraModelOnly)

[Crear hook LoRA](https://docs.comfy.org/es/built-in-nodes/CreateHookLora)[Crear hook model como LoRA](https://docs.comfy.org/es/built-in-nodes/CreateHookModelAsLora)
