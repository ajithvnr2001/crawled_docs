---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningSetMask/
title: Acondicionamiento (Establecer m\u00e1scara) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:40.749685+00:00
---

# Acondicionamiento (Establecer máscara) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningSetMask/

Transformación

# Acondicionamiento (Establecer máscara) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo está diseñado para modificar el condicionamiento de un modelo generativo aplicando una máscara con una intensidad específica a ciertas áreas.

Copiar páginaCopiar página

Este nodo está diseñado para modificar el condicionamiento de un modelo generativo aplicando una máscara con una intensidad específica a ciertas áreas. Permite realizar ajustes dirigidos dentro del condicionamiento, brindando un control más preciso sobre el proceso de generación.

## 

​

Entradas

### 

​

Obligatorias

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`CONDITIONING`| Los datos de condicionamiento que se modificarán. Sirven como base para aplicar la máscara y los ajustes de intensidad.| CONDITIONING  
`máscara`| Un tensor de máscara que especifica las áreas dentro del condicionamiento que se modificarán.| `MASK`  
`fuerza`| La intensidad del efecto de la máscara sobre el condicionamiento, lo que permite un ajuste fino de las modificaciones aplicadas.| `FLOAT`  
`establecer_area_cond`| Determina si el efecto de la máscara se aplica al área predeterminada o está limitado por la propia máscara, ofreciendo flexibilidad para apuntar a regiones específicas.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`CONDITIONING`| Los datos de condicionamiento modificados, con los ajustes de máscara e intensidad aplicados.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningSetMask.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningSetMask)

[Acondicionamiento (Establecer intensidad de área)](https://docs.comfy.org/es/built-in-nodes/ConditioningSetAreaStrength)[Acondicionamiento (Establecer rango de pasos)](https://docs.comfy.org/es/built-in-nodes/ConditioningSetTimestepRange)
