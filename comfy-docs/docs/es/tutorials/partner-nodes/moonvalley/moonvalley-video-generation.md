---
url: https://docs.comfy.org/es/tutorials/partner-nodes/moonvalley/moonvalley-video-generation/
title: Moonvalley Marey en ComfyUI: generaci\u00f3n de video (obsoleta) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:52.995349+00:00
---

# Moonvalley Marey en ComfyUI: generación de video (obsoleta) - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/moonvalley/moonvalley-video-generation/

## En esta página

Volver arriba

  * En qué destaca Moonvalley
  * Flujo de trabajo de texto a video de Moonvalley
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Seguir los pasos para ejecutar el flujo de trabajo
  * Flujo de trabajo de imagen a video de Moonvalley
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Seguir los pasos para ejecutar el flujo de trabajo
  * Flujo de trabajo de video a video de Moonvalley
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Sigue los pasos para ejecutar el flujo de trabajo



Moonvalley

# Moonvalley Marey en ComfyUI: generación de video (obsoleta)

Copiar páginaCopiar página

Nodos asociados de Moonvalley Marey en ComfyUI, obsoletos, para generación de texto a video, imagen a video y video a video. La API ya no está disponible.

Copiar páginaCopiar página

**Servicio no disponible** : El servicio de la API de Moonvalley ya no está disponible. Estos nodos están obsoletos y es posible que no funcionen como se espera.

Moonvalley Marey Realism v1.5 es un modelo de generación de video con IA diseñado para la creación de nivel cinematográfico. El modelo está **entrenado por completo con contenido con licencia comercial** , lo que garantiza el **cumplimiento de derechos de autor y la seguridad comercial**.

## 

​

En qué destaca Moonvalley

  * Comprensión excepcional del prompt: interpreta con precisión instrucciones complejas del prompt.
  * Calidad HD 1080p nativa: el conjunto de datos de entrenamiento se basa en videos **1080P** , lo que da como resultado una salida fina y detallada.
  * Física realista y desempeño dinámico: simula con precisión modelos de movimiento físico y dinámicas naturales, y ofrece un realismo de nivel profesional.
  * Capas de escenas complejas y efectos de iluminación avanzados: admite capas de primer plano, plano medio y fondo en escenas complejas, con comprensión inteligente de las relaciones espaciales.
  * Funciones de control de nivel de producción, como la transferencia de movimiento y de pose: genera automáticamente iluminación realista para escenas compuestas.

Actualmente, ComfyUI admite de forma nativa los Nodos asociados de Moonvalley. Puedes usar directamente en ComfyUI las capacidades correspondientes de texto a video, imagen a video y video a video.

**Servicio no disponible** : el servicio de la API de Moonvalley ya no está disponible. Estos nodos han quedado obsoletos y puede que no funcionen como se espera.

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

Flujo de trabajo de texto a video de Moonvalley

### 

​

1\. Descargar el archivo del flujo de trabajo

[Descarga el archivo del flujo de trabajo en formato JSON](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_text_to_video.json)

### 

​

2\. Seguir los pasos para ejecutar el flujo de trabajo

![Flujo de trabajo de texto a video](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_text_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=75dc005efbab705ab95cea22b36f7a24)

  1. Ingresa el prompt positivo (contenido que quieres que aparezca en el video)
  2. Ingresa el prompt negativo (contenido que no quieres que aparezca en el video)
  3. Modifica la resolución de salida del video
  4. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter` para iniciar la generación del video
  5. Después de que la API devuelva el resultado, puedes ver el video generado en el nodo `Save Video`. El video también se guardará en el directorio `ComfyUI/output/`



## 

​

Flujo de trabajo de imagen a video de Moonvalley

### 

​

1\. Descargar el archivo del flujo de trabajo

[Descarga el archivo del flujo de trabajo en formato JSON](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_image_to_video.json) Descarga la siguiente imagen como imagen de entrada ![Input Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_image_to_video_input.webp)

### 

​

2\. Seguir los pasos para ejecutar el flujo de trabajo

![Image-to-Video Workflow](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_image_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=9467e0f19d709f9b77cc4778a97f04a8)

  1. Carga la imagen de entrada en el nodo `Load Image`
  2. Ingresa el prompt positivo (el contenido que quieres que aparezca en el video)
  3. Ingresa el prompt negativo (el contenido que no quieres que aparezca en el video)
  4. Modifica la resolución de salida del video
  5. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter` para iniciar la generación del video
  6. Después de que la API devuelva el resultado, puedes ver el video generado en el nodo `Save Video`. El video también se guardará en el directorio `ComfyUI/output/`



## 

​

Flujo de trabajo de video a video de Moonvalley

El nodo `Moonvalley Marey Video to Video` te permite introducir un video de referencia para el redibujado de video. Puedes usar el movimiento o las poses de los personajes del video de referencia para generar el video.

### 

​

1\. Descargar el archivo del flujo de trabajo

[Descargar el archivo del flujo de trabajo en formato JSON](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/moonvalley/api_moonvalley_video_to_video.json) Descarga el video de abajo como video de entrada:

### 

​

2\. Sigue los pasos para ejecutar el flujo de trabajo

![Flujo de trabajo de video a video](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/moonvalley/api_moonvalley_video_to_video.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ee9e202bdc9a3b39c8dc6ba5b10577b5)

  1. Carga el video de referencia (o tu propio material) en el nodo `Load Video`
     * Si la duración final del video es de 5s, el video de entrada debe durar más de 5s
     * Si la duración final del video es de 10s, el video de entrada debe durar más de 10s
  2. Introduce el prompt positivo (el contenido que quieres que aparezca en el video)
  3. Introduce el prompt negativo (el contenido que no quieres que aparezca en el video)
  4. Configura el parámetro `control_type` para elegir el tipo de referencia para el redibujado de video 
     * `Motion Transfer`: Genera a partir del movimiento del video de referencia
     * `Pose Transfer`: Genera a partir de las poses de los personajes del video de referencia
  5. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter` para iniciar la generación del video
  6. Cuando la API devuelve el resultado, puedes ver el video generado en el nodo `Save Video`. El video también se guarda en el directorio `ComfyUI/output/`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/moonvalley/moonvalley-video-generation.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/moonvalley/moonvalley-video-generation)

[Minimax H3](https://docs.comfy.org/es/tutorials/partner-nodes/minimax/minimax-h3)[PixVerse AI](https://docs.comfy.org/es/tutorials/partner-nodes/pixverse/overview)
