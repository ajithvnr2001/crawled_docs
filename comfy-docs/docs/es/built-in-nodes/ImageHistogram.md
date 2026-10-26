---
url: https://docs.comfy.org/es/built-in-nodes/ImageHistogram/
title: Histograma de imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:56.173949+00:00
---

# Histograma de imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/ImageHistogram/

Utilidades

# Histograma de imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo ImageHistogram analiza la distribución de color de una imagen de entrada.

Copiar páginaCopiar página

El nodo ImageHistogram analiza la distribución de color de una imagen de entrada. Calcula y genera varios histogramas, que son gráficos que muestran cuántos píxeles de la imagen tienen cada valor de intensidad posible. Genera histogramas separados para los canales de color rojo, verde y azul, un histograma RGB compuesto y un histograma de luminancia basado en una fórmula estándar de brillo. Cada histograma contiene 256 bins, que cubren niveles de intensidad de 0 a 255.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Requerido| Rango  
---|---|---|---|---  
`imagen`| La imagen de entrada a analizar. El nodo procesa la primera imagen del lote.| IMAGE| Sí| N/A  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`rgb`| Un histograma compuesto que representa la intensidad de píxel promedio en los canales rojo, verde y azul.| HISTOGRAM  
`luminancia`| Un histograma del brillo percibido de la imagen, calculado mediante la fórmula estándar de luminancia ITU-R BT.709.| HISTOGRAM  
`rojo`| Un histograma que muestra la distribución de intensidades de píxel en el canal de color rojo.| HISTOGRAM  
`verde`| Un histograma que muestra la distribución de intensidades de píxel en el canal de color verde.| HISTOGRAM  
`azul`| Un histograma que muestra la distribución de intensidades de píxel en el canal de color azul.| HISTOGRAM  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/es.md)

* * *

**Source fingerprint (SHA-256):** `5020f5cedd325250a207a00950011f4b6dc19ddfe4d172665ffca4982731dd5e`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/ImageHistogram.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/ImageHistogram)

[Obtener elemento de la lista](https://docs.comfy.org/es/built-in-nodes/GetItemFromList)[Vista previa como texto](https://docs.comfy.org/es/built-in-nodes/PreviewAny)
