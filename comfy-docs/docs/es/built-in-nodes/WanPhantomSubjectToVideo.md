---
url: https://docs.comfy.org/es/built-in-nodes/WanPhantomSubjectToVideo/
title: Wan Phantom sujeto a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:46.462475+00:00
---

# Wan Phantom sujeto a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WanPhantomSubjectToVideo/

Phantom Subject

# Wan Phantom sujeto a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo WanPhantomSubjectToVideo prepara datos de condicionamiento y un latente para la generación de video Wan.

Copiar páginaCopiar página

El nodo WanPhantomSubjectToVideo prepara datos de condicionamiento y un latente para la generación de video Wan. Crea un video latente vacío a partir del ancho, alto, longitud y tamaño de lote solicitados y, cuando se proporcionan imágenes de referencia, las codifica con el VAE y las agrega a los condicionamientos como guía visual en la dimensión temporal.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`positivo`| Entrada de condicionamiento positivo para guiar la generación de video| CONDITIONING| Sí| -  
`negativo`| Entrada de condicionamiento negativo para evitar ciertas características| CONDITIONING| Sí| -  
`vae`| Modelo VAE utilizado para codificar las imágenes de referencia cuando se proporcionan| VAE| Sí| -  
`ancho`| Ancho del video de salida en píxeles (predeterminado: 832)| INT| Sí| 16 a MAX_RESOLUTION (paso 16)  
`alto`| Alto del video de salida en píxeles (predeterminado: 480)| INT| Sí| 16 a MAX_RESOLUTION (paso 16)  
`longitud`| Número de fotogramas en el video generado (predeterminado: 81)| INT| Sí| 1 a MAX_RESOLUTION (paso 4)  
`tamaño_lote`| Número de videos a generar simultáneamente (predeterminado: 1)| INT| Sí| 1 a 4096  
`imágenes`| Imágenes de referencia opcionales utilizadas como guía visual en la dimensión temporal| IMAGE| No| -  
  
**Nota:** Cuando se proporcionan `images`, se escalan automáticamente hacia arriba para coincidir con el `width` y el `height` especificados, y solo las primeras `length` imágenes se utilizan para el procesamiento. Cada imagen se codifica con el `vae` y se concatena a lo largo de la dimensión temporal, y solo se utilizan los canales RGB de cada imagen. Cuando no se proporcionan `images`, las tres salidas de condicionamiento se devuelven sin cambios desde los condicionamientos de entrada.

## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positive`| Condicionamiento positivo con concatenación en la dimensión temporal de las imágenes de referencia codificadas cuando se proporcionan imágenes; de lo contrario, se devuelve el `positive` de entrada sin cambios| CONDITIONING  
`negative_text`| Condicionamiento negativo con concatenación en la dimensión temporal de las imágenes de referencia codificadas cuando se proporcionan imágenes; de lo contrario, se devuelve el `negative` de entrada sin cambios| CONDITIONING  
`negative_img_text`| Condicionamiento negativo con una concatenación en la dimensión temporal puesta a cero cuando se proporcionan imágenes; de lo contrario, se devuelve el `negative` de entrada sin cambios| CONDITIONING  
`latent`| Tensor de video latente lleno de ceros con 16 canales; su número de fotogramas se deriva de `length` y sus dimensiones espaciales de `height` y `width`| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WanPhantomSubjectToVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WanPhantomSubjectToVideo)

[Wan pista a video](https://docs.comfy.org/es/built-in-nodes/WanTrackToVideo)[Crear máscara coloreada SCAIL-2](https://docs.comfy.org/es/built-in-nodes/SCAIL2ColoredMask)
