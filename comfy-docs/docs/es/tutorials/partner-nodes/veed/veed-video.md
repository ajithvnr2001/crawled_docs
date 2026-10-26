---
url: https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-video/
title: Nodos de video de VEED: Talking Photo, Lip Sync y eliminaci\u00f3n de fondo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:56.477322+00:00
---

# Nodos de video de VEED: Talking Photo, Lip Sync y eliminación de fondo - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-video/

## En esta página

Volver arriba

  * Flujos de trabajo disponibles
    * Fabric 1.0: Talking Photo
    * Lipsync 2.0
    * Remove Video Background
  * Controles del nodo
  * Consejos
  * Empezar



VEED

# Nodos de video de VEED: Talking Photo, Lip Sync y eliminación de fondo

Copiar páginaCopiar página

Usa los Nodos asociados de VEED en ComfyUI para hacer hablar a una foto, sincronizar un rostro con audio nuevo y recortar un sujeto como máscara alfa.

Copiar páginaCopiar página

Los nodos de video de **VEED** cubren los pasos de edición que normalmente requieren una segunda aplicación: convertir una imagen fija en un retrato que habla, reemplazar el habla de un metraje existente y recortar un sujeto de su fondo. En ComfyUI el proveedor funciona a través de tres nodos asociados. **VEED Fabric 1.0** anima una foto a partir de una pista de audio. **VEED Lipsync 2.0** vuelve a sincronizar a un hablante con un diálogo nuevo. **VEED Remove Video Background** devuelve los fotogramas y una máscara alfa en lugar de un video plano, así puedes componer el sujeto sobre cualquier cosa. Los tres son nodos API en la nube: necesitan una cuenta de Comfy con créditos y no descargan archivos de modelo en local. Cada nodo cobra por segundo o por fotograma del clip que envíes. Para limpiar la voz en audio y video, consulta [VEED Clean Audio](https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-clean-audio).

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

Flujos de trabajo disponibles

### 

​

Fabric 1.0: Talking Photo

