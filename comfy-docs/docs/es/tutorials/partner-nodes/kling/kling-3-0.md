---
url: https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-3-0/
title: Generaci\u00f3n de video e im\u00e1genes con Kling 3.0 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.014423+00:00
---

# Generación de video e imágenes con Kling 3.0 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-3-0/

## En esta página

Volver arriba

  * En qué destaca Kling 3.0
  * Salidas de ejemplo
  * Modelos disponibles
  * Aprende más
  * Kling 3.0: Texto a imagen
  * Kling 3.0: generación de video
  * Kling 3.0: Primer y último fotograma a video
  * Kling 3.0: control de movimiento
  * Modelos Kling clásicos (EOL)
    * Plantillas de flujo de trabajo retiradas y sus reemplazos



Kling

# Generación de video e imágenes con Kling 3.0 en ComfyUI

Copiar páginaCopiar página

Aprende a usar los modelos Kling 3.0 en ComfyUI para generar video multi-shot, mantener la consistencia del sujeto, audio multilingüe y texto nativo

Copiar páginaCopiar página

Kling 3.0 es uno de los sistemas de generación multimodal más avanzados y ahora está disponible en ComfyUI a través de los Nodos asociados. Esta versión incluye **Kling Video 3.0** , **Kling Video 3.0 Omni** , **Kling Image 3.0** y **Kling Image 3.0 Omni** , y lleva las capacidades de generación de video, imagen, audiovisual y narrativa directamente a tus flujos de trabajo basados en nodos.

## 

​

En qué destaca Kling 3.0

  * **Generación de varias tomas** : Genera varias tomas con control de duración en una sola generación
  * **Consistencia del sujeto fijado** : Mantiene la identidad de personajes y objetos a través del movimiento de cámara y la evolución de la escena
  * **Audio nativo con reconocimiento de personajes** : Diálogos multilingües con sincronización labial precisa y alineación de las expresiones faciales
  * **Renderizado de texto nativo** : Texto en pantalla claro y estructurado para anuncios, escenas de interfaz y contenido de marca



## 

​

Salidas de ejemplo

Generación de texto a imagen con el modelo Kling 3.0: ![Kling 3.0: ejemplo de texto a imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_kling_v3_t2i.png)

## 

​

Modelos disponibles

Modelo| Tipo| Descripción  
---|---|---  
**Kling Video 3.0**|  Video| Generación de video estándar con soporte para múltiples tomas  
**Kling Video 3.0 Omni**|  Video| Generación de video avanzada con capacidades audiovisuales  
**Kling Image 3.0**|  Image| Generación de imágenes de alta calidad  
**Kling Image 3.0 Omni**|  Image| Generación de imágenes multimodal con funciones mejoradas  
  
## 

​

Aprende más

Para ver ejemplos detallados, prompts y demostraciones en video de las capacidades de Kling 3.0, consulta nuestra publicación del blog:

## Los modelos Kling 3.0 ya están disponibles

Lee el anuncio completo con ejemplos en video, consejos de prompt y análisis detallados de las funciones.

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

Kling 3.0: Texto a imagen

