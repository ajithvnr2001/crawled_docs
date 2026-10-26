---
url: https://docs.comfy.org/es/tutorials/audio/ace-step/ace-step-v1/
title: Ejemplo nativo de ACE-Step en ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:41.007201+00:00
---

# Ejemplo nativo de ACE-Step en ComfyUI - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/audio/ace-step/ace-step-v1/

## En esta página

Volver arriba

  * Ejemplo de flujo de trabajo de generación de texto a audio con ACE-Step en ComfyUI
    * 1\. Descarga el flujo de trabajo y los modelos relacionados
    * 2\. Completa el flujo de trabajo paso a paso
  * Flujo de trabajo de audio a audio con ACE-Step en ComfyUI
    * 1\. Descargar el archivo del flujo de trabajo
    * 2\. Completar el flujo de trabajo paso a paso
    * 3\. Notas adicionales sobre el flujo de trabajo
  * Guía de prompts de ACE-Step
    * Etiquetas (prompt)
    * Estilos musicales populares
    * Tipos de escena
    * Elementos instrumentales
    * Tipos de voz
    * Términos profesionales
    * Letras
    * Etiquetas de estructura de la letra
    * Soporte multilingüe
  * Recursos relacionados con ACE-Step



ACE-Step

# Ejemplo nativo de ACE-Step en ComfyUI

Copiar páginaCopiar página

Generación de música con ACE-Step en ComfyUI: flujos de texto a música y edición musical con el modelo de código abierto Apache-2.0 de StepFun y ACE Studio.

Copiar páginaCopiar página

