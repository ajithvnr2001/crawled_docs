---
url: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seed-audio-1-0/
title: ByteDance Seed Audio 1.0 - Generaci\u00f3n universal de audio - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:47.031225+00:00
---

# ByteDance Seed Audio 1.0 - Generación universal de audio - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/bytedance/seed-audio-1-0/

## En esta página

Volver arriba

  * Para qué sirve Seed Audio 1.0
  * Flujos de trabajo disponibles
    * Seed Audio 1.0: Texto a audio
    * Seed Audio 1.0: Texto + audio a audio
    * Seed Audio 1.0: Texto + imagen a audio
  * Cómo usar Seed Audio 1.0 en ComfyUI
    * Elegir un modo de referencia
    * Estructura del prompt
    * Ajuste de parámetros
    * Casos límite y limitaciones
  * Empezar



ByteDance

# ByteDance Seed Audio 1.0 - Generación universal de audio

Copiar páginaCopiar página

Genera voz, música, efectos de sonido y diálogos con varios hablantes desde un solo prompt con clonación de voz y voces predefinidas usando Seed Audio 1.0 en ComfyUI

Copiar páginaCopiar página

Seed Audio 1.0 es el modelo de generación de audio universal de ByteDance, ahora disponible como nodo integrado en ComfyUI. A diferencia de los sistemas tradicionales de texto a voz, que solo leen palabras en voz alta, Seed Audio comprende todo el espectro del sonido. Puede generar voz, música, efectos de sonido, atmósferas ambientales y diálogos con varios hablantes a partir de un solo prompt de texto.

## 

​

Para qué sirve Seed Audio 1.0

  * **Generación de audio multimodal** : voz, música, efectos de sonido y audio ambiente a partir de un solo prompt. Describe lo que oyes y Seed Audio lo produce
  * **Clonación de voz** : clona voces a partir de hasta 3 clips de referencia (etiquetados como `@Audio1`, `@Audio2`, `@Audio3` en el prompt) para diálogos con varios personajes o una narración consistente
  * **Voces predefinidas** : elige entre las voces integradas de TTS 2.0 cuando necesites una narración confiable y de alta calidad sin un clip de referencia
  * **Voz a partir de una imagen** : deriva una voz de la imagen de un personaje, ajustando el tono y el estilo al sujeto visual
  * **Control detallado** : ajusta la velocidad del habla, el tono, el volumen y la frecuencia de muestreo de forma independiente en cada generación
  * **Diálogo con varios hablantes** : nombra a los personajes directamente en el prompt y Seed Audio se encarga de la asignación de voces, los turnos de palabra y la expresividad emocional
  * **Hasta 2 minutos por ejecución** : genera clips de audio extensos, adecuados para narración, fragmentos de pódcast, doblaje de video y diseño sonoro

Con estas capacidades, Seed Audio 1.0 se adapta a una amplia variedad de casos de uso, como las locuciones de video, los dramas de audio con varios personajes, las demostraciones de producto, la narración para e-learning, los prototipos de audio para juegos y el contenido de accesibilidad.

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

Seed Audio 1.0: Texto a audio

