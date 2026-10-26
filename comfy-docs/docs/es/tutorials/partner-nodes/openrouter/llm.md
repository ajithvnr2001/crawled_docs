---
url: https://docs.comfy.org/es/tutorials/partner-nodes/openrouter/llm/
title: OpenRouter LLM en ComfyUI: muchos modelos en un solo nodo - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:53.771709+00:00
---

# OpenRouter LLM en ComfyUI: muchos modelos en un solo nodo - ComfyUI

> Source: https://docs.comfy.org/es/tutorials/partner-nodes/openrouter/llm/

## En esta página

Volver arriba

  * Para qué sirve OpenRouter LLM
  * Modelos compatibles
  * Entradas específicas del modelo
    * OpenRouter LLM
    * Notas adicionales



OpenRouter

# OpenRouter LLM en ComfyUI: muchos modelos en un solo nodo

Copiar páginaCopiar página

Usa el nodo asociado OpenRouter LLM en ComfyUI para chat, razonamiento, visión y respuestas fundamentadas en la web de varios proveedores de modelos.

Copiar páginaCopiar página

[OpenRouter](https://openrouter.ai) es una plataforma de enrutamiento unificada para modelos de lenguaje grandes. Expone muchos proveedores a través de una sola API para que puedas cambiar de modelo sin modificar tu integración. ComfyUI se conecta mediante el nodo asociado **OpenRouter LLM** , que ofrece una lista seleccionada de modelos de texto y multimodales (Claude, GPT, Gemini, Grok, DeepSeek, Qwen, Mistral, GLM, Kimi y Perplexity Sonar) en un solo nodo.

## 

​

Para qué sirve OpenRouter LLM

  * **Chat de texto** : prompts y un `system_prompt` opcional para instrucciones de rol o tarea
  * **Visión** : adjunta imágenes de referencia en los modelos compatibles (la cantidad de ranuras depende del modelo)
  * **Entrada de video** : Gemini 3.5 Flash y Qwen 3.6 Plus/Flash admiten videos de referencia opcionales
  * **Razonamiento** : `reasoning_effort` en modelos de razonamiento o de razonamiento frontier (`off`, `low`, `medium`, `high`)
  * **Búsqueda web** : los modelos Perplexity Sonar exponen `search_context_size` para respuestas fundamentadas

Los precios por token se muestran en [Precios de nodos asociados](https://docs.comfy.org/es/tutorials/partner-nodes/pricing#openrouter).

## 

​

Modelos compatibles

Modelo| Visión (máx. de imágenes)| Video| Opciones adicionales  
---|---|---|---  
`anthropic/claude-opus-4.8`| 20| Ninguno| Esfuerzo de razonamiento  
`anthropic/claude-opus-4.7`| 20| Ninguno| Esfuerzo de razonamiento  
`anthropic/claude-fable-5`| 20| Ninguno| Esfuerzo de razonamiento  
`anthropic/claude-sonnet-5`| 20| Ninguno| Esfuerzo de razonamiento  
`anthropic/claude-haiku-4.5`| 20| Ninguno| Esfuerzo de razonamiento  
`openai/gpt-5.6-sol-pro`| 20| Ninguno| Esfuerzo de razonamiento  
`openai/gpt-5.6-sol`| 20| Ninguno| Esfuerzo de razonamiento  
`openai/gpt-5.6-terra-pro`| 20| Ninguno| Esfuerzo de razonamiento  
`openai/gpt-5.6-terra`| 20| Ninguno| Esfuerzo de razonamiento  
`openai/gpt-5.6-luna-pro`| 20| Ninguno| Esfuerzo de razonamiento  
`openai/gpt-5.6-luna`| 20| Ninguno| Esfuerzo de razonamiento  
`openai/gpt-5.5-pro`| 20| Ninguno| Esfuerzo de razonamiento  
`openai/gpt-5.5`| 20| Ninguno| Esfuerzo de razonamiento  
`google/gemini-3.5-flash`| 20| Hasta 4| Esfuerzo de razonamiento  
`x-ai/grok-4.5`| 20| Ninguno| Esfuerzo de razonamiento  
`x-ai/grok-4.20`| 20| Ninguno| Esfuerzo de razonamiento  
`x-ai/grok-4.3`| 20| Ninguno| Esfuerzo de razonamiento  
`deepseek/deepseek-v4-pro`| Ninguno| Ninguno| Esfuerzo de razonamiento  
`deepseek/deepseek-v4-flash`| Ninguno| Ninguno| Esfuerzo de razonamiento  
`deepseek/deepseek-v3.2`| Ninguno| Ninguno| Esfuerzo de razonamiento  
`qwen/qwen3.6-max-preview`| Ninguno| Ninguno| Esfuerzo de razonamiento  
`qwen/qwen3.6-plus`| 10| Hasta 4| Esfuerzo de razonamiento  
`qwen/qwen3.6-flash`| 10| Hasta 4| Esfuerzo de razonamiento  
`mistralai/mistral-large-2512`| 8| Ninguno| Ninguno  
`mistralai/mistral-medium-3-5`| 8| Ninguno| Esfuerzo de razonamiento  
`z-ai/glm-4.6`| Ninguno| Ninguno| Esfuerzo de razonamiento  
`z-ai/glm-5`| Ninguno| Ninguno| Esfuerzo de razonamiento  
`moonshotai/kimi-k3`| 10| Ninguno| Esfuerzo de razonamiento  
`moonshotai/kimi-k2.6`| 10| Ninguno| Esfuerzo de razonamiento  
`moonshotai/kimi-k2-thinking`| Ninguno| Ninguno| Esfuerzo de razonamiento  
`perplexity/sonar-pro`| Ninguno| Ninguno| Tamaño del contexto de búsqueda  
`perplexity/sonar-reasoning-pro`| Ninguno| Ninguno| Tamaño del contexto de búsqueda, esfuerzo de razonamiento  
`perplexity/sonar-deep-research`| Ninguno| Ninguno| Tamaño del contexto de búsqueda, esfuerzo de razonamiento  
  
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

Entradas específicas del modelo

El menú desplegable **model** es un cuadro combinado dinámico. Cuando cambias el modelo, el nodo actualiza qué entradas aparecen:

  * **Ranuras de imagen** : se muestran solo en modelos con capacidad de visión; el número de ranuras coincide con el límite del modelo
  * **Ranuras de video** : se muestran solo en Gemini 3.5 Flash y Qwen 3.6 Plus/Flash
  * **Esfuerzo de razonamiento** : se muestra en modelos de razonamiento y modelos de razonamiento de frontera
  * **Tamaño del contexto de búsqueda** : se muestra en modelos Perplexity Sonar

Los modelos de solo texto ocultan las entradas de imagen y video.

### 

​

OpenRouter LLM

Selecciona un modelo de la lista curada de OpenRouter (Claude, GPT, Gemini, etc.). Genera una respuesta de texto con subidas opcionales de contenido multimedia para los modelos con capacidad de visión. ![Vista previa del flujo de trabajo de OpenRouter LLM](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_llm-1.webp)

## Ejecutar en Comfy Cloud

Abrir en Comfy Cloud

## Descargar flujo de trabajo

Descarga el JSON o busca “OpenRouter LLM” en la Biblioteca de plantillas

**Materiales de entrada** Sube este archivo al nodo `LoadImage` correspondiente:

## contact_sheet_app_input_1.png

Nodo `LoadImage` 2 · `contact_sheet_app_input_1.png`

![contact_sheet_app_input_1.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/contact_sheet_app_input_1.png)

En este ejemplo, el flujo de trabajo analiza una imagen de referencia y devuelve un prompt de texto a imagen para los nodos de imagen posteriores. Puedes omitir **Load Image** , cambiar los prompts o reconstruir el gráfico por completo para tu propio caso de uso.

Si usas la plantilla como referencia, una ejecución típica es la siguiente:

  1. En **Load Image** , carga la imagen de referencia (omite este paso para chat de solo texto)
  2. En **OpenRouter LLM** , conecta la imagen a `image_1` (aparecen más ranuras cuando el modelo las admite)
  3. Configura **prompt** , por ejemplo, pide al modelo que analice la imagen y devuelva un prompt de generación
  4. (Opcional) Configura **system_prompt** en las opciones avanzadas para el tono, el formato o las restricciones
  5. Elige un **model** ; ajusta **reasoning_effort** o **search_context_size** cuando aparezcan
  6. Haz clic en **Run** o presiona `Ctrl(cmd) + Enter`
  7. Consulta la respuesta en **Preview Any**



### 

​

Notas adicionales

  * **seed** : establece `0` para omitirla; la mayoría de los modelos solo la tratan como una sugerencia
  * La carga de las imágenes y los videos de referencia es automática al ejecutar el flujo de trabajo; solo conectas las salidas de imagen/video de ComfyUI al nodo
  * Para consultar el precio por modelo, visita [OpenRouter en la página de precios](https://docs.comfy.org/es/tutorials/partner-nodes/pricing#openrouter)



¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/tutorials/partner-nodes/openrouter/llm.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/tutorials/partner-nodes/openrouter/llm)

[GPT-6 Astra](https://docs.comfy.org/es/tutorials/partner-nodes/openai/gpt-6-astra)
