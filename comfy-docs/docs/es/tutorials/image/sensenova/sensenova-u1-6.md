---
url: https://docs.comfy.org/es/tutorials/image/sensenova/sensenova-u1-6/
title: SenseNova U1.6 en ComfyUI: texto a imagen y edici\u00f3n de im\u00e1genes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:29.340927+00:00
---

# SenseNova U1.6 en ComfyUI: texto a imagen y edición de imágenes - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/image/sensenova/sensenova-u1-6/

## En esta página

Volver arriba

  * Muestras
    * Fotografía, ilustración y pósteres
  * La autocorrección en la práctica
  * Flujo de trabajo de texto a imagen
    * SenseNova U1.6: Text to Image
    * Archivo del flujo de trabajo
    * Descarga de modelos
    * Ajustes de muestreo
    * Consejos de prompting
  * Flujo de trabajo de edición de imágenes
    * SenseNova U1.6: Image Edit
    * Archivo del flujo de trabajo
    * Descarga de modelos
    * Ajustes de muestreo
    * Consejos de prompting
    * Edición multiturno
  * Sobre el ampliador de prompts



Sensenova

# SenseNova U1.6 en ComfyUI: texto a imagen y edición de imágenes

Copiar páginaCopiar página

Genera y edita imágenes con SenseNova U1.6 en ComfyUI: un backbone multimodal de 8B, Turbo de 8 pasos o Quality de 50 pasos, y una pasada de autocorrección.

Copiar páginaCopiar página

![Muestras de SenseNova U1.6: retrato con desenfoque de movimiento, calle pintada, póster ilustrado, macrofotografía e ilustración de personaje](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/showcase-hero.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=4a6ff8eeed454dc97fa18eb383115758) **SenseNova-U1.6** es un modelo multimodal unificado. La comprensión visual y la generación de imágenes se ejecutan en un único backbone `mot` de 8B, así que el mismo modelo lee un prompt o una imagen de origen y devuelve el resultado. Está pensado para trabajos donde importan por igual la precisión y el aspecto: retratos, pósteres, ilustraciones e infografías. También ejecuta una pasada de autocorrección autónoma. Cuando vuelve un resultado, el modelo compara su propia salida con el prompt y regenera si algo no coincide, hasta 5 pasadas. **Aspectos destacados** :

  * **Un backbone, dos direcciones** : el mismo modelo `mot` de 8B se encarga de interpretar y de renderizar, tanto en texto a imagen como en ediciones guiadas por una imagen de origen.
  * **Autocorrección autónoma** : el modelo compara su propia salida con el prompt y regenera, hasta 5 pasadas.
  * **Dos modos de muestreo** : Turbo con el LoRA de 8 pasos a 8 pasos y CFG 1.0, o Quality sin el LoRA a 50 pasos y CFG 4.0.
  * **Estética más fina, expresión más rica** : **10% de mejora en calidad estética global frente a U1.5** en evaluaciones subjetivas, con modelos de recompensa estética entrenados por separado para retratos y escenas fotorrealistas, obra artística e infografías.
  * **Reflexión autónoma** : en tareas densas de infografía de UltraTextBench, el bucle de autocorrección logra una **mejora relativa media del 7% sobre la generación de una sola pasada**.
  * **Reescritura de prompt PE opcional** : un codificador de texto PE Qwen Image 2.1 expande un prompt corto en una descripción visual completa y rellena el texto exacto que aparece en la imagen.