ACE-Step es un modelo fundacional de generación de música de código abierto desarrollado conjuntamente por el equipo chino StepFun y ACE Studio, cuyo objetivo es ofrecer a los creadores musicales herramientas de generación y edición de música eficientes, flexibles y de alta calidad. El modelo se publica bajo la [licencia Apache-2.0](https://github.com/ace-step/ACE-Step?tab=readme-ov-file#-license) y es gratis para uso comercial. Como potente base de generación musical, ACE-Step ofrece una gran extensibilidad. Mediante técnicas de ajuste fino como LoRA y ControlNet, los desarrolladores pueden personalizar el modelo según sus necesidades reales. Ya sea para edición de audio, síntesis vocal, producción de acompañamientos, clonación de voz o aplicaciones de transferencia de estilo, ACE-Step brinda un soporte técnico estable y confiable. Esta arquitectura flexible simplifica enormemente el proceso de desarrollo de aplicaciones de IA musical y permite que más creadores apliquen rápidamente la tecnología de IA a la creación musical. Actualmente, ACE-Step ha publicado el código de entrenamiento relacionado, incluido el entrenamiento de modelos LoRA, y el código de entrenamiento de ControlNet correspondiente se publicará en el futuro. Puedes visitar su [GitHub](https://github.com/ace-step/ACE-Step?tab=readme-ov-file#-roadmap) para aprender más detalles.

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

Ejemplo de flujo de trabajo de generación de texto a audio con ACE-Step en ComfyUI

### 

​

1\. Descarga el flujo de trabajo y los modelos relacionados

Haz clic en el botón de abajo para descargar el archivo del flujo de trabajo correspondiente. Arrástralo a ComfyUI para cargar la información del flujo de trabajo. El flujo de trabajo incluye la información de descarga de los modelos. [Descargar el archivo de flujo de trabajo en formato JSON](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/audio/ace-step/ace_step_1_t2m.json) También puedes descargar manualmente [ace_step_v1_3.5b.safetensors](https://huggingface.co/Comfy-Org/ACE-Step_ComfyUI_repackaged/blob/main/all_in_one/ace_step_v1_3.5b.safetensors) y guardarlo en la carpeta `ComfyUI/models/checkpoints`

### 

​

2\. Completa el flujo de trabajo paso a paso

![Guía de pasos](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_t2a_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=236a3db013af8dda09a7730916f24da0)

  1. Asegúrate de que el nodo `Load Checkpoints` haya cargado el modelo `ace_step_v1_3.5b.safetensors`
  2. (Opcional) En el nodo `EmptyAceStepLatentAudio` puedes definir la duración de la música que se va a generar
  3. (Opcional) En el nodo `LatentOperationTonemapReinhard` puedes ajustar el `multiplier` para controlar el volumen de la voz (valores más altos hacen que la voz destaque más)
  4. (Opcional) Introduce los estilos musicales correspondientes, etc., en el campo `tags` de `TextEncodeAceStepAudio`
  5. (Opcional) Introduce la letra correspondiente en el campo `lyrics` de `TextEncodeAceStepAudio`
  6. Haz clic en el botón `Run`, o usa el atajo `Ctrl(cmd) + Enter`, para ejecutar la generación de audio
  7. Cuando el flujo de trabajo termine,, puedes escuchar el audio generado en el nodo `Save Audio`. Puedes hacer clic para reproducirlo, y el audio también se guardará en `ComfyUI/output/audio` (el subdirectorio lo determina el nodo `Save Audio`).



## 

​

Flujo de trabajo de audio a audio con ACE-Step en ComfyUI

De forma similar a los flujos de trabajo de imagen a imagen, puedes ingresar un fragmento de música y usar el flujo de trabajo de abajo para remuestrear y generar música. También puedes ajustar la diferencia respecto al audio original controlando el parámetro `denoise` en el `Ksampler`.

### 

​

1\. Descargar el archivo del flujo de trabajo

Haz clic en el botón de abajo para descargar el archivo del flujo de trabajo correspondiente. Arrástralo a ComfyUI para cargar la información del flujo de trabajo. [Descargar archivo de flujo de trabajo en formato JSON](https://raw.githubusercontent.com/Comfy-Org/example_workflows/main/audio/ace-step/ace_step_1_m2m_editing.json) Descarga el siguiente archivo de audio como audio de entrada: [Descargar archivo de audio de ejemplo para la entrada](https://github.com/Comfy-Org/example_workflows/raw/refs/heads/main/audio/ace-step/input.mp3)

### 

​

2\. Completar el flujo de trabajo paso a paso

![Guía paso a paso de ACE-Step](https://mintcdn.com/dripart/OltlUSVBSNcJsDMs/images/tutorial/audio/ace_step/ace_step_1_m2m_step_guide.jpg?fit=max&auto=format&n=OltlUSVBSNcJsDMs&q=85&s=74b041e1a727b4d4bfa22f6ae446d611)

  1. Asegúrate de que el nodo `Load Checkpoints` haya cargado el modelo `ace_step_v1_3.5b.safetensors`
  2. Sube el archivo de audio proporcionado en el nodo `LoadAudio`
  3. (Opcional) Ingresa los estilos musicales y la letra correspondientes en los campos `tags` y `lyrics` de `TextEncodeAceStepAudio`. Proporcionar la letra es muy importante para la edición de audio
  4. (Opcional) Modifica el parámetro `denoise` del nodo `Ksampler` para ajustar el ruido que se añade durante el muestreo y así controlar la similitud con el audio original (los valores más pequeños dan como resultado una mayor similitud con el audio original; establecerlo en `1.00` equivale aproximadamente a no tener entrada de audio)
  5. Haz clic en el botón `Run` o usa el atajo `Ctrl(cmd) + Enter` para ejecutar la generación de audio
  6. Cuando el flujo de trabajo termine, puedes previsualizar el audio generado en el nodo `Save Audio`. Puedes hacer clic para reproducirlo y escucharlo, y el audio también se guardará en `ComfyUI/output/audio` (el subdirectorio lo determina el nodo `Save Audio`).

También puedes usar la funcionalidad de modificación y edición de la letra de la página del proyecto ACE-Step, modificando la letra original para cambiar el efecto del audio.

### 

​

3\. Notas adicionales sobre el flujo de trabajo

  1. En el flujo de trabajo de ejemplo, puedes cambiar los `tags` de `TextEncodeAceStepAudio` de `male voice` a `female voice` para generar voces femeninas.
  2. También puedes modificar los `lyrics` de `TextEncodeAceStepAudio` para cambiar la letra y, con ello, el audio generado. Consulta los ejemplos de la página del proyecto ACE-Step para más detalles.



## 

​

Guía de prompts de ACE-Step

Actualmente, ACE usa dos tipos de prompts: `tags` y `lyrics`.

  * `tags`: se usan principalmente para describir estilos musicales, escenas, etc. De forma similar a los prompts que usamos en otras generaciones, describen sobre todo el estilo general y los requisitos del audio, y se separan con comas en inglés.
  * `lyrics`: se usan principalmente para describir la letra y admiten etiquetas de estructura como [verse], [chorus] y [bridge] para distinguir las distintas partes de la letra. También puedes escribir nombres de instrumentos para música puramente instrumental.

Puedes encontrar abundantes ejemplos de `tags` y `lyrics` en la [página del modelo ACE-Step](https://ace-step.github.io/). Puedes consultar esos ejemplos para probar los prompts correspondientes. La guía de prompts de este documento está organizada a partir del proyecto para ayudarte a probar combinaciones rápidamente y lograr el efecto que buscas.

### 

​

Etiquetas (prompt)

#### 

​

Estilos musicales populares

Usa combinaciones cortas de etiquetas para generar estilos musicales concretos

  * electronic
  * rock
  * pop
  * funk
  * soul
  * cyberpunk
  * Acid jazz
  * electro
  * em (electronic music)
  * soft electric drums
  * melodic



#### 

​

Tipos de escena

Combina situaciones de uso y atmósferas concretas para generar música que encaje con el estado de ánimo correspondiente

  * background music for parties
  * radio broadcasts
  * workout playlists



#### 

​

Elementos instrumentales

  * saxophone
  * jazz
  * piano, violin



#### 

​

Tipos de voz

  * female voice
  * male voice
  * clean vocals



#### 

​

Términos profesionales

Usa algunos términos habituales del mundo de la música para controlar con precisión el resultado musical

  * 110 bpm (110 pulsaciones por minuto)
  * fast tempo
  * slow tempo
  * loops
  * fills
  * acoustic guitar
  * electric bass



### 

​

Letras

#### 

​

Etiquetas de estructura de la letra

  * [outro]
  * [verse]
  * [chorus]
  * [bridge]



#### 

​

Soporte multilingüe

  * ACE-Step V1 admite varios idiomas. Al usarlo, ACE-Step convierte los distintos idiomas a letras del alfabeto inglés y luego genera la música.
  * En ComfyUI, todavía no hemos implementado por completo la conversión de todos los idiomas a letras del alfabeto inglés. Por ahora, solo están implementados los [caracteres japoneses hiragana y katakana](https://github.com/Comfy-Org/ComfyUI/commit/5d3cc85e13833aeb6ef9242cdae243083e30c6fc). Así que, si necesitas usar varios idiomas para generar música, primero debes convertir el idioma correspondiente a letras del alfabeto inglés y luego escribir la abreviatura del código de idioma al comienzo de `lyrics`, como el chino `[zh]`, el coreano `[ko]`, etc.

Por ejemplo:
    
    
    [verse]
    
    [zh]wo3zou3guo4shen1ye4de5jie1dao4
    [zh]leng3feng1chui1luan4si1nian4de5piao4liang4wai4tao4
    [zh]ni3de5wei1xiao4xiang4xing1guang1hen3xuan4yao4
    [zh]zhao4liang4le5wo3gu1du2de5mei3fen1mei3miao3
    
    [chorus]
    
    [verse]​
    [ko]hamkke si-kkeuleo-un sesang-ui sodong-eul pihae​
    [ko]honja ogsang-eseo dalbich-ui eolyeompus-ileul balaboda​
    [ko]niga salang-eun lideum-i ganghan eum-ag gatdago malhaess-eo​
    [ko]han ta han tamada ma-eum-ui ondoga eolmana heojeonhanji ijge hae
    
    [bridge]
    [es]cantar mi anhelo por ti sin ocultar
    [es]como poesía y pintura, lleno de anhelo indescifrable
    [es]tu sombra es tan terca como el viento, inborrable
    [es]persiguiéndote en vuelo, brilla como cruzar una mar de nubes
    
    [chorus]
    [fr]que tu sois le vent qui souffle sur ma main
    [fr]un contact chaud comme la douce pluie printanière
    [fr]que tu sois le vent qui s'entoure de mon corps
    [fr]un amour profond qui ne s'éloignera jamais
    

Actualmente, ACE-Step admite 19 idiomas, pero los siguientes diez tienen mejor soporte:

  * Inglés
  * Chino: [zh]
  * Ruso: [ru]
  * Español: [es]
  * Japonés: [ja]
  * Alemán: [de]
  * Francés: [fr]
  * Portugués: [pt]
  * Italiano: [it]
  * Coreano: [ko]



Las etiquetas de idioma anteriores no se han probado por completo en el momento de redactar esta documentación. Si alguna etiqueta de idioma es incorrecta, [envía un problema a nuestro repositorio de documentación](https://github.com/Comfy-Org/docs/issues) y haremos las correcciones oportunas.

## 

​

Recursos relacionados con ACE-Step

  * [Página del proyecto](https://ace-step.github.io/)
  * [Hugging Face](https://huggingface.co/ACE-Step/ACE-Step-v1-3.5B)
  * [GitHub](https://github.com/ace-step/ACE-Step)
  * [Scripts de entrenamiento](https://github.com/ace-step/ACE-Step?tab=readme-ov-file#-train)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/audio/ace-step/ace-step-v1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/audio/ace-step/ace-step-v1)

[Stable Audio 3](https://docs.comfy.org/es/tutorials/audio/stable-audio/stable-audio-3)[ACE-Step 1.5](https://docs.comfy.org/es/tutorials/audio/ace-step/ace-step-v1-5)
