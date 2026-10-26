---
url: https://docs.comfy.org/es/built-in-nodes/SaveConditioning/
title: Guardar condicionamiento - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:28.798223+00:00
---

# Guardar condicionamiento - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveConditioning/

Acondicionamiento

# Guardar condicionamiento - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo guarda un único condicionamiento en la carpeta de salida como un archivo safetensors.

Copiar páginaCopiar página

Este nodo guarda un único condicionamiento en la carpeta de salida como un archivo safetensors. El archivo guardado se puede mover a la carpeta models/embeddings y cargar posteriormente con Load Conditioning, por ejemplo, para omitir el codificador de texto. El nodo pasa el condicionamiento sin cambios, de modo que aún se puede usar más adelante en el flujo de trabajo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`conditioning`| El condicionamiento que se va a guardar. Solo se admite una única entrada de condicionamiento.| CONDITIONING| Sí| -  
`filename_prefix`| Prefijo utilizado para construir el nombre del archivo de salida. El archivo se escribe en la carpeta de salida con un contador numérico añadido. Predeterminado: `conditioning/ComfyUI`| STRING| Sí| -  
  
**Notas:**

  * Si la entrada `conditioning` contiene más de una entrada (por ejemplo, después de combinar condicionamientos), el nodo genera un error: “Save Conditioning supports a single conditioning entry, save it before combining.”
  * Las opciones de condicionamiento que son tensores, listas/tuplas de tensores, booleanos, enteros, flotantes o cadenas se guardan junto con el condicionamiento. Las opciones que son `None` se omiten. Cualquier otro tipo de opción genera un error que indica que la opción no se puede guardar.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`conditioning`| El mismo condicionamiento que se pasó, sin cambios.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveConditioning/es.md)

* * *

**Source fingerprint (SHA-256):** `07b7d2be5262c4782f237138d034b130322507e62ae8775b9c94634df8e7a3fa`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveConditioning.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveConditioning)

[Audio de referencia](https://docs.comfy.org/es/built-in-nodes/ReferenceTimbreAudio)[Aplicar Condicionamiento SeedVR2](https://docs.comfy.org/es/built-in-nodes/SeedVR2Conditioning)
