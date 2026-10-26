---
url: https://docs.comfy.org/es/tutorials/partner-nodes/recraft/recraft-v4/
title: Generaci\u00f3n de im\u00e1genes y vectores con Recraft V4 y V4.1 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:54.883300+00:00
---

# Generación de imágenes y vectores con Recraft V4 y V4.1 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/recraft/recraft-v4/

## En esta página

Volver arriba

  * Qué hace bien Recraft V4
  * Salidas de ejemplo
  * Flujo de trabajo de Recraft V4 texto a imagen
    * Pasos para ejecutar el flujo de trabajo
    * Muestra de imágenes
  * Flujo de trabajo de texto a vector con Recraft V4
    * Muestra de vectores
  * Flujo de trabajo de texto a imagen con Recraft V4.1
    * Pasos para ejecutar el flujo de trabajo
  * Flujo de trabajo de texto a imagen con Recraft V4.1 Flash
    * Pasos para ejecutar el flujo de trabajo
  * Flujo de trabajo de texto a vector con Recraft V4.1
  * Estilos de Recraft V4
    * Flujo de trabajo de referencia de estilo de Recraft V4
  * Notas adicionales



Recraft

# Generación de imágenes y vectores con Recraft V4 y V4.1 en ComfyUI

Copiar páginaCopiar página

Genera imágenes profesionales y vectores listos para producción con Recraft V4 y V4.1 en ComfyUI

Copiar páginaCopiar página

Recraft V4 es un modelo de generación de imágenes creado para el trabajo de diseño profesional. Se desarrolló en colaboración con diseñadores y se optimizó para la composición, la iluminación, las relaciones de color y el realismo de los materiales. Recraft V4.1 es la última actualización de la familia de modelos, diseñada para interpretar prompts cortos y producir un fotorrealismo natural en una variedad de estilos de salida. Recraft V4.1 Flash es el modelo más rápido y de menor costo de la familia V4: genera una imagen por ejecución a partir de un prompt corto y no admite estilos.

## 

​

Qué hace bien Recraft V4

  * **Ráster y vector en un solo modelo** : imágenes fotorrealistas, ilustraciones estilizadas y SVG listos para producción con el mismo modelo
  * **Mejor detalle** : texturas más limpias, iluminación más precisa y geometría más ajustada. Se mantiene en escenas complejas
  * **Rostros y anatomía que funcionan** : proporciones y expresiones confiables, incluso con varios sujetos o poses de acción
  * **Renderizado de texto** : texto legible para señalización, empaques e infografías. Maneja bien frases cortas y de longitud media
  * **Salida SVG** : vectores editables con líneas limpias y segmentación de color adecuada. Salida vectorial con calidad de producción
  * **Precisión del prompt** : sigue de cerca las indicaciones creativas detalladas, incluidas relaciones espaciales, materiales y reflejos
  * **V4 Pro** : el mismo modelo, mayor resolución. Salidas a 2048×2048 para trabajos de impresión y gran formato



## 

​

Salidas de ejemplo