Haz que una imagen fija hable. Los labios de la cara de la foto se sincronizan con el audio que conectes, y el clip conserva la relación de aspecto de la imagen, así que un retrato sigue siendo un retrato. Funciona con fotos, ilustraciones y mascotas de marca, lo que lo convierte en una forma de darle voz a una obra de arte o a un personaje que nunca se filmó. ![Vista previa del flujo de trabajo VEED Fabric 1.0: Talking Photo](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_fabric_1_0-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “VEED Fabric 1.0: Talking Photo” en la Biblioteca de plantillas

**Materiales de entrada**

## black_fashion_portrait.png

Cárgala en el nodo `LoadImage`. Un rostro nítido y de frente

## audio_see_beyond_the_light.mp3

Cárgalo en el nodo `LoadAudio`. La voz define el movimiento de los labios y la duración del clip

El audio puede durar hasta 300 segundos y el video tiene exactamente la misma duración que el audio. La resolución es 480p o 720p: aproximadamente 864x480 en 16:9 para 480p y 1312x736 para 720p.

### 

​

Lipsync 2.0

Conserva el metraje que ya grabaste y reemplaza lo que dice la persona que habla. La boca se vuelve a sincronizar con el audio nuevo mientras el resto del fotograma permanece tal como se grabó; así puedes reescribir una línea o doblar un clip sin hacer otra grabación. ![Vista previa del flujo de trabajo VEED Lipsync 2.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_lipsync_2_0-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “VEED Lipsync 2.0: Lip Sync” en la Biblioteca de plantillas

**Materiales de entrada**

## rainbow_face_portrait_prism_video.mp4

Cárgalo en el nodo `LoadVideo`. Una persona que habla de frente

## veed_lipsync_rainbow_night_speech.wav

Cárgalo en el nodo `LoadAudio`. La voz nueva para sincronizar

La voz nueva puede durar hasta 600 segundos y define la duración de la salida. El video conserva su resolución de origen a 25 fps. Cuando el metraje es más corto que el audio, se reproduce hacia adelante y luego hacia atrás hasta que el audio termina, así que envía un clip que sea lo bastante largo cuando la toma deba mantener su dirección.

### 

​

Remove Video Background

Extrae el sujeto de un clip. En lugar de un video aplanado, el nodo devuelve los fotogramas más una máscara que marca lo que era fondo, así que puedes componer el sujeto sobre una escena nueva o exportarlo como una secuencia transparente. ![Vista previa del flujo de trabajo VEED Remove Video Background](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_remove_video_background-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “VEED Remove Video Background: Matte Export” en la Biblioteca de plantillas

**Material de entrada**

## swimcap_glass_pop_video.mp4

Cárgalo en el nodo `LoadVideo`. Los clips pueden durar hasta 60 segundos

La plantilla convierte la máscara en alfa para una secuencia PNG. Agrega `Invert Mask` antes de `Image Composite Masked` cuando quieras el sujeto como máscara de composición, o `Join Image with Alpha` seguido de `Save WEBM` para un video transparente. Configura el códec de WEBM en `vp9`: es la única opción que escribe el canal alfa, y `av1` lo descarta.

## 

​

Controles del nodo

Control| Valores| Se aplica a| Efecto  
---|---|---|---  
`model`| `fabric-1.0`, `lipsync-2.0`, `standard`, `fast`, `green screen`| cada nodo| El modelo de VEED para ese nodo  
`image`| imagen| Fabric 1.0| La cara que habla. La relación de aspecto define la forma de la salida  
`video`| clip| Lipsync 2.0, Remove Video Background| Material de origen. Hasta 60 segundos en la eliminación de fondo  
`audio`| pista| Fabric 1.0, Lipsync 2.0| El habla a la que sincronizar. Define la duración de la salida  
`resolution`| `480p`, `720p`| Fabric 1.0| Clase de tamaño de salida, 720p por defecto  
`seed`| entero| Lipsync 2.0| Solo para volver a ejecutar. Los resultados siguen siendo no deterministas  
`refine_foreground_edges`| activado por defecto| Remove Video Background, standard y fast| Bordes más limpios en el cabello y el pelaje. Desactivarlo reduce el precio  
`subject_is_person`| activado por defecto| Remove Video Background, standard y fast| Desactívalo cuando el sujeto sea un objeto o un animal  
`spill_suppression_strength`| 0.0 a 1.0, por defecto 0.8| Remove Video Background, green screen| Con qué intensidad se elimina el tinte verde. Súbelo cuando queden manchas verdes, bájalo cuando los colores se desplacen  
  
La resolución de salida en la eliminación de fondo no tiene control: standard y green screen devuelven hasta 3840x2160, fast devuelve hasta 1920x1080, y la entrada más grande se reduce.

## 

​

Consejos

  * **Envía metraje limpio y de frente.** Fabric necesita un rostro visible, y Lipsync necesita un solo hablante que mire a la cámara. Los perfiles y los encuadres saturados son los casos en los que cualquiera de los dos nodos pierde detalle.
  * **Deja que el audio defina la duración.** Ambos nodos de conversación producen un clip que dura exactamente lo mismo que el habla que conectas, así que recorta el audio antes de ejecutar en lugar de recortar el video después.
  * **Introduce el habla generada directamente.** Conecta un nodo de texto a voz a `audio` y el retrato o el clip doblado sigue ese audio sin un paso de exportación.
  * **Paga por el refinamiento de bordes solo cuando lo necesites.** Desactivar `refine_foreground_edges` en la eliminación de fondo reduce la tarifa por fotograma, lo que vale la pena en sujetos con bordes duros.
  * **Usa pantalla verde solo en tomas reales de pantalla verde.** El modo de pantalla verde aplica una clave al fondo y no tiene refinamiento de bordes ni detección de personas, así que un fondo natural va con standard o fast.



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `VEED`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/veed/veed-video.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/veed/veed-video)

[Astra 2](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/astra-2)[Veo](https://docs.comfy.org/es/tutorials/partner-nodes/veo/overview)
