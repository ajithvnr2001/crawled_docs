---
url: https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/drama-3/
title: Fish Audio Drama 3: direcciones, etiquetas de palabras y plantillas - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:48.609950+00:00
---

# Fish Audio Drama 3: direcciones, etiquetas de palabras y plantillas - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/drama-3/

## En esta página

Volver arriba

  * Usar Drama 3 en ComfyUI
    * Seleccionar el modelo
    * Conectar las voces
  * Dirigir una interpretación
    * Describir la interpretación
    * Añadir sonidos y pausas
    * Dirigir en cualquier idioma
    * Cambiar solo palabras específicas
    * Cambiar de idioma a mitad de línea
    * Combinarlas
  * Flujos de trabajo disponibles
    * Fish Audio Drama 3: Actuación dirigida
    * Fish Audio Drama 3: Diálogo de dos hablantes
  * Cuenta y precios
  * Empezar



Fish Audio

# Fish Audio Drama 3: direcciones, etiquetas de palabras y plantillas

Copiar páginaCopiar página

Ejecuta Fish Audio Drama 3 en ComfyUI con direcciones en lenguaje natural y etiquetas de palabras emparejadas, y aprovecha las plantillas listas.

Copiar páginaCopiar página

Drama 3 es el modelo de texto a voz más reciente de Fish Audio, diseñado para la dirección de voz. Una escena completa se escribe como un solo guion, la interpretación se describe en lenguaje natural dentro del texto y las etiquetas de palabras emparejadas cambian solo las palabras que envuelven. En ComfyUI se ejecuta en el nodo Fish Audio Text to Speech con `model` establecido en `drama-3`. Para ver los demás modelos de Fish Audio, consulta [Fish Audio: texto a voz, clonación de voz y voz a texto](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/fish-audio).

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

Usar Drama 3 en ComfyUI

Los nodos asociados de Fish Audio están disponibles en el menú de nodos dentro de `partner/audio/Fish Audio`, y Drama 3 usa los mismos que los otros modelos: Text to Speech, Speech to Text, Voice Selector e Instant Voice Clone.

### 

​

Seleccionar el modelo

Establece `model` en `drama-3` en el nodo Text to Speech.

### 

​

Conectar las voces

La salida `voice` del Voice Selector o del Instant Voice Clone se conecta al nodo Text to Speech. `drama-3` expone la entrada `voices` ampliable con hasta 5 ranuras. Con una voz conectada, el nodo la pasa internamente como `reference_id`. Con dos o más, el texto debe marcar a los hablantes con `@Voice1`, `@Voice2`, etc., y cada voz conectada debe aparecer en el texto al menos una vez; de lo contrario, el nodo produce un error.

## 

​

Dirigir una interpretación

`drama-3` recibe indicaciones del propio guion. Una indicación en lenguaje natural entre corchetes cambia la interpretación a partir de ese punto, y una etiqueta de palabra emparejada cambia solo las palabras que envuelve:
    
    
    [calm and inviting] Welcome back to the studio.
    [leans in, conspiratorial] There is one trick nobody tells you about.
    [light, playful] Ready? <whisper>It is all in the timing.</whisper> [bright, back to full voice] And that is the whole secret.
    

### 

​

Describir la interpretación

Coloca una indicación entre corchetes antes de las palabras a las que se aplica y escríbela como se la explicarías a un actor de doblaje: emoción, intención, ritmo o a quién le habla el personaje.
    
    
    [barely holding it together, forcing a smile] I'm fine. Really. Go on without me.
    [professional broadcast tone] And now, the headlines.
    

Una indicación se aplica hasta la siguiente. `[calm]` al inicio de una línea se mantiene durante toda la línea a menos que otra indicación la reemplace, y varias indicaciones en una misma línea cambian la interpretación dentro de esa línea.

### 

​

Añadir sonidos y pausas

Escribe un sonido o una pausa entre corchetes en el punto donde debe ocurrir, como un suspiro, una risa o una respiración:
    
    
    I'm fine. [shaky breath] Really. [small laugh] Go on without me.
    

### 

​

Dirigir en cualquier idioma

Las indicaciones no tienen que coincidir con el idioma del guion. Un guion en inglés se puede dirigir en chino, y viceversa:
    
    
    [像是在强忍着眼泪，却努力笑着] I'm fine. Really. Go on without me.
    

### 

​

Cambiar solo palabras específicas

