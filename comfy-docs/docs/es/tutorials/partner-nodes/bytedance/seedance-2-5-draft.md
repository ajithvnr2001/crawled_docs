---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-5-draft/
title: Modo Draft de Seedance 2.5: vista previa a 480p y render final a 1080p - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:47.450394+00:00
---

# Modo Draft de Seedance 2.5: vista previa a 480p y render final a 1080p - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-5-draft/

## En esta página

Volver arriba

  * Cómo funcionan las dos etapas
  * Plantillas de flujos de trabajo
  * Materiales de entrada
  * Consejos



ByteDance

# Modo Draft de Seedance 2.5: vista previa a 480p y render final a 1080p

Copiar páginaCopiar página

Itera con bajo costo en ComfyUI con el modo Draft de Seedance 2.5: vista previa a 480p con draft_task_id y render final a 1080p desde ese ID.

Copiar páginaCopiar página

El modo Draft de Seedance 2.5 genera una vista previa rápida y de bajo costo en 480p antes de que te decidas por un render completo en 1080p, así puedes iterar sobre un prompt, un primer fotograma o un conjunto de imágenes de referencia sin pagar por generaciones a resolución completa. El modo Draft está disponible en tres flujos de trabajo de Seedance 2.5. Selecciona **Seedance 2.5 Draft** como modelo en el nodo Text to Video, First-Last-Frame to Video o Reference to Video:

  * **Texto a video (T2V)** : itera sobre el prompt y la duración
  * **Imagen a video (I2V)** : itera sobre el primer fotograma
  * **Referencia a video (R2V)** : itera sobre las imágenes de referencia y el storyboard

La resolución está fijada en 480p en el modo Draft, y cada ejecución devuelve tanto la vista previa como un `draft_task_id` que usa el render final.

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

Cómo funcionan las dos etapas

Cada flujo de trabajo de borrador se ejecuta en dos etapas:

  1. **Crear el borrador** : ejecuta el nodo Seedance 2.5 con el modelo **Seedance 2.5 Draft** para obtener la vista previa en 480p y su `draft_task_id`, que el nodo **Save Text** escribe en un archivo `.txt` en la carpeta de salida. Vuelve a ejecutar con un prompt o una entrada distintos hasta que el borrador se vea bien.
  2. **Renderizar el video final** : copia el `draft_task_id` de ese archivo `.txt` en el campo `draft_task_id` del nodo **ByteDance Seedance 2.5 Draft to Final Video** y ejecútalo. El nodo renderiza el final en 1080p y reutiliza aquello con lo que se creó el borrador, incluidos el prompt, la entrada, la duración, la relación de aspecto y la configuración de audio, así que no hay que volver a introducir nada.

Cada plantilla coloca las dos etapas en grupos de nodos separados, llamados **Stage 1: Create and preview the draft video** y **Stage 2: Render the final video from the draft task ID**. Deja la etapa 1 en bypass cuando estés conforme con el borrador, porque una segunda ejecución del nodo de borrador crea un borrador nuevo en lugar de reutilizar el que revisaste.

## 

​

Plantillas de flujos de trabajo

## Ejecutar Draft Text-to-Video en Cloud

Prueba el flujo de trabajo Draft Text-to-Video al instante en Comfy Cloud.

## Descargar el flujo de trabajo Draft Text-to-Video

Descarga el JSON del flujo de trabajo.

## Ejecutar Draft Image-to-Video en Cloud

Prueba el flujo de trabajo Draft Image-to-Video al instante en Comfy Cloud.

## Descargar el flujo de trabajo Draft Image-to-Video

Descarga el JSON del flujo de trabajo.

## Ejecutar Draft Reference-to-Video en Cloud

Prueba el flujo de trabajo Draft Reference-to-Video al instante en Comfy Cloud.

## Descargar el flujo de trabajo Draft Reference-to-Video

Descarga el JSON del flujo de trabajo.

## 

​

Materiales de entrada

Las plantillas de borrador de imagen a video y de referencia a video usan estas entradas de muestra:

## Primer fotograma

Descargar primer fotograma de muestra

## Imagen de referencia

Descargar imagen de referencia de muestra

## Guion gráfico

Descargar guion gráfico de muestra

## 

​

Consejos

  * **Ejecuta solo la etapa que necesites** : selecciona los nodos de la Etapa 1 y presiona `Ctrl+B` (`Cmd+B` en macOS) para omitirlos, luego selecciona los nodos de la Etapa 2 y presiona `Ctrl+B` de nuevo para habilitarlos, así solo se ejecuta el render final
  * **Conserva el ID de la tarea de borrador** : el nodo **Save Text** lo escribe en un archivo `.txt` en la carpeta de salida, y la Etapa 2 lo lee desde ahí
  * **Los borradores se pueden renderizar durante 7 días** después de crearse, así que genera el render final dentro de ese plazo

Consulta [Seedance 2.5](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-5) para ver la descripción general del modelo, los flujos de trabajo estándar y la edición de video.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bytedance/seedance-2-5-draft.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bytedance/seedance-2-5-draft)

[Seedance 2 5](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-5)[Seedance 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seedance-2-0)
