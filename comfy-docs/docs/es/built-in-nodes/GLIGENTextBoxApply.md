---
url: https://docs.comfy.org/es/built-in-nodes/GLIGENTextBoxApply/
title: Aplicar cuadro de texto GLIGEN - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:49.630687+00:00
---

# Aplicar cuadro de texto GLIGEN - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/GLIGENTextBoxApply/

Gligen

# Aplicar cuadro de texto GLIGEN - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo GLIGENTextBoxApply está diseñado para integrar condicionamiento basado en texto en la entrada de un modelo generativo

Copiar páginaCopiar página

El nodo `GLIGENTextBoxApply` está diseñado para integrar condicionamiento basado en texto en la entrada de un modelo generativo, específicamente aplicando parámetros de cuadro de texto y codificándolos mediante un modelo CLIP. Este proceso enriquece el condicionamiento con información espacial y textual, facilitando una generación más precisa y consciente del contexto.

## 

​

Entradas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`acondicionamiento_a`| Especifica la entrada de condicionamiento inicial a la que se agregarán los parámetros del cuadro de texto y la información textual codificada. Desempeña un papel crucial en la determinación de la salida final al integrar nuevos datos de condicionamiento.| `CONDITIONING`  
`clip`| El modelo CLIP utilizado para codificar el texto proporcionado en un formato que pueda ser utilizado por el modelo generativo. Es esencial para convertir la información textual en un formato de condicionamiento compatible.| `CLIP`  
`modelo_caja_texto_gligen`| Representa la configuración específica del modelo GLIGEN que se utilizará para generar el cuadro de texto. Es crucial para garantizar que el cuadro de texto se genere según las especificaciones deseadas.| `GLIGEN`  
`texto`| El contenido de texto que se codificará e integrará en el condicionamiento. Proporciona la información semántica que guía al modelo generativo.| `STRING`  
`ancho`| El ancho del cuadro de texto en píxeles. Define la dimensión espacial del cuadro de texto dentro de la imagen generada.| `INT`  
`altura`| La altura del cuadro de texto en píxeles. Al igual que el ancho, define la dimensión espacial del cuadro de texto dentro de la imagen generada.| `INT`  
`x`| La coordenada x de la esquina superior izquierda del cuadro de texto dentro de la imagen generada. Especifica la posición horizontal del cuadro de texto.| `INT`  
`y`| La coordenada y de la esquina superior izquierda del cuadro de texto dentro de la imagen generada. Especifica la posición vertical del cuadro de texto.| `INT`  
  
## 

​

Salidas

Parámetro| Descripción| Tipo Comfy  
---|---|---  
`conditioning`| La salida de condicionamiento enriquecida, que incluye los datos de condicionamiento originales junto con los parámetros del cuadro de texto recién agregados y la información textual codificada. Se utiliza para guiar al modelo generativo en la producción de resultados conscientes del contexto.| `CONDITIONING`  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENTextBoxApply/es.md)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/GLIGENTextBoxApply.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/GLIGENTextBoxApply)

[Método de referencia del modelo de edición](https://docs.comfy.org/es/built-in-nodes/FluxKontextMultiReferenceLatentMethod)[Codificar texto CLIP para HiDream](https://docs.comfy.org/es/built-in-nodes/CLIPTextEncodeHiDream)
