---
url: https://docs.comfy.org/es/built-in-nodes/IdeogramPreciseEditApi/
title: Edici\u00f3n precisa de Ideogram 4.5 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:55.048451+00:00
---

# Edición precisa de Ideogram 4.5 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/es/built-in-nodes/IdeogramPreciseEditApi/

Ideogram

# Edición precisa de Ideogram 4.5 - ComfyUI Built-in Node Documentation

Copiar páginaCopiar página

Edita una imagen usando como guía un prompt de texto con la edición precisa de Ideogram 4.5: solo cambia lo que el prompt solicita

Copiar páginaCopiar página

Edita una imagen usando como guía un prompt de texto con la edición precisa de Ideogram 4.5: solo cambia lo que el prompt solicita, los píxeles no modificados permanecen idénticos y la salida conserva el tamaño de la imagen 1. La imagen 1 es la imagen que se va a editar y se pueden conectar hasta 4 imágenes adicionales como referencias.

## 

​

Entradas

Parámetro| Descripción| Tipo de datos| Obligatorio| Rango  
---|---|---|---|---  
`modelo`| Modelo a usar. (predeterminado: `"ideogram-4.5"`)| DYNAMIC_COMBO| Sí| `"ideogram-4.5"`  
`images`| Ranura ampliable: la imagen 1 es la imagen que se va a editar y las imágenes 2 a 5 son referencias opcionales (`image_1` … `image_5`). Refiérase a ellas en el prompt como @Image1, @Image2, …; una entrada en lote cuenta una vez por imagen. Cada imagen debe tener una relación de aspecto entre 1:6 y 6:1.| IMAGE| Sí| 1 a 5 imágenes  
`prompt`| Instrucciones de edición. Admite referencias al estilo @Image1 para las imágenes conectadas. (predeterminado: cadena vacía)| STRING| Sí| 1 a 10000 caracteres  
`quality`| Nivel de calidad. Los niveles más altos cuestan más y tardan más. (predeterminado: `"medium"`)| COMBO| Sí| `"very_low"`  
`"low"`  
`"medium"`  
`"high"`  
`seed`| Semilla para la generación. Las mismas imágenes, prompt, configuración y semilla producen el mismo resultado. (predeterminado: 42)| INT| Sí| 0 a 2147483647  
  
### 

​

Restricciones de parámetros

  * **Cantidad de imágenes:** al menos 1 y como máximo 5 imágenes; una entrada en lote cuenta una vez por imagen. La imagen 1 es la imagen que se va a editar y las imágenes 2 a 5 son referencias.
  * **Tamaño de salida:** el resultado conserva el tamaño de la imagen 1, por lo que este nodo no tiene entradas de tamaño, ancho ni alto.
  * **Relación de aspecto de la imagen:** cada imagen no debe ser más ancha que 6 veces su altura ni más alta que 6 veces su ancho (entre 1:6 y 6:1).
  * **Etiquetas del prompt:** `@ImageN` se compara sin distinguir entre mayúsculas y minúsculas y no debe superar el número de imágenes conectadas; el prompt no debe estar vacío ni contener solo espacios en blanco y debe tener como máximo 10000 caracteres.
  * **Escalado de subida:** las imágenes de más de aproximadamente 4 MP, o de más de 4608 px en el lado más largo, se reducen de escala antes de enviarse.
  * **Seguridad del contenido:** si el filtro de seguridad de contenido de Ideogram bloquea el resultado, el nodo lanza un error en lugar de devolver una imagen.



## 

​

Salidas

Nombre de salida| Descripción| Tipo de datos  
---|---|---  
`IMAGE`| La imagen editada como un lote, con el tamaño de la imagen 1.| IMAGE  
  
> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/es.md)

* * *

**Source fingerprint (SHA-256):** `74ba429ac93e4528e44c864ccfd3928f6c42108cfcc83577c8963a099a66f527`

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/built-in-nodes/IdeogramPreciseEditApi.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/built-in-nodes/IdeogramPreciseEditApi)

[Ideogram & Pruna P-Image](https://docs.comfy.org/es/built-in-nodes/IdeogramPImage)[Ideogram 4.5 de texto a imagen](https://docs.comfy.org/es/built-in-nodes/IdeogramTextToImageApi)
