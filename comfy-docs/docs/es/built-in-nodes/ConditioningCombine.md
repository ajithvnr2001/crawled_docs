---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningCombine/
title: Acondicionamiento (Combinar) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:40.447770+00:00
---

# Acondicionamiento (Combinar) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningCombine/

Imagen

# Acondicionamiento (Combinar) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo combina dos entradas de condicionamiento en una única salida, fusionando efectivamente su información.

Copiar páginaCopiar página

Este nodo combina dos entradas de condicionamiento en una única salida, fusionando efectivamente su información. Las dos condiciones se combinan mediante concatenación de listas.

## 

​

Entradas

Nombre del Parámetro| Descripción| Tipo de Dato  
---|---|---  
`acondicionamiento_1`| La primera entrada de condicionamiento que se va a combinar. Tiene la misma importancia que `acondicionamiento_2` en el proceso de combinación.| `CONDITIONING`  
`acondicionamiento_2`| La segunda entrada de condicionamiento que se va a combinar. Tiene la misma importancia que `acondicionamiento_1` en el proceso de combinación.| `CONDITIONING`  
  
## 

​

Salidas

Nombre del Parámetro| Descripción| Tipo de Dato  
---|---|---  
`conditioning`| El resultado de combinar `acondicionamiento_1` y `acondicionamiento_2`, que encapsula la información fusionada.| `CONDITIONING`  
  
## 

​

Escenarios de Uso

Compara los dos grupos a continuación: el lado izquierdo utiliza el nodo ConditioningCombine, mientras que el lado derecho muestra la salida normal. ![Comparar](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/ConditioningCombine/compare.jpg?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=b12d255c2a5bc25704099f40aedabf0c) En este ejemplo, las dos condiciones utilizadas en `Conditioning Combine` tienen importancia equivalente. Por lo tanto, puedes usar diferentes codificaciones de texto para el estilo de la imagen, las características del sujeto, etc., permitiendo que las características del prompt se generen de manera más completa. El segundo prompt utiliza el prompt completo combinado, pero la comprensión semántica puede codificar condiciones completamente diferentes. Usando este nodo, puedes lograr:

  * **Combinación básica de texto** : Conecta las salidas de dos nodos `CLIP Text Encode` a los dos puertos de entrada de `Conditioning Combine`
  * **Combinación compleja de prompts** : Combina prompts positivos y negativos, o codifica por separado descripciones principales y descripciones de estilo antes de fusionarlas
  * **Combinación en cadena condicional** : Se pueden usar múltiples nodos `Conditioning Combine` en serie para lograr la combinación gradual de múltiples condiciones



> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningCombine/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningCombine.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningCombine)

[Procesar imágenes por lotes](https://docs.comfy.org/es/built-in-nodes/BatchImagesNode)[Imagen vacía](https://docs.comfy.org/es/built-in-nodes/EmptyImage)
