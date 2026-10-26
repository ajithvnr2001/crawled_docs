---
url: https://docs.comfy.org/es/built-in-nodes/DisableNoise/
title: Desactivar ruido - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:43.485154+00:00
---

# Desactivar ruido - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/DisableNoise/

Ruido

# Desactivar ruido - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo proporciona una configuración de ruido vacía que desactiva la generación de ruido durante el muestreo.

Copiar páginaCopiar página

Este nodo proporciona una configuración de ruido vacía que desactiva la generación de ruido durante el muestreo. Genera un objeto de ruido especial que no contiene datos de ruido, por lo que cualquier nodo conectado a él omite las operaciones relacionadas con el ruido. También se puede buscar con el alias “zero noise”.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
 _Sin parámetros de entrada_|  Este nodo no requiere ningún parámetro de entrada.| -| -| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`NOISE`| Devuelve una configuración de ruido vacía que se puede usar para desactivar la generación de ruido en los procesos de muestreo.| NOISE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/es.md)

* * *

**Source fingerprint (SHA-256):** `b9edcda655dab3196233b6c66fdb41eb0585b153616b793016d532992b922934`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/DisableNoise.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/DisableNoise)

[Agregar ruido](https://docs.comfy.org/es/built-in-nodes/AddNoise)[Ruido aleatorio](https://docs.comfy.org/es/built-in-nodes/RandomNoise)
