---
url: https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-motion-control/
title: Kling 2.6 Motion Control en ComfyUI: transferencia de movimiento desde un video de referencia - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:51.168084+00:00
---

# Kling 2.6 Motion Control en ComfyUI: transferencia de movimiento desde un video de referencia - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-motion-control/

## En esta página

Volver arriba

  * En qué destaca Kling 2.6 Motion Control
  * Modos de orientación del personaje
  * Niveles de modelo
  * Kling2.6: Control de movimiento
  * Requisitos de entrada
  * Consejos para obtener mejores resultados



Kling

# Kling 2.6 Motion Control en ComfyUI: transferencia de movimiento desde un video de referencia

Copiar páginaCopiar página

Transfiere movimiento de un video de referencia a una imagen de personaje en ComfyUI con el nodo Kling 2.6 Motion Control, con modos de orientación y niveles.

Copiar páginaCopiar página

Kling 2.6 Motion Control es un modelo multimodal especializado desarrollado por Kuaishou que permite transferir con precisión el movimiento de videos de referencia a imágenes de personajes. Al combinar una **Imagen de referencia** (tu personaje) y un **Video de referencia de movimiento** (la acción), la IA aplica el movimiento, la expresión y el ritmo del video a tu personaje estático mientras mantiene su identidad. A diferencia de la generación estándar de imagen a video, que adivina el movimiento a partir de prompts de texto, Motion Control usa un video de referencia como plano del movimiento. El modelo actúa como un titiritero digital: extrae la coreografía de tu video de referencia y la aplica a tu personaje con fidelidad de nivel cinematográfico.

## 

​

En qué destaca Kling 2.6 Motion Control

  * **Manejo de movimientos complejos** : ejecuta secuencias complicadas como rutinas de baile, artes marciales o movimientos atléticos sin perder la coherencia del personaje. El modelo entiende la transferencia de peso y el impulso para lograr un impacto físico realista.
  * **Rendimiento preciso de manos y dedos** : las manos han sido tradicionalmente un punto débil para el video con IA. Esta función mejora específicamente la articulación de los dedos y los movimientos de las manos al imitar metraje real, lo que la hace ideal para presentaciones y demostraciones.
  * **Flexibilidad de escena y entorno** : usa prompts de texto para cambiar el entorno mientras el personaje continúa su movimiento de referencia. No estás limitado al fondo del video de referencia.
  * **Modos avanzados de cámara y perspectiva** : control granular sobre cómo la cámara interpreta tu referencia con modos de orientación distintos.
  * **Soporte de toma única de 30 segundos** : genera acciones continuas de hasta 30 segundos en una sola generación, lo que permite un movimiento ininterrumpido del personaje para escenas narrativas.



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

Modos de orientación del personaje

El parámetro `character_orientation` determina cómo interpreta el modelo la información espacial y restringe la duración de salida:

Modo| Descripción| Duración máx.  
---|---|---  
`video`| La orientación del personaje de salida coincide con el video de referencia. Ideal para actuaciones complejas de cuerpo completo, como secuencias de baile y coreografías elaboradas.| 30 segundos  
`image`| La orientación del personaje de salida coincide con la imagen de referencia. Ideal para animaciones de retrato con movimiento de cámara, como paneos, inclinaciones y tomas de seguimiento.| 10 segundos  
  
## 

​

Niveles de modelo

Nivel| Resolución| Ideal para  
---|---|---  
**Estándar**|  720p| Animaciones sencillas, contenido para redes sociales, memes y pruebas rápidas. Más rápido y más eficiente en créditos.  
**Pro**|  1080p| Coreografías complejas, movimientos intrincados de manos, recursos profesionales de marketing y contenido con calidad de emisión.  
  
## 

​

Kling2.6: Control de movimiento

Aplica a tu imagen de personaje las acciones y expresiones precisas de un personaje de un video de referencia, con control de movimiento sincronizado. ![Vista previa del flujo de trabajo Kling2.6: Control de movimiento](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_motion_control-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Kling2.6: Motion Control” en la Biblioteca de plantillas

**Materiales de entrada** Sube estos archivos a los nodos `LoadImage` y `LoadVideo` correspondientes:

## streetwear_fox.jpg

Nodo `LoadImage` 11 · `streetwear_fox.jpg`

## street_dancer.mp4

Nodo `LoadVideo` 2 · `street_dancer.mp4`

![streetwear_fox.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/streetwear_fox.jpg)

## 

​

Requisitos de entrada

  * **Formatos de imagen** : JPG, PNG, WEBP, GIF, AVIF (máx. 10 MB)
  * **Formatos de video** : MP4, MOV, WEBM, M4V, GIF (máx. 100 MB)
  * **Duración del video** : de 3 a 30 segundos según el modo de orientación
  * **Resolución mínima** : 720 px de ancho y alto
  * **Visibilidad del sujeto** : el personaje debe mostrar claramente la cabeza, los hombros y el torso



## 

​

Consejos para obtener mejores resultados

  * **Iguala las relaciones de aspecto** : asegúrate de que tu imagen de personaje y tu video de referencia tengan relaciones de aspecto similares (por ejemplo, ambos 16:9 o ambos 9:16) para evitar estiramientos o recortes extraños.
  * **Fondos limpios** : usa videos de referencia con fondos simples o estáticos para obtener la mejor extracción de movimiento. Los videos de alto contraste en los que la silueta del actor es nítida funcionan mejor.
  * **Ángulos claros del personaje** : si tu video de referencia muestra rotación, usa personajes estilo 3D o fotos realistas que manejen mejor la rotación. Los dibujos animados 2D planos pueden tener problemas con las vistas de espaldas.
  * **Extremidades visibles** : asegúrate de que las extremidades del personaje se vean en la imagen fuente. Si un personaje tiene las manos en los bolsillos pero el movimiento requiere saludar, la IA alucinará las manos, lo que a menudo genera artefactos.
  * **Deja espacio para respirar** : deja espacio negativo alrededor del sujeto. Si el personaje va a bailar o a mover los brazos ampliamente, necesita espacio dentro del encuadre para evitar recortes.
  * **Alineación del encuadre** : iguala el encuadre entre tu imagen y el video de referencia. Usa una referencia de primer plano para animaciones faciales, o una referencia de cuerpo completo para secuencias de caminar o bailar.



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/kling/kling-motion-control.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/kling/kling-motion-control)

[Kling Virtual Try-On](https://docs.comfy.org/es/tutorials/partner-nodes/kling/kling-virtual-try-on)[Ltx 2 5](https://docs.comfy.org/es/tutorials/partner-nodes/lightricks/ltx-2-5)
