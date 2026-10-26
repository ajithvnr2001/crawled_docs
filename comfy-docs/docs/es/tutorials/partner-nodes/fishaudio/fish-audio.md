---
url: https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/fish-audio/
title: Fish Audio: texto a voz, clonaci\u00f3n de voz y voz a texto en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:48.696697+00:00
---

# Fish Audio: texto a voz, clonación de voz y voz a texto en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/fish-audio/

## En esta página

Volver arriba

  * Usar Fish Audio en ComfyUI
    * Elegir un modelo
    * Conectar voces
    * Límites de la clonación de voz
    * Cuenta y precios
  * Flujos de trabajo disponibles
    * Fish Audio: Text to Speech
    * Fish Audio: Voice Clone to Speech
    * Fish Audio: Speech to Text
  * Empezar



Fish Audio

# Fish Audio: texto a voz, clonación de voz y voz a texto en ComfyUI

Copiar páginaCopiar página

Ejecuta flujos de texto a voz, clonación de voz y voz a texto de Fish Audio en ComfyUI: recorridos de plantillas, configuración de nodos y enlaces de Cloud

Copiar páginaCopiar página

Fish Audio es un servicio de IA de voz que abarca texto a voz, clonación de voz y voz a texto. En ComfyUI se distribuye como cuatro Nodos asociados: Text to Speech, Speech to Text, Voice Selector e Instant Voice Clone. Esta página recorre las plantillas de flujos de trabajo listas para usar y cómo conectar los nodos. Para la referencia completa de etiquetas en línea (emociones, tono, pausas, fonemas), consulta la [guía de prompts de Fish Audio](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/prompt-guide). El modelo de texto a voz más reciente, Drama 3, tiene su propia página: [Fish Audio Drama 3](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/drama-3).

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

Usar Fish Audio en ComfyUI

Los nodos asociados de Fish Audio están disponibles en el menú de nodos dentro de `partner/audio/Fish Audio`. Cuatro nodos cubren el flujo de trabajo:

  * **Fish Audio Text to Speech** : convierte texto a voz y genera `AUDIO`.
  * **Fish Audio Speech to Text** : transcribe audio a texto y genera `text`, `language_code` y `segments_json`.
  * **Fish Audio Voice Selector** : selecciona una de las voces predefinidas o conecta cualquier modelo de voz de fish.audio mediante `custom` (el ID en `https://fish.audio/m/<id>/`); genera `voice`.
  * **Fish Audio Instant Voice Clone** : crea una voz clonada privada a partir de grabaciones; genera `voice`.



### 

​

Elegir un modelo

El parámetro `model` del nodo Fish Audio Text to Speech ofrece dos opciones:

  * `s2.1-pro` (recomendado): admite varios hablantes mediante una lista que crece automáticamente de 0 a 5 entradas de voz.
  * `s1` (clásico): acepta una única entrada de voz opcional y usa la sintaxis de etiquetas de emoción entre paréntesis que se describe en la guía de prompts.

La documentación del modelo más reciente, `drama-3`, está en su propia página: [Fish Audio Drama 3](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/drama-3).

### 

​

Conectar voces

