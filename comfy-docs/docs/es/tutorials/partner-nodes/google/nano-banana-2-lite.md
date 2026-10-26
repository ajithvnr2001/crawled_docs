---
url: https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-lite/
title: Nano Banana 2 Lite: generaci\u00f3n r\u00e1pida de im\u00e1genes con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:49.092090+00:00
---

# Nano Banana 2 Lite: generación rápida de imágenes con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-lite/

## En esta página

Volver arriba

  * En qué destaca Nano Banana 2 Lite
  * Salidas de ejemplo
  * Usarlo
  * Flujos de trabajo
    * Texto a imagen
    * Edición de imagen
  * ¿Qué modelo deberías elegir?
  * Empezar



Google

# Nano Banana 2 Lite: generación rápida de imágenes con IA

Copiar páginaCopiar página

Genera imágenes con la máxima velocidad y el menor costo de Google usando Nano Banana 2 Lite, el modelo Gemini 3.1 Flash-Lite Image en ComfyUI

Copiar páginaCopiar página

Nano Banana 2 Lite es el modelo Gemini Image más rápido y con mejor relación costo-eficiencia de Google DeepMind, diseñado para la ideación rápida y los flujos de trabajo de gran volumen. Impulsado por `gemini-3.1-flash-lite-image`, ofrece generación de texto a imagen en aproximadamente 4 segundos a $0.041 por imagen, lo que lo hace ideal para la visualización rápida de conceptos, la creación de prototipos ágiles y la exploración iterativa de diseño.

## 

​

En qué destaca Nano Banana 2 Lite

  * **Generación ultrarrápida** : salidas de texto a imagen en tan solo 4 segundos, pensadas para prototipado interactivo y borradores visuales rápidos
  * **Costo eficiente** : con un precio de $0.041 por imagen de resolución 1K, la opción más asequible de la familia Nano Banana
  * **Consistencia de personajes** : mantén la identidad de los personajes y la fidelidad de los objetos en varias generaciones rápidas
  * **Renderizado de texto en la imagen** : redacta el texto publicitario y renderiza texto legible directamente en las imágenes generadas para variaciones de anuncios localizadas
  * **Selección de modelo configurable** : elige entre Nano Banana 2 Lite, Nano Banana 2 y Nano Banana Pro dentro del mismo nodo



## 

​

Salidas de ejemplo

Generación de texto a imagen a partir de un solo prompt: ![Nano Banana 2 Lite Texto a imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_lite_t2i.png) Edición de imagen a partir de una instrucción de texto: ![Nano Banana 2 Lite Edición de imagen - Salida](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_lite_image_edit.png)

## 

​

Usarlo

## Llámalo desde el código

Llámalo por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript, Swift y cURL listos para copiar y pegar

Esto se ejecuta en la misma cuenta de Comfy y se factura con los mismos créditos que ejecutarlo en ComfyUI más abajo. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Flujos de trabajo

### 

​

Texto a imagen

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Nano Banana 2 Lite” en la Biblioteca de plantillas

Genera imágenes a partir de descripciones de texto. No necesitas archivos de entrada: solo escribe tu prompt y el flujo de trabajo produce una o más imágenes generadas con soporte para entradas intercaladas de texto e imagen. ![Nano Banana 2 Lite Texto a imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_lite_t2i.png)

### 

​

Edición de imagen

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Nano Banana 2 Lite” en la Biblioteca de plantillas

## Descargar imagen de ejemplo

Obtén la imagen de entrada de ejemplo para este flujo de trabajo

Sube una imagen y proporciona una instrucción de texto para editarla. El flujo de trabajo produce una comparación lado a lado del resultado original y el editado.

![Nano Banana 2 Lite Edición de imagen - Entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/red_f1_track_car.png)![Nano Banana 2 Lite Edición de imagen - Salida](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_2_lite_image_edit.png)

## 

​

¿Qué modelo deberías elegir?

Modelo| Ideal para  
---|---  
**Nano Banana 2 Lite**|  Velocidad y costo: iteración rápida, pipelines de alto rendimiento y aplicaciones de baja latencia  
**[Nano Banana 2](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2)**|  La mayoría de los creadores: calidad y velocidad equilibradas para la generación y edición de imágenes de uso general  
**[Nano Banana Pro](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-pro)**|  Casos de uso profesionales: máxima calidad, generación en 4K, diseños complejos y control preciso  
  
## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Haz doble clic en el lienzo y busca el nodo “Nano Banana 2” (incluye Nano Banana 2 Lite como opción de modelo)
  3. O ve a la Biblioteca de plantillas para usar el flujo de trabajo listo para usar
  4. Selecciona “Nano Banana 2 Lite” en el menú desplegable de modelo para la generación más rápida



Nano Banana 2 Lite está disponible dentro del nodo Nano Banana 2 existente. Si tienes flujos de trabajo antiguos que usan este nodo, puedes seleccionar “Nano Banana 2 Lite” en el menú desplegable de versión del modelo sin reconstruir tu flujo de trabajo.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/google/nano-banana-2-lite.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/google/nano-banana-2-lite)

[Nano Banana 2](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2)[Descripción general](https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-overview)
