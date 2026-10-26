---
url: https://docs.comfy.org/es/tutorials/audio/yue2/yue2/
title: Gu\u00eda de generaci\u00f3n de m\u00fasica con YuE2 en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:41.273294+00:00
---

# Guía de generación de música con YuE2 en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/audio/yue2/yue2/

## En esta página

Volver arriba

  * Texto a música
    * 1\. Pasos para ejecutar
    * 2\. Descarga del modelo
    * 3\. Escribir el estilo
    * 4\. Escribir la letra
    * 5\. Planificación ABC
    * 6\. Duración máxima
    * 7\. Escala de orientación
  * Versión de una canción existente (Music Cover)
    * 1\. Pasos para ejecutar
    * 2\. Descarga de modelos
    * 3\. Cómo funciona la versión
    * 4\. Escribir el Style y la letra



YuE2

# Guía de generación de música con YuE2 en ComfyUI

Copiar páginaCopiar página

Genera canciones completas con voces en ComfyUI con el modelo de código abierto YuE2: texto a música con planificación ABC y covers que conservan la melodía con SheetSage2.

Copiar páginaCopiar página

YuE2 es un modelo de generación musical de código abierto de Multimodal Art Projection (m-a-p) que convierte un prompt de estilo y una letra en una canción completa con voces y acompañamiento instrumental. Es un modelo de 3B de parámetros, genera estructuras de canción completas con secciones como intro, verso, estribillo, puente y outro, y admite varios idiomas de canto, incluidos el inglés, el chino y el japonés. Lo que distingue a YuE2 de la mayoría de los sistemas de texto a música es su paso de composición editable. Antes de generar el audio, YuE2 puede escribir primero un plan musical simbólico en notación ABC: una melodía, opcionalmente con acordes, que puedes inspeccionar y editar. La canción final se renderiza a partir de ese plan. Esto hace que los resultados sean más fáciles de dirigir que la generación de audio en una sola pasada, y también habilita el flujo de trabajo de cover que aparece más abajo, donde una canción de referencia se transcribe a la misma notación y se vuelve a cantar con un nuevo estilo y una nueva letra. YuE2 es compatible de forma nativa con ComfyUI. Actualiza a la última versión de [ComfyUI](https://github.com/comfyanonymous/ComfyUI) antes de empezar. Se requiere ComfyUI v0.36.0 o posterior.

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

YuE2 aún no está disponible en Comfy Cloud. Ambos flujos de trabajo de esta página se ejecutan en una instalación local de ComfyUI, así que no hay ninguna plantilla de Cloud que abrir para ellos.

## 

​

Texto a música

Genera una canción completa a partir de una descripción del estilo musical y tu propia letra. Con la planificación ABC activada, YuE2 primero crea un plan de música simbólica editable (melodía y, opcionalmente, acordes), y luego genera el audio final a partir de ese plan. ![Vista previa del flujo de trabajo de texto a música de YuE2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_yue2_text2music-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “YuE2: Text to Music” en la Biblioteca de plantillas

### 

​

1\. Pasos para ejecutar

  1. Escribe una descripción de la música que quieres en **Style**
  2. Introduce la letra de tu canción en **Lyrics** usando etiquetas de sección como `[Verse]` y `[Chorus]`
  3. Elige un **Mode** de planificación: `full` genera melodía y acordes, `melody` genera solo la melodía
  4. Define la **Max Duration** de la canción
  5. Pon el flujo de trabajo en cola para generar la canción



### 

​

2\. Descarga del modelo

## checkpoint de YuE2

yue2_3b_int8_convrot.safetensors

Coloca el archivo en el siguiente directorio:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   └── 📂 checkpoints/
    │       └── yue2_3b_int8_convrot.safetensors
    

### 

​

3\. Escribir el estilo

Describe las características musicales principales. Algunos elementos útiles son:

  * **Género** : pop, jazz, rock, electrónica, folk
  * **Voz** : voz femenina cálida, voz masculina expresiva, voz suave
  * **Idioma** : inglés, chino, japonés y más
  * **Tempo** : 90 BPM, lento, animado
  * **Instrumentos** : piano, guitarra eléctrica, bajo, batería, sintetizadores

Ejemplo:

> Inglés, voz femenina cálida, pop contemporáneo, 96 BPM, piano, bajo eléctrico redondo, batería contenida, dicción clara

Mantén las indicaciones musicales en **Style** y no en la letra.

### 

​

4\. Escribir la letra

Usa etiquetas de sección para describir la estructura de la canción:
    
    
    [Verse]
    Morning light across the window
    City waking down below
    
    [Chorus]
    Run with me into the sunlight
    Leave the shadows far behind
    

Puedes estructurar la canción con secciones como `[Verse]`, `[Chorus]`, `[Bridge]` y `[Outro]`. Coloca en el campo de la letra solo las palabras que se van a cantar.

### 

​

5\. Planificación ABC

La opción **Mode** controla el paso de planificación simbólica:

  * **full** : crea un plan con melodía y acordes antes de generar la canción. Recomendado para la generación general de texto a música.
  * **melody** : crea un plan solo de melodía y deja que el acompañamiento se genere con más libertad.

Si dejas la entrada **abc** vacía, la planificación se desactiva y la música se genera directamente a partir de Style y Lyrics.

### 

​

6\. Duración máxima

**Max Duration** establece la longitud máxima de la canción generada en segundos, hasta 900. El presupuesto de generación es de 25 tokens semánticos por segundo de duración solicitada, y el muestreo se detiene en cuanto el modelo escribe el token de fin de la canción, así que una canción cuya estructura termina antes puede acabar mucho antes del límite. La plantilla Text to Music lo establece en 120 segundos, y Music Cover mantiene el valor predeterminado de 360 segundos del nodo. La duración solicitada está limitada por el contexto del modelo. Cuando el estilo, la letra y el plan ABC ocupan más contexto del que la ejecución puede ceder, ComfyUI reduce el presupuesto a lo que queda y lo informa en la consola: `YuE2 music budget reduced to ... tokens (... seconds) to fit the prompt.` Por eso, un prompt largo acorta la canción en lugar de hacer fallar la ejecución. Cuando no queda nada en absoluto, la ejecución se detiene con `YuE2 prompt leaves no room for music; shorten the style, lyrics, or ABC.` Cuando la consola muestra la advertencia `YuE2 semantic reached its token budget before the end token.`, el modelo se quedó sin presupuesto antes de escribir el token de fin de la canción, y el audio renderizado puede cortarse de golpe en lugar de terminar la canción, porque esos tokens semánticos son el contenido de la canción que renderiza la etapa de audio. Aumenta **Max Duration** para dar más espacio a la canción. Si esa misma ejecución también registró una reducción de presupuesto, el prompt ya está usando el contexto disponible, así que acorta el estilo, la letra o el plan ABC. La fase de notación informa la misma advertencia como `YuE2 abc reached its token budget before the end token.`, donde la partitura se corta y `max_abc_tokens` del nodo YuE2 Generate ABC es el presupuesto que debes aumentar.

### 

​

7\. Escala de orientación

El nodo **YuE2 Generate Music** tiene una opción avanzada `cfg_scale` (de 0 a 100, valor predeterminado 1.0) que establece la orientación autoregresiva sobre el estilo y la letra:

  * `1.0` desactiva la orientación, lo que coincide con el flujo de trabajo ABC. Las plantillas incluidas mantienen este valor predeterminado
  * `1.01` coincide con la escala de orientación que el modelo usaba antes de añadir esta opción, para ejecuciones con la planificación desactivada (`abc` vacío)



## 

​

Versión de una canción existente (Music Cover)

Crea una nueva versión de una canción existente. Este flujo de trabajo usa SheetSage2 para transcribir la melodía de un audio de referencia a una partitura ABC editable y luego usa YuE2 para regenerar la canción con un estilo y una letra nuevos. ![Vista previa del flujo de trabajo de Music Cover de YuE2](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_yue2_music_cover-1.webp)

## Descargar flujo de trabajo

Descarga el JSON o busca “YuE2: Music Cover” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadAudio` correspondiente:

## yue2_reference_song.flac

Nodo `LoadAudio` · `yue2_reference_song.flac`

### 

​

1\. Pasos para ejecutar

  1. Carga una canción de referencia en **Audio**
  2. Describe la nueva dirección musical en **Style**
  3. Introduce la letra que quieres que se cante en **Lyrics**
  4. Encola el flujo de trabajo para generar una nueva versión

El audio de referencia aporta la melodía, mientras que YuE2 crea una nueva interpretación y un nuevo arreglo a partir de tu Style y tu Lyrics.

### 

​

2\. Descarga de modelos

## checkpoint de YuE2

yue2_3b_int8_convrot.safetensors

## codificador de audio SheetSage2

sheetsage2_bf16.safetensors

Coloca los archivos en los siguientes directorios:
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── yue2_3b_int8_convrot.safetensors
    │   └── 📂 audio_encoders/
    │       └── sheetsage2_bf16.safetensors
    

### 

​

3\. Cómo funciona la versión

El flujo de trabajo no pasa el audio de referencia directamente a YuE2. En su lugar:
    
    
    Reference Audio
        ↓
    SheetSage2 (transcription)
        ↓
    Melody ABC score
        ↓
    YuE2 (generation with new Style and Lyrics)
    

Como el vínculo con la canción original es la melodía, las versiones funcionan mejor cuando la letra nueva se mantiene razonablemente cerca de la frase y del número de sílabas del original.

### 

​

4\. Escribir el Style y la letra

Describe con claridad el estilo musical objetivo. Los elementos útiles incluyen género, tipo de voz, idioma, tempo, instrumentos y ambiente:

> English, soulful jazz-pop, expressive male vocal, relaxed 88 BPM, Rhodes piano, upright bass, brushed drums, warm saxophone, intimate late-night atmosphere

Usa las mismas etiquetas de sección `[Verse]` / `[Chorus]` / `[Bridge]` / `[Outro]` que en el flujo de trabajo de texto a música. Para que la melodía encaje mejor, mantén la letra nueva con una longitud similar a la de los versos originales.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/audio/yue2/yue2.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/audio/yue2/yue2)

[SCAIL-2](https://docs.comfy.org/es/tutorials/video/zai/scail2)[MiniMax Music 3](https://docs.comfy.org/es/tutorials/audio/minimax/minimax-music-3)
