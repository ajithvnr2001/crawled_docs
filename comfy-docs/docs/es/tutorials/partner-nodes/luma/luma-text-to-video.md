---
url: https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-text-to-video/
title: Gu\u00eda del nodo asociado Luma Text to Video (heredado) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.721610+00:00
---

# Guía del nodo asociado Luma Text to Video (heredado) - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-text-to-video/

## En esta página

Volver arriba

  * En qué destaca Luma Text to Video
  * Flujo de trabajo de texto a video con los nodos asociados de Luma
    * 1\. Descargar el flujo de trabajo
    * 2\. Notas adicionales



Luma

# Guía del nodo asociado Luma Text to Video (heredado)

Copiar páginaCopiar página

Cómo funcionaba el nodo asociado Luma Text to Video (heredado) en ComfyUI, por qué dejó de funcionar y qué nodo lo reemplaza.

Copiar páginaCopiar página

**Obsoleto** : El nodo heredado **Luma Text to Video** está obsoleto y Luma eliminará los endpoints que utiliza el 24 de octubre de 2026. Usa el nodo [**Luma Ray 3.2 Text to Video**](https://docs.comfy.org/es/built-in-nodes/LumaRay32TextToVideoNode) en su lugar.

El nodo Luma Text to Video te permite crear videos suaves de alta calidad a partir de descripciones de texto usando la innovadora tecnología de generación de video de Luma AI.

## 

​

En qué destaca Luma Text to Video

  * **Generación de texto a video** : Crea videos suaves y de alta calidad a partir de descripciones de texto de escenas, sujetos, acciones y ambiente
  * **Control de cámara** : La función Luma Concepts añade movimientos de cámara para tomas de video profesionales y cinematografía
  * **Selección de modelo** : Puedes seleccionar distintos modelos de video con diferentes funciones mediante el parámetro model
  * **Salida ajustable** : La resolución y la duración del video son ajustables (excepto con el modelo Ray 1.6, donde estos parámetros no aplican)



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

Flujo de trabajo de texto a video con los nodos asociados de Luma

El nodo Luma Text to Video requiere prompts de texto para describir el contenido del video. En esta guía creamos ejemplos con `prompt` y `luma_concepts` para mostrar las excelentes capacidades de generación de video de Luma AI.

### 

​

1\. Descargar el flujo de trabajo

Esta página documenta el nodo **Luma Text to Video** retirado y el flujo de trabajo de ejemplo que lo acompañaba, el cual seleccionaba `ray-2`. Luma deja de ofrecer ese modelo el 24 de octubre de 2026, así que ni el nodo ni el ejemplo pueden ejecutarse. El ejemplo y su guía de pasos permanecen en el código fuente de esta página como comentario. El reemplazo es un nodo independiente. Su propia guía:

## Luma Ray 3.2: Text to Video

Consulta el nodo de reemplazo y sus entradas.

### 

​

2\. Notas adicionales

  * **Redacción de prompts** : Describe con detalle las escenas, los sujetos, las acciones y el estado de ánimo para obtener mejores resultados
  * **Luma Concepts** : Se usa principalmente para el control de cámara y para crear tomas de video profesionales
  * **Parámetro de semilla** : Solo determina si el nodo debe volver a ejecutarse; no afecta a los resultados de la generación
  * **Selección de modelo** : Los distintos modelos de video tienen características diferentes, ajustables mediante el parámetro de modelo
  * **Resolución y duración** : Ajusta la resolución y la duración del video de salida con estos parámetros
  * **Nota sobre el modelo Ray 1.6** : Los parámetros de duración y resolución no funcionan con el modelo Ray 1.6. Luma dejó de ofrecer Ray 1.6 en septiembre de 2026, así que esa opción ya no se ejecuta.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/luma/luma-text-to-video.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/luma/luma-text-to-video)

[Ltx 2 5](https://docs.comfy.org/es/tutorials/partner-nodes/lightricks/ltx-2-5)[Luma imagen a video (heredado)](https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-image-to-video)
