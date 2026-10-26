---
url: https://docs.comfy.org/es/development/comfy-router/models/openrouter/chat-completions/code/
title: Usa Chat Completions con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:17.026280+00:00
---

# Usa Chat Completions con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/openrouter/chat-completions/code/

## En esta página

Volver arriba

  * Configurar la solicitud
  * Esquema
    * Entrada
    * Salida
  * Ejemplos
    * Salida
  * Antes de lanzar



Openrouter

# Usa Chat Completions con Comfy Router

Copiar páginaCopiar página

Llama a openrouter/chat-completions mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `openrouter/chat-completions`, servida por Comfy Router desde Openrouter. **Entrada:** Texto, Imagen · **Salida:** Texto

## 

​

Configurar la solicitud

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Para Python, ejecuta `pip install comfy-sdk`. Para TypeScript, ejecuta `npm install @comfyorg/sdk`. cURL usa HTTP sin procesar. **ID del modelo:** `openrouter/chat-completions` **Endpoint:** `POST https://api.comfy.org/v2/models/openrouter/chat-completions`

Este modelo no tiene un ejemplo de solicitud ejecutable. Construye el cuerpo a partir de la documentación de entrada que aparece abajo y luego úsalo con la [guía de inicio rápido del Router](https://docs.comfy.org/es/development/comfy-router/quickstart).

## 

​

Esquema

### 

​

Entrada

​

cache_control

object

Habilita el almacenamiento en caché automático de prompts. Cuando se define en el nivel superior, el sistema aplica automáticamente puntos de interrupción de caché al último bloque que se puede almacenar en caché en la solicitud. Actualmente es compatible con modelos de Anthropic Claude.

​

cache_control.ttl

string

Valores posibles: `5m`, `1h`

​

cache_control.type

string

requerido

Valores posibles: `ephemeral`

​

debug

object

Opciones de depuración para inspeccionar las transformaciones de la solicitud (solo streaming)

​

debug.echo_upstream_body

boolean

Si es verdadero, incluye el cuerpo de la solicitud upstream transformado en un fragmento de depuración al inicio del stream. Solo funciona en modo streaming.

​

frequency_penalty

number

Penalización por frecuencia (-2.0 a 2.0)Formato: `double`

​

image_config

object | string | number | object[]

​

logit_bias

object

Ajustes de sesgo de logit de tokens

​

logprobs

boolean

Devuelve las probabilidades logarítmicas

​

max_completion_tokens

integer

Máximo de tokens en la respuesta

​

max_tokens

integer

Máximo de tokens (obsoleto, usa max_completion_tokens). Nota: algunos proveedores exigen un mínimo de 16.

​

messages

object[]

requerido

Lista de mensajes de la conversación

​

metadata

object

Pares clave-valor con información adicional del objeto (máximo 16 pares, claves de 64 caracteres y valores de 512 caracteres)

​

modalities

`text`, `image`, `audio`[]

Modalidades de salida de la respuesta. Los valores admitidos son “text”, “image” y “audio”.

​

model

string

Modelo a usar para la respuesta

​

models

string[]

Modelos a usar para la respuesta

​

parallel_tool_calls

boolean

Indica si se habilita el llamado paralelo de funciones durante el uso de herramientas. Cuando es verdadero, el modelo puede generar varias llamadas a herramientas en una sola respuesta.

​

plugins

object[]

Plugins que quieres habilitar para esta solicitud, incluidos sus ajustes.

​

presence_penalty

number

Penalización por presencia (-2.0 a 2.0)Formato: `double`

​

provider

object

Cuando hay varios proveedores de modelos disponibles, puedes indicar opcionalmente tu preferencia de enrutamiento.

​

provider.allow_fallbacks

boolean

Indica si se permite que proveedores de respaldo atiendan las solicitudes

  * true: (predeterminado) cuando el proveedor principal (o tus proveedores personalizados en “order”) no está disponible, usa el siguiente mejor proveedor.
  * false: usa solo el proveedor principal/personalizado y devuelve el error del upstream si no está disponible.



​

provider.data_collection

`deny`, `allow`

Configuración de recopilación de datos. Si ningún proveedor de modelos disponible cumple el requisito, tu solicitud devolverá un error.

  * allow: (predeterminado) permite proveedores que almacenan datos de usuario de forma no transitoria y que pueden entrenar con ellos
  * deny: usa solo proveedores que no recopilan datos de usuario.



​

provider.enforce_distillable_text

boolean

Indica si se restringe el enrutamiento solo a modelos que permiten la destilación de texto. Cuando es verdadero, solo se usarán los modelos en los que el autor haya permitido la destilación.

​

provider.ignore

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

Lista de slugs de proveedores que se deben ignorar. Si se proporciona, esta lista se combina con la configuración de proveedores ignorados de toda tu cuenta para esta solicitud.

​

provider.max_price

object

El objeto que especifica el precio máximo que quieres pagar por esta solicitud. Precio en USD por millón de tokens, para prompt y respuesta.

​

provider.max_price.audio

string

Precio por millón de tokens de prompt

​

provider.max_price.completion

string

Precio por millón de tokens de prompt

​

provider.max_price.image

string

Precio por millón de tokens de prompt

​

provider.max_price.prompt

string

Precio por millón de tokens de prompt

​

provider.max_price.request

string

Precio por millón de tokens de prompt

​

provider.only

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

Lista de slugs de proveedor permitidos. Si se proporciona, esta lista se combina con las configuraciones de proveedores permitidos de tu cuenta para esta solicitud.

​

provider.order

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

Una lista ordenada de slugs de proveedor. El enrutador intentará usar el primer proveedor del subconjunto de esta lista que admita el modelo que solicitaste y recurrirá al siguiente si no está disponible. Si no hay proveedores disponibles, la solicitud fallará con un mensaje de error.

​

provider.preferred_max_latency

number | object

Latencia máxima preferida (en segundos). Puede ser un número (se aplica a p50) o un objeto con umbrales específicos por percentil. Los endpoints por encima de los umbrales aún pueden usarse, pero tienen menor prioridad en el enrutamiento. Al usar modelos de respaldo, esto puede provocar que se use un modelo de respaldo en lugar del modelo principal si cumple con el umbral.

​

provider.preferred_min_throughput

number | object

Rendimiento mínimo preferido (en tokens por segundo). Puede ser un número (se aplica a p50) o un objeto con umbrales específicos por percentil. Los endpoints por debajo de los umbrales aún pueden usarse, pero tienen menor prioridad en el enrutamiento. Al usar modelos de respaldo, esto puede provocar que se use un modelo de respaldo en lugar del modelo principal si cumple con el umbral.

​

provider.quantizations

`int4`, `int8`, `fp4`, `fp6`, `fp8`, `fp16`, `bf16`, `fp32`, `unknown`[]

Una lista de niveles de cuantización para filtrar los proveedores.

​

provider.require_parameters

boolean

Indica si se deben filtrar los proveedores para dejar solo aquellos que admitan los parámetros que proporcionaste. Si se omite esta configuración o se establece en false, los proveedores recibirán solo los parámetros que admitan e ignorarán el resto.

​

provider.sort

`price`, `throughput`, `latency`, `exacto` | object

La estrategia de ordenamiento que se usará para esta solicitud si no se especifica “order”. Cuando se establece, no se realiza balanceo de carga.

​

provider.zdr

boolean

Indica si se debe restringir el enrutamiento solo a endpoints ZDR (Zero Data Retention). Cuando es true, solo se usarán los endpoints que no retienen prompts.

​

reasoning

object

Opciones de configuración para modelos de razonamiento

​

reasoning.effort

`xhigh`, `high`, `medium`, `low`, `minimal`, `none`

Restringe el esfuerzo de razonamiento en los modelos de razonamiento

​

reasoning.summary

string

Valores posibles: `auto`, `concise`, `detailed`

​

response_format

object

Configuración del formato de respuesta

​

route

object

Cualquier tipo

​

seed

integer

Semilla aleatoria para salidas deterministas

​

service_tier

`auto`, `default`, `flex`, `priority`, `scale`

El nivel de servicio que se usará para procesar esta solicitud.

​

session_id

string

Un identificador único para agrupar solicitudes relacionadas (por ejemplo, una conversación o un flujo de trabajo de agente) para observabilidad. Si se proporciona tanto en el cuerpo de la solicitud como en el encabezado x-session-id, el valor del cuerpo tiene prioridad. Máximo de 256 caracteres.

​

stop

string | string[] | object

Secuencias de parada (hasta 4)

​

stop_server_tools_when

object[]

Condiciones de parada para el bucle del agente de herramientas del servidor. Si se activa cualquier condición, se detiene el bucle (lógica OR). Cuando se establece, anula `max_tool_calls`.

​

stream

boolean

predeterminado:"false"

Habilitar la respuesta en streaming

​

stream_options

object

Opciones de configuración de streaming

​

stream_options.include_usage

boolean

Obsoleto: este campo no tiene efecto. Los detalles de uso completo siempre se incluyen.

​

temperature

number

Temperatura de muestreo (0-2)Formato: `double`

​

tool_choice

`none` | `auto` | `required` | object

Configuración de elección de herramienta

​

tools

object[]

Herramientas disponibles para llamadas a funciones

​

top_logprobs

integer

Número de log probabilidades principales a devolver (0-20)

​

top_p

number

Parámetro de muestreo de núcleo (0-1)Formato: `double`

​

trace

object

Metadatos para observabilidad y trazabilidad. Las claves conocidas (trace_id, trace_name, span_name, generation_name, parent_span_id) tienen un manejo especial. Las claves adicionales se pasan como metadatos personalizados a los destinos de difusión configurados.

​

trace.generation_name

string

​

trace.parent_span_id

string

​

trace.span_name

string

​

trace.trace_id

string

​

trace.trace_name

string

​

user

string

Identificador único de usuario

Generado a partir del esquema que Router sirve en `GET /v2/models/openrouter/chat-completions/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

choices

object[]

requerido

Lista de opciones de completado

​

choices[].finish_reason

string

requerido

Valores posibles: `tool_calls`, `stop`, `length`, `content_filter`, `error`

​

choices[].index

integer

requerido

Índice de la opción

​

choices[].logprobs

object

Logaritmos de probabilidad del completado

​

choices[].logprobs.content

object[]

requerido

Logaritmos de probabilidad de los tokens de contenido

​

choices[].logprobs.content[].bytes

integer[]

requerido

Bytes UTF-8 del token

​

choices[].logprobs.content[].logprob

number

requerido

Logaritmo de probabilidad del tokenFormato: `double`

​

choices[].logprobs.content[].token

string

requerido

El token

​

choices[].logprobs.content[].top_logprobs

object[]

requerido

Tokens alternativos principales con sus probabilidades

​

choices[].logprobs.content[].top_logprobs[].bytes

integer[]

requerido

​

choices[].logprobs.content[].top_logprobs[].logprob

number

requerido

Formato: `double`

​

choices[].logprobs.content[].top_logprobs[].token

string

requerido

​

choices[].logprobs.refusal

object[]

Logaritmos de probabilidad de los tokens de rechazo

​

choices[].logprobs.refusal[].bytes

integer[]

requerido

Bytes UTF-8 del token

​

choices[].logprobs.refusal[].logprob

number

requerido

Logaritmo de probabilidad del tokenFormato: `double`

​

choices[].logprobs.refusal[].token

string

requerido

El token

​

choices[].logprobs.refusal[].top_logprobs

object[]

requerido

Tokens alternativos principales con sus probabilidades

​

choices[].logprobs.refusal[].top_logprobs[].bytes

integer[]

requerido

​

choices[].logprobs.refusal[].top_logprobs[].logprob

number

requerido

Formato: `double`

​

choices[].logprobs.refusal[].top_logprobs[].token

string

requerido

​

choices[].message

object

requerido

Mensaje del asistente para solicitudes y respuestas

​

choices[].message.audio

object

Datos o referencia de salida de audio

​

choices[].message.audio.data

string

Datos de audio codificados en Base64

​

choices[].message.audio.expires_at

integer

Marca de tiempo de expiración del audio

​

choices[].message.audio.id

string

Identificador de la salida de audio

​

choices[].message.audio.transcript

string

Transcripción del audio

​

choices[].message.content

string | object[] | object

Contenido del mensaje del asistente

​

choices[].message.images

object[]

Imágenes generadas por modelos de generación de imágenes

​

choices[].message.images[].image_url

object

requerido

​

choices[].message.images[].image_url.url

string

requerido

URL o datos codificados en base64 de la imagen generada

​

choices[].message.name

string

Nombre opcional para el asistente

​

choices[].message.reasoning

string

Salida de razonamiento

​

choices[].message.reasoning_details

object[]

Detalles de razonamiento para modelos de pensamiento extendido

​

choices[].message.refusal

string

Mensaje de rechazo si se rechazó el contenido

​

choices[].message.tool_calls

object[]

Llamadas a herramientas realizadas por el asistente

​

choices[].message.tool_calls[].function

object

requerido

​

choices[].message.tool_calls[].function.arguments

string

requerido

Argumentos de la función como cadena JSON

​

choices[].message.tool_calls[].function.name

string

requerido

Nombre de la función a llamar

​

choices[].message.tool_calls[].id

string

requerido

Identificador de la llamada a la herramienta

​

choices[].message.tool_calls[].type

string

requerido

Valores posibles: `function`

​

created

integer

requerido

Marca de tiempo Unix de creación

​

id

string

requerido

Identificador único del completado

​

model

string

requerido

Modelo usado para el completado

​

object

string

requerido

Valores posibles: `chat.completion`

​

openrouter_metadata

object

​

openrouter_metadata.attempt

integer

requerido

​

openrouter_metadata.attempts

object[]

​

openrouter_metadata.attempts[].model

string

requerido

​

openrouter_metadata.attempts[].provider

string

requerido

​

openrouter_metadata.attempts[].status

integer

requerido

​

openrouter_metadata.endpoints

object

requerido

​

openrouter_metadata.endpoints.available

object[]

requerido

​

openrouter_metadata.endpoints.available[].model

string

requerido

​

openrouter_metadata.endpoints.available[].provider

string

requerido

​

openrouter_metadata.endpoints.available[].selected

boolean

requerido

​

openrouter_metadata.endpoints.total

integer

requerido

​

openrouter_metadata.is_byok

boolean

requerido

​

openrouter_metadata.params

object

​

openrouter_metadata.params.quality_floor

number

Formato: `double`

​

openrouter_metadata.params.throughput_floor

number

Formato: `double`

​

openrouter_metadata.params.version_group

string

​

openrouter_metadata.pipeline

object[]

​

openrouter_metadata.pipeline[].cost_usd

number

Formato: `double`

​

openrouter_metadata.pipeline[].data

object

​

openrouter_metadata.pipeline[].guardrail_id

string

​

openrouter_metadata.pipeline[].guardrail_scope

string

​

openrouter_metadata.pipeline[].name

string

requerido

​

openrouter_metadata.pipeline[].summary

string

​

openrouter_metadata.pipeline[].type

string

requerido

Tipo categórico de una etapa de pipeline. Varios plugins pueden compartir un tipo (por ejemplo, todos los plugins de nivel guardrail emiten `guardrail`); el campo `name` distingue qué plugin lo emitió.Valores posibles: `guardrail`, `plugin`, `server_tools`, `response_healing`, `context_compression`

​

openrouter_metadata.region

string

requerido

​

openrouter_metadata.requested

string

requerido

​

openrouter_metadata.strategy

string

requerido

Valores posibles: `direct`, `auto`, `free`, `latest`, `alias`, `fallback`, `pareto`, `bodybuilder`, `fusion`

​

openrouter_metadata.summary

string

requerido

​

service_tier

string

El nivel de servicio que utiliza el proveedor upstream para esta solicitud

​

system_fingerprint

string

requerido

Huella del sistema

​

usage

object

Estadísticas de uso de tokens

​

usage.completion_tokens

integer

requerido

Número de tokens de la finalización

​

usage.completion_tokens_details

object

Uso detallado de tokens de finalización

​

usage.cost

number

Costo de la finalizaciónFormato: `double`

​

usage.cost_details

object

Desglose de los costos de inferencia upstream

​

usage.cost_details.upstream_inference_completions_cost

number

requerido

Formato: `double`

​

usage.cost_details.upstream_inference_cost

number

Formato: `double`

​

usage.cost_details.upstream_inference_prompt_cost

number

requerido

Formato: `double`

​

usage.is_byok

boolean

Indica si una solicitud se realizó con una configuración Bring Your Own Key

​

usage.prompt_tokens

integer

requerido

Número de tokens del prompt

​

usage.prompt_tokens_details

object

Uso detallado de tokens del prompt

​

usage.total_tokens

integer

requerido

Número total de tokens

## 

​

Ejemplos

### 

​

Salida
    
    
    {
      "choices": [
        {
          "finish_reason": "stop",
          "index": 0,
          "message": {
            "content": "ok"
          }
        }
      ],
      "created": 1750000000,
      "id": "gen-0000000000-examplecompletion",
      "model": "anthropic/claude-sonnet-4.5",
      "object": "chat.completion",
      "system_fingerprint": null,
      "usage": {
        "completion_tokens": 128,
        "cost": 0.00123,
        "prompt_tokens": 42,
        "total_tokens": 170
      }
    }
    

## 

​

Antes de lanzar

Los SDK crean una `Idempotency-Key` y la reutilizan para los reintentos automáticos. Para los reintentos manuales, reutiliza la clave original. Router puede mantener la conexión abierta hasta 10 minutos. Cuando una solicitud falla, Router envía un encabezado de respuesta `X-Comfy-Error-Type` que explica el motivo. Un `422` significa que Router rechazó la entrada antes de llamar al proveedor, y un `413` significa que el cuerpo de la solicitud era más grande de lo que Router acepta. Descarga los recursos generados de inmediato, porque [las URL de resultados pueden caducar](https://docs.comfy.org/es/development/comfy-router/reference#recursos-del-resultado). Cualquier límite de tamaño mencionado en la descripción de un campo más arriba es el límite propio del proveedor para ese campo, citado de la especificación del proveedor. Router aplica un tope aparte al cuerpo completo de la solicitud, con el que cuentan los medios codificados en base64: consulta [tamaño del cuerpo de la solicitud](https://docs.comfy.org/es/development/comfy-router/limitations#los-cuerpos-de-las-solicitudes-tienen-un-l%C3%ADmite). Esta página documenta un modelo socio al que se llama a través de Comfy Router. El mismo paquete `comfy-sdk` / `@comfyorg/sdk` también incluye un segundo cliente, para ejecutar todo un gráfico de flujo de trabajo de ComfyUI en Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, con `client.workflows`, `client.assets` y `client.jobs`. Consulta [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks).

## Encabezados

Autenticación, idempotencia, IDs de solicitud, agrupaciones de errores, ritmo de reintentos y límites de gasto.

## Uso de la API de Router

Descubrimiento de modelos, errores de validación, reintentos y facturación.

## Limitaciones

Lo que Router no hace hoy y qué usar en su lugar.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/openrouter/chat-completions/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/openrouter/chat-completions/code)

[o4-mini](https://docs.comfy.org/es/development/comfy-router/models/openai/o4-mini/code)[Pika 2.5 Image To Video](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-2-5-image-to-video/code)