Genera una imagen a partir de un prompt de texto con el modelo Kling 3.0. ![Vista previa del flujo de trabajo Kling 3.0: Texto a imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling 3.0: Text to Image” en la Biblioteca de plantillas

**Salida de ejemplo** ![Ejemplo de Kling 3.0: Texto a imagen](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_kling_v3_t2i.png)

## 

​

Kling 3.0: generación de video

Escribe prompts de texto o imagen para generar secuencias de video de 15 segundos con composiciones de varios planos, movimientos de cámara complejos y sujetos consistentes. ![Vista previa del flujo de trabajo Kling 3.0: generación de video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descargar el JSON o buscar “Kling 3.0: Video Generation” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## boxing.png

Nodo `LoadImage` 1 · `boxing.png`

![boxing.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/boxing.png)

## 

​

Kling 3.0: Primer y último fotograma a video

Ingresa una imagen de primer y último fotograma para generar una secuencia de video continua con generación de múltiples tomas y control preciso de los elementos. ![Vista previa del flujo de trabajo Kling 3.0: Primer y último fotograma a video](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_flf2v-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling 3.0: First Last Frame to Video” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` correspondientes:

## goldenfish_in_bag.png

Nodo `LoadImage` 1 · `goldenfish_in_bag.png`

## man_in_daydream.png

Nodo `LoadImage` 13 · `man_in_daydream.png`

![goldenfish_in_bag.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/goldenfish_in_bag.png)![man_in_daydream.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/man_in_daydream.png)

## 

​

Kling 3.0: control de movimiento

Aplica el movimiento de un video de referencia a la imagen de un personaje. Sube una imagen de personaje y un video de referencia de movimiento, y el modelo mueve a tu personaje a través de la acción del clip mientras conserva su identidad. Este flujo de trabajo ejecuta el modelo Kling 3.0, que mejora la consistencia facial respecto a versiones anteriores. ![Vista previa del flujo de trabajo Kling 3.0: control de movimiento](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_motion_control3-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling 3.0: Motion Control” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` y `LoadVideo` correspondientes:

## future_robot.png

Nodo `LoadImage` 2 · `future_robot.png`

## boxing_man.mp4

Nodo `LoadVideo` 3 · `boxing_man.mp4`

![future_robot.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/future_robot.png)

**Ajustes de control de movimiento** Configura `character_orientation` en `video` cuando la cámara y el encuadre deban seguir el clip de movimiento, lo que permite clips de referencia de hasta 30 segundos, o en `image` cuando el personaje conserve el encuadre de la imagen fija, lo que limita el clip a 10 segundos. Mantén `mode` en `pro` para la salida final y cambia a `std` para pruebas más económicas. `keep_original_sound` traslada el audio del clip al resultado, y `model` vuelve a `kling-v2-6` para la generación anterior. Este flujo de trabajo usa el mismo nodo `Kling Motion Control` que el ejemplo de [Kling 2.6 Motion Control](https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-motion-control), así que los consejos de entrada de esa página también se aplican aquí.

## 

​

Modelos Kling clásicos (EOL)

**Fin de vida útil (EOL)** : Los siguientes modelos Kling clásicos y plantillas de flujo de trabajo están programados para retirarse el **15 de septiembre de 2026** : Kling V1.5, V1.6, V2.1, V2.1 Master y la API de Kolors Virtual Try-On. Los Nodos asociados relacionados permanecen en ComfyUI, pero estas opciones de modelo dejarán de funcionar después de la fecha de retiro.

### 

​

Plantillas de flujo de trabajo retiradas y sus reemplazos

Plantilla eliminada| Reemplazo sugerido  
---|---  
`api_kling_i2v` (V2.1 Master)| [`api_kling_o3_i2v`](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_o3_i2v.json) o [`api_kling2_6_i2v`](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling2_6_i2v.json)  
`api_kling_effects` (V1.6)| Flujos de trabajo de efectos de Kling 3.0 (`api_kling_v3_*`)  
`api_kling_flf` (V1.6)| [`api_kling_v3_flf2v`](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_v3_flf2v.json) o [`api_kling_o3_flf2v`](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_o3_flf2v.json)  
`api_kling_dual_characters_effects` (V1.6)| Flujos de trabajo de efectos de Kling 3.0 (`api_kling_v3_*`)  
  
Para la prueba virtual de ropa, usa el nodo [Flux Virtual Try-On](https://docs.comfy.org/es/built-in-nodes/FluxVTONode) (`api_flux_vto`) u otras alternativas compatibles. Las plantillas de moda basadas en FLUX VTO y Gemini no se ven afectadas por este retiro.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/kling/kling-3-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/kling/kling-3-0)

[HitPaw Video Enhance](https://docs.comfy.org/es/tutorials/partner-nodes/hitpaw/hitpaw-video-enhance)[Kling Virtual Try-On](https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-virtual-try-on)