Introduce un prompt de texto para generar voz hablada, diálogo, música de fondo y efectos de sonido en un solo archivo de audio. ![Vista previa del flujo de trabajo Seed Audio 1.0: Texto a audio](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_t2a-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Seed Audio 1.0: Text to Audio” en la Biblioteca de plantillas

### 

​

Seed Audio 1.0: Texto + audio a audio

Sube un clip de audio de referencia y escribe un prompt de texto para clonar la voz en una nueva escena. ![Vista previa del flujo de trabajo Seed Audio 1.0: Texto + audio a audio](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_ta2a-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Seed Audio 1.0: Text + Audio to Audio” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadAudio` correspondiente:

## seed_audio_ref_audio1.mp3

Nodo `LoadAudio` 8 · `seed_audio_ref_audio1.mp3`

### 

​

Seed Audio 1.0: Texto + imagen a audio

Sube una imagen de un personaje y escribe un prompt de texto para generar audio con un estilo de voz que coincida con el sujeto visual. ![Vista previa del flujo de trabajo Seed Audio 1.0: Texto + imagen a audio](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed_audio1_0_ti2a-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Seed Audio 1.0: Text + Image to Audio” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## girl_and_fish.png

Nodo `LoadImage` 6 · `girl_and_fish.png`

![girl_and_fish.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/girl_and_fish.png)

## 

​

Cómo usar Seed Audio 1.0 en ComfyUI

Seed Audio 1.0 se distribuye como el nodo integrado **ByteDanceSeedAudio**. Lo encuentras en el menú de nodos, dentro de ByteDance.

### 

​

Elegir un modo de referencia

El nodo ofrece cuatro modos de referencia que determinan cómo se condiciona la voz generada:

Modo| Descripción| Cuándo usarlo  
---|---|---  
**Solo texto**|  Describe todo (estilo de voz, emoción, ambiente y diálogo) en el prompt| Generación rápida sin material de referencia  
**Referencia de audio**|  Conecta hasta 3 clips de audio de referencia (máx. 30 s cada uno) y etiquétalos como `@Audio1`, `@Audio2`, `@Audio3` en el prompt| Clonar voces específicas o crear diálogos con varios personajes  
**Referencia de imagen**|  Conecta una imagen de personaje; el modelo deriva una voz a partir de ella| Derivar una voz a partir de un diseño visual de personaje  
**Voz predefinida**|  Selecciona una voz integrada de TTS 2.0 en el menú desplegable| Narración confiable sin clonación  
  
### 

​

Estructura del prompt

Para obtener los mejores resultados, estructura tu prompt para describir la escena de audio:

  * **Voz y emoción** : describe el tono, la edad, el género, el acento o la entrega emocional
  * **Ambiente y fondo** : describe el entorno acústico (estudio silencioso, calle concurrida, sala de conciertos)
  * **Efectos de sonido** : describe sonidos específicos en el momento adecuado de la línea de tiempo
  * **Líneas de diálogo** : escribe las líneas que se van a pronunciar y nombra a los personajes en escenas con varios hablantes

**Ejemplo: narración con ambiente**

> Una voz masculina tranquila y cálida habla con confianza. Cae lluvia suave de fondo, con truenos lejanos ocasionales. “Seed Audio 1.0 genera habla natural con control total sobre el ritmo, el tono y la presencia.”

**Ejemplo: diálogo con varios hablantes y referencias de audio**

> @Audio1 dice con nerviosismo, en un susurro bajo y rápido: “¿Viste eso?” @Audio2 responde con un deje lento y tranquilo: “¿Ver qué? Solo es el viento.” Ambiente de viento suave durante todo el audio.

### 

​

Ajuste de parámetros

Después de conectar tus entradas, ajusta estos parámetros para obtener el resultado deseado:

  * **Velocidad del habla** : predeterminado 0 (normal). Alcance de -50 (0.5x) a 100 (2.0x). Usa valores negativos para una narración relajada y positivos para locuciones energéticas
  * **Tono** : desplazamiento en semitonos (-12 a +12). Útil para voces de personajes o para igualar un registro vocal específico
  * **Volumen** : predeterminado 0 (normal). Alcance de -50 (0.5x) a 100 (2.0x). Ajusta para lograr un volumen constante entre distintos materiales de origen
  * **Frecuencia de muestreo** : elige entre 8 kHz y 48 kHz. 24 kHz es un buen valor predeterminado para voz; 44.1 kHz o 48 kHz para música
  * **Semilla** : controla si el nodo se vuelve a ejecutar; los resultados no son deterministas, sin importar el valor de la semilla



### 

​

Casos límite y limitaciones

  * **Duración de los clips de referencia** : los clips de audio de referencia tienen un límite de 30 segundos cada uno. Para material de referencia más largo, recorta o edita el clip antes de conectarlo
  * **Orden de las referencias de audio** : las entradas de referencia deben conectarse de forma secuencial (1, 2, 3), sin espacios
  * **Límite de etiquetas** : el máximo es de 3 etiquetas `@AudioN` por prompt
  * **Límite de caracteres** : los prompts tienen un límite de 3000 caracteres
  * **Límite de duración** : máximo 2 minutos de audio por ejecución



## 

​

Empezar

  1. Actualiza ComfyUI a la última versión
  2. Agrega el nodo **ByteDanceSeedAudio** desde el menú de nodos, o abre una de las plantillas de flujo de trabajo de arriba
  3. Elige tu modo de referencia y conecta las entradas
  4. Escribe tu prompt describiendo la escena de audio y el diálogo
  5. Ejecuta el flujo de trabajo



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/bytedance/seed-audio-1-0.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/bytedance/seed-audio-1-0)

[Guía de prompts](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/prompt-guide)[Video a música](https://docs.comfy.org/es/tutorials/partner-nodes/sonilo/video-to-music)
