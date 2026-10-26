---
url: https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2/
title: Nano Banana 2 - Generaci\u00f3n r\u00e1pida de im\u00e1genes con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:49.167575+00:00
---

# Nano Banana 2 - Generación rápida de imágenes con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2/

## En esta página

Volver arriba

  * En qué destaca Nano Banana 2
  * Salidas de ejemplo
  * Usarlo
  * Flujo de trabajo de edición de imagen con Nano Banana 2
  * Flujo de trabajo de hoja de vistas de personaje
  * ¿Qué modelo deberías elegir?
  * Empezar



Google

# Nano Banana 2 - Generación rápida de imágenes con IA

Copiar páginaCopiar página

Genera imágenes de alta calidad con calidad Pro a velocidad Flash usando Nano Banana 2 en ComfyUI

Copiar páginaCopiar página

Nano Banana 2 ya está disponible en ComfyUI a través de los Nodos asociados. Este lanzamiento cambia de forma fundamental la opción predeterminada para la mayoría de los creadores, ya que ofrece calidad de nivel Pro a la velocidad de Flash.

## 

​

En qué destaca Nano Banana 2

  * **Calidad de nivel profesional a la velocidad de Flash** : texturas más ricas, detalles más nítidos, iluminación más sólida y mejor adherencia al prompt sin la penalización de latencia
  * **Conocimiento del mundo basado en búsquedas** : activa de forma inteligente la fundamentación en Google Image Search para mejorar la precisión de los datos en puntos de referencia poco conocidos, objetos de nicho o detalles del mundo real
  * **Consistencia del sujeto** : mantén el parecido de hasta 5 personajes y la fidelidad de hasta 14 objetos en un solo flujo de trabajo
  * **Niveles de razonamiento configurables** : controla cuánto “piensa” el modelo antes de generar (Minimal para exploración rápida, High/Dynamic para composiciones complejas)
  * **Renderizado y traducción de texto de precisión** : genera texto preciso y legible para maquetas de marketing, tarjetas de felicitación y recursos localizados



## 

​

Salidas de ejemplo

Reemplazo de texto en una imagen existente, manteniendo la calidad intacta: ![Comparación de calidad](https://substack-post-media.s3.amazonaws.com/public/images/1f92ae2e-14d8-4a3b-9ed7-e57dacd2584f_1825x1696.png) _Reemplaza el texto de la imagen de entrada con: Nano Banana 2 Available on ComfyUI Cheaper and Faster_ Conocimiento del mundo fundamentado en búsqueda para infografías factualmente precisas: ![Infografía educativa](https://substack-post-media.s3.amazonaws.com/public/images/edfe3b6b-8942-472e-8772-a3700946fc23_1024x559.png) _Infografía de estilo cómic educativo que explica cinco especies nativas de Norteamérica poco conocidas, con fundamentación en búsqueda para garantizar representaciones precisas de hábitats raros y roles ecológicos._ ![Infografía sobre la cultura del skateboard](https://substack-post-media.s3.amazonaws.com/public/images/536b845b-b278-4924-b8e4-114e5e5defa9_2752x1536.png) _Infografía de estilo cómic sobre la evolución de la cultura del skateboard estadounidense desde los años 70 hasta los 2020._ Consistencia del sujeto a lo largo de una secuencia de storyboard: ![Consistencia del sujeto](https://substack-post-media.s3.amazonaws.com/public/images/e38f7afb-9752-49a1-9e6c-1ea99dba42ff_4908x2626.png) _Mantén la semejanza del personaje y la fidelidad del objeto en todas las secuencias de storyboard._ Niveles de pensamiento configurables para distintas profundidades de razonamiento: ![Comparación de niveles de pensamiento](https://substack-post-media.s3.amazonaws.com/public/images/6d0d4773-3ff5-4319-bc00-8afb62c2a1ad_4608x1332.png) _Retrato cinematográfico con distintos niveles de pensamiento: Minimal para iteraciones rápidas, High para salidas detalladas._ ![Retrato Art Nouveau](https://substack-post-media.s3.amazonaws.com/public/images/49e5f98a-b375-4fda-b280-7b695f535807_4608x1332.png) _Retrato inspirado en el Art Nouveau con profundidad de razonamiento configurable._ Renderizado y traducción de texto a variantes localizadas: ![Renderizado de texto](https://substack-post-media.s3.amazonaws.com/public/images/808ca8d0-acac-470d-a666-23e411254276_1376x768.png) _Fotografía amateur tomada con celular con renderizado de texto de graffiti estilizado._ ![Traducción al español](https://substack-post-media.s3.amazonaws.com/public/images/6af9b091-7bbe-49da-b70f-e766394039ef_2784x1536.png) _Traduce el texto al español._ ![Traducción al hindi](https://substack-post-media.s3.amazonaws.com/public/images/548d44f6-d43e-484f-a8d8-37638f9ff482_2784x1536.png) _Traduce el texto al hindi._ ![Traducción al mandarín](https://substack-post-media.s3.amazonaws.com/public/images/5f4a52f9-1995-440f-8394-245e43f3a9a2_2784x1536.png) _Traduce el texto al mandarín._

## 

​

Usarlo

## Llámalo desde código

Llámalo por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript, Swift y cURL listos para copiar y pegar

Esto se ejecuta en la misma cuenta de Comfy y se factura con los mismos créditos que ejecutarlo en ComfyUI más abajo. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Flujo de trabajo de edición de imagen con Nano Banana 2

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Nano Banana 2” en la Biblioteca de plantillas

![Vista previa del flujo de trabajo de Nano Banana 2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana2_image_edit-1.webp)

## Descargar imagen de entrada de ejemplo

Obtén la imagen de entrada de ejemplo para este flujo de trabajo

## 

​

Flujo de trabajo de hoja de vistas de personaje

Genera una hoja de vistas de personaje a partir de una sola imagen de referencia: vistas de frente, de lado y de espaldas del mismo sujeto en una sola hoja. La hoja alimenta directamente el flujo de trabajo [Pixal3D Multi Views to 3D](https://docs.comfy.org/es/tutorials/3d/pixal3d#pixal3d-multi-views), o puedes usarla como hoja de referencia de personaje para la generación de video e imágenes.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Character Turnaround Sheet Generator” en la Biblioteca de plantillas

![Vista previa del flujo de trabajo de hoja de vistas de personaje](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana_create_turnaround_sheet-1.webp)

## Descargar imagen de entrada de ejemplo

Obtén la imagen de entrada de ejemplo para este flujo de trabajo

## 

​

¿Qué modelo deberías elegir?

Modelo| Ideal para  
---|---  
**Nano Banana 2**|  La mayoría de los creadores: suficientemente rápido para explorar, suficientemente inteligente para refinar y suficientemente pulido para publicar  
**Nano Banana Pro**|  Máxima precisión factual y casos límite de alto riesgo  
  
## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Haz doble clic en el lienzo y busca el nodo “Nano Banana 2”
  3. O ve a la Biblioteca de plantillas para usar el flujo de trabajo listo para usar
  4. Elige tu resolución, define la relación de aspecto y decide si el prompt necesita un razonamiento más profundo



La nueva versión del modelo también se agregó al nodo anterior “Nano Banana Pro”. Si tienes flujos de trabajo antiguos con este nodo, no necesitas reconstruirlos: solo vuelve a seleccionar la versión del modelo.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/google/nano-banana-2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/google/nano-banana-2)

[Nano Banana Pro](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-pro)[Nano Banana 2 Lite](https://docs.comfy.org/es/tutorials/partner-nodes/google/nano-banana-2-lite)