La salida `voice` del Voice Selector o del Instant Voice Clone se conecta al nodo Text to Speech. El nombre de la entrada depende del modelo: `s2.1-pro` (recomendado) expone la entrada `voices`, que puede crecer (hasta 5 espacios de voz), mientras que `s1` tiene una única entrada `voice` opcional. Con una voz conectada, el nodo la pasa internamente como `reference_id`. Con dos o más, el texto debe marcar a los hablantes con `@Voice1`, `@Voice2`, etc., y cada voz conectada debe aparecer al menos una vez en el texto; de lo contrario, el nodo genera un error. Consulta [Diálogo con varios hablantes](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/prompt-guide#multi-speaker-dialogue) en la guía de prompts.

### 

​

Límites de la clonación de voz

El nodo Instant Voice Clone acepta de 1 a 20 grabaciones, recomienda entre 10 y 30 segundos por clip y valida que la duración total no supere los 270 segundos. La opción `enhance_audio_quality` está habilitada de forma predeterminada. Para obtener consejos de grabación, consulta [Calidad de la clonación de voz](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/prompt-guide#calidad-de-la-clonaci%C3%B3n-de-voz) en la guía de prompts.

### 

​

Cuenta y precios

Los nodos requieren iniciar sesión en una cuenta de ComfyUI y el cobro es por uso. Precios de referencia de los nodos: la función de texto a voz cuesta alrededor de $21.45 por 1M de bytes de texto, la de voz a texto cuesta $0.00858 por minuto y la clonación de voz es gratis.

## 

​

Flujos de trabajo disponibles

Tres plantillas listas cubren los flujos principales de Fish Audio: texto a voz, clonación de voz a voz y voz a texto. Ábrelas desde la Biblioteca de plantillas en ComfyUI o ejecútalas directamente en Comfy Cloud. Las plantillas de clonación de voz y de voz a texto requieren ComfyUI 0.34.0 o posterior. Drama 3 tiene sus propias dos plantillas, descritas en la [página de Drama 3](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/drama-3).

### 

​

Fish Audio: Text to Speech

Genera voz a partir de tu guion con una voz predefinida. Escribe tu texto con las etiquetas en línea de la [guía de prompts](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/prompt-guide) y luego elige otra voz predefinida en el Voice Selector o conecta una voz clonada. ![Vista previa del flujo de trabajo Fish Audio: Text to Speech](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_text_to_speech-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Fish Audio: Text to Speech” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadAudio` correspondiente:

## fish_audio_example.mp3

Nodo `LoadAudio` 11 · `fish_audio_example.mp3`

### 

​

Fish Audio: Voice Clone to Speech

Clona una voz a partir de una grabación corta y úsala para leer cualquier guion. Graba de 2 a 3 clips de 15 a 20 segundos, súbelos a través del nodo `LoadAudio` (o graba directamente en el nodo `RecordAudio`) y conecta la salida de Instant Voice Clone al nodo Text to Speech. Para consejos de grabación, consulta [Calidad de la clonación de voz](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/prompt-guide#calidad-de-la-clonaci%C3%B3n-de-voz) en la guía de prompts. ![Vista previa del flujo de trabajo Fish Audio: Voice Clone to Speech](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_voice_clone_tts-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Fish Audio: Voice Clone to Speech” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadAudio` correspondiente:

## api_fishaudio_voice_clone_tts_fish_audio_example.mp3

Nodo `LoadAudio` 11 · `api_fishaudio_voice_clone_tts_fish_audio_example.mp3`

### 

​

Fish Audio: Speech to Text

Transcribe un clip de audio a texto. El idioma se detecta automáticamente entre más de 80 idiomas, y activar `precise_timestamps` devuelve los tiempos de inicio y fin de cada segmento como JSON, lo que resulta muy útil para subtítulos. ![Vista previa del flujo de trabajo Fish Audio: Speech to Text](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_speech_to_text-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Fish Audio: Speech to Text” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadAudio` correspondiente:

## fish_audio_example.mp3

Nodo `LoadAudio` 11 · `fish_audio_example.mp3`

## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Abre una plantilla de flujo de trabajo de las de arriba, o agrega los nodos de Fish Audio desde el menú de nodos en `partner/audio/Fish Audio`
  3. Inicia sesión en tu cuenta de ComfyUI cuando se te solicite
  4. Escribe tu guion con las etiquetas en línea de la [guía de prompts](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/prompt-guide)
  5. Ejecuta el flujo de trabajo y previsualiza o guarda el audio



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/fishaudio/fish-audio.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/fishaudio/fish-audio)

[Aislamiento de voz](https://docs.comfy.org/es/tutorials/partner-nodes/elevenlabs/voice-isolation)[Drama 3](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/drama-3)
