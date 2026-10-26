---
url: https://docs.comfy.org/es/tutorials/partner-nodes/heygen/heygen-voice-1/
title: HeyGen Voice 1.0 en ComfyUI: clonaci\u00f3n de voz y texto a voz - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:50.139941+00:00
---

# HeyGen Voice 1.0 en ComfyUI: clonación de voz y texto a voz - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/heygen/heygen-voice-1/

## En esta página

Volver arriba

  * Para qué sirve HeyGen Voice 1.0
  * Ejemplo de salida
  * Usarlo
  * Flujo de trabajo de HeyGen Voice 1.0
    * Pasos para ejecutar
  * Controles del nodo
    * HeyGen Voice 1.0 Instant Clone
    * HeyGen Voice 1.0 Text to Speech
  * Límites
  * Empezar



HeyGen

# HeyGen Voice 1.0 en ComfyUI: clonación de voz y texto a voz

Copiar páginaCopiar página

Clona una voz a partir de una grabación y reproduce cualquier guion con HeyGen Voice 1.0 en ComfyUI mediante los nodos asociados Instant Clone y Text to Speech.

Copiar páginaCopiar página

**HeyGen Voice 1.0** convierte una grabación corta de un solo hablante en una voz reutilizable y luego lee cualquier guion con esa voz. No hay espera de entrenamiento: el clon se crea a partir del clip que conectas, y el `voice_id` devuelto es todo lo que necesita el nodo de texto a voz. Está pensado para narración con tu propia voz, diálogos de personajes y voz en off multilingüe. En ComfyUI, la función se ejecuta mediante dos nodos asociados: **HeyGen Voice 1.0 Instant Clone** toma la grabación y devuelve un `voice_id`, y **HeyGen Voice 1.0 Text to Speech** lee el texto escrito con esa voz. Ambos son nodos API en la nube: requieren una cuenta de Comfy con créditos y no descargan ningún modelo local. Clonar es gratis y el texto a voz se cobra por cada 1K caracteres. Consulta [Precios de los nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para ver las tarifas. La plantilla conecta los dos nodos y guarda ambas salidas: el audio hablado y un archivo de texto con el `voice_id`, para que puedas reutilizar la misma voz en una sesión posterior sin volver a clonar.

## 

​

Para qué sirve HeyGen Voice 1.0

  * **Clona a partir de una grabación corta** : basta con 10 segundos de habla clara, y se usan hasta 3 minutos del clip
  * **Reutiliza la voz** : la salida `voice_id` se conecta a text to speech, o a `custom_voice_id` en HeyGen Avatar Video y HeyGen Talking Photo
  * **Dos velocidades** : `heygen-voice-1-turbo` es más rápida y cuesta aproximadamente una cuarta parte de lo que cuesta `heygen-voice-1`
  * **Control de expresividad** : `expressiveness_boost` se mantiene cerca de la grabación con valores bajos y añade emoción con valores altos



## 

​

Ejemplo de salida

Clonar una voz a partir de una grabación y después interpretar un guion con esa voz: ![Vista previa del flujo de trabajo HeyGen Voice 1.0](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_voice_1-1.webp)

## 

​

Usarlo

Esto se ejecuta en la misma cuenta de Comfy y se factura con los mismos créditos que ejecutarlo en ComfyUI a continuación. Consulta [Precios de los Nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas por modelo y [Límites de concurrencia](https://docs.comfy.org/es/tutorials/partner-nodes/concurrency-limits) para saber cuántas solicitudes puedes tener en curso.

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

Flujo de trabajo de HeyGen Voice 1.0

Clona la voz, escribe el guion y ejecuta. La plantilla mantiene ambos nodos en un mismo gráfico, así que el `voice_id` pasa directamente del clon al nodo de texto a voz.

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “HeyGen Voice 1.0” en la Biblioteca de plantillas

**Material de entrada**

## long_demo.mp3

Cárgalo en el nodo `LoadAudio` que alimenta a HeyGen Voice 1.0 Instant Clone

### 

​

Pasos para ejecutar

  1. **Carga una grabación** : conecta en el nodo **LoadAudio** la voz de un solo hablante, con al menos 10 segundos de habla clara. Solo se usan los primeros 3 minutos
  2. **Clona la voz** : en **HeyGen Voice 1.0 Instant Clone** , asigna a `language` el idioma que se habla en la grabación y elige `similarity`. Cambia `seed` para clonar de nuevo y obtener una voz ligeramente distinta
  3. **Escribe el guion** : en **HeyGen Voice 1.0 Text to Speech** , introduce hasta 5000 caracteres de prosa simple en `text` y conecta la salida `voice_id` del nodo de clonación a su entrada `voice_id`
  4. **Define la interpretación** : `expressiveness_boost` va de 0 a 1. `0` se mantiene más cerca de la grabación, `1` aporta la mayor emoción
  5. **Haz clic en Queue** o pulsa `Ctrl+Enter` para generar
  6. **Guarda el resultado** : la plantilla escribe el audio con **SaveAudioAdvanced** y el ID de voz con **SaveText** , en `output/HeyGen_Voice_id/`



## 

​

Controles del nodo

### 

​

HeyGen Voice 1.0 Instant Clone

Control| Valores| Efecto  
---|---|---  
`audio`| un clip de audio| Grabación de un solo hablante. Se recomienda que dure al menos 10 segundos; solo se usan los primeros 3 minutos  
`language`| `auto` o un idioma| Idioma que se habla en la grabación  
`similarity`| `medium`, `high`, `extra_high`, `max` (predeterminado)| Nivel de fidelidad de la voz clonada respecto a la grabación  
`remove_background_noise`| activado de forma predeterminada| Limpia la grabación antes de clonarla  
`seed`| predeterminado 42| Cambia la semilla para volver a clonar; cada clon es una voz ligeramente distinta  
  
### 

​

HeyGen Voice 1.0 Text to Speech

Control| Valores| Efecto  
---|---|---  
`model`| `heygen-voice-1`, `heygen-voice-1-turbo`| Turbo es más rápido y cuesta aproximadamente una cuarta parte del precio  
`voice_id`| un ID de voz clonada| Salida del nodo Instant Clone  
`text`| de 1 a 5000 caracteres| El guion que se va a decir. La generación falla si la locución supera unos 12 minutos, así que divide los textos muy largos en chino o japonés  
`language`| `auto` o un idioma| Configúralo para idiomas estrechamente relacionados, como el serbio o el malayo, que la detección automática puede confundir  
`expressiveness_boost`| de 0.0 a 1.0, predeterminado 0.5| Los valores más altos son más expresivos; los más bajos se mantienen más cerca de la voz original  
  
## 

​

Límites

  * El clon usa los primeros 3 minutos de la grabación, y 10 segundos de habla clara son el mínimo práctico.
  * El texto está limitado a 5000 caracteres, aproximadamente 12 minutos de habla. Solo prosa simple; todo lo demás se rechaza.
  * Las voces instantáneas ignoran `seed`, `speed` y `pitch` en la conversión de texto a voz. `expressiveness_boost` es el único control de expresividad.
  * El `voice_id` debe provenir de un clon. Un ID vacío falla con un error.
  * La clonación es gratis; la conversión de texto a voz se cobra por 1K caracteres a la tarifa del modelo.



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Ve a la Biblioteca de plantillas y busca `HeyGen Voice 1.0`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/heygen/heygen-voice-1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/heygen/heygen-voice-1)

[Video a música](https://docs.comfy.org/es/tutorials/partner-nodes/sonilo/video-to-music)[SFX 2.0](https://docs.comfy.org/es/tutorials/partner-nodes/mirelo/mirelo-sfx)
