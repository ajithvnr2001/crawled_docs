---
url: https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-4-6/
title: Ideogram 4.6 en ComfyUI: texto a imagen nativo en 4K y edici\u00f3n - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-26T17:36:33.294429+00:00
---

# Ideogram 4.6 en ComfyUI: texto a imagen nativo en 4K y edición - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-4-6/

## En esta página

Volver arriba

  * Texto a imagen
  * Editar imagen
  * Edición precisa
    * Editar una sola región
  * Empezar



Ideogram

# Ideogram 4.6 en ComfyUI: texto a imagen nativo en 4K y edición

Copiar páginaCopiar página

Ejecuta Ideogram 4.6 en ComfyUI para texto a imagen nativo en 4K, edición de imagen y edición precisa que mantiene intactos los píxeles sin tocar.

Copiar páginaCopiar página

**Ideogram 4.6** es el modelo de generación y edición de imágenes de Ideogram con salida 4K nativa. Genera hasta 4096x4096 en una sola pasada, así que los carteles, los empaques y las fotos de producto no necesitan un upscale aparte. Precise Edit conserva los colores y el detalle de los píxeles que no pediste cambiar. Se ejecuta como una opción de modelo en tres nodos asociados de ComfyUI: **Ideogram Text to Image** , **Ideogram Edit** e **Ideogram Precise Edit**. Establece `model` en `ideogram-4.6` en cualquiera de ellos, y elige `ideogram-4.5` en la misma lista para usar el modelo anterior, que tiene [su propia página](https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-4-5).

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

## Texto a imagen

