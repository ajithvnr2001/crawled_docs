---
url: https://docs.comfy.org/es/built-in-nodes/LoopProgress/
title: LoopProgress - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:06.239297+00:00
---

# LoopProgress - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoopProgress/

Avanzado

# LoopProgress - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

LoopProgress es un nodo auxiliar solo para desarrollo que informa el progreso de un bucle a la interfaz del servidor de ComfyUI.

Copiar páginaCopiar página

LoopProgress es un nodo auxiliar solo para desarrollo que informa el progreso de un bucle a la interfaz del servidor de ComfyUI. En cada ejecución envía el texto “Iteration X / Y” al cliente y devuelve la posición actual de la iteración sin cambios, lo que le permite situarse en línea dentro de un bucle sin alterar el flujo de datos.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`start_id`| Identificador de la instancia de prompt/bucle a la que pertenece el mensaje de progreso. Se utiliza el primer elemento de la lista proporcionada para dirigir el texto de progreso a la ejecución en curso correcta.| STRING| Sí| -  
`position`| La posición actual de la iteración (índice). El primer elemento de la lista proporcionada se utiliza en el mensaje de progreso y también se devuelve como salida.| INT| Sí| -  
`total`| El número total de iteraciones. Se utiliza junto con `position` para construir el mensaje de progreso “Iteration X / Y”.| INT| Sí| -  
  
Nota: este nodo está declarado con entradas de lista (`is_input_list=True`) y acepta todas las entradas, por lo que cada valor conectado se trata como una lista y solo se lee su primer elemento. El nodo siempre se ejecuta (su huella de entrada es fija), por lo que se vuelve a ejecutar en cada pasada del bucle.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`position`| La posición actual de la iteración, transferida sin cambios desde la entrada `position`.| INT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopProgress/es.md)

* * *

**Source fingerprint (SHA-256):** `505ba814b93533679516b4f4239f5eee0dbac125d7ea16746c6cdbb7a68f803d`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoopProgress.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoopProgress)

[LoopIteration](https://docs.comfy.org/es/built-in-nodes/LoopIteration)[LoopResult](https://docs.comfy.org/es/built-in-nodes/LoopResult)
