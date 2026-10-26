---
url: https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-clean-audio/
title: VEED Clean Audio: limpieza de voz para audio y video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:56.546909+00:00
---

# VEED Clean Audio: limpieza de voz para audio y video - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-clean-audio/

## En esta página

Volver arriba

  * Flujos de trabajo disponibles
    * Clean Audio
    * Clean Audio (in Video)
  * Controles del nodo
  * Consejos
  * Empezar



VEED

# VEED Clean Audio: limpieza de voz para audio y video

Copiar páginaCopiar página

Elimina el ruido de fondo de la voz con VEED Clean Audio en ComfyUI, en una grabación o en la pista de audio de un video, con normalización de volumen opcional.

Copiar páginaCopiar página

**VEED Clean Audio** aísla la voz en una grabación. Elimina el ruido de fondo y, como está diseñado para la voz, la música y los efectos de sonido se van junto con el ruido: lo que devuelve es el diálogo por sí solo, limpio y listo para usar. En ComfyUI, el modelo se ejecuta mediante dos Nodos asociados. **VEED Clean Audio** toma una grabación independiente y devuelve el audio limpio. **VEED Clean Audio (in Video)** toma un clip, limpia solo su banda sonora y devuelve el video con la imagen intacta. Ambos son Nodos API en la nube: requieren una cuenta de Comfy con créditos y no descargan archivos de modelo localmente. Los dos nodos devuelven cosas distintas. **Clean Audio** devuelve audio mono a 48 kHz. **Clean Audio (in Video)** devuelve el video en sí, con la imagen intacta y su banda sonora reemplazada por esa voz limpia en mono a 48 kHz. Ambos aceptan ejecuciones de hasta 1799 segundos, justo por debajo de 30 minutos. Para sincronización labial, retratos que hablan y eliminación de fondo, consulta [VEED Video Nodes](https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-video).

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

Clean Audio

Limpia una grabación de voz antes de que pase a cualquier otra etapa. Este nodo es el primer paso de un pipeline de voz: envía el habla limpia a un nodo de lip sync, a un paso de transcripción o a una mezcla, y el piso de ruido del original nunca llega hasta ellos. ![Vista previa del flujo de trabajo VEED Clean Audio: Speech Cleanup](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_clean_audio-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “VEED Clean Audio: Speech Cleanup” en la Biblioteca de plantillas

**Material de entrada**

## veed_clean_audio_noisy_input.wav

Cárgalo en el nodo `LoadAudio`

### 

​

Clean Audio (in Video)

Limpia el habla dentro de un clip sin tocar la imagen. Solo se reemplaza la banda sonora, con el habla limpia en mono a 48 kHz, así que el resultado es el mismo montaje con una pista de voz utilizable. ![Vista previa del flujo de trabajo VEED Clean Audio: Video Speech Cleanup](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_clean_audio_video-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “VEED Clean Audio: Video Speech Cleanup” en la Biblioteca de plantillas

**Material de entrada**

## veed_clean_audio_input_h3_omniref_person_dialogue_plus_noise.mp4

Cárgalo en el nodo `LoadVideo`. El clip necesita una pista de audio

Un clip sin pista de audio se detiene con un error en lugar de devolver un video silencioso. Solo se conserva la primera pista de audio: las pistas adicionales y los subtítulos incrustados se descartan, así que expórtalos primero cuando el clip tenga más de una.

## 

​

Controles del nodo

Control| Valores| Se aplica a| Efecto  
---|---|---|---  
`audio`| grabación, hasta 1799 segundos| Clean Audio| El habla que se debe limpiar  
`video`| clip con audio, hasta 1799 segundos| Clean Audio (in Video)| El clip cuya banda sonora se limpia. El paso de limpieza no recodifica la imagen  
`strength`| 0.0 a 1.0, predeterminado 0.874| ambos nodos| Cuánto ruido se elimina bajo el habla. Un valor menor conserva más tono de sala detrás de la voz  
`loudness`| `normalize`, `keep input level`| ambos nodos| Indica si la salida se normaliza a una sonoridad objetivo  
`target_lufs`| -40 a -8, predeterminado -19| ambos nodos, solo `normalize`| Sonoridad integrada de la salida  
  
Las pausas entre palabras siempre se limpian por completo, sin importar el valor de `strength`, y los valores por encima del predeterminado apenas cambian. Los picos se limitan a -1.1 dBTP, por lo que un objetivo alto se detiene antes: el habla típica se estabiliza cerca de -15 LUFS.

## 

​

Consejos

  * **Deja`strength` en el valor predeterminado primero.** Está ajustado para voz. Bájalo solo cuando el tono de sala detrás de la voz sea parte del sonido que quieres conservar.
  * **Normaliza cuando el audio limpio deba coincidir con otros clips.** Un `target_lufs` compartido es lo que hace que una serie de grabaciones quede al mismo nivel.
  * **No esperes recuperar la música.** La música y los efectos se eliminan junto con el ruido, así que este nodo limpia diálogo, no una mezcla completa. Ejecútalo sobre el stem de voz cuando una banda sonora deba sobrevivir.
  * **Corta las grabaciones largas antes de la ejecución.** El límite es de 1799 segundos, y un archivo más corto cuesta menos con la tarifa por minuto.
  * **Encadénalo con los nodos de talking.** El habla limpia es una mejor entrada para lip sync y retratos que hablan que la grabación sin procesar.



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `VEED`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/veed/veed-clean-audio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/veed/veed-clean-audio)

[SFX 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/mirelo/mirelo-sfx)[Descripción general](https://docs.comfy.org/es/tutorials/partner-nodes/language/overview)
