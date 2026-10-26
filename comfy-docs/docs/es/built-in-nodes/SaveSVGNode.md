---
url: https://docs.comfy.org/es/built-in-nodes/SaveSVGNode/
title: Guardar SVG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:29.865683+00:00
---

# Guardar SVG - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveSVGNode/

Imagen

# Guardar SVG - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Guarda archivos SVG en disco. Este nodo toma datos SVG como entrada y los escribe en el directorio de salida de ComfyUI

Copiar páginaCopiar página

Guarda archivos SVG en disco. Este nodo toma datos SVG como entrada y los escribe en el directorio de salida de ComfyUI, gestionando automáticamente el nombre de archivo con sufijos de contador. Cuando la información del prompt del flujo de trabajo está disponible, se incrusta directamente en el archivo SVG como un elemento de metadatos.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`svg`| Los datos SVG que se guardarán en disco| SVG| Sí| -  
`prefijo_nombre_archivo`| El prefijo del archivo que se guardará. Puede incluir información de formato, como %date:yyyy-MM-dd% o %Empty Latent Image.width%, para incluir valores de los nodos. (predeterminado: “svg/ComfyUI”)| STRING| Sí| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`svg`| Los datos SVG originales, que se pasan después de guardarlos| SVG  
`ui`| Información del archivo guardado, incluidos el nombre de archivo, la subcarpeta y el tipo para mostrarla en la interfaz de ComfyUI| DICT  
  
**Nota:** Este nodo incorpora automáticamente metadatos del flujo de trabajo (prompt e información PNG adicional) en el archivo SVG cuando están disponibles. Los metadatos se insertan como una sección CDATA dentro del elemento metadata del SVG. Los archivos se guardan usando el patrón `filename_prefix_00001_.svg`; cuando se procesa un lote, `%batch_num%` en el prefijo se reemplaza con el índice del elemento actual del lote. El nodo es un nodo de salida, por lo que produce un resultado guardado en la carpeta de salida aunque el archivo en sí no se muestre como vista previa de imagen.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/es.md)

* * *

**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveSVGNode.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveSVGNode)

[Guardar conjunto de imágenes y textos en carpeta](https://docs.comfy.org/es/built-in-nodes/SaveImageTextDataSetToFolder)[Captura de Webcam](https://docs.comfy.org/es/built-in-nodes/WebcamCapture)
