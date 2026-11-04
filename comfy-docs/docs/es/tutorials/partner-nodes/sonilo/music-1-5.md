---
url: https://docs.comfy.org/es/tutorials/partner-nodes/sonilo/music-1-5/
title: Sonilo Music 1.5 en ComfyUI: de la letra a la canci\u00f3n - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:41.244542+00:00
---

# Sonilo Music 1.5 en ComfyUI: de la letra a la canción - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/sonilo/music-1-5/

## En esta página

Volver arriba

  * Empezar
  * Sonilo: Music 1.5 (letras a canción)



Sonilo

# Sonilo Music 1.5 en ComfyUI: de la letra a la canción

Copiar páginaCopiar página

Genera una canción completa con voz cantada en ComfyUI con el Nodo asociado Sonilo Music 1.5: formato del prompt, etiquetas de letra y control de duración.

Copiar páginaCopiar página

Sonilo Music 1.5 convierte un prompt escrito en una canción completa con voz cantada. Describe primero el estilo, añade un bloque `Lyrics:` con tus propias palabras y el nodo las canta. Sin bloque de letra, el modelo escribe la suya. Para las bandas sonoras de video de Sonilo y el nodo anterior de texto a música, consulta [Sonilo: de video a música y de texto a audio](https://docs.comfy.org/es/tutorials/partner-nodes/sonilo/video-to-music).

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

Empezar

1

Actualizar ComfyUI

Actualiza ComfyUI a una versión que incluya el nodo `Sonilo Music 1.5`.

2

Buscar el flujo de trabajo de Sonilo Music 1.5

Abre la **Workflow Library** , explora **Templates** y busca “Sonilo Music 1.5”.

3

Escribir la dirección musical y la letra

Rellena el prompt y luego pulsa el botón **Run** o usa `Ctrl(Cmd) + Enter`.

## 

​

Sonilo: Music 1.5 (letras a canción)

Genera una canción a partir de un prompt de texto. El prompt define la dirección musical y el bloque de letra define las palabras que se cantan. ![Vista previa del flujo de trabajo de letras a canción de Sonilo Music 1.5](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_music1_5-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descargar JSON o buscar “Sonilo Music 1.5” en la Biblioteca de plantillas

**Formato del prompt** : describe primero la dirección musical, después pon `Lyrics:` en su propia línea y escribe la canción debajo. Las etiquetas entre corchetes como `[Verse]`, `[Chorus]` y `[Bridge]` van en su propia línea encima de cada sección, y se repiten cada vez que esa sección vuelve.

  * **Duración** : `auto` ajusta la canción a la letra. Cambia `duration` a `custom` para fijar entre 10 y 360 segundos; una duración personalizada recorta la letra que no cabe y repite la que es corta
  * **Límite del prompt** : 2000 caracteres entre la dirección y la letra
  * **Instrumental** : sin bloque `Lyrics:`, indica `instrumental`, `no vocals` o `lyric-free` en la dirección para obtener una base musical en lugar de una canción
  * **Salida** : la plantilla escribe un MP3 mediante Save Audio (Advanced)

**Prompt de ejemplo:**
    
    
    Warm indie folk at 104 BPM, fingerpicked guitar, brushed drums, upright bass,
    male vocal with light harmonies, written for a cooking video intro.
    
    Lyrics:
    [Verse]
    Flour on the wooden board
    Make a well right in the core
    
    [Chorus]
    Roll it out, roll it thin
    Let the kitchen groove begin
    

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/sonilo/music-1-5.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/sonilo/music-1-5)

[Video a música](https://docs.comfy.org/es/tutorials/partner-nodes/sonilo/video-to-music)[HeyGen Voice 1.0](https://docs.comfy.org/es/tutorials/partner-nodes/heygen/heygen-voice-1)
