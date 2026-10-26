---
url: https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-uni-1/
title: Gu\u00eda de Luma Uni-1 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:52.162124+00:00
---

# Guía de Luma Uni-1 - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-uni-1/

## En esta página

Volver arriba

  * Qué hace diferente a Uni-1
  * En qué destaca Luma Uni-1
  * La distinción clave: Create vs Modify
  * Flujos de trabajo disponibles
    * Flujo de trabajo Image Create
    * Flujo de trabajo Image Edit
  * Parámetros principales
  * Trabajar con imágenes de referencia
    * Ejemplos del modo Create
    * Ejemplos del modo Modify
  * Pautas para el prompt
  * Relaciones de aspecto
  * Semillas: control y reproducibilidad
  * Técnicas avanzadas
    * Consistencia de personaje
    * Arquitectura de múltiples referencias
    * Cadena Create → Modify
    * Refinamiento iterativo
  * Solución de problemas
  * Referencia rápida
  * Las reglas de oro
  * Punto clave



Luma

# Guía de Luma Uni-1

Copiar páginaCopiar página

Usa los nodos asociados de Luma Uni-1 en ComfyUI para flujos de trabajo de imagen de Create y Modify.

Copiar páginaCopiar página

En **ComfyUI** , Luma **Uni-1** aparece como **Nodos asociados** para el trabajo unificado con imágenes: los grafos **Create** generan imágenes nuevas a partir de prompts (con referencias opcionales); los grafos **Modify** toman una imagen existente como entrada y la editan en el mismo sitio. Ambos se manejan con el flujo de trabajo habitual: conecta **Load Image** y **Save Image** , define prompts, semillas, relación de aspecto y ranuras de referencia en el nodo de Luma, y luego pon el grafo en cola de forma local o abre una plantilla en **Comfy Cloud**. Luma describe Uni-1 como un modelo autorregresivo que no usa diffusion y que solo tiene decodificador, y que razona sobre tu prompt antes de dibujar. En el lienzo, lo más importante es elegir entre **Create** y **Modify** , etiquetar las referencias con claridad e iterar con semillas.

## 

​

Qué hace diferente a Uni-1

  * **Dos modos claros** : Create Image (generar algo nuevo) y Modify Image (editar algo existente)
  * **Hasta 9 imágenes de referencia** , cada una con un rol definido
  * **Control sólido sobre estilos visuales específicos y de nicho**
  * **Soporte de semilla** para reproducibilidad e iteración controlada
  * **Nueve relaciones de aspecto** , de ultra vertical a ultra horizontal
  * **Renderizado de texto** que sea realmente legible
  * **Anclaje en búsqueda web** para contexto del mundo real
  * **Prompts multilingües**
  * **Salida multipanel** con consistencia temporal

Si entiendes los modos y cómo controlar las referencias, entiendes Uni-1.

## 

​

En qué destaca Luma Uni-1

Uni-1 sobresale en una amplia variedad de tareas:

  * **Fotorrealismo** con precisión en los materiales
  * **Ilustración y arte estilizado** con un fuerte control estético
  * **Restauración de fotos antiguas** y reproducción de estilo vintage
  * Composiciones **surrealistas y conceptuales**
  * **Renderizado de texto** : texto legible dentro de las imágenes, ideal para infografías y carteles
  * **Edición de imágenes** y refinamiento en varios turnos
  * **Generación guiada por referencias** con preservación de la identidad
  * **Salida de varios paneles** : personajes y escenas coherentes entre paneles



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

La distinción clave: Create vs Modify

Todo en Uni-1 empieza con una pregunta: **¿estoy creando algo nuevo o cambiando algo que ya existe?**

Modo| Qué hace| Cuándo usarlo  
---|---|---  
**Create Image**|  Genera una composición completamente nueva. Puede inspirarse en referencias.| ”Crea una escena nueva con el estilo de esta foto”  
**Modify Image**|  Edita una imagen de entrada específica. Conserva la composición y la estructura a menos que indiques lo contrario.| ”Haz que esta foto parezca de noche”  
  
