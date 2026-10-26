---
url: https://docs.comfy.org/es/built-in-nodes/GrowMask/
title: Expandir m\u00e1scara - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:52.389916+00:00
---

# Expandir máscara - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/GrowMask/

Máscara

# Expandir máscara - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo GrowMask está diseñado para modificar el tamaño de una máscara dada, ya sea expandiéndola o contrayéndola

Copiar páginaCopiar página

El nodo `GrowMask` está diseñado para modificar el tamaño de una máscara dada, ya sea expandiéndola o contrayéndola, con la opción de aplicar un efecto de biselado en las esquinas. Esta funcionalidad es crucial para ajustar dinámicamente los límites de las máscaras en tareas de procesamiento de imágenes, permitiendo un control más flexible y preciso sobre el área de interés.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`máscara`| La máscara de entrada que se va a modificar. Este parámetro es central para el funcionamiento del nodo, ya que sirve como base sobre la cual se expande o contrae la máscara.| MASK  
`expandir`| Determina la magnitud y dirección de la modificación de la máscara. Los valores positivos expanden la máscara, mientras que los valores negativos la contraen. Este parámetro influye directamente en el tamaño final de la máscara.| INT  
`esquinas_afiladas`| Un indicador booleano que, cuando se establece en Verdadero, aplica un efecto de biselado en las esquinas de la máscara durante la modificación. Esta opción permite transiciones más suaves y resultados visualmente atractivos.| BOOLEAN  
  
## 

​

Salidas

Parámetro| Descripción| Tipo de dato  
---|---|---  
`máscara`| La máscara modificada después de aplicar la expansión/contracción especificada y el efecto opcional de biselado en las esquinas.| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrowMask/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/GrowMask.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/GrowMask)

[Difuminar máscara](https://docs.comfy.org/es/built-in-nodes/FeatherMask)[Color de imagen a máscara](https://docs.comfy.org/es/built-in-nodes/ImageColorToMask)
