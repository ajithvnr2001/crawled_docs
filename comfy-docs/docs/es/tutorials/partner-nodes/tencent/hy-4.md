---
url: https://docs.comfy.org/es/tutorials/partner-nodes/tencent/hy-4/
title: Tencent HY4 en ComfyUI: imagen a prompt y an\u00e1lisis de im\u00e1genes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-06T14:51:55.236276+00:00
---

# Tencent HY4 en ComfyUI: imagen a prompt y análisis de imágenes - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/tencent/hy-4/

## En esta página

Volver arriba

  * Para qué sirve el nodo Tencent HY
  * Flujo de trabajo de Tencent HY4 de imagen a prompt
    * Pasos para ejecutar el flujo de trabajo
    * Consejos para los prompts
  * Empezar



Tencent

# Tencent HY4 en ComfyUI: imagen a prompt y análisis de imágenes

Copiar páginaCopiar página

Ejecuta Tencent HY4 en ComfyUI para convertir una imagen de referencia en un prompt, una descripción o un desglose de gráficos, con control de tokens.

Copiar páginaCopiar página

**Tencent HY4** es el modelo de lenguaje grande de Tencent, disponible en ComfyUI a través del nodo socio `Tencent HY`. El nodo recibe un prompt de texto y hasta 20 imágenes, y devuelve texto: un prompt artístico escrito a partir de una imagen de referencia, una descripción de imagen, un desglose de gráfico o cualquier otra respuesta que pidas. Hy4 se lanzó el 4 de noviembre de 2026. Es la primera generación Hy con comprensión visual, y Tencent reporta mejoras sobre Hy4 preview en el seguimiento de instrucciones, la comprensión de contexto largo y las tareas agénticas de horizonte largo. El nodo llama al modelo a través de Comfy API, así que no se requieren descargas de modelos ni una GPU local. La plantilla que se cubre aquí es el ejemplo image to prompt: lee una foto y escribe un prompt separado por comas que puedes pegar en un modelo de imagen.

## 

​

Para qué sirve el nodo Tencent HY

  * **De imagen a prompt** : escribe un prompt estructurado que cubre sujeto, composición, cámara, iluminación, color, textura y estilo
  * **Comprensión de imágenes** : descripciones, desglose de gráficos y diagramas, y revisión de detalles finos en fotos, capturas de pantalla y documentos
  * **Varias imágenes por solicitud** : hasta 20 imágenes en una sola llamada, donde cada imagen de un lote cuenta una vez
  * **Control por instrucciones** : `system_prompt` mantiene un rol permanente, mientras que `prompt` lleva la tarea de esta ejecución
  * **Alternar el razonamiento** : `reasoning` hace que el modelo piense antes de responder, para las tareas que lo necesitan
  * **Respuestas largas** : `max_tokens` acepta hasta 64000 tokens



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

Flujo de trabajo de Tencent HY4 de imagen a prompt

La plantilla carga una foto de referencia, solicita a Tencent HY un prompt de arte estándar y, si quieres, puede guardar el prompt y la respuesta junto con la ejecución. ![Vista previa del flujo de trabajo de Tencent HY4 de imagen a prompt](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tencent_hy4-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “Tencent: Hy4” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## blue_poppies_field.png

Nodo `LoadImage` · `blue_poppies_field.png`

### 

​

Pasos para ejecutar el flujo de trabajo

Este flujo de trabajo muestra cómo generar una respuesta con Tencent HY y, si lo necesitas, guardar esa conversación en ComfyUI. Carga una imagen de referencia, ejecuta el grafo y lee la respuesta en `Preview Any`. Si quieres una copia guardada, mantén `Save Text` para escribir el prompt y la respuesta en `output/Hy4/`; si no necesitas guardar, omite o elimina ese nodo.

### 

​

Consejos para los prompts

  * Indica el formato de salida. La línea de la plantilla `Only output positive prompt, no extra explanations` es lo que mantiene la respuesta lista para pegar
  * Cuando conectes varias imágenes, refiérete a ellas en orden (`the first image`, `the second image`) para que los detalles correspondan a la imagen correcta
  * Coloca las instrucciones repetidas en `system_prompt` y deja `prompt` para la tarea, por ejemplo `You write photography prompts for a stock library`
  * La `seed` solo decide si el nodo se vuelve a ejecutar. Las respuestas siguen variando entre ejecuciones



## 

​

Empezar

Actualiza ComfyUI, busca `Tencent: Hy4` en la Biblioteca de plantillas y abre el flujo de trabajo de imagen a prompt. Tencent HY4 factura según el consumo de tokens de la API. Consulta la [tabla de precios](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas de Hy4.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/tencent/hy-4.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/tencent/hy-4)

[Generación de imágenes](https://docs.comfy.org/es/tutorials/partner-nodes/runway/image-generation)[HY Image 3.5](https://docs.comfy.org/es/tutorials/partner-nodes/tencent/hy-image-3-5)