Si tienes dudas:

  * Si el resultado debe parecerse a una **versión de tu entrada** , usa Modify
  * Si debe sentirse **inspirado pero nuevo** , usa Create



## 

​

Flujos de trabajo disponibles

### 

​

Flujo de trabajo Image Create

![Vista previa del flujo de trabajo Luma Uni-1 Image Create](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_uni_1_image_create-1.webp)

## Ejecutar Image Create en Cloud

Prueba el flujo de trabajo Image Create al instante en Comfy Cloud.

## Descargar el flujo de trabajo Image Create

Descarga el JSON o busca “Luma UNI-1 Image Create” en Biblioteca de plantillas

### 

​

Flujo de trabajo Image Edit

![Vista previa del flujo de trabajo Luma Uni-1 Image Edit](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_uni_1_image_edit-1.webp)

## Ejecutar Image Edit en Cloud

Prueba el flujo de trabajo Image Edit al instante en Comfy Cloud.

## Descargar el flujo de trabajo Image Edit

Descarga el JSON o busca “Luma UNI-1 Image Edit” en Biblioteca de plantillas

El flujo de trabajo es simple: **prompt → evaluar → refinar**. Deja la semilla en blanco mientras exploras. Cuando encuentres algo bueno, fija la semilla e itera a partir de ahí.

## 

​

Parámetros principales

Parámetro| Descripción  
---|---  
**Prompt**|  Tu control principal. Hasta 6,000 caracteres. Sé preciso.  
**Relación de aspecto**|  Controla el encuadre, no la calidad. Elige según el caso de uso.  
**Semilla**|  Misma semilla + mismo prompt → mismo resultado. Misma semilla + prompt cambiado → variación controlada. Sin semilla → exploración.  
**Imágenes de referencia** (Create)| Hasta 9 imágenes para guiar distintos aspectos.  
**Imagen de origen** (Modify)| La imagen que estás editando. Las dimensiones se conservan automáticamente.  
  
## 

​

Trabajar con imágenes de referencia

Las referencias solo funcionan si le dices al modelo para qué sirven. Usa esta estructura:
    
    
    Use IMAGE1 ([description]) as a [ROLE] reference.
    

Roles posibles: **Style** , **Character** , **Composition** , **Color palette** , **Lighting** , **Texture** , **Mood**. Sin roles, el modelo adivina, y las conjeturas no son fiables.

### 

​

Ejemplos del modo Create

**Referencia de estilo**
    
    
    Use IMAGE1 (impressionist oil painting with loose brushwork and warm
    sunset tones) as a STYLE reference. Create a portrait of a woman in her
    30s applying IMAGE1's color palette and painterly texture. The subject
    should be new.
    

**Referencia de personaje**
    
    
    Use IMAGE1 (woman with short copper-red hair, freckles) as a CHARACTER
    reference. Preserve her features. Generate a new scene: she's sitting
    in a softly lit café.
    

**Referencia múltiple**
    
    
    Use IMAGE1 as a COLOR PALETTE reference, IMAGE2 as LIGHTING, IMAGE3 as
    COMPOSITION. Create a lone figure walking through a rain-slicked street
    at night.
    

### 

​

Ejemplos del modo Modify

En el modo Modify, la claridad lo es todo. Indica siempre **qué cambiar** y **qué debe quedar intacto**.
    
    
    Change the time of day to golden hour. Update sky, light direction,
    shadows, and color temperature. Keep all subjects and composition
    unchanged.
    
    
    
    Make the rain heavier and add reflections on the ground. Keep all other
    elements unchanged.
    

## 

​

Pautas para el prompt

Longitudes recomendadas:

  * **Texto a imagen** → 80–250 palabras
  * **Guiado por referencia** → 100–300 palabras
  * **Modificar** → 30–100 palabras

