---
url: https://docs.comfy.org/es/tutorials/partner-nodes/happyhorse/happyhorse1-1/
title: Generaci\u00f3n de video con HappyHorse 1.1 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:49.868167+00:00
---

# Generación de video con HappyHorse 1.1 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/happyhorse/happyhorse1-1/

## En esta página

Volver arriba

  * En qué destaca HappyHorse 1.1
  * HappyHorse 1.1 texto a video
  * HappyHorse 1.1 imagen a video
  * HappyHorse 1.1 referencia a video
  * Primeros pasos



HappyHorse

# Generación de video con HappyHorse 1.1 en ComfyUI

Copiar páginaCopiar página

Usa HappyHorse 1.1 con los Nodos asociados de ComfyUI para imagen a video, texto a video y referencia a video con audio sincronizado nativo y escenas de varios planos.

Copiar páginaCopiar página

HappyHorse 1.1 es la última versión del modelo de generación de video de nivel profesional de Alibaba, ahora disponible en ComfyUI como nodo asociado. Está diseñado para la producción creativa del mundo real: series episódicas cortas, comerciales de comercio electrónico, contenido de marketing de marca y cinemáticas de videojuegos. Una característica destacada es la **generación de audio sincronizado nativo** : HappyHorse 1.1 produce diálogos, efectos de sonido y música de fondo en una sola pasada de renderizado, con el audio estrechamente vinculado a la línea de tiempo visual. No hay pasos adicionales de audio. La versión 1.1 apunta a cinco capacidades críticas para la producción: movimiento dinámico y expresivo, renderizado consistente de personajes, adherencia confiable al prompt, renderizado estable de texto y encuadre cinematográfico auténtico.

## 

​

En qué destaca HappyHorse 1.1

  * **Sincronización nativa de audio y video** : Diálogos, efectos de sonido y música de fondo en una sola pasada (sin pasos adicionales)
  * **Tres rutas de creación** : texto a video (T2V), imagen a video (I2V) y referencia a video (R2V)
  * **R2V con varias imágenes** : Hasta **9 imágenes de referencia** por generación con la identidad preservada
  * **Consistencia entre varios personajes** : Varias referencias de personajes se mantienen distintas, sin contaminación visual cruzada
  * **Separación de personaje y escena** : Pasa personajes y escenas como referencias independientes; los personajes se mantienen consistentes aunque cambie el fondo
  * **Prompts de contexto largo** : Admite prompts de más de 2,500 caracteres; un solo prompt puede describir de 6 a 8 escenas consecutivas mientras el modelo asigna el tiempo y cambia los ángulos de cámara de forma autónoma
  * **Lenguaje cinematográfico** : Compatibilidad total con plano y contraplano, tomas de seguimiento y transiciones y ritmo coherentes entre planos
  * **Salida flexible** : 720p y 1080p, de 3 a 15 segundos, relaciones de aspecto 16:9 / 9:16 / 1:1 / 4:3 / 3:4 / 21:9 y más
  * **Visuales listos para producción** : Corrige los problemas de piel brillante y exceso de nitidez de la v1.0 para lograr primeros planos y contenido de series con aspecto natural



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

HappyHorse 1.1 texto a video

Crea una escena completa desde cero. Tú controlas el estilo, el tamaño de plano, la iluminación, la acción y el audio por completo mediante el prompt. HappyHorse 1.1 devuelve un solo video con diálogo, efectos de sonido y música ya integrados.

## Ejecutar HappyHorse 1.1 T2V en Cloud

Prueba el flujo de trabajo de texto a video al instante en Comfy Cloud.

## Descargar flujo de trabajo HappyHorse 1.1 T2V

Descarga el JSON del flujo de trabajo o busca “HappyHorse 1.1” en la Biblioteca de plantillas.

![Vista previa del flujo de trabajo HappyHorse 1.1 de texto a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_1_t2v-1.webp)

## 

​

HappyHorse 1.1 imagen a video

Anima un primer fotograma estático. La imagen ya aporta el aspecto visual, así que tú describes el movimiento y el desplazamiento de cámara. HappyHorse 1.1 devuelve un video con el audio incorporado.

## Ejecuta HappyHorse 1.1 I2V en Comfy Cloud

Prueba el flujo de trabajo de imagen a video al instante en Comfy Cloud.

## Descargar el flujo de trabajo I2V de HappyHorse 1.1

Descarga el JSON del flujo de trabajo o busca “HappyHorse 1.1” en la Biblioteca de plantillas.

## Descargar imagen de ejemplo

Obtén la imagen de entrada de ejemplo para este flujo de trabajo.

![Vista previa del flujo de trabajo de imagen a video de HappyHorse 1.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_1_i2v-1.webp)

## 

​

HappyHorse 1.1 referencia a video

Orquesta una obra de teatro con varios personajes. Asigna personajes y escenas a imágenes de referencia y luego dirígelos mediante un storyboard con marcas de tiempo y diálogo por personaje. Hasta 9 imágenes de referencia por generación, con las referencias de personaje y de escena separadas para que los personajes se mantengan consistentes aunque cambie el fondo.

## Ejecuta HappyHorse 1.1 R2V en Comfy Cloud

Prueba el flujo de trabajo de referencia a video al instante en Comfy Cloud.

## Descarga el flujo de trabajo HappyHorse 1.1 R2V

Descarga el JSON del flujo de trabajo o busca “HappyHorse 1.1” en la Biblioteca de plantillas.

## Descarga la referencia de personaje

Obtén la imagen de referencia de personaje del ejemplo.

## Descarga la referencia de escena

Obtén la imagen de referencia de escena del ejemplo.

![Vista previa del flujo de trabajo HappyHorse 1.1 de referencia a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_1_r2v-1.webp)

## 

​

Primeros pasos

  1. Actualiza ComfyUI a la última versión
  2. Encuentra los nodos HappyHorse en la Biblioteca de nodos (busca “HappyHorse”) o carga una plantilla lista para usar desde la Biblioteca de plantillas
  3. Elige tu modo: texto a video, imagen a video o referencia a video
  4. Conecta tu prompt y las imágenes de referencia; luego, ejecuta
  5. El resultado llega con audio incorporado en 720p o 1080p



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/happyhorse/happyhorse1-1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/happyhorse/happyhorse1-1)

[Grok Imagine Video 1 5](https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-imagine-video-1-5)[Happyhorse1 0](https://docs.comfy.org/es/tutorials/partner-nodes/happyhorse/happyhorse1-0)
