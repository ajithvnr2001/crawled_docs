---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-5/
title: Seedream 5.5 en ComfyUI: texto a imagen y edici\u00f3n de imagen - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:12:12.790833+00:00
---

# Seedream 5.5 en ComfyUI: texto a imagen y edición de imagen - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-5/

## En esta página

Volver arriba

  * Qué hace
  * Seedream 5.5: texto a imagen
  * Editar imágenes con Seedream 5.5
  * Tamaño y transparencia
  * Empezar



ByteDance

# Seedream 5.5 en ComfyUI: texto a imagen y edición de imagen

Copiar páginaCopiar página

Ejecuta Seedream 5.5 de ByteDance en ComfyUI con la API de socios: texto a imagen, edición con varias referencias y salida transparente nativa de 1K a 2K.

Copiar páginaCopiar página

Seedream 5.5 es el modelo de imágenes de ByteDance Seed, lanzado el 9 de noviembre de 2026 como sucesor de Seedream 5.0 Pro. Se ejecuta en ComfyUI a través del API de socios, así que no hay nada que descargar: cada ejecución se factura a tu cuenta de Comfy API. Tres cosas cambiaron respecto a 5.0 Pro. Las zonas sin editar se mantienen a nivel de píxel a lo largo de cadenas de edición largas, así que una imagen sobrevive docenas de rondas sin desviación de color ni deformación de los rostros. El modelo devuelve transparencia real en lugar de un fondo falso. Y el texto dentro de la imagen se renderiza de forma más fiable, algo que importa para carteles, embalajes y pegatinas. ByteDance dice que habrá una versión Pro de la serie 5.5.

## Qué hace

  * **Texto a imagen** : un prompt de entrada y una imagen de salida, en cualquier preajuste de 1K a 2K
  * **Edición de imagen** : hasta 10 imágenes de referencia y una salida; la salida conserva la resolución de la fuente cuando vuelves a introducir el tamaño
  * **Salida transparente** : elige `transparent` en el nodo y la imagen devuelta incluye un canal alfa
  * **Tipografía** : las leyendas, las etiquetas y el texto de los titulares se dibujan dentro de la imagen, sin un paso aparte para superponer
  * **Una imagen por ejecución** : la generación por lotes y la secuencial no están disponibles para este modelo



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

## Seedream 5.5: texto a imagen

Ingresa un prompt y recibes una imagen. La plantilla se abre en `(1K) 1024x1024 (1:1)`. ![Vista previa del flujo de trabajo de texto a imagen de Seedream 5.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_5_t2i-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Seedream 5.5” en la Biblioteca de plantillas

## Editar imágenes con Seedream 5.5

Carga una imagen, describe el cambio y repite lo que debe permanecer igual. La plantilla lee el tamaño de la fuente con `Get Image Size` y lo vuelve a introducir, así el resultado sale con la resolución y la relación de aspecto de la fuente. ![Vista previa del flujo de trabajo para editar imágenes con Seedream 5.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_5_image_edit-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Seedream 5.5” en la Biblioteca de plantillas

**Materiales de entrada** Descarga la imagen de muestra para probar la edición tal como viene:

## api_bytedance_seedream_5_5_image_edit_input.png

Retrato de origen que edita la plantilla

## Tamaño y transparencia

El preajuste de tamaño abarca 1K, 1.5K y 2K en ocho relaciones de aspecto cada uno, además de `Custom`. El ancho y alto personalizados aceptan de 240 a 8594 px, pero el modelo solo genera entre 0.92 MP y 4.62 MP, así que un lienzo pequeño se rechaza antes de que se envíe la solicitud. La relación de aspecto debe mantenerse entre 1:16 y 16:1. Con el límite de 4.62 MP, un cuadrado llega como máximo a unos 2150 x 2150 px, por eso el preajuste cuadrado más grande es `(2K) 2048x2048`. La plantilla de edición hereda ese mínimo: una imagen fuente de menos de 0.92 MP debe ampliarse antes de poder editarla. `background` tiene tres valores: `auto` decide a partir del prompt y devuelve transparencia principalmente para stickers y logotipos, `opaque` pinta un fondo y `transparent` fuerza un canal alfa. `transparent` funciona mejor cuando el prompt describe un sujeto aislado sobre un fondo liso. Guarda el resultado como PNG para conservar el canal alfa. JPEG lo descarta.

## Empezar

  1. Actualiza ComfyUI a la versión 0.45.0 o posterior.
  2. Abre la Biblioteca de plantillas, busca `Seedream 5.5` y abre cualquiera de los dos flujos de trabajo.
  3. En el nodo, elige el modelo `seedream 5.5` y un preajuste de tamaño, y luego ejecuta.

Cambia el menú desplegable de modelos del nodo a otra versión de Seedream para reutilizar el mismo flujo de trabajo. Seedream 5.0 Pro y Flash también permanecen en preajustes seleccionables, mientras que 5.0 Lite y 4.5 ofrecen filas de 3K y 4K.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bytedance/seedream-5-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bytedance/seedream-5-5)

[Seedream 5 Flash](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-flash)[Seedream 5 Pro](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedream-5-pro)