**Enlaces oficiales** :

  * [Hugging Face: Comfy-Org/SenseNova-U1](https://huggingface.co/Comfy-Org/SenseNova-U1) (checkpoint y LoRA de 8 pasos)
  * [GitHub: OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1)
  * [Hugging Face: sensenova/SenseNova-U1.6-8B-MoT](https://huggingface.co/sensenova/SenseNova-U1.6-8B-MoT) (pesos oficiales del modelo)
  * [Hugging Face: sensenova/SenseNova-U1.6-8B-MoT-LoRAs](https://huggingface.co/sensenova/SenseNova-U1.6-8B-MoT-LoRAs) (LoRA oficial de 8 pasos)

Ambas plantillas requieren ComfyUI 0.46.0 o una versión posterior.

## Muestras

Seis ejemplos oficiales de SenseNova, que cubren las direcciones creativas a las que apunta el modelo; no son resultados generados con estos flujos de trabajo. La propuesta oficial combina dos objetivos: expresión visual creativa y autocorrección nativa, para entregar belleza y precisión a la vez.

### Fotografía, ilustración y pósteres

![Obturación lenta: el sujeto queda nítido y la multitud se estira.](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-slow-shutter.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=e3f928499b6cdfb6b866f3fbe5042c3b)

Obturación lenta: el sujeto queda nítido y la multitud se estira.

![Foto de producto de alta velocidad: una jarra suspendida con su salpicadura.](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-glass-mug.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=6a5960442733eb4c41a825c47660f02d)

Foto de producto de alta velocidad: una jarra suspendida con su salpicadura.

![Ilustración: una niña de azul entre flores y gatos.](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-blue-girl.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=2c0eeb7171e1d772fbb8470a6e0f35a0)

Ilustración: una niña de azul entre flores y gatos.

![Ilustración: montañas brumosas bajo luz naranja.](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-orange-mountains.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=b83c457b55cb66443204095befbe1bd4)

Ilustración: montañas brumosas bajo luz naranja.

![Póster con tipografía de titular: «Tasty ideas. Fresh design.»](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-tasty-ideas.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=f11375c552eb2f3809903573d6fb9e8f)

Póster con tipografía de titular: «Tasty ideas. Fresh design.»

![Póster: festival de moda Y2K, tipografía de bloques de píxeles sobre un set plano.](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-y2k-poster.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=04d9d37c49b5ae4f26df7e03be574460)

Póster: festival de moda Y2K, tipografía de bloques de píxeles sobre un set plano.

## La autocorrección en la práctica

Cada pareja usa el mismo prompt y la misma semilla: una sola pasada frente al bucle de generar / revisar / refinar. La tercera imagen es un recorte ampliado del texto que el bucle corrigió.

![Póster de mascota roja Antes](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-dog-before.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=cf19620f9370a12a275f5eefba2bf153)

Póster de mascota roja · Antes

![Póster de mascota roja Después](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-dog-after.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=4d5965dd66c9f0cfa39ba30cbbdc6005)

Póster de mascota roja · Después

![Póster de mascota roja Comparación de detalle](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-dog-detail.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=5a5e91bac9dd061fde4df0479cb0eefe)

Póster de mascota roja · Comparación de detalle

![Póster de bebida de la era Showa Antes](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-showa-before.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=618dbcc6375f447473d77d0634b3f5a6)

Póster de bebida de la era Showa · Antes

![Póster de bebida de la era Showa Después](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-showa-after.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=dd85dad132bb973158f18b158bb6dcc7)

Póster de bebida de la era Showa · Después

![Póster de bebida de la era Showa Comparación de detalle](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-showa-detail.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=df3fbcfda4dda66ccdf0cccfc1f9955c)

Póster de bebida de la era Showa · Comparación de detalle

## Flujo de trabajo de texto a imagen

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

### SenseNova U1.6: Text to Image

Convierte una escena escrita en una imagen terminada. El modelo lee el prompt, completa el detalle visual y devuelve una imagen de 4 megapíxeles con la relación de aspecto que elijas. ![Vista previa del flujo de trabajo de texto a imagen de SenseNova U1.6](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sensenova_u16_t2i-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “SenseNova U1.6: Text to Image” en la Biblioteca de plantillas

**Salida de ejemplo** ![Salida de ejemplo de texto a imagen de SenseNova U1.6](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_sensenova_u16_t2i.png)

#### Archivo del flujo de trabajo

Después de actualizar ComfyUI, abre la plantilla desde la Biblioteca de plantillas o arrastra la vista previa de arriba a ComfyUI para cargarla. El flujo de trabajo incluye dos pipelines:

  * **Pipeline Base** : una sola pasada de generación, para retratos, fotografía, pósteres e ilustración general.
  * **Pipeline con autocorrección** : genera, revisa y refina, hasta 5 pasadas, y después decodifica. Ideal para infografías, texto denso, gráficos y diagramas de pasos.

Los interruptores del lienzo seleccionan el pipeline, el LoRA Turbo y los valores de pasos y CFG.

#### Descarga de modelos

**Checkpoint**

  * [sensenova_u1.6_8b_mot_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/checkpoints/sensenova_u1.6_8b_mot_int8_convrot.safetensors)

**LoRA (modo Turbo)**

  * [sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/loras/sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors)

**Codificador de texto (PE)**

  * [qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors) (8.82 GB)

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── sensenova_u1.6_8b_mot_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   └── sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors
    │   └── 📂 text_encoders/
    │       └── qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors
    

#### Ajustes de muestreo

Modo| Pasos| CFG  
---|---|---  
**Turbo** (LoRA de 8 pasos)| 8| 1.0  
**Quality** (sin LoRA)| 50| 4.0  
  
  * **Turbo Mode?** carga u omite el LoRA de 8 pasos. Déjalo activo mientras iteras y desactívalo para obtener la máxima fidelidad de texto y detalle fino.
  * **Self-Correction** añade el bucle de generar, revisar y refinar. Actívalo en maquetas con mucho texto y desactívalo en retratos sencillos, porque cada pasada es otro muestreo completo.
  * **Enable PE** activa el reescritor de prompt descrito arriba.
  * **Resolution** fija el presupuesto total de megapíxeles con ajustes predefinidos de 1:1 a 21:9. El valor predeterminado es 4:3 (Standard) con 4 megapíxeles, es decir 2368 × 1760.



#### Consejos de prompting

  * Pon entre comillas cada palabra que deba aparecer en la imagen. El texto entrecomillado se renderiza tal cual, y el texto sin comillas es donde surgen los errores.
  * Con PE desactivado, escribes tú la descripción visual completa. Una petición de una línea no aprovecha la tipografía ni las dotes de maquetación del modelo.



## Flujo de trabajo de edición de imágenes

### SenseNova U1.6: Image Edit

Edita una foto adjuntándola como referencia y describiendo el cambio. El mismo backbone de 8B lee la imagen de origen, la reelabora y devuelve la edición con la resolución y la relación de aspecto de la propia imagen de origen. ![Vista previa del flujo de trabajo de edición de imágenes de SenseNova U1.6](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sensenova_u16_image_edit-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “SenseNova U1.6: Image Edit” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## sensenova_u16_edit_women_in_car.png

Nodo `LoadImage` 79 · `sensenova_u16_edit_women_in_car.png`

![sensenova_u16_edit_women_in_car.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/sensenova_u16_edit_women_in_car.png)

**Salida de ejemplo**

![Imagen de entrada](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/sensenova_u16_edit_women_in_car.png)![Salida de ejemplo de edición de imágenes de SenseNova U1.6](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_sensenova_u16_image_edit.png)

#### Archivo del flujo de trabajo

Después de actualizar ComfyUI, abre la plantilla desde la Biblioteca de plantillas o arrastra la vista previa de arriba a ComfyUI para cargarla. La imagen de origen se escala a 4 megapíxeles, el rango con el que se entrenó el modelo, y luego se rellena hasta un múltiplo de 32. La salida sigue la resolución y la relación de aspecto de la imagen de origen, así que la edición conserva el encuadre original. El modelo admite hasta 5 imágenes de referencia. Pasar de 1 a 4 referencias es el rango útil, y cada una consume tokens de visión y memoria. `ImageCompare` muestra la imagen de origen y el resultado lado a lado.

#### Descarga de modelos

**Checkpoint**

  * [sensenova_u1.6_8b_mot_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/checkpoints/sensenova_u1.6_8b_mot_int8_convrot.safetensors)

**LoRA (modo Turbo)**

  * [sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/loras/sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors)

**Codificador de texto (PE, edición de imágenes)**

  * [qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors) (8.82 GB)

**Ubicación de almacenamiento de los modelos**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── sensenova_u1.6_8b_mot_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   └── sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors
    │   └── 📂 text_encoders/
    │       └── qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors
    

#### Ajustes de muestreo

Modo| Pasos| CFG  
---|---|---  
**Turbo** (LoRA de 8 pasos)| 8| 1.0  
**Quality** (sin LoRA)| 50| 4.0  
  
  * **Turbo Mode?** carga u omite el LoRA de 8 pasos. Déjalo activo mientras iteras y desactívalo para obtener la máxima fidelidad de texto y detalle fino.
  * **Self-Correction** añade el bucle de editar, revisar y refinar, que rinde más cuando la maqueta lleva texto.
  * **Enable PE** lee la imagen de origen junto con tu instrucción y la expande en un prompt de edición completo.
  * **Imágenes de referencia** fijan el encuadre. El tamaño de salida sigue a la imagen de origen, así que recorta o redimensiona la referencia antes de encolar si necesitas otra forma.



#### Consejos de prompting

  * Di qué cambiar y enumera qué debe permanecer igual. La identidad, el encuadre, la iluminación y el fondo son los detalles que conviene nombrar.
  * Pon entre comillas cada palabra que deba aparecer en la imagen editada. El texto entrecomillado se renderiza tal cual.
  * Con PE desactivado, escribes tú la instrucción de edición completa, tanto el cambio como la lista de elementos que se conservan.



#### Edición multiturno

Esta versión todavía no incluye edición multiturno. Cada ejecución aplica una sola instrucción sobre la imagen de referencia que cargas y el modelo no mantiene un historial de conversación entre ejecuciones. Más adelante podría llegar como LoRA o como una rama específica. Por ahora, encadena tú las ediciones: guarda el resultado, cárgalo como siguiente referencia y describe el cambio siguiente.

## Sobre el ampliador de prompts

SenseNova U1.6 no incluye un modelo propio para ampliar prompts. Ambos flujos cargan opcionalmente el codificador de texto PE de **Qwen Image 2.1** — `qwen3.5_9b_qwen_image_2.1_pe_t2i` para texto a imagen y `..._pe_i2i` para edición — que convierte un prompt corto en una descripción visual completa y rellena el texto exacto que debe aparecer. Desactiva **Enable PE** para trabajar con tu prompt original.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/image/sensenova/sensenova-u1-6.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/image/sensenova/sensenova-u1-6)

[Qwen-Image-Layered](https://docs.comfy.org/es/tutorials/image/qwen/qwen-image-layered)[Z-Image](https://docs.comfy.org/es/tutorials/image/z-image/z-image)
