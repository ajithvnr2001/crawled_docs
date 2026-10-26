---
url: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image/
title: FLUX 1.1 Pro Ultra en ComfyUI: texto a imagen de 4 MP y remix de im\u00e1genes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:46.115383+00:00
---

# FLUX 1.1 Pro Ultra en ComfyUI: texto a imagen de 4 MP y remix de imágenes - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image/

## En esta página

Volver arriba

  * En qué destaca FLUX 1.1 Pro Ultra Image
  * Salidas de ejemplo
  * Cómo usarlo
  * Documentación del nodo FLUX 1.1 Pro Ultra Image
  * Tutorial de texto a imagen con FLUX 1.1 [pro]
    * 1\. Descargar el archivo de flujo de trabajo
    * 2\. Completar los pasos del flujo de trabajo
  * Tutorial de imagen a imagen con FLUX 1.1[pro]
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Completar los pasos del flujo de trabajo



Black Forest Labs

# FLUX 1.1 Pro Ultra en ComfyUI: texto a imagen de 4 MP y remix de imágenes

Copiar páginaCopiar página

Usa el nodo asociado FLUX 1.1 Pro Ultra en ComfyUI para generar imágenes de 4 MP con los modos Ultra o Raw, además de remix de imagen a imagen.

Copiar páginaCopiar página

FLUX 1.1 Pro Ultra es una herramienta de generación de imágenes con IA de alto rendimiento de BlackForestLabs, que ofrece resolución ultra alta y capacidades de generación eficientes. Admite hasta 4 MP de resolución (4 veces la versión estándar) y mantiene el tiempo de generación de una sola imagen por debajo de los 10 segundos, 2.5 veces más rápido que modelos similares de alta resolución. La herramienta ofrece dos modos principales:

  * **Modo Ultra** : Diseñado para necesidades de alta resolución, perfecto para publicidad y comercio electrónico donde la ampliación de detalles es importante. Refleja con precisión los prompts mientras mantiene la velocidad de generación.
  * **Modo Raw** : Se centra en el realismo natural, optimizando tonos de piel, iluminación y detalles de paisajes. Reduce el “aspecto de IA” y es ideal para fotografía y creación de estilos realistas.



## 

​

En qué destaca FLUX 1.1 Pro Ultra Image

  * **Resolución ultra alta** : genera imágenes de hasta 4MP, 4 veces la resolución de la versión Estándar
  * **Generación rápida** : mantiene el tiempo de generación de una sola imagen por debajo de los 10 segundos, 2,5 veces más rápido que modelos similares de alta resolución
  * **Precisión del prompt a gran escala** : el modo Ultra refleja los prompts con precisión y mantiene la velocidad de generación, ideal para trabajos de publicidad y comercio electrónico
  * **Realismo natural** : el modo Raw optimiza los tonos de piel, la iluminación y los detalles de los paisajes para reducir el “aspecto de IA”
  * **Remezcla de imagen a imagen** : una entrada `image_prompt` combina características de una imagen de entrada, y `image_prompt_strength` controla la relación de la mezcla



## 

​

Salidas de ejemplo

Generación de texto a imagen con el nodo Flux 1.1 [pro] Ultra Image: ![Flujo de trabajo de texto a imagen con FLUX 1.1 pro](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_t2i.png) Remezcla de imagen a imagen, combinando características de una imagen de entrada en la salida: ![Remezcla de imagen a imagen con FLUX 1.1 pro](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_i2i.png)

## 

​

Cómo usarlo

## Llámalo desde el código

Llámalo por HTTP a través de Comfy Router, con fragmentos de Python, TypeScript, Swift y cURL listos para copiar y pegar

Esto se ejecuta con la misma cuenta de Comfy y consume los mismos créditos que ejecutarlo en ComfyUI más abajo. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Documentación del nodo FLUX 1.1 Pro Ultra Image

Consulta la siguiente documentación para ver la configuración detallada de los parámetros del nodo:

  * [FLUX 1.1 Pro Ultra Image](https://docs.comfy.org/images/built-in-nodes/api_nodes/bfl/flux-1-1-pro-ultra-image.jpg)



## 

​

Tutorial de texto a imagen con FLUX 1.1 [pro]

### 

​

1\. Descargar el archivo de flujo de trabajo

Descarga el siguiente archivo y arrástralo a ComfyUI para cargar el flujo de trabajo: ![Flujo de trabajo de texto a imagen con FLUX 1.1 pro](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_t2i.png)

### 

​

2\. Completar los pasos del flujo de trabajo

![Pasos del flujo de trabajo](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=b9403dd3baf434686961672addef2a39) Sigue los pasos numerados para completar el flujo de trabajo básico:

  1. (Opcional) Modifica el prompt en el nodo `Flux 1.1 [pro] Ultra Image`
  2. (Opcional) Establece el parámetro `raw` en `false` para obtener un resultado más realista
  3. Haz clic en `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen
  4. Cuando la API devuelva los resultados, consulta la imagen generada en el nodo `Save Image`. Las imágenes se guardan en el directorio `ComfyUI/output/`



## 

​

Tutorial de imagen a imagen con FLUX 1.1[pro]

Cuando agregas un `image_prompt` a la entrada del nodo, el resultado combina características de la imagen de entrada (Remix). El valor de `image_prompt_strength` afecta la relación de mezcla: los valores más altos hacen que el resultado se parezca más a la imagen de entrada.

### 

​

1\. Descargar el archivo del flujo de trabajo

Descarga y arrastra el siguiente archivo a ComfyUI, o haz clic derecho en el nodo morado del flujo de trabajo de texto a imagen y establece `mode` en `always` para habilitar la entrada `image_prompt`: ![FLUX 1.1 pro Image-to-Image Remix](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/bfl/flux_1_1_pro_i2i.png) Usaremos esta imagen como entrada: ![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/openai-dall-e-3/text2image.png)

### 

​

2\. Completar los pasos del flujo de trabajo

![Pasos del flujo de trabajo](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0217606be6c3f599e3d6ebd2fb14829a) Sigue estos pasos numerados:

  1. Haz clic en **Upload** en el nodo `Load Image` para subir tu imagen de entrada
  2. (Opcional) Ajusta `image_prompt_strength` en `Flux 1.1 [pro] Ultra Image` para cambiar la relación de mezcla
  3. Haz clic en `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen
  4. Después de que la API devuelva los resultados, visualiza la imagen generada en el nodo `Save Image`. Las imágenes se guardan en el directorio `ComfyUI/output/`

Aquí tienes una comparación de los resultados con distintos valores de `image_prompt_strength`: ![Comparación](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/bfl/flux_1_1_pro_image_prompt_strength.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=eea7014b92e63f0b8d1bb50d5dae11c3)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image)

[FLUX 3 Image](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-3-image)[FLUX 1 Kontext](https://docs.comfy.org/es/tutorials/partner-nodes/black-forest-labs/flux-1-kontext)