Fotografía editorial a partir de un prompt detallado: ![Ejemplo de fotografía urbana](https://substack-post-media.s3.amazonaws.com/public/images/9fe39ca3-b0ba-4f26-aa26-b3eaa11185de_1792x1024.png) Salida de ilustración vectorial, lista para editar como SVG: ![Ilustración de azotea](https://substack-post-media.s3.amazonaws.com/public/images/571c5214-5c7f-43f9-81c4-80cad1e5578b_1792x1024.png) Texto a imagen con Recraft V4.1, que produce un fotorrealismo natural a partir de un prompt corto: ![Salida de Texto a imagen de Recraft V4.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_recraft_v4_1_t2i.png)

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

Flujo de trabajo de Recraft V4 texto a imagen

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Recraft V4 Text to Image” en la Biblioteca de plantillas

![Vista previa del flujo de trabajo Recraft V4 texto a imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_t2i-1.webp)

### 

​

Pasos para ejecutar el flujo de trabajo

  1. (Opcional) Modifica el nodo `Recraft Style` para controlar el estilo visual
  2. (Opcional) Edita el parámetro `prompt` en el nodo `Recraft Text to Image`
  3. (Opcional) Cambia el parámetro `size` para obtener dimensiones de salida distintas
  4. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen
  5. Después de que la API devuelva el resultado, visualiza la imagen generada en el nodo `Save Image`



### 

​

Muestra de imágenes

![Ejemplo de fotografía callejera](https://substack-post-media.s3.amazonaws.com/public/images/9fe39ca3-b0ba-4f26-aa26-b3eaa11185de_1792x1024.png) _Foto editorial callejera de cuerpo completo de una persona joven con una franela vintage oversize de Fear of God sobre una sudadera con capucha Pyrex Vision descolorida, denim desgastado de pierna ancha, una gorra snapback original Just Don con visera de pitón y unas Nike Dunk Low gastadas. Capturada en una acera áspera de Brooklyn, hora dorada, grano de película de 35 mm._ ![Editorial hypebeast](https://substack-post-media.s3.amazonaws.com/public/images/9fd968f1-f5f9-42a9-973d-74bd163babde_2560x1664.png) _Toma de outfit completo: sudadera con capucha de camuflaje en azul eléctrico y coral, joggers de camuflaje a juego, reloj G-Shock blanco, bolso bandolera técnico negro mate y unas New Balance 550 en tono crema. Fondo de estacionamiento de concreto, iluminación fluorescente cenital intensa que proyecta sombras marcadas._ ![Toma de acción](https://substack-post-media.s3.amazonaws.com/public/images/a8643f80-8cc4-4246-a95a-bed1f9ee10f1_2560x1664.png) _Lente ojo de pez, tomada desde dentro de una piscina de concreto vacía: un chico con una bomber de borrego y una capa exterior de PVC transparente está en pleno kickflip en el borde de la piscina, justo encima de la cámara, la tabla se separa de sus pies y su outfit por capas se infla con el aire y se abre, dejando ver la camiseta de hockey que lleva debajo._

## 

​

Flujo de trabajo de texto a vector con Recraft V4

Recraft V4 puede generar directamente salidas vectoriales SVG listas para producción. Esto resulta útil para logotipos, iconos, recursos de marca o cualquier elemento que necesite escalar. Las salidas SVG son compatibles con Illustrator, Figma y Sketch.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descargar JSON o buscar “Recraft V4 Text to Vector” en la biblioteca de plantillas

![Vista previa del flujo de trabajo de texto a vector con Recraft V4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_text_to_vector-1.webp)

### 

​

Muestra de vectores

![Ilustración de azotea](https://substack-post-media.s3.amazonaws.com/public/images/571c5214-5c7f-43f9-81c4-80cad1e5578b_1792x1024.png) _Un grupo de amigos descansando en una azotea al atardecer, con luces colgantes encima, una persona atendiendo una pequeña parrilla, otra rasgueando un ukelele y un perro dormitando sobre una manta junto a una hielera: ilustración cálida, relajada y retro de estilo de vida_ ![Ilustración de boombox](https://substack-post-media.s3.amazonaws.com/public/images/748f04c7-50b9-433d-93cb-c619984c8e89_1792x1024.png) _Un boombox de neón gigante reproduciendo música a todo volumen, con rayos y ondas de sonido saliendo disparados de los altavoces, cintas de casete derritiéndose que giran a su alrededor y un par de auriculares de gran tamaño colgados encima: audaz, caótico y electrizante_ ![Calcomanía de gatito](https://substack-post-media.s3.amazonaws.com/public/images/3ddce7b4-8f37-4256-bd93-2e5796dfacca_1024x1024.png) _Adorable calcomanía de un gatito: el gatito usa ComfyUI en una laptop diminuta_

## 

​

Flujo de trabajo de texto a imagen con Recraft V4.1

Genera imágenes fotorrealistas e ilustrativas a partir de prompts de texto con Recraft V4.1, y produce una imagen de alta calidad por generación. El modelo interpreta prompts cortos y ofrece resultados fotorrealistas naturales.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Recraft V4.1” en la Biblioteca de plantillas

![Vista previa del flujo de trabajo de texto a imagen con Recraft V4.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_1_t2i-1.webp) ![Salida de texto a imagen de Recraft V4.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_recraft_v4_1_t2i.png)

### 

​

Pasos para ejecutar el flujo de trabajo

  1. (Opcional) Modifica el nodo `Recraft Style` para controlar el estilo visual
  2. (Opcional) Edita el parámetro `prompt` del nodo `Recraft Text to Image`
  3. (Opcional) Cambia el parámetro `size` para obtener diferentes dimensiones de salida
  4. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen
  5. Cuando la API devuelva el resultado, consulta la imagen generada en el nodo `Save Image`



## 

​

Flujo de trabajo de texto a imagen con Recraft V4.1 Flash

Genera una imagen por ejecución con Recraft V4.1 Flash, el modelo más rápido y de menor costo de la familia V4. Es compatible con los preajustes de tamaño estándar de V4 y no tiene controles de estilo, así que resulta ideal para generación de alto volumen, iteración rápida y exploración ágil de conceptos.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Recraft 4.1 flash” en la biblioteca de plantillas

![Salida de texto a imagen de Recraft V4.1 Flash](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_recraft_v4_1_flash_t2i.png)

### 

​

Pasos para ejecutar el flujo de trabajo

  1. (Opcional) Edita el parámetro `prompt` en el nodo `Recraft V4 Text to Image`
  2. (Opcional) Establece `model` en `recraftv4_1_flash`
  3. (Opcional) Cambia el parámetro `size` para obtener distintas dimensiones de salida
  4. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen
  5. Cuando la API devuelva el resultado, consulta la imagen generada en el nodo `Save Image`



## 

​

Flujo de trabajo de texto a vector con Recraft V4.1

Genera un logo vectorial limpio y plano a partir de un prompt de texto con Recraft V4.1, que produce una única salida SVG escalable y no requiere archivos de entrada. Ideal para branding y diseño de logos, proyectos de ilustración vectorial y gráficos de color plano consistentes.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Recraft V4.1” en la Biblioteca de plantillas

![Vista previa del flujo de trabajo Recraft V4.1 texto a vector](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_1_text_to_vector-1.webp)

## 

​

Estilos de Recraft V4

Los nodos de generación de Recraft V4 y V4.1 pueden aplicar un estilo reutilizable. Pasa un `style_id` o conecta imágenes de referencia de estilo para mantener cada resultado consistente con el mismo aspecto.

  * **Recraft V4 Create Style** : Crea un estilo reutilizable a partir de 1 a 10 imágenes de referencia y devuelve un `style_id`. El estilo funciona con todos los modelos Recraft V4 y V4.1 del mismo tipo de salida (raster o vector), y el tamaño total de las imágenes de referencia está limitado a 10 MB
  * **Modelos que requieren estilo** : Los modelos `recraftv4_styles` y `recraftv4_styles_pro`, junto con sus variantes vectoriales, siempre requieren un `style_id` o imágenes de referencia de estilo. Los demás modelos V4 aceptan estilos como entrada opcional
  * **Entradas de estilo** : No puedes combinar `style_id` y `style_references` en una misma ejecución. Las imágenes de referencia de estilo se cobran además de la generación, y el nodo devuelve el `style_id` creado para reutilizarlo
  * **Coincidencia de estilo** : `precise` reproduce el estilo en detalle, `flexible` coincide con el aspecto general



### 

​

Flujo de trabajo de referencia de estilo de Recraft V4

Genera imágenes con el estilo de una o más imágenes de referencia con Recraft V4 Styles. La plantilla crea un `style_id` reutilizable a partir de cuatro imágenes de referencia con el nodo Recraft V4 Create Style y luego lo introduce en una generación de Recraft V4 texto a imagen. No se requiere entrenamiento ni ajuste fino: el estilo captura la textura, la composición y el renderizado solo a partir de las referencias. ![Vista previa del flujo de trabajo de referencia de estilo de Recraft V4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_style_reference-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Recraft V4: Style-Reference Image Generation” en la biblioteca de plantillas

## Referencia de estilo 1: recraft_v4_style_ref_1.png

Referencia de estilo para el flujo de trabajo, o usa tus propias imágenes.

## Referencia de estilo 2: recraft_v4_style_ref_2.png

Referencia de estilo para el flujo de trabajo, o usa tus propias imágenes.

## Referencia de estilo 3: recraft_v4_style_ref_3.png

Referencia de estilo para el flujo de trabajo, o usa tus propias imágenes.

## Referencia de estilo 4: recraft_v4_style_ref_4.png

Referencia de estilo para el flujo de trabajo, o usa tus propias imágenes.

El ID de estilo creado se guarda en `ComfyUI/output/Recraft_Style_v4/`, y puedes personalizar la ubicación de salida con el `filename_prefix` del nodo de guardado. Reutiliza el mismo ID de estilo en generaciones futuras para mantener el aspecto consistente entre ejecuciones.

## 

​

Notas adicionales

  * **Recraft Style** : ofrece varios estilos predefinidos, como fotos realistas, arte digital y diseños de logotipos
  * **Parámetro Seed** : solo se usa para determinar si el nodo debe ejecutarse de nuevo; el resultado real de la generación no se ve afectado por el valor de la semilla



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/recraft/recraft-v4.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/recraft/recraft-v4)

[Qwen Image 3 0 Pro](https://docs.comfy.org/es/tutorials/partner-nodes/qwen/qwen-image-3-0-pro)[Recraft Text To Image](https://docs.comfy.org/es/tutorials/partner-nodes/recraft/recraft-text-to-image)
