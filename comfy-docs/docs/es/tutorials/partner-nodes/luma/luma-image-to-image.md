---
url: https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-image-to-image/
title: Luma Imagen a Imagen en ComfyUI: edici\u00f3n de im\u00e1genes con prompts - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.885434+00:00
---

# Luma Imagen a Imagen en ComfyUI: edición de imágenes con prompts - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-image-to-image/

## En esta página

Volver arriba

  * Para qué sirve Luma Imagen a Imagen
  * Salidas de ejemplo
  * Flujo de trabajo de los nodos asociados de Luma Imagen a Imagen
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Completar los pasos del flujo de trabajo
    * 3\. Resultados con distintos valores de image_weight



Luma

# Luma Imagen a Imagen en ComfyUI: edición de imágenes con prompts

Copiar páginaCopiar página

Edita imágenes existentes con el nodo Luma Imagen a Imagen de ComfyUI: cambios guiados por prompt en objetos y formas, con control del peso de la imagen de entrada.

Copiar páginaCopiar página

El nodo Luma Imagen a Imagen te permite modificar imágenes existentes a partir de prompts de texto usando la tecnología de Luma AI, conservando ciertas características y estructuras de la imagen original.

## 

​

Para qué sirve Luma Imagen a Imagen

  * **Edición de imágenes guiada por prompt** : modifica imágenes existentes a partir de prompts de texto y conserva ciertas características y estructuras de la original
  * **Cambio de objetos y formas** : el nodo funciona bien para cambiar objetos y formas, aunque puede no ser ideal para cambios de color
  * **Influencia ajustable de la entrada** : el parámetro `image_weight` controla con qué fuerza la imagen de entrada determina el resultado; los valores más bajos se mantienen más cerca de la original



## 

​

Salidas de ejemplo

Resultados con distintos valores de `image_weight`, que muestran con qué fuerza influye la imagen de entrada en la salida generada: ![Comparación de pesos](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d6fc32e5bdbf4f1368f73cfac583643d)

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

Flujo de trabajo de los nodos asociados de Luma Imagen a Imagen

Esta función funciona bien para cambiar objetos y formas. Sin embargo, puede no ser ideal para cambios de color. Recomendamos usar valores de peso bajos, alrededor de 0.0 a 0.1.

### 

​

1\. Descargar el archivo del flujo de trabajo

Descarga y arrastra la siguiente imagen a ComfyUI para cargar el flujo de trabajo (la información del flujo de trabajo está incluida en los metadatos de la imagen): ![Flujo de trabajo de Luma Imagen a Imagen](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2i/luma_i2i.png) Descarga esta imagen para usarla como entrada: ![Imagen de entrada del flujo de trabajo de Luma Imagen a Imagen](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/i2i/input.png)

### 

​

2\. Completar los pasos del flujo de trabajo

![Pasos del flujo de trabajo de Luma Imagen a Imagen](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_i2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=0169a042868519a3cd76ef832fdc714a) Sigue estos pasos numerados:

  1. Haz clic en **Upload** en el nodo `Load Image` para subir tu imagen de entrada
  2. (Opcional) Modifica los prompts del flujo de trabajo
  3. (Opcional) Ajusta `image_weight` para cambiar la influencia de la imagen de entrada (los valores más bajos se mantienen más cerca de la original)
  4. Haz clic en `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen
  5. Cuando la API devuelva los resultados, verás la imagen generada en el nodo `Save Image`. Las imágenes se guardan en el directorio `ComfyUI/output/`



### 

​

3\. Resultados con distintos valores de `image_weight`

![Comparación de pesos](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/i2i_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=d6fc32e5bdbf4f1368f73cfac583643d)

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/luma/luma-image-to-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/luma/luma-image-to-image)

[Luma texto a imagen](https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-text-to-image)[Magnific AI](https://docs.comfy.org/es/tutorials/partner-nodes/magnific/overview)
