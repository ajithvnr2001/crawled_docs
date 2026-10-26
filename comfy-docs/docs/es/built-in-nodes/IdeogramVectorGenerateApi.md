---
url: https://docs.comfy.org/es/built-in-nodes/IdeogramVectorGenerateApi/
title: Generar SVG vectorial de Ideogram - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:54.772130+00:00
---

# Generar SVG vectorial de Ideogram - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/IdeogramVectorGenerateApi/

Imagen

# Generar SVG vectorial de Ideogram - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Este nodo genera un SVG editable a partir de un prompt de texto con Ideogram Vector, opcionalmente guiado por hasta 5 imágenes de referencia.

Copiar páginaCopiar página

Este nodo genera un SVG editable a partir de un prompt de texto con Ideogram Vector, opcionalmente guiado por hasta 5 imágenes de referencia. El resultado es marcado vectorial en lugar de una imagen de mapa de bits, por lo que las formas permanecen editables en un editor vectorial.

## 

​

Entradas

Parámetro| Descripción| Tipo de dato| Obligatorio| Rango  
---|---|---|---|---  
`model`| Modelo a utilizar. Predeterminado: `"ideogram-vector-1"`.| DYNAMIC_COMBO| Sí| `"ideogram-vector-1"`  
`images`| Imágenes de referencia opcionales. La imagen 1 es la fuente principal y las imágenes 2 a 5 son referencias adicionales; menciónalas en el prompt como `@Image1`, `@Image2`, etc. Una entrada por lotes cuenta una vez por imagen.| AUTOGROW| No| 0 a 5 imágenes  
`prompt`| Descripción del SVG. Admite referencias al estilo `@Image1` para las imágenes de entrada.| STRING| Sí| 1 a 9500 caracteres  
`aspect_ratio`| `"auto"` sigue a la imagen 1, o al prompt cuando no hay ninguna imagen conectada. Predeterminado: `"auto"`.| COMBO| Sí| `"auto"`  
`"1:3"`  
`"1:2"`  
`"9:16"`  
`"10:16"`  
`"2:3"`  
`"3:4"`  
`"4:5"`  
`"1:1"`  
`"5:4"`  
`"4:3"`  
`"3:2"`  
`"16:10"`  
`"16:9"`  
`"2:1"`  
`"3:1"`  
`quality`| Nivel de calidad. Los niveles más altos cuestan más y tardan más. Predeterminado: `"medium"`.| COMBO| Sí| `"low"`  
`"medium"`  
`"high"`  
`seed`| Semilla para la generación. El mismo prompt, las mismas imágenes, la misma configuración y la misma semilla producen el mismo SVG. Predeterminado: 42.| INT| Sí| 0 a 2147483647  
  
**Restricciones:**

  * El prompt debe contener entre 1 y 9500 caracteres.
  * `images` acepta como máximo 5 imágenes, contadas por imagen cuando la entrada se envía por lotes, y cada imagen debe tener una relación de aspecto entre 1:6 y 6:1.
  * Las imágenes cuyo lado más largo supere los 2048 píxeles se reducen de escala antes de la carga.
  * Hacer referencia a una imagen que no está conectada, como `@Image4` con solo dos imágenes proporcionadas, genera un error.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de dato  
---|---|---  
`SVG`| El SVG generado como marcado vectorial editable.| SVG  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorGenerateApi/es.md)

* * *

**Source fingerprint (SHA-256):** `5bd24ad48d6c26daf43f84544a9c22a18961dea645799104591f3785a851f819`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/IdeogramVectorGenerateApi.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/IdeogramVectorGenerateApi)

[Imagen Flux.1 Kontext [pro]](https://docs.comfy.org/es/built-in-nodes/FluxKontextProImageNode)[Imagen a SVG de Ideogram Vector](https://docs.comfy.org/es/built-in-nodes/IdeogramVectorImageToSVGApi)
