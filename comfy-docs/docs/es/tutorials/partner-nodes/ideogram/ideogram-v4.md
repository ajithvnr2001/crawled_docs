---
url: https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-v4/
title: Ideogram 4.0 en ComfyUI: texto a imagen con prompts JSON - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:50.606406+00:00
---

# Ideogram 4.0 en ComfyUI: texto a imagen con prompts JSON - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-v4/

## En esta página

Volver arriba

  * En qué destaca Ideogram 4.0
  * Salidas de ejemplo
  * Conversación en vivo con Ideogram y ComfyOrg
  * Úsalo
  * Flujo de trabajo de texto a imagen con el nodo asociado Ideogram 4.0
    * Formato del prompt
    * Pasos del flujo de trabajo
    * Usar el generador de prompts JSON (opcional)
  * Notas adicionales



Ideogram

# Ideogram 4.0 en ComfyUI: texto a imagen con prompts JSON

Copiar páginaCopiar página

Genera imágenes con Ideogram 4.0 en ComfyUI desde lenguaje natural o prompts JSON, con control del diseño, las paletas de color y el texto renderizado.

Copiar páginaCopiar página

Ideogram 4.0 es un modelo de texto a imagen de Ideogram que ofrece calidad fotorrealista, renderizado de texto preciso y control de estilo preciso. Puedes usar lenguaje natural sin más o **prompts JSON estructurados** para un control detallado de la disposición, los colores y el texto dentro de la imagen. Ideogram 4.5 es el modelo más reciente de la familia y tiene su propia página: [Ideogram 4.5 en ComfyUI](https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-4-5).

## 

​

En qué destaca Ideogram 4.0

  * **Calidad fotorrealista** : Fotorrealismo superior en las imágenes generadas
  * **Representación precisa del texto** : Representa texto literal en la imagen, ideal para composiciones tipo póster
  * **Control preciso del estilo** : Los prompts JSON estructurados controlan la paleta de estilo, la ubicación de los elementos (`bbox`) y las paletas de color por elemento
  * **Prompts flexibles** : Acepta lenguaje natural sencillo para ideas rápidas o JSON estructurado para un control detallado
  * **No necesitas prompts negativos** : Usa orientación asimétrica sin clasificador en lugar de una cadena de prompt negativo independiente



## 

​

Salidas de ejemplo

Generación de texto a imagen a partir de un prompt JSON estructurado: ![Salida de ejemplo de Ideogram 4.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_ideogram_v4_t2i.png) _Salida de ejemplo de la API de Ideogram 4.0_

## 

​

Conversación en vivo con Ideogram y ComfyOrg

Una conversación en vivo especial con Mohammad Norouzi (CEO de Ideogram) y Yoland Yan (CEO de ComfyOrg), presentada por Purz y Rob.

## 

​

Úsalo

## Llámalo desde código

Llámalo por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript, Swift y cURL listos para copiar y pegar

Esto usa la misma cuenta de Comfy y consume los mismos créditos que ejecutarlo en ComfyUI más abajo. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Flujo de trabajo de texto a imagen con el nodo asociado Ideogram 4.0

![Vista previa del flujo de trabajo de texto a imagen de Ideogram 4.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Ideogram v4: Text to Image (API)” en la Biblioteca de plantillas

![Salida de ejemplo de Ideogram 4.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_ideogram_v4_t2i.png) _Salida de ejemplo de la API de Ideogram 4.0_

### 

​

Formato del prompt

El nodo Ideogram V4 admite dos formatos de prompt:

  1. **Lenguaje natural** : simple e intuitivo, ideal para ideas rápidas.
  2. **JSON estructurado** : ofrece control detallado sobre la paleta de estilos, la ubicación de los elementos (`bbox`) y la representación de texto literal en la imagen. RECOMENDADO para composiciones tipo póster.

El flujo de trabajo de ejemplo predeterminado usa un prompt JSON estructurado que incluye:

  * `high_level_description`: descripción general de la escena
  * `style_description`: estética, iluminación, medio y paleta de colores
  * `compositional_deconstruction`: cuadros delimitadores, descripciones y paletas de colores por elemento



### 

​

Pasos del flujo de trabajo

  1. Descarga y arrastra el archivo del flujo de trabajo a ComfyUI
  2. El nodo `Ideogram V4` ya contiene un prompt JSON estructurado predeterminado: puedes modificarlo o escribir lenguaje natural simple
  3. Haz clic en `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen
  4. DESPUÉS de que la API devuelva los resultados, revisa la imagen generada en el nodo `Save Image`. Las imágenes se guardan en el directorio `ComfyUI/output/`



### 

​

Usar el generador de prompts JSON (opcional)

El flujo de trabajo incluye un nodo **Gemini** integrado (Gemini 3.1 Pro) que te ayuda a construir prompts JSON estructurados:

  1. Describe tu idea en el campo de prompt de usuario del nodo Gemini
  2. El modelo generará un prompt JSON que coincide con el esquema
  3. Conecta la salida `STRING` a la entrada `prompt` del nodo `Ideogram V4`
  4. Ejecuta el flujo de trabajo



## 

​

Notas adicionales

  * **No necesitas prompts negativos** : el modelo Ideogram 4.0 usa orientación asimétrica sin clasificador, donde la pasada incondicional descarta los tokens de texto, en lugar de requerir una cadena de prompt negativa independiente.
  * **Creación de prompts asistida por el modelo** : considera usar **Ideogram 4 Prompt Builder** (KJNodes) para tener control visual sobre la construcción de prompts en ComfyUI.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/ideogram/ideogram-v4.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/ideogram/ideogram-v4)

[Ideogram P Image](https://docs.comfy.org/es/tutorials/partner-nodes/ideogram/ideogram-p-image)[Krea 3](https://docs.comfy.org/es/tutorials/partner-nodes/krea/krea-3)
