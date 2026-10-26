---
url: https://docs.comfy.org/es/built-in-nodes/MaskComposite/
title: Componer m\u00e1scara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:09.347427+00:00
---

# Componer máscara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/MaskComposite/

Máscara

# Componer máscara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo se especializa en combinar dos máscaras de entrada mediante diversas operaciones como suma, resta y operaciones lógicas

Copiar páginaCopiar página

Este nodo se especializa en combinar dos máscaras de entrada mediante diversas operaciones como suma, resta y operaciones lógicas, para producir una nueva máscara modificada. Maneja de forma abstracta la manipulación de datos de máscara para lograr efectos de enmascaramiento complejos, sirviendo como un componente crucial en flujos de trabajo de edición y procesamiento de imágenes basados en máscaras.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`destino`| La máscara principal que se modificará según la operación con la máscara de origen. Desempeña un papel central en la operación compuesta, actuando como base para las modificaciones.| MASK  
`fuente`| La máscara secundaria que se utilizará junto con la máscara de destino para realizar la operación especificada, influyendo en la máscara final de salida.| MASK  
`x`| El desplazamiento horizontal en el que se aplicará la máscara de origen sobre la máscara de destino, afectando el posicionamiento del resultado compuesto.| INT  
`y`| El desplazamiento vertical en el que se aplicará la máscara de origen sobre la máscara de destino, afectando el posicionamiento del resultado compuesto.| INT  
`operación`| Especifica el tipo de operación a aplicar entre las máscaras de destino y origen, como ‘sumar’, ‘restar’ u operaciones lógicas, determinando la naturaleza del efecto compuesto.| COMBO[STRING]  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de Dato  
---|---|---  
`mask`| La máscara resultante tras aplicar la operación especificada entre las máscaras de destino y origen, representando el resultado compuesto.| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskComposite/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/MaskComposite.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/MaskComposite)

[Invertir máscara](https://docs.comfy.org/es/built-in-nodes/InvertMask)[Previsualizar máscara](https://docs.comfy.org/es/built-in-nodes/MaskPreview)
