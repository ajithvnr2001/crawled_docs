---
url: https://docs.comfy.org/es/tutorials/partner-nodes/wan/wan3-0/
title: Wan 3.0 en ComfyUI: generaci\u00f3n de video con audio sincronizado - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:57.224916+00:00
---

# Wan 3.0 en ComfyUI: generación de video con audio sincronizado - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/wan/wan3-0/

## En esta página

Volver arriba

  * En qué destaca Wan 3.0
  * Salidas de ejemplo
  * Flujo de trabajo de texto a video con Wan 3.0
    * Consejos para el prompt
  * Flujo de trabajo de imagen a video con Wan 3.0
    * Consejos para el prompt
  * Flujo de trabajo de referencia a video con Wan 3.0
    * Consejos para el prompt
  * Empezar
  * Preguntas frecuentes



Wan

# Wan 3.0 en ComfyUI: generación de video con audio sincronizado

Copiar páginaCopiar página

Genera hasta 30 segundos de video con audio sincronizado en ComfyUI con los Nodos asociados de Wan 3.0, desde prompts de texto, imágenes de primer fotograma o medios de referencia.

Copiar páginaCopiar página

Wan 3.0 es el modelo de generación de video más reciente de Alibaba, ahora disponible en ComfyUI a través de Nodos asociados. Genera hasta 30 segundos de video en una sola pasada con una pista de audio sincronizada, y combina prompts de texto con imágenes, videos y audio de referencia para mantener personajes y escenas consistentes.

## 

​

En qué destaca Wan 3.0

  * **Hasta 30 segundos** : Genera clips largos con movimiento y audio coherentes en una sola pasada
  * **Audio nativo** : Cada resultado incluye una pista de audio sincronizada de forma predeterminada
  * **Entrada de texto, imagen y referencia** : Prompts de solo texto, animación desde el primer fotograma o hasta 10 imágenes de referencia, 5 videos de referencia y 5 clips de audio de referencia
  * **Etiquetas de referencia** : Menciona los medios conectados directamente en el prompt como `@Image1`, `@Video1` o `@Audio1`
  * **Salida flexible** : Resolución de 480p, 720p o 1080p con relaciones de aspecto adaptativas, 16:9, 9:16, 1:1, 4:3 o 3:4
  * **Modelo WAN3-Prime** : La opción `model` también ofrece `wan3.0-video-prime` para obtener resultados de mayor fidelidad a una tarifa por segundo más alta
  * **Prompts bilingües** : Escribe el prompt en inglés o chino



## 

​

Salidas de ejemplo

Generación de texto a video a partir de un prompt, con audio sincronizado incluido de forma predeterminada: ![Ejemplo de salida de texto a video de Wan 3.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_t2v-1.webp) Generación de imagen a video, animando una sola imagen para convertirla en un clip completo: ![Ejemplo de salida de imagen a video de Wan 3.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_i2v-1.webp) Generación de referencia a video, manteniendo un producto y un personaje consistentes a partir de imágenes de referencia: ![Ejemplo de salida de referencia a video de Wan 3.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_r2v-1.webp)

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

Flujo de trabajo de texto a video con Wan 3.0

