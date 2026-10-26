---
url: https://docs.comfy.org/es/built-in-nodes/SaveImage/
title: Guardar imagen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:28.942775+00:00
---

# Guardar imagen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/SaveImage/

Imagen

# Guardar imagen - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo SaveImage guarda las imágenes de entrada como archivos PNG en tu directorio de salida de ComfyUI.

Copiar páginaCopiar página

El nodo SaveImage guarda las imágenes de entrada como archivos PNG en tu directorio de salida de ComfyUI. Puede incrustar metadatos del flujo de trabajo, como el prompt, en cada archivo guardado, y devuelve las imágenes sin cambios para que aún puedan ser utilizadas por otros nodos.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`imágenes`| Las imágenes que se van a guardar.| IMAGE| Sí| -  
`prefijo_nombre_archivo`| El prefijo para el archivo que se va a guardar. Puede incluir información de formato como `%date:yyyy-MM-dd%` o `%Empty Latent Image.width%` para incluir valores de los nodos (predeterminado: “ComfyUI”).| STRING| Sí| -  
  
El nodo también recibe dos entradas ocultas, `prompt` y `extra_pnginfo`, que ComfyUI rellena automáticamente con el prompt del flujo de trabajo y la información adicional del PNG. Cuando los metadatos están habilitados, esta información se incrusta como metadatos de texto en cada archivo PNG guardado. El nombre de archivo de cada imagen guardada se construye a partir de `filename_prefix`, un marcador de posición opcional `%batch_num%` que se reemplaza con la posición de la imagen en el lote, y un contador de cinco dígitos, por ejemplo `ComfyUI_00001_.png`. Las imágenes se escriben con nivel de compresión PNG 4.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`images`| Las imágenes de entrada originales, devueltas sin cambios después de guardarse en disco.| IMAGE  
`ui`| Un resultado solo para la UI que contiene la lista de archivos de imagen guardados (nombre de archivo, subcarpeta y tipo) para mostrarla en el frontend.| UI_RESULT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/es.md)

* * *

**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/SaveImage.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/SaveImage)

[Guardar WEBP animado](https://docs.comfy.org/es/built-in-nodes/SaveAnimatedWEBP)[Guardar imagen (avanzado)](https://docs.comfy.org/es/built-in-nodes/SaveImageAdvanced)
