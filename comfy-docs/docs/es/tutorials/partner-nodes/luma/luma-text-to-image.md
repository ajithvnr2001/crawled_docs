---
url: https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-text-to-image/
title: Luma texto a imagen en ComfyUI: referencias de estilo y de personaje - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.815677+00:00
---

# Luma texto a imagen en ComfyUI: referencias de estilo y de personaje - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-text-to-image/

## En esta página

Volver arriba

  * En qué destaca Luma Text to Image
  * Salidas de ejemplo
  * Flujo de trabajo de nodos asociados de Luma Text to Image
    * 1\. Descargar archivos del flujo de trabajo
    * 2\. Seguir los pasos para ejecutar el flujo de trabajo
    * 3\. Notas adicionales



Luma

# Luma texto a imagen en ComfyUI: referencias de estilo y de personaje

Copiar páginaCopiar página

Genera imágenes desde texto con el nodo Luma texto a imagen en ComfyUI: imágenes de estilo, control de peso de estilo y hasta cuatro referencias.

Copiar páginaCopiar página

El nodo Luma texto a imagen te permite generar imágenes de alta calidad a partir de prompts de texto con la avanzada tecnología de Luma AI, capaz de crear contenido fotorrealista e imágenes con estilo artístico.

## 

​

En qué destaca Luma Text to Image

  * **Generación de imágenes de texto a imagen de alta calidad** : crea contenido fotorrealista e imágenes de estilo artístico a partir de prompts de texto
  * **Referencias de estilo** : una entrada `style_image` guía el aspecto del resultado, y `style_image_weight` controla la influencia de la imagen de referencia de estilo
  * **Referencias de imagen y de personaje** : la entrada `image_luma_ref` admite generación guiada por referencias, con hasta 4 imágenes de referencia y referencias de personaje que puedes usar al mismo tiempo



## 

​

Salidas de ejemplo

Generación guiada por estilo con diferentes valores de `style_image_weight`, que muestra la influencia de la imagen de referencia de estilo: ![Comparación de peso de imagen de estilo](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7f47d2d3a6acdde87df046460afa393f)

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

Flujo de trabajo de nodos asociados de Luma Text to Image

Cuando el nodo `Luma Text to Image` se usa sin entradas de imagen, funciona como un flujo de trabajo de texto a imagen. En esta guía, hemos creado ejemplos usando `style_image` e `image_luma_ref` para mostrar las excelentes capacidades de procesamiento de imágenes de Luma AI.

### 

​

1\. Descargar archivos del flujo de trabajo

La información del flujo de trabajo está incluida en los metadatos de la imagen a continuación. Descárgala y arrástrala a ComfyUI para cargar el flujo de trabajo. ![Flujo de trabajo de Luma Text to Image](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/luma_t2i.png) Descarga estas imágenes para usarlas como entrada: ![Imagen de entrada: referencia](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/input_ref.png) ![Imagen de entrada: estilo](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/luma/t2i/input_style.png)

### 

​

2\. Seguir los pasos para ejecutar el flujo de trabajo

![Pasos del flujo de trabajo de Luma Text to Image](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/luma_t2i_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=e3122c711034e8270d086ae8c139cb64) Sigue los pasos numerados de la imagen para completar el flujo de trabajo básico:

  1. Sube la imagen de referencia en el nodo `Load image`
  2. Sube la imagen de referencia de estilo en el nodo `Load image (renamed to styleref)`
  3. (Opcional) Modifica los prompts en el nodo `Luma Text to Image`
  4. (Opcional) Ajusta `style_image_weight` para controlar la influencia de la imagen de referencia de estilo
  5. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen
  6. Después de que la API devuelva los resultados, visualiza la imagen generada en el nodo `Save Image`. Las imágenes se guardan en el directorio `ComfyUI/output/`

![Comparación del peso de la imagen de estilo](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/luma/t2i_style_image_weight.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=7f47d2d3a6acdde87df046460afa393f)

### 

​

3\. Notas adicionales

  * El nodo permite hasta 4 imágenes de referencia y referencias de personajes simultáneamente.
  * Para habilitar varias entradas de imagen, haz clic derecho en los nodos morados “Bypassed” y establece su `mode` en `always`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/luma/luma-text-to-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/luma/luma-text-to-image)

[Luma Uni 1](https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-uni-1)[Luma Imagen a Imagen](https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-image-to-image)