Evita términos vagos (“hermoso”, “asombroso”), frases redundantes e instrucciones en conflicto. En su lugar, usa estéticas específicas y con nombre:

  * `Golden hour, 85mm lens, shallow depth of field`
  * `1970s Italian giallo film poster, high-contrast color blocking`

La precisión supera a la generalidad.

## 

​

Relaciones de aspecto

Elige según dónde se mostrará la imagen:

Relación| Caso de uso  
---|---  
1:1| Publicaciones para redes sociales  
9:16| video vertical  
16:9| Pantalla ancha  
3:2 / 2:3| Fotografía  
2:1 / 3:1| Cinemático / panorámico  
1:2 / 1:3| Ultra alto  
  
En el modo Modify, la relación de aspecto queda fijada a la imagen de origen.

## 

​

Semillas: control y reproducibilidad

Las semillas convierten la experimentación en sistemas.

  * **Semilla fija** → consistencia
  * **Sin semilla** → exploración

Flujo de trabajo:

  1. Explora sin semilla
  2. Encuentra un buen resultado
  3. Fija la semilla
  4. Cambia una sola variable a la vez

Guarda tu prompt y tu semilla juntos. Esa es tu receta reutilizable.

## 

​

Técnicas avanzadas

### 

​

Consistencia de personaje

  1. Genera una imagen de referencia limpia y de frente
  2. Reutilízala como `IMAGE1 (CHARACTER)` en cada escena
  3. Mantén la etiqueta idéntica en todos los prompts



### 

​

Arquitectura de múltiples referencias

Asigna un rol por imagen:

  * IMAGE1 → personaje
  * IMAGE2 → estilo
  * IMAGE3 → iluminación
  * IMAGE4 → entorno

Termina el prompt con:
    
    
    Treat each reference as having authority over its assigned layer only.
    

### 

​

Cadena Create → Modify

Usa Create para explorar composiciones y luego Modify para refinar detalles. Este es uno de los flujos de trabajo más potentes.

### 

​

Refinamiento iterativo

  1. Explora (sin semilla)
  2. Fija la semilla
  3. Cambia una sola variable por generación
  4. Documenta los resultados

Parece más lento, pero en realidad es más rápido, porque siempre sabes qué cambió.

## 

​

Solución de problemas

Problema| Solución  
---|---  
Referencias ignoradas| Etiqueta cada una claramente  
Modify cambia demasiado| Indica explícitamente qué debe permanecer sin cambios  
Salidas inconsistentes| Fija la semilla  
El prompt se ignora parcialmente| Elimina los conflictos o divide en pasos  
La salida se parece a la imagen de referencia| Es posible que estés en el modo Modify  
Inconsistencia del personaje| Reutiliza una imagen de referencia canónica  
  
## 

​

Referencia rápida

**Create Image**

  * Composiciones nuevas
  * Texto + hasta 9 referencias
  * Prompts descriptivos

**Modify Image**

  * Edita imágenes existentes
  * Imagen fuente + referencias
  * Prompts directos y precisos



## 

​

Las reglas de oro

  1. Etiqueta cada referencia
  2. En el modo Modify, indica siempre qué **no** debe cambiar
  3. Cambia una sola variable a la vez al refinar
  4. Guarda el prompt y la semilla para poder reproducirlo
  5. Create = escenas nuevas, Modify = ediciones



## 

​

Punto clave

Dominar Uni-1 se reduce a tres cosas: **elige el modo correcto → controla tus referencias → itera con intención**. Una vez que tengas eso en su lugar, ya no estarás adivinando, estarás dirigiendo.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/luma/luma-uni-1.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/luma/luma-uni-1)

[Krea2 T2I](https://docs.comfy.org/es/tutorials/partner-nodes/krea/krea-2-t2i)[Luma texto a imagen](https://docs.comfy.org/es/tutorials/partner-nodes/luma/luma-text-to-image)