Genera una imagen a partir de un prompt de texto en un lienzo de 1K, 2K o 4K. ![Vista previa del flujo de trabajo de texto a imagen de Ideogram 4.6](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_6_t2i-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Ideogram 4.6: Text to Image” en la Biblioteca de plantillas

![Ejemplo de salida de texto a imagen de Ideogram 4.6](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_ideogram_v4_6_t2i.png) El nodo **Ideogram Text to Image** recibe:

Entrada| Valores| Efecto  
---|---|---  
`prompt`| hasta 10000 caracteres| La descripción de la imagen. También funciona una leyenda JSON estructurada, por ejemplo un `final_prompt` de una ejecución anterior  
`size`| `auto`, un preset de 1K, 2K o 4K, o `custom`| `auto` elige un lienzo que se adapta al prompt. Los presets cubren lienzos de 1K, 2K y 4K desde vertical `1:3` y `9:23` hasta horizontal `3:1` y `23:9`, por ejemplo `(2K) 2048x2048 (1:1)` y `(4K) 5120x2880 (16:9)`  
`width`, `height`| 256 a 8192, paso 32| Solo se usan cuando `size` es `custom`. Las dos dimensiones deben mantenerse dentro de 16777216 píxeles (4096x4096) y dentro de una relación de aspecto de 6:1  
`quality`| `very_low`, `low`, `medium` (predeterminado), `high`| Los niveles más altos cuestan más y tardan más. `very_low` está limitado a 4194304 píxeles (2048x2048)  
`background`| `auto` (predeterminado), `opaque`, `transparent`| `transparent` devuelve la imagen con canal alfa, `opaque` fuerza un fondo sólido y `auto` sigue el prompt  
`magic_prompt`| `auto` (predeterminado), `on`, `off`| Reescribe el prompt como una leyenda estructurada y detallada antes de generar. `off` mantiene tu redacción lo más literal posible  
`seed`| entero| Texto a imagen no es reproducible solo con la semilla, porque el prompt se reescribe en cada ejecución  
  
El nodo también entrega como salida `final_prompt`, la leyenda estructurada con la que se generó la imagen. Para reproducir una imagen, vuelve a pasar esa leyenda con `magic_prompt` en `off` y la misma semilla.

## Editar imagen

Edita o combina hasta cinco imágenes con una sola instrucción. `image_1` es la imagen que se edita; las imágenes 2 a 5 aportan referencias de diseño, material o color. Menciónalas en el prompt como `@Image1`, `@Image2`, etc. ![Vista previa del flujo de trabajo de edición de imagen de Ideogram 4.6](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_6_image_edit-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Ideogram 4.6: Image Edit” en Template Library

**Material de entrada**

## retro_crt_room.png

Cárgala en el espacio `image_1` del nodo Ideogram Edit

La plantilla arma su instrucción con un nodo **Build JSON Prompt** , así que puedes marcar una región de la imagen y añadirle una descripción. Activa [Nodes 2.0](https://docs.comfy.org/es/interface/nodes-2) si el editor no aparece. El nodo **Ideogram Edit** con `ideogram-4.6` agrega:

Entrada| Valores| Efecto  
---|---|---  
`size`| `auto` (predeterminado), `source`, un preset o `custom`| `auto` elige un lienzo de aproximadamente 2K a partir de las imágenes y el prompt. `source` conserva el tamaño de `image_1`. Un preset con una relación de aspecto distinta recompone la escena. `custom` usa el `width` y el `height` de abajo  
`width`, `height`| 256 a 8192, paso 32| Se usan solo cuando `size` es `custom`. Las dos dimensiones deben mantenerse dentro de 16777216 píxeles (4096x4096) y dentro de una relación de aspecto de 6:1  
`quality`| `very_low`, `low`, `medium` (predeterminado), `high`| Los niveles más altos cuestan más y tardan más  
`background`| `auto` (predeterminado), `opaque`, `transparent`| `transparent` devuelve la imagen con un canal alfa  
`seed`| entero| Las mismas imágenes, el prompt, las configuraciones y la semilla dan el mismo resultado  
  
Las entradas de más de 16.7 MP o de 8192 píxeles por lado se reducen antes de subirlas, y cada imagen debe quedar entre 1:6 y 6:1. La edición vuelve a renderizar toda la imagen, así que puede desplazar el encuadre y las zonas sin tocar junto con la edición. Usa Precise Edit cuando el resto de la imagen deba quedar exactamente como está.

## Edición precisa

Cambia solo lo que pide el prompt. Los píxeles que no se tocan permanecen idénticos y la salida conserva el tamaño de `image_1`, salvo que la fuente supere 16.7 MP o 8192 píxeles por lado sin una región, en cuyo caso se reduce primero. Acepta hasta cuatro imágenes de referencia además de la imagen que se edita, o tres si usas una máscara. ![Vista previa del flujo de trabajo de edición precisa de Ideogram 4.6](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_6_precise_image_edit-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Ideogram 4.6 Precise Edit” en la Biblioteca de plantillas

**Material de entrada**

## carbon_fibre_controller.png

Carga la imagen en el espacio `image_1` del nodo Ideogram Precise Edit

Precise Edit comparte con Edit los espacios de referencia, el direccionamiento `@Image1` y los controles `quality` y `seed`. No tiene control de tamaño: con una región, la salida conserva el tamaño de `image_1`, y sin región, una fuente de más de 16.7 MP o de 8192 píxeles por lado se reduce primero.

### Editar una sola región

Configura `context_window` para editar una región a resolución nativa:

`context_window`| Entrada adicional| Región que se edita  
---|---|---  
`none`| ninguna| Toda la imagen, reducida si supera 16.7 MP  
`auto` (predeterminado)| `mask`| El área que marca la máscara, o toda la imagen cuando no hay una máscara conectada  
`custom`| `context_window_bboxes`| Un rectángulo envolvente alrededor de todas las cajas conectadas (el espacio entre cajas separadas se incluye y puede editarse), por ejemplo desde el nodo **Crear Cajas Delimitadoras**  
  
Una región puede medir hasta 8192 píxeles por lado y unos 16.7 MP, con una relación máxima de 6:1. Con una región, `image_1` puede medir hasta 8192x8192 píxeles con cualquier relación de aspecto, y los píxeles fuera de la región se copian sin cambios. Úsalo para recolorear productos, cambiar materiales y hacer retoques que deban dejar intactas la iluminación, el fondo y el encuadre del resto de la foto.

## Empezar

  1. Actualiza ComfyUI a la última versión.
  2. Abre **Flujo de trabajo** > **Explorar plantillas** y busca “Ideogram 4.6”, o descarga un flujo de trabajo de la parte superior y arrástralo al lienzo.
  3. Establece `model` en `ideogram-4.6` en el nodo si comenzaste a partir de un flujo de trabajo de Ideogram 4.5.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/ideogram/ideogram-4-6.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/ideogram/ideogram-4-6)

[Ideogram Vector](https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-vector)[Ideogram 4.5](https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-4-5)
