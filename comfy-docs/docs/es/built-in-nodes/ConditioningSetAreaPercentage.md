---
url: https://docs.comfy.org/es/built-in-nodes/ConditioningSetAreaPercentage/
title: Acondicionamiento (Establecer \u00e1rea con porcentaje) - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:40.176318+00:00
---

# Acondicionamiento (Establecer área con porcentaje) - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ConditioningSetAreaPercentage/

Transformación

# Acondicionamiento (Establecer área con porcentaje) - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ConditioningSetAreaPercentage está especializado en ajustar el área de influencia de los elementos de condicionamiento basándose en valores

Copiar páginaCopiar página

El nodo `ConditioningSetAreaPercentage` está especializado en ajustar el área de influencia de los elementos de condicionamiento basándose en valores porcentuales. Permite especificar las dimensiones y la posición del área como porcentajes del tamaño total de la imagen, junto con un parámetro de intensidad para modular la potencia del efecto de condicionamiento.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`CONDITIONING`| Representa los elementos de condicionamiento que se modificarán, sirviendo como base para aplicar ajustes de área e intensidad.| CONDITIONING  
`ancho`| Especifica el ancho del área como un porcentaje del ancho total de la imagen, influyendo en la extensión horizontal del condicionamiento sobre la imagen.| `FLOAT`  
`alto`| Determina la altura del área como un porcentaje de la altura total de la imagen, afectando la extensión vertical de la influencia del condicionamiento.| `FLOAT`  
`x`| Indica el punto de inicio horizontal del área como un porcentaje del ancho total de la imagen, posicionando el efecto de condicionamiento.| `FLOAT`  
`y`| Especifica el punto de inicio vertical del área como un porcentaje de la altura total de la imagen, posicionando el efecto de condicionamiento.| `FLOAT`  
`fuerza`| Controla la intensidad del efecto de condicionamiento dentro del área especificada, permitiendo un ajuste preciso de su impacto.| `FLOAT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`CONDITIONING`| Devuelve los elementos de condicionamiento modificados con los parámetros de área e intensidad actualizados, listos para su posterior procesamiento o aplicación.| CONDITIONING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ConditioningSetAreaPercentage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ConditioningSetAreaPercentage)

[Acondicionamiento (Establecer área)](https://docs.comfy.org/es/built-in-nodes/ConditioningSetArea)[Acondicionamiento (establecer área con porcentaje para video)](https://docs.comfy.org/es/built-in-nodes/ConditioningSetAreaPercentageVideo)
