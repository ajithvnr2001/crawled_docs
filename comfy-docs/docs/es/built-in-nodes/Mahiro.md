---
url: https://docs.comfy.org/es/built-in-nodes/Mahiro/
title: \u00a1Mahiro es tan linda que merece una mejor funci\u00f3n de gu\u00eda!! (\u3002\u30fb\u03c9\u30fb\u3002) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:08.985231+00:00
---

# ¡Mahiro es tan linda que merece una mejor función de guía!! (。・ω・。) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Mahiro/

Experimental

# ¡Mahiro es tan linda que merece una mejor función de guía!! (。・ω・。) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo Mahiro modifica la función de guía para enfocarse más en la dirección del prompt positivo en lugar de la diferencia entre los prompts positivo y

Copiar páginaCopiar página

El nodo Mahiro modifica la función de guía para enfocarse más en la dirección del prompt positivo en lugar de la diferencia entre los prompts positivo y negativo. Crea un modelo parcheado que aplica un enfoque personalizado de escalado de guía utilizando similitud de coseno entre las salidas de eliminación de ruido condicionales e incondicionales normalizadas. Este nodo experimental ayuda a dirigir la generación más fuertemente hacia la dirección prevista del prompt positivo.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| El modelo a parchear con la función de guía modificada| MODEL| Sí|   
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`modelo_parcheado`| El modelo modificado con la función de guía Mahiro aplicada| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/es.md)

* * *

**Source fingerprint (SHA-256):** `8b4a73cfa488f97d87e5a18d5ab30765055b5d5a66c6c2f1a5f016eed2af0300`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Mahiro.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Mahiro)

[Extraer y guardar LoRA](https://docs.comfy.org/es/built-in-nodes/LoraSave)[Perp-Neg (obsoleto; usar la guía Perp-Neg)](https://docs.comfy.org/es/built-in-nodes/PerpNeg)
