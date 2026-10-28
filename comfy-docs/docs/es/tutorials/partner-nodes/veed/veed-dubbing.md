---
url: https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-dubbing/
title: VEED Dubbing: traduce y sincroniza los labios del habla de un video en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-28T13:54:25.181618+00:00
---

# VEED Dubbing: traduce y sincroniza los labios del habla de un video en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-dubbing/

## En esta página

Volver arriba

  * Flujo de trabajo disponible
    * VEED Dubbing: traducción de video
  * Controles del nodo
  * Consejos
  * Empezar



VEED

# VEED Dubbing: traduce y sincroniza los labios del habla de un video en ComfyUI

Copiar páginaCopiar página

Traduce el habla de un video a otro idioma en ComfyUI con VEED Dubbing: clona la voz de cada hablante y resincroniza los labios con la traducción.

Copiar páginaCopiar página

VEED Dubbing traduce el habla de un clip a otro idioma. La voz de cada persona se clona y sus labios se resincronizan con la traducción, así que el resultado se ve hablado en el idioma objetivo en lugar de subtitulado. En ComfyUI el nodo es **VEED Dubbing** , con dos niveles de modelo. `standard` es el más económico: audio mono, 85 idiomas objetivo, con el español como latinoamericano y el portugués como brasileño. `pro` añade acentos regionales y audio estéreo, y llega a 101 idiomas objetivo, incluidas variantes como `English (UK)`, `Spanish (Mexico)` y `Chinese (Taiwan)`. Es un nodo de API en la nube. Necesita una cuenta de Comfy con créditos, no descarga ningún archivo de modelo y cobra por segundo de salida. Consulta [Precios de los nodos socio](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas actuales.

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

Flujo de trabajo disponible

### 

​

VEED Dubbing: traducción de video

Traduce un clip que ya tengas. La interpretación, la toma y el tiempo se mantienen tal como se grabaron; lo que cambia es el idioma en el que se escucha al hablante. ![Vista previa del flujo de trabajo VEED Dubbing](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_dubbing-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “VEED Dubbing: Video Translation” en la Biblioteca de plantillas

**Materiales de entrada**

## api_veed_dubbing_input_video.mp4

Cárgalo en el nodo `LoadVideo`. Un solo hablante frente a la cámara

El clip dura hasta 599 segundos y la salida es tan larga como su pista de audio, a 25 fps.

## 

​

Controles del nodo

Control| Valores| Efecto  
---|---|---  
`model`| `standard`, `pro`| El nivel de doblaje. `standard` es mono con 85 idiomas objetivo; `pro` añade acentos regionales y audio estéreo con 101  
`video`| clip| El material que se va a doblar. Hasta 599 segundos, con un rostro visible y voz en la pista de audio  
`target_language`| lista de idiomas| El idioma al que se dobla. La lista depende del nivel, y `pro` incluye las variantes de acento  
`source_language`| `auto` o un idioma| El idioma que se habla en el video. `auto` es el predeterminado  
`seed`| entero| Solo para volver a ejecutar. Los resultados siguen siendo no deterministas  
  
## 

​

Consejos

  * **Envía material con un hablante visible.** El doblaje trabaja sobre lo que puede ver, así que una sola persona de frente a la cámara es el caso confiable. Nucas, manos, tomas de producto y escenas de multitud no se doblan.
  * **Comprueba que el audio tenga voz de verdad.** La narración, el diálogo y las entrevistas funcionan. La música, los efectos de sonido y el silencio no le dan al modelo nada que traducir.
  * **Indica el idioma fuente cuando`auto` oiga mal.** `auto` funciona bien con grabaciones limpias, pero un clip corto o un acento marcado se dobla con más precisión cuando configuras `source_language` tú mismo.
  * **Elige`pro` cuando el acento importe.** El nivel Estándar ofrece una sola variante por idioma, así que una solicitud de inglés británico o español de México solo existe en `pro`.
  * **Recorta primero hasta el límite de duración.** El nodo acepta hasta 599 segundos de video, y la salida dura lo mismo que la pista de audio, así que recorta antes de ejecutar y no después.



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a Template Library y busca `VEED Dubbing`
  3. Carga un clip de talking-head en el nodo `LoadVideo`
  4. Elige el nivel en `model`, define `target_language` y luego ejecuta el flujo de trabajo



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/veed/veed-dubbing.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/veed/veed-dubbing)

[Astra 2](https://docs.comfy.org/es/tutorials/partner-nodes/topaz/astra-2)[Nodos de video](https://docs.comfy.org/es/tutorials/partner-nodes/veed/veed-video)
