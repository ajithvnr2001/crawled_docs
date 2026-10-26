---
url: https://docs.comfy.org/es/built-in-nodes/SaveLoRA/
title: Guardar pesos de LoRA - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:29.174461+00:00
---

# Guardar pesos de LoRA - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveLoRA/

Fusión

# Guardar pesos de LoRA - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SaveLoRA guarda un modelo LoRA (Low-Rank Adaptation) en un archivo.

Copiar páginaCopiar página

El nodo SaveLoRA guarda un modelo LoRA (Low-Rank Adaptation) en un archivo. Toma un modelo LoRA como entrada y lo escribe en un archivo `.safetensors` en el directorio de salida. Puede especificar un prefijo de nombre de archivo y un número de pasos opcional que se incluirá en el nombre de archivo final.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`lora`| El modelo LoRA que se va a guardar. No use un modelo con capas LoRA.| LORA_MODEL| Sí| N/A  
`prefix`| El prefijo que se usará para el archivo LoRA guardado (predeterminado: “loras/ComfyUI_trained_lora”).| STRING| Sí| N/A  
`steps`| Opcional: El número de pasos para los que se ha entrenado el LoRA, usado para nombrar el archivo guardado.| INT| No| N/A  
  
**Nota:** La entrada `lora` debe ser un modelo LoRA puro. No proporcione un modelo base al que se le hayan aplicado capas LoRA. **Nota:** El archivo se guarda en el directorio de salida de ComfyUI con extensión `.safetensors`. El nombre del archivo se construye a partir del `prefix` y un contador con ceros a la izquierda (5 dígitos) para evitar sobrescribir archivos existentes. Cuando se proporciona `steps`, el recuento de pasos también se incluye en el nombre del archivo (por ejemplo, `1000_steps` para 1000 pasos). **Nota:** Este nodo está marcado como experimental.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
 _None_|  Este nodo no emite ningún dato al flujo de trabajo. Es un nodo de salida que guarda un archivo en disco.| N/A  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/es.md)

* * *

**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveLoRA.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveLoRA)

[Guardar modelo](https://docs.comfy.org/es/built-in-nodes/ModelSave)[Guardar VAE](https://docs.comfy.org/es/built-in-nodes/VAESave)
