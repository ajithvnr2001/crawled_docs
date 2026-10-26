---
url: https://docs.comfy.org/es/built-in-nodes/LoadLoraTextEncoder/
title: Cargar LoRA (codificador de texto) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:05.739491+00:00
---

# Cargar LoRA (codificador de texto) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/LoadLoraTextEncoder/

Cargadores

# Cargar LoRA (codificador de texto) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Aplica una pila de LoRAs a un codificador de texto CLIP en un solo nodo.

Copiar páginaCopiar página

Aplica una pila de LoRAs a un codificador de texto CLIP en un solo nodo. Cada fila de `loras` contiene un archivo LoRA, su intensidad y un interruptor de activación/desactivación, y las filas se aplican de arriba hacia abajo, de modo que cada fila aplica un parche al resultado de la fila superior. Los archivos LoRA que modifican el codificador de texto también suelen aplicarse al modelo, por lo que este nodo normalmente se combina con Load LoRA (Model) usando las mismas filas.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`clip`| El codificador de texto CLIP al que se aplicarán los LoRAs.| CLIP| Sí| -  
`loras`| Grupo ampliable de LoRAs, aplicado al codificador de texto en el orden de las filas (`loras.0`, `loras.1`, etc.). Agregue una fila por LoRA; cada fila contiene un archivo, una intensidad y un interruptor de activación/desactivación.| DYNAMIC_GROUP| Sí| 1 a 20 filas  
  
### 

​

Campos de las filas de `loras`

Cada fila repite los siguientes campos, y cada campo es obligatorio dentro de una fila enviada.

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`lora_name`| El nombre del archivo LoRA que se va a aplicar.| COMBO| Sí| Múltiples opciones disponibles  
`strength`| Con qué intensidad aplicar este LoRA al codificador de texto. `0` lo desactiva, y un valor negativo invierte el efecto. (predeterminado: 1.0)| FLOAT| Sí| -100 a 100 (paso 0.01)  
`enabled`| Desactive esta opción para omitir este LoRA sin cambiar su archivo ni su intensidad. (predeterminado: true)| BOOLEAN| Sí| false / true  
  
### 

​

Restricciones de parámetros

  * **Cantidad de filas:** se debe enviar al menos una fila y se aceptan como máximo 20 filas, por lo que el índice de fila más alto es 19.
  * **Filas omitidas:** una fila se omite cuando su archivo está vacío, cuando `enabled` está desactivado o cuando `strength` es `0`. Una intensidad negativa se pasa en lugar de omitirse.
  * **Orden de las filas:** las filas se aplican en el orden en que aparecen, y cada fila parte del codificador de texto devuelto por la fila anterior.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`CLIP`| El codificador de texto CLIP después de aplicar las filas de LoRA que no se omiten.| CLIP  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLoraTextEncoder/es.md)

* * *

**Source fingerprint (SHA-256):** `0b290d2caddc3937e962e65c70a5c99cbd4cdb40ab6f86bba8f0c270e5cebf00`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/LoadLoraTextEncoder.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/LoadLoraTextEncoder)

[Cargar LoRA (modelo)](https://docs.comfy.org/es/built-in-nodes/LoadLoraModel)[Cargar MediaPipe Face Landmarker](https://docs.comfy.org/es/built-in-nodes/LoadMediaPipeFaceLandmarker)
