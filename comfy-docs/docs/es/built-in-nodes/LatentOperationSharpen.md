---
url: https://docs.comfy.org/es/built-in-nodes/LatentOperationSharpen/
title: Operaci\u00f3n de enfoque de latente - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:03.705586+00:00
---

# Operación de enfoque de latente - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LatentOperationSharpen/

Operaciones

# Operación de enfoque de latente - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo LatentOperationSharpen crea una operación de nitidez para representaciones latentes utilizando un kernel basado en Gaussian.

Copiar páginaCopiar página

El nodo LatentOperationSharpen crea una operación de nitidez para representaciones latentes utilizando un kernel basado en Gaussian. Normaliza los datos latentes, aplica un kernel de nitidez personalizado mediante convolución y luego restaura la luminancia original, lo que realza los detalles y los bordes en la representación del espacio latente.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`radio_afilado`| El radio del kernel de nitidez, que controla el tamaño del área utilizada para el enfoque (predeterminado: 9)| INT| Sí| 1-31  
`sigma`| La desviación estándar del kernel gaussiano utilizado para construir el kernel de nitidez (predeterminado: 1.0)| FLOAT| Sí| 0.1-10.0  
`alfa`| El factor de intensidad del enfoque; valores más altos producen un efecto de nitidez más fuerte (predeterminado: 0.1)| FLOAT| Sí| 0.0-5.0  
  
Las tres entradas son parámetros avanzados y tienen valores predeterminados, por lo que el nodo se puede usar sin modificarlos. Este nodo está marcado como experimental.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`operation`| Devuelve una operación de nitidez que se puede aplicar a los datos latentes| LATENT_OPERATION  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/es.md)

* * *

**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LatentOperationSharpen.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LatentOperationSharpen)

[Mezcla de operación latent](https://docs.comfy.org/es/built-in-nodes/LatentOperationBlend)[Operación latente tonemap Reinhard](https://docs.comfy.org/es/built-in-nodes/LatentOperationTonemapReinhard)
