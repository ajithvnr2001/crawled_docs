---
url: https://docs.comfy.org/es/built-in-nodes/Epsilon Scaling/
title: Escalado \u00c9psilon - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:46.609662+00:00
---

# Escalado Épsilon - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/Epsilon Scaling/

Unet

# Escalado Épsilon - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo implementa el método de escalado épsilon del artículo de investigación “Elucidating the Exposure Bias in Diffusion Models”

Copiar páginaCopiar página

Este nodo implementa el método de escalado épsilon del artículo de investigación “Elucidating the Exposure Bias in Diffusion Models” (arxiv.org/abs/2308.15321v6). Funciona escalando el ruido predicho durante el proceso de muestreo para ayudar a reducir el sesgo de exposición, lo que puede mejorar la calidad de las imágenes generadas. Esta implementación utiliza el “programa uniforme” recomendado por el artículo por su practicidad y efectividad.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`modelo`| El modelo al que se le aplicará el parche de escalado épsilon.| MODEL| Sí| -  
`factor_escala`| El factor por el cual se escala el ruido predicho. Un valor mayor que 1.0 reduce el ruido, mientras que un valor menor que 1.0 lo aumenta (predeterminado: 1.005). Este es un parámetro avanzado.| FLOAT| No| 0.5 - 1.5 (paso: 0.001)  
  
Nota: Si `scaling_factor` se establece en 0, el nodo lo reemplaza automáticamente con un valor muy pequeño (1e-9) para evitar la división por cero. El valor mínimo de 0.5 en la interfaz normalmente evita que esto ocurra.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`model`| Una versión modificada del modelo de entrada con la función de escalado épsilon aplicada a su proceso de muestreo.| MODEL  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](<https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon> Scaling/es.md)

* * *

**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/Epsilon%20Scaling.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/Epsilon%20Scaling)

[Aplicar SUPIR](https://docs.comfy.org/es/built-in-nodes/SUPIRApply)[FreeU](https://docs.comfy.org/es/built-in-nodes/FreeU)
