---
url: https://docs.comfy.org/es/built-in-nodes/SaveTrainingDataset/
title: Guardar conjunto de datos de entrenamiento - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:29.735663+00:00
---

# Guardar conjunto de datos de entrenamiento - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveTrainingDataset/

Entrenamiento

# Guardar conjunto de datos de entrenamiento - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo guarda en disco un dataset de entrenamiento codificado para cargarlo de forma eficiente durante el entrenamiento.

Copiar páginaCopiar página

Este nodo guarda en disco un dataset de entrenamiento codificado para cargarlo de forma eficiente durante el entrenamiento. Toma los latentes de imagen y su condicionamiento de texto correspondiente, los divide en archivos más pequeños llamados fragmentos y los almacena en una carpeta dentro del directorio datasets. También escribe un archivo de metadatos que describe el dataset.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`latents`| Lista de diccionarios de latentes de MakeTrainingDataset.| LATENT| Sí| N/A  
`conditioning`| Lista de listas de condicionamiento de MakeTrainingDataset.| CONDITIONING| Sí| N/A  
`folder_name`| Nombre de la carpeta en la que se guardará el dataset, dentro del directorio datasets. Se permiten subcarpetas como ‘project/run1’. (predeterminado: “training_dataset”)| STRING| Sí| N/A  
`shard_size`| Número de muestras por archivo de fragmento. (predeterminado: 1000)| INT| Sí| 1 a 100000  
  
**Nota:** La cantidad de elementos en `latents` debe coincidir exactamente con la cantidad de elementos en `conditioning`; el nodo lanza un error si estas cantidades no coinciden. El `folder_name` debe especificar una subcarpeta del directorio datasets (por ejemplo, `my_dataset`); no puede ser el propio directorio datasets, y se rechazan los nombres de carpeta que se resuelvan fuera del directorio datasets. El parámetro `shard_size` es una configuración avanzada.

## 

​

Salidas

Este nodo no produce ningún dato de salida. Su función es guardar archivos en el disco. Cada fragmento se guarda como un archivo `shard_XXXX.pkl` en la carpeta elegida, y un archivo `metadata.json` registra el número total de muestras, el número de fragmentos y el tamaño de los fragmentos.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/es.md)

* * *

**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveTrainingDataset.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveTrainingDataset)

[Agrupación por resolución](https://docs.comfy.org/es/built-in-nodes/ResolutionBucket)[Entrenar LoRA](https://docs.comfy.org/es/built-in-nodes/TrainLoraNode)