Genera un video a partir de un prompt de texto únicamente, con audio sincronizado incluido de forma predeterminada. ![Ejemplo de salida de texto a video con Wan 3.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_t2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan 3.0” en la Biblioteca de plantillas

#### 

​

Consejos para el prompt

  1. **Duración** : Configura de 2 a 30 segundos, o `auto` para que el modelo elija una duración que se ajuste al prompt
  2. **Resolución y relación** : el flujo de trabajo viene en 720p con relación `adaptive`; cambia a 1080p o a una relación fija como `16:9` para formatos específicos
  3. **Audio** : el audio se genera de forma predeterminada. Desactiva la opción `audio` para obtener un video sin sonido
  4. **Ampliación del prompt** : la mejora del prompt está activada de forma predeterminada y reescribe tu prompt para obtener mejores resultados. Desactívala en las configuraciones avanzadas si necesitas el texto exacto



## 

​

Flujo de trabajo de imagen a video con Wan 3.0

Anima una sola imagen y conviértela en un video, con un último fotograma opcional hacia el que transiciona el resultado. ![Ejemplo de salida de imagen a video con Wan 3.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_i2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan 3.0” en la Biblioteca de plantillas

#### 

​

Consejos para el prompt

  1. **Primer fotograma** : La entrada `first_frame` es requerida. La entrada `last_frame` es opcional, y el modelo genera el movimiento entre ambos
  2. **Relación adaptable** : Con `adaptive`, las dimensiones de salida siguen a la imagen de entrada
  3. **Prompt** : Describe qué se mueve y cómo, además del audio que quieras. Mantén los sujetos y la composición sin cambios a menos que quieras que el modelo los modifique



## 

​

Flujo de trabajo de referencia a video con Wan 3.0

Genera un video condicionado por imágenes, videos y audio de referencia, y asigna a cada referencia una tarea mediante etiquetas en el prompt. ![Ejemplo de salida del flujo de trabajo de referencia a video con Wan 3.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_r2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Wan 3.0” en la Biblioteca de plantillas

#### 

​

Consejos para el prompt

  1. **Referencia por etiqueta** : menciona cada entrada en el prompt como `@Image1`, `@Video1` o `@Audio1`, numeradas por tipo en el orden de entrada. El prompt de ejemplo asigna el diseño del zapato a `@Image1` y el personaje a `@Image2`
  2. **Límites** : hasta 10 imágenes de referencia, 5 videos de referencia y 5 clips de audio de referencia. Cada video o clip de audio de referencia debe durar 15 segundos o menos, y la duración combinada de todos los videos de referencia debe mantenerse dentro de 15 segundos (lo mismo para el audio). La duración total de los videos de referencia más la salida no debe superar los 30 segundos
  3. **Asigna una tarea** : indica qué controla cada referencia (diseño del producto, identidad del personaje, estilo, movimiento, voz) y qué debe permanecer sin cambios. Las asignaciones explícitas producen resultados más consistentes
  4. **Se requiere un prompt o una referencia** : proporciona un prompt o al menos una entrada de referencia; de lo contrario, el nodo devuelve un error



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión o usa el [Comfy Desktop](https://www.comfy.org/download) más reciente
  2. Ve a Biblioteca de plantillas y busca `Wan 3.0`
  3. Carga uno de los tres flujos de trabajo (texto a video, imagen a video o referencia a video)
  4. Inicia sesión con tu cuenta de Comfy y asegúrate de tener suficientes [créditos](https://docs.comfy.org/es/interface/credits)
  5. Conecta los materiales de entrada (el primer fotograma o las imágenes de referencia) y ejecuta



## 

​

Preguntas frecuentes

¿Qué es Wan 3.0?

Wan 3.0 es el modelo de generación de video más reciente de Alibaba, disponible en ComfyUI a través de los Nodos asociados. Genera hasta 30 segundos de video con audio sincronizado en una sola pasada y acepta prompts de texto, imágenes de referencia, videos de referencia y audio de referencia.

¿Cuánto pueden durar los videos de Wan 3.0?

Hasta 30 segundos por clip. La entrada de duración acepta de 2 a 30 segundos, o `auto` para que el modelo elija una duración que se ajuste al prompt.

¿Wan 3.0 genera audio?

Sí. Cada salida incluye de forma predeterminada una pista de audio sincronizada, con diálogo, efectos de sonido y música generados junto con el video. Desactiva la opción `audio` para obtener video sin sonido.

¿Wan 3.0 puede usar imágenes, videos o audio de referencia?

Sí, en el flujo de trabajo de referencia a video. Conecta hasta 10 imágenes de referencia, 5 videos de referencia y 5 clips de audio de referencia, y luego consúltalos en el prompt como `@Image1`, `@Video1` o `@Audio1`.

¿Cuál es la diferencia entre Wan 3.0 y Wan 2.7?

Wan 3.0 es la generación más reciente del modelo de video de Alibaba. Amplía el pipeline multimodal con etiquetas de referencia para imágenes, videos y audio, audio sincronizado nativo de forma predeterminada y hasta 30 segundos de salida por clip. Consulta la [página de Wan 2.7](https://docs.comfy.org/es/tutorials/partner-nodes/wan/wan2-7) para la generación anterior.

¿Wan 3.0 admite prompts en chino?

Sí. La entrada de prompt admite tanto inglés como chino.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/wan/wan3-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/wan/wan3-0)

[Vidu Q4 Preview](https://docs.comfy.org/es/tutorials/partner-nodes/vidu/vidu-q4-preview)[Wan2 7](https://docs.comfy.org/es/tutorials/partner-nodes/wan/wan2-7)
