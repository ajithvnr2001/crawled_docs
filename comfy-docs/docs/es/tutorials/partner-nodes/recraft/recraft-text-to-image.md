---
url: https://docs.comfy.org/es/tutorials/partner-nodes/recraft/recraft-text-to-image/
title: Recraft Text to Image en ComfyUI: im\u00e1genes con estilos predefinidos - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:54.795608+00:00
---

# Recraft Text to Image en ComfyUI: imágenes con estilos predefinidos - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/recraft/recraft-text-to-image/

## En esta página

Volver arriba

  * En qué destaca Recraft Text to Image
  * Flujo de trabajo con los nodos asociados Recraft Text to Image
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Seguir los pasos para ejecutar el flujo de trabajo
    * 3\. Notas adicionales



Recraft

# Recraft Text to Image en ComfyUI: imágenes con estilos predefinidos

Copiar páginaCopiar página

Genera imágenes desde texto en ComfyUI con el nodo asociado Recraft Text to Image, con estilos predefinidos, control de color RGB y vectorización SVG opcional.

Copiar páginaCopiar página

El nodo Recraft Text to Image te permite crear imágenes de alta calidad en diversos estilos con la tecnología de generación de imágenes de Recraft AI a partir de descripciones de texto.

## 

​

En qué destaca Recraft Text to Image

  * **Generación de alta calidad** : crea imágenes a partir de descripciones de texto con la tecnología de generación de imágenes de Recraft AI
  * **Control de estilos** : estilos predefinidos como arte digital, fotos realistas y diseños de logotipos mediante el nodo `Recraft Style`
  * **Control de color** : define el color deseado con el nodo `Recraft Color RGB`
  * **Tamaño de salida ajustable** : cambia el parámetro `size` para controlar las dimensiones de salida
  * **Conversión a SVG** : un nodo opcional `Recraft Vectorize Image` convierte la imagen generada a formato SVG



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

Flujo de trabajo con los nodos asociados Recraft Text to Image

### 

​

1\. Descargar el archivo del flujo de trabajo

La información del flujo de trabajo está incluida en los metadatos de la imagen a continuación. Descárgala y arrástrala a ComfyUI para cargar el flujo de trabajo. ![Recraft Text to Image Workflow](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/api_nodes/recraft/t2i/recraft_t2i.png)

### 

​

2\. Seguir los pasos para ejecutar el flujo de trabajo

![Recraft Text to Image Workflow Steps](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/recraft/recraft_t2v_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=26e3744a4e7c44a1d72840e8ffef5c3c) Sigue estos pasos numerados para ejecutar el flujo de trabajo básico:

  1. (Opcional) Cambia el `Recraft Color RGB` del nodo `Color` al color que desees
  2. (Opcional) Modifica el nodo `Recraft Style` para controlar el estilo visual, como arte digital, foto realista o diseño de logotipo. Este grupo incluye otros nodos de estilo que puedes habilitar según sea necesario
  3. (Opcional) Edita el parámetro `prompt` del nodo `Recraft Text to Image`. También puedes cambiar el parámetro `size`
  4. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para generar la imagen
  5. Después de que la API devuelva el resultado, puedes ver la imagen generada en el nodo `Save Image`. La imagen también se guardará en el directorio `ComfyUI/output/`



> (Opcional) Hemos incluido un grupo **Convert to SVG** en el flujo de trabajo. Como el nodo `Recraft Vectorize Image` de este grupo consume créditos adicionales, habilítalo solo cuando necesites convertir la imagen generada al formato SVG

### 

​

3\. Notas adicionales

  * **Recraft Style** : ofrece varios estilos predefinidos como fotos realistas, arte digital y diseños de logotipos
  * **Parámetro Seed** : solo se usa para determinar si el nodo debe ejecutarse de nuevo; el resultado real de la generación no se ve afectado por el valor de la semilla



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/recraft/recraft-text-to-image.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/recraft/recraft-text-to-image)

[Recraft V4](https://docs.comfy.org/es/tutorials/partner-nodes/recraft/recraft-v4)[Reve Image](https://docs.comfy.org/es/tutorials/partner-nodes/reve/reve-image)