Envuelve las palabras en una etiqueta emparejada para cambiar la interpretación solo de esas palabras. Las etiquetas compatibles son `<whisper>`, `<emphasis>`, `<soft>`, `<fast>`, `<slow>`, `<stress>` y `<forceful>`:
    
    
    It is going to <emphasis>blow</emphasis>.
    I'm fine. Really. <whisper>Go on without me.</whisper>
    

### 

​

Cambiar de idioma a mitad de línea

Fish Audio clasifica las etiquetas de idioma como experimentales.

Envuelve una frase en una etiqueta de idioma para cambiar el idioma solo en esas palabras. Esto ayuda en una línea que mezcla dos idiomas, o cuando una frase debe leerse en otro idioma:
    
    
    She looked at the menu and said <french>Je voudrais une table pour deux, s'il vous plaît.</french> The waiter smiled.
    

### 

​

Combinarlas

Las indicaciones, las etiquetas de palabra y las [etiquetas de fonemas](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/prompt-guide#phoneme-control) funcionan en el mismo guion, incluso dentro de un turno con varios hablantes:
    
    
    @Voice1 [calm and inviting] Welcome back to the studio.
    @Voice2 [leans in, conspiratorial] There is one trick nobody tells you about.
    @Voice1 [light, playful] Ready? <whisper>It is all in the timing.</whisper> [bright, back to full voice] And that is the whole secret.
    

Las etiquetas de emoción, tono y efecto de la [guía de prompts](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/prompt-guide) pertenecen a los otros modelos. En `drama-3`, usa las indicaciones y las etiquetas de palabra de esta página en su lugar.

## 

​

Flujos de trabajo disponibles

Dos plantillas listas para usar cubren Drama 3: una actuación dirigida con una sola voz y un diálogo de dos hablantes. Ábrelas desde la Biblioteca de plantillas en ComfyUI o ejecútalas directamente en Comfy Cloud. Ambas requieren ComfyUI 0.39.3 o posterior.

### 

​

Fish Audio Drama 3: Actuación dirigida

Interpreta un guion con una sola voz. Las indicaciones en el campo `text` modifican la entrega línea por línea, y `<whisper>...</whisper>` cambia algunas palabras sin alterar el resto de la línea. La plantilla parte de la voz predefinida Delia y puedes cambiarla en el Voice Selector. ![Fish Audio Drama 3: Directed Performance workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_drama3_directed-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Fish Audio Drama 3: Directed Performance” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadAudio` correspondiente:

## fish_audio_example.mp3

`LoadAudio` nodo 11 · `fish_audio_example.mp3`

### 

​

Fish Audio Drama 3: Diálogo de dos hablantes

Genera una escena completa en una sola pasada, con un Voice Selector por hablante y las etiquetas de diálogo en el guion. La plantilla incluye las voces predefinidas Delia y Sheila:
    
    
    [deep, cinematic narrator] @Voice1 Every night, the city tells a story.
    [soft, close, like a secret] @Voice2 But only one voice ever finishes it.
    [drops to a whisper, then brightens] @Voice1 Fish Audio Drama 3, <whisper>now in ComfyUI</whisper>.
    

![Fish Audio Drama 3: Two-Speaker Dialogue workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_drama3_dialogue-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Fish Audio Drama 3: Two-Speaker Dialogue” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadAudio` correspondiente:

## fish_audio_example.mp3

`LoadAudio` nodo 11 · `fish_audio_example.mp3`

## 

​

Cuenta y precios

Los nodos requieren iniciar sesión en una cuenta de ComfyUI y se cobran por uso. Drama 3 cuesta aproximadamente $14.30 por 1M de bytes de texto durante la oferta de lanzamiento, y luego $35.75 a partir del 13 de noviembre de 2026. Consulta [Precios de los nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing) para conocer las tarifas de créditos y la ventana de la oferta.

## 

​

Empezar

  1. Actualiza ComfyUI a 0.39.3 o una versión más reciente
  2. Abre una de las plantillas de Drama 3 de arriba, o agrega los nodos de Fish Audio desde `partner/audio/Fish Audio`
  3. Selecciona `drama-3` en el nodo Text to Speech y conecta una voz mediante el Voice Selector o el Instant Voice Clone
  4. Escribe el guion con indicaciones y etiquetas de palabras y luego ejecútalo



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/fishaudio/drama-3.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/fishaudio/drama-3)

[Descripción general](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/fish-audio)[Guía de prompts](https://docs.comfy.org/es/tutorials/partner-nodes/fishaudio/prompt-guide)
