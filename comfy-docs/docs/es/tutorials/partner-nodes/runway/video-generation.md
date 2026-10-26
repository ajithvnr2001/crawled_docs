---
url: https://docs.comfy.org/es/tutorials/partner-nodes/runway/video-generation/
title: Runway Gen4 Turbo en ComfyUI: flujo de trabajo de imagen a video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:55.242666+00:00
---

# Runway Gen4 Turbo en ComfyUI: flujo de trabajo de imagen a video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/runway/video-generation/

## En esta página

Volver arriba

  * En qué destaca Runway Video Generation
    * Flujos de trabajo retirados y sus reemplazos
  * Flujo de trabajo de imagen a video con Gen4 turbo
    * 1\. Descargar el archivo de flujo de trabajo
    * 2\. Completar la ejecución del flujo de trabajo paso a paso



Runway

# Runway Gen4 Turbo en ComfyUI: flujo de trabajo de imagen a video

Copiar páginaCopiar página

Genera video desde una imagen fija en ComfyUI con el nodo asociado Runway Gen4 Turbo y ajusta la duración y la relación de aspecto.

Copiar páginaCopiar página

Runway es una empresa enfocada en la IA generativa que ofrece potentes capacidades de generación de video. Actualmente, ComfyUI ha integrado la API de Runway, lo que te permite usar directamente los nodos relacionados en ComfyUI para generar video. Actualmente, ComfyUI integra de forma nativa el siguiente modelo de generación de video de Runway:

  * Runway Gen4 turbo



**Fin de soporte (EOL)** : **Runway Gen3a Turbo** y **Runway Primer-Fotograma-Último a video** llegaron al final de su vida útil el **30 de julio de 2026**. Runway retiró Gen-3 Alpha Turbo en esa fecha. Los Nodos asociados relacionados (`RunwayImageToVideoNodeGen3a`, `RunwayFirstLastFrameNode`) y las plantillas de flujo de trabajo están obsoletos y ya no reciben soporte.

## 

​

En qué destaca Runway Video Generation

  * **Generación de imagen a video** : el nodo `Runway Gen4 turbo` genera un video a partir de una imagen de entrada y un prompt de texto que describe el contenido del video
  * **Duración del video ajustable** : modifica el parámetro `duration` para establecer la duración del video
  * **Relación de aspecto ajustable** : modifica el parámetro `ratio` para establecer la relación de aspecto del video



**Fin de vida útil (EOL)** : **Runway Gen3a Turbo** y **Runway Primer-Fotograma-Último a video** alcanzaron el fin de su vida útil el **30 de julio de 2026**. Runway retiró Gen-3 Alpha Turbo en esa fecha. Los Nodos asociados relacionados (`RunwayImageToVideoNodeGen3a`, `RunwayFirstLastFrameNode`) y las plantillas de flujo de trabajo están obsoletos y ya no reciben soporte.

### 

​

Flujos de trabajo retirados y sus reemplazos

Plantilla eliminada| Reemplazo sugerido  
---|---  
`api_runway_gen3a_turbo_image_to_video`| [`api_runway_gen4_turbo_image_to_video`](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_runway_gen4_turbo_image_to_video.json) (Gen4 Turbo)  
`api_runway_first_last_frame`| [Kling 3.0 FLF2V](https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-3-0) (`api_kling_v3_flf2v`) u otras plantillas de primer-último fotograma  
  
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

Flujo de trabajo de imagen a video con Gen4 turbo

### 

​

1\. Descargar el archivo de flujo de trabajo

El siguiente video contiene la información del flujo de trabajo en sus `metadata`. Descárgalo y arrástralo a ComfyUI para cargar el flujo de trabajo correspondiente. [Descargar archivo de flujo de trabajo en formato Json](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen4_turbo_image_to_video/runway_gen4_turo_image_to_video.json) Descarga la siguiente imagen como imagen de entrada ![Imagen de entrada de imagen a video de ComfyUI Runway gen4 turbo](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/api_nodes/runway/gen4_turbo_image_to_video/godfather.jpg)

### 

​

2\. Completar la ejecución del flujo de trabajo paso a paso

![Guía paso a paso de imagen a video de ComfyUI Runway gen4 turbo](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/runway/runway_gen4_turbo_image_to_video_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=1c2df6f00cd1a0fc221a058621cd1449) Puedes guiarte por los números de la imagen para completar la ejecución del flujo de trabajo básico de imagen a video:

  1. En el nodo `Load Image`, carga la imagen de entrada proporcionada
  2. En el nodo `Runway Gen4 turbo`, configura el `prompt` para describir el contenido del video, modifica el parámetro `duration` para establecer la duración del video y modifica el parámetro `ratio` para establecer la relación de aspecto del video
  3. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación del video.
  4. Después de esperar a que la API devuelva los resultados, puedes ver el video generado en el nodo `Save Video` (haz clic derecho para guardar). El video correspondiente también se guardará en el directorio `ComfyUI/output/`.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/runway/video-generation.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/runway/video-generation)

[Pruna P-Video-2](https://docs.comfy.org/es/tutorials/partner-nodes/pruna/p-video-2)[Topaz Labs](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/overview)
