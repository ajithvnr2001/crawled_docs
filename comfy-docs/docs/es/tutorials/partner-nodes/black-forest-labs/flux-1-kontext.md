---
url: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-1-kontext/
title: FLUX.1 Kontext en ComfyUI: edici\u00f3n de im\u00e1genes con Pro y Max - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:46.215825+00:00
---

# FLUX.1 Kontext en ComfyUI: edición de imágenes con Pro y Max - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-1-kontext/

## En esta página

Volver arriba

  * En qué destaca FLUX.1 Kontext
  * Salidas de ejemplo
  * Úsalo
  * Flujo de trabajo con múltiples imágenes de entrada de FLUX.1 Kontext
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Completar el flujo de trabajo paso a paso
  * Flujo de trabajo de nodos asociados de FLUX.1 Kontext Pro Image
    * 1\. Descargar el archivo de flujo de trabajo
    * 2\. Completar el flujo de trabajo paso a paso
  * Flujo de trabajo de nodos asociados de FLUX.1 Kontext Max Image
    * 1\. Descargar el archivo de flujo de trabajo
    * 2\. Completar el flujo de trabajo paso a paso
  * Técnicas de prompts para FLUX Kontext
    * 1\. Modificaciones básicas
    * 2\. Transferencia de estilo
    * 3\. Consistencia de personajes
    * 4\. Edición de texto
  * Soluciones a problemas comunes
    * El personaje cambia demasiado
    * Cambios en la posición de la composición
    * Aplicación imprecisa del estilo
  * Principios fundamentales
  * Plantillas de buenas prácticas



Black Forest Labs

# FLUX.1 Kontext en ComfyUI: edición de imágenes con Pro y Max

Copiar páginaCopiar página

Edita imágenes en ComfyUI con los nodos asociados FLUX.1 Kontext Pro y Max: cambios de objetos y estilo, fondo, consistencia de personajes y texto.

Copiar páginaCopiar página

FLUX.1 Kontext es un modelo profesional de edición de imagen a imagen desarrollado por Black Forest Labs, centrado en la comprensión inteligente del contexto de la imagen y en la edición precisa. Puede realizar diversas tareas de edición sin descripciones complejas, como la modificación de objetos, la transferencia de estilo, el reemplazo de fondo, la edición con consistencia de personajes y la edición de texto. La ventaja principal de Kontext reside en su excelente capacidad para comprender el contexto y mantener la consistencia de los personajes, lo que garantiza que elementos clave como los rasgos del personaje y la composición se mantengan estables incluso después de múltiples iteraciones de edición. Actualmente, ComfyUI es compatible con dos modelos de FLUX.1 Kontext:

  * **Kontext Pro** es ideal para editar, componer y remezclar.
  * **Kontext Max** lleva al límite la tipografía, la precisión del prompt y la velocidad.



## 

​

En qué destaca FLUX.1 Kontext

  * **Edición versátil sin descripciones complejas** : modificación de objetos, transferencia de estilo, reemplazo de fondo, edición con consistencia de personaje y edición de texto
  * **Comprensión del contexto** : la comprensión inteligente del contexto de la imagen permite realizar ediciones precisas y específicas
  * **Consistencia de personaje** : las características del personaje y la disposición de la composición se mantienen estables incluso después de varias iteraciones de edición
  * **Entrada de varias imágenes** : el nodo `Image Stitch` combina varias imágenes en una sola para editarla con FLUX.1 Kontext
  * **Dos niveles de modelo** : Kontext Pro para editar, componer y remezclar; Kontext Max para tipografía, precisión del prompt y velocidad



## 

​

Salidas de ejemplo

Edición de una entrada de varias imágenes unidas (una niña, un perro y un sofá combinados en una sola escena): ![Ejemplo de entrada de varias imágenes con FLUX.1 Kontext](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/multiple_image_input.png) Edición de imágenes con Kontext Pro, ideal para editar, componer y remezclar: ![Ejemplo de edición de imágenes con FLUX.1 Kontext Pro](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_pro_image.png) Edición de imágenes con Kontext Max, que lleva al límite la tipografía, la precisión del prompt y la velocidad: ![Ejemplo de edición de imágenes con FLUX.1 Kontext Max](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_max_image.png)

## 

