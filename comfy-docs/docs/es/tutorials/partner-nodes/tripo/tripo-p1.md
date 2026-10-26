---
url: https://docs.comfy.org/es/tutorials/partner-nodes/tripo/tripo-p1/
title: Tripo P1 en ComfyUI: generaci\u00f3n 3D a partir de texto, imagen y m\u00faltiples vistas - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:56.145638+00:00
---

# Tripo P1 en ComfyUI: generación 3D a partir de texto, imagen y múltiples vistas - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/tripo/tripo-p1/

## En esta página

Volver arriba

  * Para qué es bueno Tripo P1
  * Tripo P1: Texto a modelo
    * Pasos para ejecutar
    * Nodos clave del procesamiento
  * Tripo P1: Imagen a modelo
    * Pasos para ejecutar
  * Tripo P1: de varias vistas a modelo
    * Pasos para ejecutar
    * Consejos de entrada



Tripo

# Tripo P1 en ComfyUI: generación 3D a partir de texto, imagen y múltiples vistas

Copiar páginaCopiar página

Genera modelos 3D con Tripo P1 en ComfyUI desde texto, una sola imagen o referencias multivista: topología limpia, texturizado, rigging y retargeting.

Copiar páginaCopiar página

Los nodos asociados [Tripo P1](https://docs.comfy.org/es/built-in-nodes/TripoP1ImageToModelNode) permiten generar modelos 3D de forma rápida y con alta calidad a partir de prompts de texto, una sola imagen o referencias de múltiples vistas. Los modelos generados incluyen una topología limpia, presupuestos de polígonos optimizados y soporte para texturizado, rigging y retargeting. Están listos para usarse en motores de juego y aplicaciones 3D.

## 

​

Para qué es bueno Tripo P1

  * **Entradas flexibles** : Genera modelos 3D a partir de prompts de texto, una sola imagen o referencias multivista
  * **Topología limpia** : Los modelos incluyen topología limpia y presupuestos de polígonos optimizados
  * **Texturizado, rigging y retargeting** : Los modelos generados admiten texturizado, rigging y retargeting
  * **Salida lista para juegos** : Los recursos están listos para usarse en motores de juego y aplicaciones 3D



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

Tripo P1: Texto a modelo

Genera un modelo 3D a partir de una descripción de texto. ![Flujo de trabajo de Tripo P1 Texto a modelo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p1_text_to_model-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Tripo P1: Text to Model” en la Biblioteca de plantillas

### 

​

Pasos para ejecutar

  1. **Introduce tu prompt** : describe el modelo 3D en el nodo **TripoP1TextToModelNode**
  2. **Selecciona el modo de textura** : elige entre Textured, None o PBR
  3. **Activa el refinamiento** : alterna el remallado de quad para obtener una topología más limpia
  4. **Define la semilla** : controla la reproducibilidad
  5. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar
  6. **Previsualiza y exporta** : usa el nodo **Preview3D** para inspeccionar y **SaveGLB** para exportar



### 

​

Nodos clave del procesamiento

Después de la generación inicial, el flujo de trabajo procesa automáticamente el modelo mediante:

  * **TripoTextureNode** : aplica materiales y texturas
  * **TripoConversionNode** : convierte a formato GLTF (u otros formatos de exportación)
  * **TripoRigNode** : agrega un esqueleto para animación
  * **TripoRetargetNode** : aplica una animación predefinida (predeterminada: idle)



## 

​

Tripo P1: Imagen a modelo

Genera un modelo 3D a partir de una sola imagen de referencia. ![Flujo de trabajo de Tripo P1 de imagen a modelo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p1_image_to_model-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Tripo P1: Image to Model” en la Biblioteca de plantillas

### 

​

Pasos para ejecutar

  1. **Sube una imagen de referencia** : usa el nodo **LoadImage** para cargar una imagen de frente de tu sujeto
  2. **Selecciona el modo de textura** : elige Textured, None o PBR
  3. **Activa el refinamiento** : alterna el remallado en quads
  4. **Elige el tipo de textura** : las opciones incluyen `original_image` o `standard`
  5. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



## 

​

Tripo P1: de varias vistas a modelo

Genera un modelo 3D a partir de imágenes de varios puntos de vista para lograr mayor precisión. ![Flujo de trabajo de Tripo P1: de varias vistas a modelo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p1_mv_to_model-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Tripo P1: Multiview to Model” en la Biblioteca de plantillas

### 

​

Pasos para ejecutar

  1. **Sube imágenes de varias vistas** : usa varios nodos **LoadImage** para el frente, la izquierda, la parte trasera y otros ángulos
  2. **Selecciona el modo de textura** : elige Textured, None o PBR
  3. **Elige el nivel de detalle** : las opciones incluyen `standard` y `detailed`
  4. **Configura las referencias de textura** : elige qué imagen define la textura
  5. **Haz clic en Queue** : presiona `Ctrl+Enter` para generar



### 

​

Consejos de entrada

  * Proporciona al menos **vistas de frente y de perfil** para obtener mejores resultados
  * Asegúrate de que la iluminación y la pose sean consistentes en todas las imágenes de referencia
  * Las imágenes de entrada de mayor calidad producen una salida con mejores texturas



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/tripo/tripo-p1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/tripo/tripo-p1)

[Tripo P2](https://docs.comfy.org/es/tutorials/partner-nodes/tripo/tripo-p2)[Tripo 3 1](https://docs.comfy.org/es/tutorials/partner-nodes/tripo/tripo-3-1)
