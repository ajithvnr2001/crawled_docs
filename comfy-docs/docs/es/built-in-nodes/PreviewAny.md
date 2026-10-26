---
url: https://docs.comfy.org/es/built-in-nodes/PreviewAny/
title: Vista previa como texto - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:18.655196+00:00
---

# Vista previa como texto - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/PreviewAny/

Utilidades

# Vista previa como texto - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

PreviewAny convierte cualquier valor de entrada en texto legible para que puedas inspeccionarlo.

Copiar páginaCopiar página

PreviewAny convierte cualquier valor de entrada en texto legible para que puedas inspeccionarlo. Las cadenas se conservan sin cambios, los números y booleanos se convierten en texto plano, y otros tipos de datos se serializan a JSON cuando es posible (recurriendo a su forma de cadena simple si la serialización falla). El texto resultante se muestra en la interfaz de usuario y también se devuelve como una salida de tipo cadena para su procesamiento posterior.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`fuente`| Acepta cualquier tipo de datos de entrada para su visualización en la vista previa. Si no se proporciona un valor, la vista previa muestra ‘None’.| ANY| Sí| Cualquier tipo de datos  
  
**Comportamiento de conversión**

  * Los valores de tipo STRING se muestran exactamente como se proporcionan.
  * Los valores de tipo INT, FLOAT o BOOLEAN se convierten a texto plano.
  * Cualquier otro valor no vacío se convierte a texto JSON con una indentación de 4 espacios; si esa conversión falla, el nodo recurre a la forma de texto plano del valor. Si eso también falla, la vista previa muestra el mensaje ‘source exists, but could not be serialized.’
  * Si no se conecta ningún valor o el valor está vacío, la vista previa muestra ‘None’.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`result`| El valor de entrada convertido a formato de texto. El mismo texto también se muestra en la interfaz de usuario.| STRING  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/es.md)

* * *

**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/PreviewAny.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/PreviewAny)

[Histograma de imagen](https://docs.comfy.org/es/built-in-nodes/ImageHistogram)[Selector de resolución](https://docs.comfy.org/es/built-in-nodes/ResolutionSelector)
