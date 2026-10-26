---
url: https://docs.comfy.org/es/tutorials/partner-nodes/anthropic/claude/
title: Anthropic Claude en ComfyUI: flujos de trabajo de chat y an\u00e1lisis de im\u00e1genes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:45.850938+00:00
---

# Anthropic Claude en ComfyUI: flujos de trabajo de chat y análisis de imágenes - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/anthropic/claude/

## En esta página

Volver arriba

  * Para qué sirve Anthropic Claude
  * Modelos compatibles
  * Flujo de trabajo de chat con Anthropic Claude
    * Notas adicionales
  * Flujo de trabajo de Claude Fable 5.1



Anthropic

# Anthropic Claude en ComfyUI: flujos de trabajo de chat y análisis de imágenes

Copiar páginaCopiar página

Usa el nodo asociado Anthropic Claude en ComfyUI para chatear y analizar imágenes con las familias de modelos Opus, Sonnet y Haiku.

Copiar páginaCopiar página

Anthropic Claude es una familia de modelos de IA potentes, conocidos por su sólida capacidad de razonamiento, su seguridad y sus funciones para contextos largos. ComfyUI ha integrado la API de Anthropic Claude a través de los Nodos asociados, lo que te permite usar Claude directamente en tus flujos de trabajo para tareas de conversación y análisis de imágenes.

## 

​

Para qué sirve Anthropic Claude

  * **Razonamiento sólido** : Una familia de modelos conocida por su razonamiento sólido, su seguridad y sus capacidades de contexto largo
  * **Tareas conversacionales y de análisis de imágenes** : Usa Claude directamente dentro de tus flujos de trabajo de ComfyUI mediante los Nodos asociados
  * **Entrada multimodal** : Todos los modelos compatibles aceptan entradas solo de texto y de texto + imagen, con hasta 20 imágenes por solicitud
  * **Un modelo para cada carga de trabajo** : Desde la línea insignia Opus hasta Haiku, rápido y rentable, para casos de uso de alto rendimiento



## 

​

Modelos compatibles

Modelo| Fortalezas  
---|---  
**Opus 5.5**|  El modelo insignia más reciente de Anthropic y el sucesor de Opus 5. Diseñado para razonamiento exigente, programación y trabajo agéntico de horizonte largo, con un precio inferior al de Opus 5. El pensamiento siempre está habilitado y `temperature` no está disponible.  
**Opus 5**|  El modelo insignia anterior de Anthropic, lanzado el 24 de julio de 2026. Con la mitad del precio de Claude Fable 5.1 y un rendimiento comparable en tareas de programación y trabajo de conocimiento.  
**Fable 5.1**|  El modelo de razonamiento avanzado de Anthropic, lanzado el 1 de septiembre de 2026. Una actualización de Fable 5 con menores costos de carga agéntica y menos falsos positivos. El pensamiento siempre está habilitado y `temperature` no está disponible.  
**Sonnet 5.5**|  El modelo de gama media más reciente de Anthropic y el segundo lanzamiento de la familia Claude 5.5. Una mejora sobre Sonnet 5 al mismo precio, con una ventana de contexto de 1M. El pensamiento es adaptativo y `temperature` no está disponible.  
**Sonnet 5**|  El modelo de gama media de Anthropic, lanzado el 30 de junio de 2026. Diseñado para tareas autónomas y agénticas a un precio menor que la línea Opus. `temperature` no está disponible.  
**Opus 4.8**|  El modelo insignia de la generación anterior con un sólido rendimiento integral.  
**Opus 4.7**|  El modelo más capaz de Anthropic. Una mejora radical en programación agéntica, razonamiento complejo y análisis matizado. Ventana de contexto de 1M. Fecha de corte de conocimiento: enero de 2026.  
**Opus 4.6**|  El modelo insignia de la generación anterior con un sólido rendimiento integral. Ventana de contexto de 1M.  
**Sonnet 4.6**|  La mejor combinación de velocidad e inteligencia para la mayoría de las cargas de trabajo. Ventana de contexto de 1M. Latencia baja.  
**Sonnet 4.5**|  Rápido y capaz, ideal para tareas cotidianas. Ventana de contexto de 200k.  
**Haiku 4.5**|  La opción más rápida y rentable para consultas simples y casos de uso de alto rendimiento. Ventana de contexto de 200k.  
  
Todos los modelos admiten entradas solo de texto y multimodales (texto + imagen) con hasta 20 imágenes por solicitud.

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

Flujo de trabajo de chat con Anthropic Claude

![Vista previa del flujo de trabajo de chat con Anthropic Claude](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Anthropic Claude” en la biblioteca de plantillas

En la plantilla correspondiente hemos preparado un prompt para analizar y generar prompts de rol, que se usa para interpretar tus imágenes y convertirlas en los prompts de dibujo correspondientes.

Sigue los pasos numerados en la imagen del flujo de trabajo para completar la ejecución básica:

  1. En el nodo `Load Image`, carga la imagen que necesitas que la IA interprete (opcional: sáltalo si solo vas a hacer consultas de texto)
  2. En el nodo `Anthropic Claude`, modifica `prompt` para establecer el prompt de tu conversación, o cambia `model` para seleccionar otro modelo de Claude
  3. (Opcional) Define `system_prompt` para establecer las instrucciones de comportamiento del modelo
  4. Haz clic en `Run` o presiona `Ctrl(cmd) + Enter` para ejecutar la conversación
  5. Cuando la API devuelva los resultados, consulta la respuesta de la IA en el nodo `Preview Any`



### 

​

Notas adicionales

  * Ajusta `max_tokens` (hasta 32768) y `temperature` (de 0.0 a 1.0) en las opciones avanzadas del nodo. `temperature` no está disponible cuando el razonamiento (thinking) está habilitado ni en `Opus 4.7`
  * El parámetro `seed` controla si el nodo se vuelve a ejecutar: los resultados no son deterministas, independientemente del valor de `seed`



## 

​

Flujo de trabajo de Claude Fable 5.1

Ejecuta Claude Fable 5.1, el modelo de razonamiento avanzado de Anthropic, directamente en tu flujo de trabajo para problemas de varios pasos y larga duración. Fable 5.1 siempre se ejecuta con el pensamiento habilitado y no expone un control de `temperature`. ![Vista previa del flujo de trabajo de Claude Fable 5.1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_fable5_1-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “Claude: Fable 5.1” en la Biblioteca de plantillas

## Imagen de entrada: blue_poppies_field.png

Imagen para el flujo de trabajo, o usa tu propia imagen.

Consulta los pasos numerados en la imagen del flujo de trabajo:

  1. En el nodo `Load Image`, carga la imagen que necesitas que la IA interprete (opcional: sáltalo para consultas solo de texto)
  2. En el nodo `Anthropic Claude`, modifica `prompt` para establecer el prompt de tu conversación. El modelo está preconfigurado como `Fable 5.1` con un límite de `max_tokens` de 32768
  3. Haz clic en `Run` o presiona `Ctrl(cmd) + Enter` para ejecutar la conversación
  4. Después de que la API devuelva los resultados, consulta la respuesta de la IA en el nodo `Preview Any`



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/anthropic/claude.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/anthropic/claude)

[Descripción general](https://docs.comfy.org/es/tutorials/partner-nodes/language/overview)[Gemini](https://docs.comfy.org/es/tutorials/partner-nodes/google/gemini)
