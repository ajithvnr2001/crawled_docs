---
url: https://docs.comfy.org/es/built-in-nodes/VOIDQuadmaskPreprocess/
title: VOIDQuadmaskPreprocess - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:40.995703+00:00
---

# VOIDQuadmaskPreprocess - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/VOIDQuadmaskPreprocess/

Máscara

# VOIDQuadmaskPreprocess - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo VOIDQuadmaskPreprocess prepara una máscara para inpainting con VOID convirtiéndola en una “quadmask” especial de cuatro niveles. Toma una máscara de entrada

Copiar páginaCopiar página

## 

​

Descripción general

El nodo VOIDQuadmaskPreprocess prepara una máscara para el proceso de inpaint VOID, convirtiéndola en una “cuadrimáscara” especial de cuatro niveles. Toma una máscara de entrada, dilata opcionalmente la región primaria, y luego cuantifica los valores de la máscara en cuatro niveles distintos que representan diferentes regiones semánticas (objeto primario, superposición, área afectada y fondo). Finalmente, invierte y normaliza la máscara para que los valores de salida estén en el rango [0, 1], donde 1.0 indica el área a eliminar y 0.0 indica el área a conservar.

## 

​

Entradas

Parámetro| Descripción| Tipo de Dato| Obligatorio| Rango  
---|---|---|---|---  
`mask`| La máscara de entrada que se va a preprocesar.| MASK| Sí| N/A  
`dilate_width`| Radio de dilatación para la región de la máscara primaria. Un valor de 0 significa que no se aplica dilatación. (predeterminado: 0)| INT| No| 0 a 50 (paso: 1)  
  
## 

​

Salidas

Nombre de Salida| Descripción| Tipo de Dato  
---|---|---  
`quadmask`| La cuadrimáscara preprocesada con valores en [0, 1], que representa cuatro niveles discretos: 1.0 (objeto primario a eliminar), ~0.75 (superposición de primario y afectado), ~0.50 (región afectada) y 0.0 (fondo a conservar).| MASK  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/es.md)

* * *

**Source fingerprint (SHA-256):** `12dc5ab215b80d81289942457ce2ddffcb9ec41fc738a53ca5fbf1e9181ed439`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/VOIDQuadmaskPreprocess.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/VOIDQuadmaskPreprocess)

[Umbralizar máscara](https://docs.comfy.org/es/built-in-nodes/ThresholdMask)[Posprocesar salida de SeedVR2](https://docs.comfy.org/es/built-in-nodes/SeedVR2PostProcessing)
