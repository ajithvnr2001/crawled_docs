---
url: https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-image-2-0/
title: Grok Imagine Image 2.0 en ComfyUI: generaci\u00f3n y edici\u00f3n de im\u00e1genes con IA - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:49.329559+00:00
---

# Grok Imagine Image 2.0 en ComfyUI: generación y edición de imágenes con IA - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-image-2-0/

## En esta página

Volver arriba

  * Para qué sirve Grok Imagine Image 2.0
  * Salidas de ejemplo
  * Grok Imagine Image 2.0: Texto a imagen
    * Resumen del flujo de trabajo
    * Pasos para ejecutar
  * Grok Imagine Image 2.0: Edición de imágenes
    * Resumen del flujo de trabajo
    * Pasos para ejecutar



Grok

# Grok Imagine Image 2.0 en ComfyUI: generación y edición de imágenes con IA

Copiar páginaCopiar página

Genera y edita imágenes con Grok Imagine Image 2.0 en ComfyUI: motor Aurora, texto corto nítido, salida 1K/2K y hasta 3 imágenes de referencia

Copiar páginaCopiar página

Grok Imagine Image 2.0 es el modelo de imágenes más reciente de xAI, disponible en ComfyUI a través de los Nodos asociados de Grok. Basado en el motor Aurora, sobresale en el renderizado nítido de textos cortos y genera imágenes de 1K o 2K en 14 relaciones de aspecto, por lo que es muy adecuado para pósters, portadas, visuales de producto y marca, y escenas con personajes donde la consistencia importa.

## 

​

Para qué sirve Grok Imagine Image 2.0

  * **Texto corto nítido** : el motor Aurora procesa el texto corto con nitidez, lo que lo hace ideal para pósteres, portadas y piezas visuales de producto y marca
  * **Edición de imágenes guiada por referencias** : edita imágenes con instrucciones precisas en lenguaje natural y hasta 3 imágenes de referencia para modificar elementos, cambiar fondos o reestilizar escenas
  * **Consistencia de personajes** : mantiene a un personaje consistente en varias salidas dentro de escenas centradas en personajes
  * **14 relaciones de aspecto** : desde `1:1` hasta `9:20`
  * **Control de costos** : resolución 1K o 2K con opciones de calidad baja o media para equilibrar costo y fidelidad



## 

​

Salidas de ejemplo

Generación de texto a imagen con estilo de póster y un renderizado de texto nítido: ![Salida de texto a imagen de Grok Imagine Image 2.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_2_t2i.png) Edición de imágenes guiada por imágenes de referencia de personajes y productos: ![Salida de edición de imágenes de Grok Imagine Image 2.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_2_image_edit.png)

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

Grok Imagine Image 2.0: Texto a imagen

Genera una imagen completa estilo póster a partir de un solo prompt de texto con el motor Aurora. Este flujo de trabajo destaca en el renderizado nítido de texto corto, lo que lo hace muy adecuado para pósteres, portadas, visuales de producto y marca, y escenas centradas en personajes. Genera imágenes de 1K o 2K en 14 relaciones de aspecto, con opciones de calidad baja o media para controlar el costo. ![Vista previa del flujo de trabajo de texto a imagen de Grok Imagine Image 2.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_2_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Grok Imagine Image 2.0” en la Biblioteca de plantillas

![Salida de texto a imagen de Grok Imagine Image 2.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_2_t2i.png)

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa dos nodos:

  * **GrokImageNode** : el nodo principal, configurado con el modelo `grok-imagine-image-2.0`
  * **SaveImageAdvanced** : guarda la imagen generada como PNG



### 

​

Pasos para ejecutar

  1. **Introduce tu prompt** : describe la escena, el estilo y cualquier texto que quieras renderizar en **GrokImageNode**
  2. **Elige la relación de aspecto** : escoge entre 14 relaciones, desde `1:1` hasta `9:20`
  3. **Selecciona la resolución** : `1K` para resultados más rápidos o `2K` para más detalle
  4. **Define la calidad** : `low` o `medium` para controlar el costo y la fidelidad
  5. **Define la semilla** : controla si el nodo se vuelve a ejecutar; las salidas no son reproducibles sin importar la semilla
  6. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



## 

​

Grok Imagine Image 2.0: Edición de imágenes

Edita imágenes con instrucciones precisas en lenguaje natural y hasta 3 imágenes de referencia. Usa este flujo de trabajo para modificar elementos específicos, cambiar fondos, reestilizar escenas o mantener un personaje consistente en varias salidas. El motor Aurora ofrece un renderizado nítido de textos cortos en resolución 1K o 2K y en 14 relaciones de aspecto. ![Vista previa del flujo de trabajo de edición de imágenes de Grok Imagine Image 2.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_2_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Grok Imagine Image 2.0” en la Biblioteca de plantillas

![Resultado de la edición de imágenes de Grok Imagine Image 2.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_2_image_edit.png)

### 

​

Resumen del flujo de trabajo

Este flujo de trabajo usa cuatro nodos:

  * **LoadImage** x2: proporciona las imágenes de referencia del personaje y del producto (el nodo acepta hasta 3)
  * **GrokImageEditNodeV2** : el nodo principal, configurado con el modelo `grok-imagine-image-2.0`
  * **SaveImage** : guarda la imagen editada



### 

​

Pasos para ejecutar

  1. **Carga tus referencias** : conecta hasta 3 imágenes de referencia a los nodos **LoadImage**
  2. **Describe la edición** : indica al modelo qué mantener, cambiar o reestilizar en el prompt de **GrokImageEditNodeV2**
  3. **Establece la resolución** : `1K` o `2K`
  4. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/grok/grok-image-2-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/grok/grok-image-2-0)

[Grok Image](https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-image)[Grok Image Quality](https://docs.comfy.org/es/tutorials/partner-nodes/grok/grok-image-quality)
