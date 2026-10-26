---
url: https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-4-5/
title: Ideogram 4.5 en ComfyUI: texto a imagen y edici\u00f3n - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:50.679680+00:00
---

# Ideogram 4.5 en ComfyUI: texto a imagen y edición - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-4-5/

## En esta página

Volver arriba

  * Texto a imagen
  * Editar imagen
  * Edición precisa



Ideogram

# Ideogram 4.5 en ComfyUI: texto a imagen y edición

Copiar páginaCopiar página

Usa los nodos asociados de Ideogram 4.5 en ComfyUI para texto a imagen, edición de imagen y edición precisa que conserva intactos los píxeles.

Copiar páginaCopiar página

**Ideogram 4.5** es el modelo más reciente de la familia y el modelo de edición más preciso de Ideogram: solo cambia lo que el prompt indica, así que las ediciones repetidas conservan los colores, las texturas y los detalles en su sitio. Llega a ComfyUI como tres nodos asociados que se facturan por imagen a través de la misma cuenta de Comfy que el resto de los nodos asociados. Ideogram 4.0 conserva su propia página: [Ideogram 4.0 en ComfyUI](https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-v4).

Para usar los Nodos asociados, debes asegurarte de haber iniciado sesión correctamente y de estar utilizando un entorno de red permitido. Consulta la sección [Descripción general de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/overview) de la documentación para conocer los requisitos específicos de uso de los Nodos asociados.

  * Usuarios locales

  * Usuarios de Cloud




Asegúrate de que tu ComfyUI esté actualizado.

  * [Descargar ComfyUI](https://www.comfy.org/download)
  * [Guía de actualización](https://docs.comfy.org/es/installation/update_comfyui)

Los flujos de trabajo de esta guía se encuentran en las [Plantillas de flujos de trabajo](https://docs.comfy.org/es/interface/features/template). Si no los encuentras en las plantillas, es posible que tu ComfyUI esté desactualizado.Si faltan nodos al cargar un flujo de trabajo, estas son las posibles razones:

  1. No estás usando la última versión de ComfyUI (versión nocturna)
  2. Algunos nodos fallaron al importarse durante el inicio



  * [Cloud](https://cloud.comfy.org) se actualizará después del lanzamiento estable de ComfyUI.

Por lo tanto, si notas que falta algún nodo central en este documento, puede deberse a que los nuevos nodos centrales aún no se han publicado en la última versión estable. Espera al próximo lanzamiento estable.

## 

​

Texto a imagen

Genera una imagen a partir de un prompt de texto, con el tamaño de lienzo y el nivel de calidad que elijas. ![Vista previa del flujo de trabajo Texto a imagen de Ideogram 4.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Ideogram 4.5: Text to Image” en la Biblioteca de plantillas

![Salida de ejemplo del flujo de trabajo Texto a imagen de Ideogram 4.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_ideogram_v4_5_t2i.png) El nodo **Ideogram 4.5 Text to Image** recibe:

Entrada| Valores| Efecto  
---|---|---  
`prompt`| hasta 10000 caracteres| La descripción de la imagen. Una leyenda JSON estructurada también funciona aquí, por ejemplo un `final_prompt` de una ejecución anterior  
`size`| `auto` o un preajuste de 1K o 2K| `auto` deja que el modelo elija un lienzo que se adapte al prompt. Los preajustes cubren tanto 1K como 2K y van de `1:1` a `23:9`, por ejemplo `(2K) 2048x2048 (1:1)` y `(1K) 1280x720 (16:9)`  
`quality`| `low`, `medium` (predeterminado), `high`| Los niveles más altos cuestan más y tardan más  
`magic_prompt`| `auto` (predeterminado), `on`, `off`| Reescribe el prompt como una leyenda estructurada y detallada antes de generar. `off` mantiene tu redacción lo más literal posible  
`seed`| entero| Texto a imagen no es reproducible solo con la semilla, porque el prompt se reescribe en cada ejecución  
  
El nodo también genera `final_prompt`, la leyenda estructurada con la que se generó la imagen. Para reproducir una imagen, pasa esa leyenda de nuevo con `magic_prompt` en `off` y la misma semilla.

## 

​

Editar imagen

Edita o combina hasta cinco imágenes con una sola instrucción. `image_1` es la imagen que editas; las imágenes 2 a 5 aportan referencias de diseño, material o color. Menciónalas en el prompt como `@Image1`, `@Image2`, etc. ![Vista previa del flujo de trabajo de edición de imagen de Ideogram 4.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Ideogram 4.5: Image Edit” en la Biblioteca de plantillas

**Material de entrada**

## interior_orange_sofa.png

Carga esta imagen en la ranura `image_1` del nodo Ideogram 4.5 Edit

La plantilla construye su instrucción con un nodo **Build JSON Prompt** , así que puedes marcar una región de la imagen y añadirle una indicación, por ejemplo, “elimínalo”. Activa [Nodes 2.0](https://docs.comfy.org/es/interface/nodes-2) si el editor no aparece. El nodo **Ideogram 4.5 Edit** añade:

Entrada| Valores| Efecto  
---|---|---  
`size`| `auto` (predeterminado), `source`, un preajuste o `custom`| `auto` elige un lienzo de unos 2K a partir de las imágenes y el prompt. `source` mantiene el tamaño de `image_1`. Un preajuste con una relación de aspecto distinta recompone la escena. `custom` usa el `width` y el `height` que aparecen a continuación  
`width`, `height`| 256 a 4608, paso 32| Solo se usan cuando `size` es `custom`. En conjunto, las dos dimensiones no deben superar los 4194304 píxeles (2048x2048) ni una relación de aspecto de 6:1  
`quality`| `very_low`, `low`, `medium` (predeterminado), `high`| Los niveles más altos cuestan más y tardan más  
`seed`| entero| Las mismas imágenes, el mismo prompt, las mismas configuraciones y la misma semilla dan el mismo resultado  
  
Puedes conectar hasta cinco imágenes en total. Las entradas de más de unos 4 MP se reducen antes de subirlas, y cada imagen debe tener una relación de aspecto entre 1:6 y 6:1. La edición vuelve a renderizar toda la imagen, por lo que el encuadre y las zonas sin editar pueden cambiar junto con la edición. Usa Precise Edit cuando el resto de la imagen tenga que permanecer exactamente como está.

## 

​

Edición precisa

Cambia solo lo que pida el prompt. Los píxeles sin tocar permanecen idénticos y la salida conserva el tamaño de `image_1`. Acepta hasta cuatro imágenes de referencia además de la imagen que se edita. ![Vista previa del flujo de trabajo de edición precisa de Ideogram 4.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_precise_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Ideogram 4.5: Precise Edit” en la Biblioteca de plantillas

**Material de entrada**

## redhair_girl_portrait.png

Carga en la ranura `image_1` del nodo Ideogram 4.5 Precise Edit

La edición precisa comparte las ranuras de referencia, el direccionamiento `@Image1` y los controles `quality` y `seed` con el modo Edit. No tiene control de tamaño, porque la salida siempre coincide con el tamaño de `image_1`. La plantilla también genera su instrucción con el nodo **Build JSON Prompt**. Úsala para recolorear productos, cambiar materiales y hacer retoques que deban conservar la iluminación, el fondo y el encuadre del resto de la foto.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/ideogram/ideogram-4-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/ideogram/ideogram-4-5)

[Ideogram Vector](https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-vector)[Ideogram P Image](https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-p-image)
