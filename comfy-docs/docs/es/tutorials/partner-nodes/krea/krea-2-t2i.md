---
url: https://docs.comfy.org/es/tutorials/partner-nodes/krea/krea-2-t2i/
title: Krea 2 en ComfyUI: texto a imagen con referencias de estilo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.472207+00:00
---

# Krea 2 en ComfyUI: texto a imagen con referencias de estilo - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/krea/krea-2-t2i/

## En esta página

Volver arriba

  * Para qué sirve Krea 2 Text to Image
  * Documentación del nodo Krea 2 Image
  * Flujo de trabajo de texto a imagen de Krea 2
  * Flujo de trabajo de referencia de estilo de Krea 2
  * Notas adicionales



Krea

# Krea 2 en ComfyUI: texto a imagen con referencias de estilo

Copiar páginaCopiar página

Genera imágenes con el nodo Krea 2 Image en ComfyUI usando Krea 2 Medium o Large, hasta 10 referencias de estilo, moodboards y creatividad ajustable.

Copiar páginaCopiar página

El [nodo Krea 2 Image](https://docs.comfy.org/es/built-in-nodes/Krea2ImageNode) te permite generar imágenes de alta calidad a partir de prompts de texto con el modelo de nueva generación de Krea AI. Admite dos variantes del modelo, **Krea 2 Medium** para ilustraciones expresivas y **Krea 2 Large** para fotorrealismo expresivo, con entradas opcionales de moodboard y referencia de estilo.

## 

​

Para qué sirve Krea 2 Text to Image

  * **Dos variantes del modelo** : Krea 2 Medium para ilustraciones expresivas, Krea 2 Large para fotorrealismo expresivo
  * **Referencias de estilo** : aplica el estilo estético, el ambiente y la dirección visual de hasta 10 imágenes de referencia a tu generación
  * **Soporte de moodboard** : usa el parámetro `moodboard_id` con un moodboard del [sitio web de Krea](https://www.krea.ai)
  * **Configuraciones de generación ajustables** : controla la relación de aspecto, la resolución, el nivel de creatividad y la semilla



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

Documentación del nodo Krea 2 Image

Consulta la siguiente documentación para ver las configuraciones detalladas de los parámetros del nodo:

  * [Nodo Krea 2 Image](https://docs.comfy.org/es/built-in-nodes/Krea2ImageNode)
  * [Nodo Krea 2 Style Reference](https://docs.comfy.org/es/built-in-nodes/Krea2StyleReferenceNode)



## 

​

Flujo de trabajo de texto a imagen de Krea 2

![Flujo de trabajo de texto a imagen de Krea 2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea2_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Krea2” en la Biblioteca de plantillas

  1. **Ingresa tu prompt** : escribe una descripción de texto en el nodo **Krea2ImageNode**
  2. **Selecciona una variante del modelo** : elige entre **Krea 2 Medium** (ilustraciones) o **Krea 2 Large** (fotorrealismo)
  3. **Ajusta los parámetros** : define la relación de aspecto, la resolución, el nivel de creatividad y la semilla
  4. **Haz clic en Queue** : presiona `Ctrl+Enter` o haz clic en el botón Queue para generar
  5. **Ver el resultado** : la imagen generada aparece en el nodo **SaveImage** y se guarda en `ComfyUI/output/`



## 

​

Flujo de trabajo de referencia de estilo de Krea 2

![Flujo de trabajo de referencia de estilo de Krea 2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea2_style_reference-1.webp) El flujo de trabajo de referencia de estilo añade un paso extra: sube una o más imágenes de referencia que definen el estilo estético, la atmósfera y la dirección visual. La imagen generada coincidirá con tu prompt y, al mismo tiempo, aplicará el estilo de tus imágenes de referencia.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Krea 2: Style Reference” en la Biblioteca de plantillas

  1. **Sube imágenes de referencia** : usa los nodos **LoadImage** para cargar imágenes de referencia de estilo (admite hasta 10)
  2. **Escribe tu prompt** : describe la escena que quieres en **Krea2ImageNode**
  3. **Selecciona una variante de modelo** : elige entre Medium y Large
  4. **Ajusta la intensidad del estilo** : modifica la intensidad de la referencia de estilo en los nodos **Krea2StyleReferenceNode**
  5. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar
  6. **Consulta el resultado** : la imagen generada aparece en el nodo **SaveImage**



## 

​

Notas adicionales

  * El nodo Krea 2 Image admite hasta **10 imágenes de referencia de estilo** de forma simultánea
  * El parámetro `moodboard_id` requiere un UUID válido de un moodboard de Krea en [el sitio web de Krea](https://www.krea.ai)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/krea/krea-2-t2i.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/krea/krea-2-t2i)

[Krea 3](https://docs.comfy.org/es/tutorials/partner-nodes/krea/krea-3)[Luma Uni 1](https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-uni-1)
