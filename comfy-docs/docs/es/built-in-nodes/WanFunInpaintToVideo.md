---
url: https://docs.comfy.org/es/built-in-nodes/WanFunInpaintToVideo/
title: Wan FunInpaint a video - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:45.630798+00:00
---

# Wan FunInpaint a video - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/WanFunInpaintToVideo/

Fun Inpaint

# Wan FunInpaint a video - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

El nodo WanFunInpaintToVideo prepara los datos de condicionamiento y latentes para la generación de video con estilo de inpainting

Copiar páginaCopiar página

El nodo WanFunInpaintToVideo prepara los datos de condicionamiento y latentes para la generación de video con estilo de inpainting, utilizando una imagen inicial y una imagen final opcionales para guiar el resultado. Funciona pasando el condicionamiento, el VAE y los fotogramas de imagen proporcionados a través de la misma lógica que se usa para la generación de video con primer y último fotograma, y devuelve el condicionamiento actualizado junto con un latente vacío para el muestreo.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`positivo`| Prompts de condicionamiento positivo para la generación de video| CONDITIONING| Sí| -  
`negativo`| Prompts de condicionamiento negativo que se deben evitar en la generación de video| CONDITIONING| Sí| -  
`vae`| Modelo VAE utilizado para codificar y decodificar los fotogramas de video| VAE| Sí| -  
`ancho`| Ancho del video de salida en píxeles (predeterminado: 832, paso: 16)| INT| Sí| 16 to MAX_RESOLUTION  
`alto`| Altura del video de salida en píxeles (predeterminado: 480, paso: 16)| INT| Sí| 16 to MAX_RESOLUTION  
`longitud`| Número de fotogramas en la secuencia de video (predeterminado: 81, paso: 4)| INT| Sí| 1 to MAX_RESOLUTION  
`tamaño_de_lote`| Número de videos a generar en un lote (predeterminado: 1)| INT| Sí| 1 a 4096  
`clip_vision_output`| Salida de visión CLIP opcional utilizada como condicionamiento para la imagen inicial| CLIP_VISION_OUTPUT| No| -  
`imagen_inicial`| Imagen del fotograma inicial opcional para la generación de video| IMAGE| No| -  
`imagen_final`| Imagen del fotograma final opcional para la generación de video| IMAGE| No| -  
  
## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`positive`| Salida de condicionamiento positivo procesada| CONDITIONING  
`negative`| Salida de condicionamiento negativo procesada| CONDITIONING  
`latent`| Representación latente del video generado| LATENT  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/es.md)

* * *

**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/WanFunInpaintToVideo.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/WanFunInpaintToVideo)

[Wan FunControl a video](https://docs.comfy.org/es/built-in-nodes/WanFunControlToVideo)[Wan HuMo imagen a video](https://docs.comfy.org/es/built-in-nodes/WanHuMoImageToVideo)
