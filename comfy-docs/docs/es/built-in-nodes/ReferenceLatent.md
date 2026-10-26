---
url: https://docs.comfy.org/es/built-in-nodes/ReferenceLatent/
title: Latente de referencia - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:22.358435+00:00
---

# Latente de referencia - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ReferenceLatent/

Acondicionamiento

# Latente de referencia - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo establece el latente guía para un modelo de edición.

Copiar páginaCopiar página

Este nodo establece el latente guía para un modelo de edición. Toma datos de condicionamiento y una entrada latente opcional, y luego modifica el condicionamiento para incluir información de latente de referencia. Si el modelo lo admite, puedes encadenar varios nodos Set Reference Latent para establecer varias imágenes de referencia.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`condicionamiento`| Los datos de condicionamiento que se modificarán con información de latente de referencia| CONDITIONING| Sí| -  
`latente`| Datos latentes opcionales que se usarán como referencia para el modelo de edición. Si no se proporciona, el condicionamiento se devuelve sin cambios| LATENT| No| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`output`| Los datos de condicionamiento modificados que contienen información de latente de referencia| CONDITIONING  
  
## 

​

Notas

  * El latente de referencia se almacena como una lista de tensores de muestra, por lo que conectar varios nodos Set Reference Latent en secuencia agrega referencias adicionales en lugar de reemplazar la anterior.
  * Cuando no se conecta `latent`, el nodo pasa el `conditioning` entrante sin cambios.



> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/es.md)

* * *

**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ReferenceLatent.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ReferenceLatent)

[Condicionamiento PiD](https://docs.comfy.org/es/built-in-nodes/PiDConditioning)[Establecer múltiples latentes de referencia](https://docs.comfy.org/es/built-in-nodes/ReferenceMultiLatent)