​

Úsalo

## Llámalo desde código

Llama a Kontext Pro o Max por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript, Swift y cURL listos para pegar

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

Flujo de trabajo con múltiples imágenes de entrada de FLUX.1 Kontext

Recientemente actualizamos el soporte para flujos de trabajo con múltiples imágenes de entrada. Con el nuevo nodo `Image Stitch`, puedes unir varias imágenes en una sola y editarla con FLUX.1 Kontext.

### 

​

1\. Descargar el archivo del flujo de trabajo

Los `metadata` de las imágenes siguientes contienen la información del flujo de trabajo. Descárgalas y arrástralas a ComfyUI para cargar el flujo de trabajo correspondiente. ![Flujo de trabajo de los Nodos asociados de imagen de ComfyUI FLUX.1 Kontext Pro](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/multiple_image_input.png) Descarga las siguientes imágenes para usarlas como entrada o utiliza tus propias imágenes: ![Flujo de trabajo de los Nodos asociados de imagen de ComfyUI FLUX.1 Kontext Pro](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/girl.jpg) ![Flujo de trabajo de los Nodos asociados de imagen de ComfyUI FLUX.1 Kontext Pro](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/dog.jpg) ![Flujo de trabajo de los Nodos asociados de imagen de ComfyUI FLUX.1 Kontext Pro](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/multiple_image_input/sofa.jpg)

### 

​

2\. Completar el flujo de trabajo paso a paso

![Pasos del flujo de trabajo de los Nodos asociados de imagen de ComfyUI FLUX.1 Kontext Pro](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_multiple_image_input_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=bf6e2ac1877f37556b354699f1960129) Puedes seguir los pasos numerados de la imagen para completar el flujo de trabajo:

  1. Sube las imágenes proporcionadas en el nodo `Load image`
  2. Modifica los parámetros necesarios en `Flux.1 Kontext Pro Image`: 
     * `prompt` Ingresa el prompt de la imagen que quieres editar
     * `aspect_ratio` Define la relación de aspecto de la imagen original, que debe estar entre 1:4 y 4:1
     * `prompt_upsampling` Establece si se usa el upsampling de prompt. Si se activa, modificará automáticamente el prompt para obtener resultados más ricos, pero los resultados no son reproducibles
  3. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la edición de la imagen
  4. Después de esperar a que la API devuelva los resultados, puedes ver la imagen editada en el nodo `Save Image`, y la imagen correspondiente también se guardará en el directorio `ComfyUI/output/`



Los dos flujos de trabajo siguientes solo se diferencian en los Nodos asociados que utilizan. De hecho, solo necesitas modificar a partir del flujo de trabajo con múltiples imágenes de entrada, sin diferencias significativas.

## 

​

Flujo de trabajo de nodos asociados de FLUX.1 Kontext Pro Image

### 

​

1\. Descargar el archivo de flujo de trabajo

Los `metadata` de la imagen a continuación contienen la información del flujo de trabajo. Descárgala y arrástrala a ComfyUI para cargar el flujo de trabajo correspondiente. ![Flujo de trabajo de nodos asociados de FLUX.1 Kontext Pro Image de ComfyUI](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_pro_image.png) Descarga la imagen a continuación como entrada o usa tu propia imagen: ![Flujo de trabajo de nodos asociados de FLUX.1 Kontext Pro Image de ComfyUI](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_pro_image_input.png)

### 

​

2\. Completar el flujo de trabajo paso a paso

![Pasos del flujo de trabajo de nodos asociados de FLUX.1 Kontext Pro Image de ComfyUI](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_pro_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=ff2c42a34894ae54e32a24058ad12755) Puedes seguir los pasos numerados de la imagen para completar el flujo de trabajo:

  1. Carga la imagen que quieres editar en el nodo `Load Image`
  2. (Opcional) Modifica los parámetros necesarios en `Flux.1 Kontext Pro Image`
  3. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la edición de la imagen
  4. Después de esperar a que la API devuelva los resultados, puedes ver la imagen editada en el nodo `Save Image`, y la imagen correspondiente también se guardará en el directorio `ComfyUI/output/`



## 

​

Flujo de trabajo de nodos asociados de FLUX.1 Kontext Max Image

### 

​

