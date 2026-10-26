---
url: https://docs.comfy.org/es/built-in-nodes/LoraLoaderBypassModelOnly/
title: Cargar LoRA (Bypass, solo modelo) (para depuraci\u00f3n) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:06.519890+00:00
---

# Cargar LoRA (Bypass, solo modelo) (para depuración) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoraLoaderBypassModelOnly/

Cargadores

# Cargar LoRA (Bypass, solo modelo) (para depuración) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo aplica una LoRA (Adaptación de Bajo Rango) a un modelo para modificar su comportamiento, pero solo afecta al componente del modelo en sí.

Copiar páginaCopiar página

Este nodo aplica una LoRA (Adaptación de Bajo Rango) a un modelo para modificar su comportamiento, pero solo afecta al componente del modelo en sí. Carga un archivo LoRA específico y ajusta los pesos del modelo según una intensidad determinada, dejando sin cambios otros componentes como el codificador de texto CLIP.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`model`| El modelo base al que se aplicarán los ajustes de LoRA.| MODEL| Sí| -  
`lora_name`| El nombre del archivo LoRA a cargar y aplicar. Las opciones se obtienen de los archivos en el directorio `loras`.| STRING| Sí| (Lista de archivos LoRA disponibles)  
`strength_model`| La intensidad del efecto de LoRA sobre los pesos del modelo. Un valor positivo aplica la LoRA, un valor negativo aplica la inversa y un valor de 0 no tiene efecto (valor predeterminado: 1.0).| FLOAT| Sí| -100.0 a 100.0  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`model`| El modelo modificado con los ajustes de LoRA aplicados a sus pesos.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypassModelOnly/es.md)

* * *

**Source fingerprint (SHA-256):** `e0e1ad2d6481a1b9771d7eae833ffab0737a967d4af6e57b946d1b2223fe45bf`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoraLoaderBypassModelOnly.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoraLoaderBypassModelOnly)

[Cargar LoRA (Bypass) (Para depuración)](https://docs.comfy.org/es/built-in-nodes/LoraLoaderBypass)[Cargar modelo LoRA](https://docs.comfy.org/es/built-in-nodes/LoraModelLoader)
