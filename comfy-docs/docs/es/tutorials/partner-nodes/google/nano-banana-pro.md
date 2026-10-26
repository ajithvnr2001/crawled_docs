---
url: https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-pro/
title: Nano Banana Pro: generaci\u00f3n de im\u00e1genes con IA de calidad de estudio - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:48.948173+00:00
---

# Nano Banana Pro: generación de imágenes con IA de calidad de estudio - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-pro/

## En esta página

Volver arriba

  * En qué destaca Nano Banana Pro
  * Ejemplos de salidas
  * Úsalo
  * Nano Banana Pro
  * ¿Qué modelo deberías elegir?
  * Empezar



Google

# Nano Banana Pro: generación de imágenes con IA de calidad de estudio

Copiar páginaCopiar página

Genera y edita imágenes 4K listas para producción con Nano Banana Pro (Gemini 3 Pro Image) en ComfyUI, con texto avanzado y consistencia de personajes.

Copiar páginaCopiar página

Nano Banana Pro es el modelo de imagen insignia de Google DeepMind (Gemini 3 Pro Image) para generar y editar imágenes con calidad de estudio. Va más allá de la creación casual y llega a visuales listos para producción, con capacidades avanzadas como resolución 4K nativa, renderizado de texto preciso en 10 idiomas, mezcla de varias imágenes y conocimiento del mundo basado en búsqueda para representar con precisión el mundo real.

## 

​

En qué destaca Nano Banana Pro

  * **Generación en 4K** : crea y edita imágenes en resolución 4K nativa con corrección de color de calidad de estudio, control de ángulo y ajustes de enfoque
  * **Conocimiento del mundo** : genera imágenes precisas del mundo real aprovechando la base de conocimiento de Google Search para monumentos poco conocidos, objetos de nicho y detalles culturales
  * **Texto y traducción** : renderiza texto limpio y legible, y admite detección y traducción en 10 idiomas
  * **Combinación de varias imágenes** : combina hasta 14 imágenes con un control compositivo preciso
  * **Consistencia de personajes y sujetos** : mantén el parecido de los personajes y la fidelidad de los objetos en composiciones complejas con varios sujetos
  * **Razonamiento avanzado** : niveles de pensamiento configurables. Elige Minimal para una exploración rápida o High/Dynamic para diseños complejos y un control preciso



## 

​

Ejemplos de salidas

Mezcla de varias imágenes: combina dos imágenes de referencia en un solo resultado con calidad de estudio: ![Ejemplo de Nano Banana Pro](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_pro.png)

## 

​

Úsalo

## Llámalo desde código

Llámalo por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript, Swift y cURL listos para copiar y pegar

Esto se ejecuta en la misma cuenta de Comfy y se factura con los mismos créditos que ejecutarlo en ComfyUI a continuación. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Nano Banana Pro

Nano-banana Pro (Gemini 3.0 Pro Image) para generación y edición de imágenes 4K con calidad de estudio, con mejor renderizado de texto y consistencia de personajes. ![Nano Banana Pro workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_pro-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Nano Banana Pro” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` correspondientes:

## api_nano_banana_pro_input_image_1.png

Nodo `LoadImage` 11 · `api_nano_banana_pro_input_image_1.png`

## api_nano_banana_pro_input_image_2.png

Nodo `LoadImage` 12 · `api_nano_banana_pro_input_image_2.png`

**Ejemplo de salida** ![Nano Banana Pro example](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_nano_banana_pro.png)

## 

​

¿Qué modelo deberías elegir?

Modelo| Ideal para  
---|---  
**[Nano Banana 2 Lite](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-lite)**|  Velocidad y costo: iteración rápida, pipelines de alto rendimiento, aplicaciones de baja latencia  
**[Nano Banana 2](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2)**|  La mayoría de los creadores: calidad y velocidad equilibradas para la generación y edición de imágenes de uso general  
**Nano Banana Pro**|  Casos de uso profesionales: máxima calidad, generación en 4K, diseños complejos y control preciso  
  
## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Haz doble clic en el lienzo y busca el nodo “Nano Banana Pro”
  3. O ve a la Biblioteca de plantillas para usar el flujo de trabajo listo para usar
  4. Sube tus imágenes de referencia, introduce tu prompt y selecciona el nivel de razonamiento deseado



Nano Banana Pro ofrece la salida de mayor calidad de la familia Nano Banana. Para una generación más rápida y a menor costo, considera [Nano Banana 2 Lite](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-lite) o [Nano Banana 2](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2).

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/google/nano-banana-pro.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/google/nano-banana-pro)

[Nano Banana 2.1](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-1)[Nano Banana 2](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2)