1\. Descargar el archivo de flujo de trabajo

Los `metadata` de la imagen a continuación contienen la información del flujo de trabajo. Descárgala y arrástrala a ComfyUI para cargar el flujo de trabajo correspondiente. ![Flujo de trabajo de nodos asociados de FLUX.1 Kontext Max Image de ComfyUI](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_max_image.png) Descarga la imagen a continuación como entrada o usa tu propia imagen como demostración: ![Flujo de trabajo de nodos asociados de FLUX.1 Kontext Max Image de ComfyUI](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_kontext_max_image_input.png)

### 

​

2\. Completar el flujo de trabajo paso a paso

![Pasos del flujo de trabajo de nodos asociados de FLUX.1 Kontext Max Image de ComfyUI](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_kontext_max_image_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=3f91d4f54822bef88bca4e7024170950) Puedes seguir los pasos numerados de la imagen para completar el flujo de trabajo:

  1. Carga la imagen que quieres editar en el nodo `Load Image`
  2. (Opcional) Modifica los parámetros necesarios en `Flux.1 Kontext Max Image`
  3. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la edición de la imagen
  4. Después de esperar a que la API devuelva los resultados, puedes ver la imagen editada en el nodo `Save Image`, y la imagen correspondiente también se guardará en el directorio `ComfyUI/output/`



## 

​

Técnicas de prompts para FLUX Kontext

### 

​

1\. Modificaciones básicas

  * Simple y directo: `"Change the car color to red"`
  * Mantén el estilo: `"Change to daytime while maintaining the same style of the painting"`



### 

​

2\. Transferencia de estilo

**Principios:**

  * Nombra el estilo con claridad: `"Transform to Bauhaus art style"`
  * Describe las características: `"Transform to oil painting with visible brushstrokes, thick paint texture"`
  * Conserva la composición: `"Change to Bauhaus style while maintaining the original composition"`



### 

​

3\. Consistencia de personajes

**Marco de trabajo:**

  * Descripción específica: `"The woman with short black hair"` en lugar de “ella”
  * Conserva las características: `"while maintaining the same facial features, hairstyle, and expression"`
  * Modificaciones paso a paso: cambia primero el fondo y luego las acciones



### 

​

4\. Edición de texto

  * Usa comillas: `"Replace 'joy' with 'BFL'"`
  * Mantén el formato: `"Replace text while maintaining the same font style"`



## 

​

Soluciones a problemas comunes

### 

​

El personaje cambia demasiado

❌ Incorrecto: `"Transform the person into a Viking"` ✅ Correcto: `"Change the clothes to be a viking warrior while preserving facial features"`

### 

​

Cambios en la posición de la composición

❌ Incorrecto: `"Put him on a beach"` ✅ Correcto: `"Change the background to a beach while keeping the person in the exact same position, scale, and pose"`

### 

​

Aplicación imprecisa del estilo

❌ Incorrecto: `"Make it a sketch"` ✅ Correcto: `"Convert to pencil sketch with natural graphite lines, cross-hatching, and visible paper texture"`

## 

​

Principios fundamentales

  1. **Sé específico y claro** : usa descripciones precisas y evita términos vagos
  2. **Edición paso a paso** : divide las modificaciones complejas en varios pasos simples
  3. **Preservación explícita** : indica qué debe permanecer sin cambios
  4. **Selección de verbos** : usa “cambiar” y “reemplazar” en lugar de “transformar”



## 

​

Plantillas de buenas prácticas

**Modificación de objeto:** `"Change [object] to [new state], keep [content to preserve] unchanged"` **Transferencia de estilo:** `"Transform to [specific style], while maintaining [composition/character/other] unchanged"` **Reemplazo de fondo:** `"Change the background to [new background], keep the subject in the exact same position and pose"` **Edición de texto:** `"Replace '[original text]' with '[new text]', maintain the same font style"`

> **Recuerda:** Cuanto más específico, mejor. Kontext destaca por comprender instrucciones detalladas y mantener la consistencia.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/black-forest-labs/flux-1-kontext.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/black-forest-labs/flux-1-kontext)

[Imagen FLUX 1 1 Pro Ultra](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image)[Beeble Switchx](https://docs.comfy.org/es/tutorials/partner-nodes/beeble/beeble-switchx)
