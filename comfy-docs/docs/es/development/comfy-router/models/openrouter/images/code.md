---
url: https://docs.comfy.org/es/development/comfy-router/models/openrouter/images/code/
title: Usar im\u00e1genes con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:26.877518+00:00
---

# Usar imágenes con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/openrouter/images/code/

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

# Usar imágenes con Comfy Router

Copiar páginaCopiar página

Llama a openrouter/images con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `openrouter/images`, servida por Comfy Router desde Openrouter. **Entrada:** Texto, Imagen · **Salida:** Imagen

## Configurar la solicitud

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Para Python, ejecuta `pip install comfy-sdk`. Para TypeScript, ejecuta `npm install @comfyorg/sdk`. cURL usa HTTP sin procesar. **ID del modelo:** `openrouter/images` **Endpoint:** `POST https://api.comfy.org/v2/models/openrouter/images`

Este modelo no tiene un ejemplo de solicitud ejecutable. Construye el cuerpo a partir de la documentación de entrada que aparece a continuación y luego úsalo con la [guía de inicio rápido de Router](https://docs.comfy.org/es/development/comfy-router/quickstart).

## Esquema

### Entrada

aspect_ratio

string

Relación de aspecto de la salida

background

string

Modo de fondo

input_references

object[]

Imágenes de referencia para la generación de imagen a imagen, como data URLs o URLs HTTP(S)

input_references[].image_url

object

requerido

input_references[].image_url.detail

string

Nivel de detalle de la imagen para modelos de visiónValores posibles: `auto`, `low`, `high`

input_references[].image_url.url

string

requerido

URL de la imagen (se admiten data: URLs)

input_references[].type

string

requerido

Tipo de parte de contenido, siempre image_url

model

string

El modelo de generación de imágenes a usar, como un ID de modelo de OpenRouter tal como `microsoft/mai-image-2.6` o `microsoft/mai-image-2.6-flash`.

n

integer

Número de imágenes a generar

output_compression

integer

Nivel de compresión para la salida webp/jpeg

output_format

string

Formato de imagen de salida

prompt

string

requerido

Descripción de texto de la imagen deseada

provider

object

Cuando hay varios proveedores de modelos disponibles, puedes indicar opcionalmente tu preferencia de enrutamiento.

provider.allow_fallbacks

boolean

Si se permite que proveedores de respaldo atiendan las solicitudes

  * true: (predeterminado) cuando el proveedor principal (o tus proveedores personalizados en “order”) no está disponible, se usa el siguiente mejor proveedor.
  * false: usa solo el proveedor principal o personalizado, y devuelve el error del origen si no está disponible.



provider.data_collection

`deny`, `allow`

Configuración de recopilación de datos. Si ningún proveedor de modelos disponible cumple el requisito, tu solicitud devolverá un error.

  * allow: (predeterminado) permite proveedores que almacenan los datos del usuario de forma no transitoria y que pueden entrenar con ellos
  * deny: usa solo proveedores que no recopilan datos del usuario.



provider.enforce_distillable_text

boolean

Si se restringe el enrutamiento solo a los modelos que permiten la destilación de texto. Cuando es verdadero, solo se usan los modelos en los que el autor ha permitido la destilación.

provider.ignore

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

Lista de slugs de proveedores a ignorar. Si se proporciona, esta lista se combina con la configuración de proveedores ignorados de toda tu cuenta para esta solicitud.

provider.max_price

object

El objeto que especifica el precio máximo que quieres pagar por esta solicitud. Precio en USD por millón de tokens, para prompt y completion.

provider.max_price.audio

string

Precio por millón de tokens de prompt

provider.max_price.completion

string

Precio por millón de tokens de prompt

provider.max_price.image

string

Precio por millón de tokens de prompt

provider.max_price.prompt

string

Precio por millón de tokens de prompt

provider.max_price.request

string

Precio por millón de tokens de prompt

provider.only

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

Lista de slugs de proveedores a permitir. Si se proporciona, esta lista se combina con la configuración de proveedores permitidos de toda tu cuenta para esta solicitud.

provider.order

`AkashML`, `AI21`, `AionLabs`, `Alibaba`, `Ambient`, `Baidu`, `Amazon Bedrock`, `Amazon Nova`, `Anthropic`, `Arcee AI`, `AtlasCloud`, `Avian`, `Azure`, `BaseTen`, `BytePlus`, `Black Forest Labs`, `Cerebras`, `Chutes`, `Cirrascale`, `Clarifai`, `Cloudflare`, `Cohere`, `Crucible`, `Crusoe`, `DeepInfra`, `DeepSeek`, `DekaLLM`, `Featherless`, `Fireworks`, `Friendli`, `GMICloud`, `Google`, `Google AI Studio`, `Groq`, `Hyperbolic`, `Inception`, `Inceptron`, `InferenceNet`, `Ionstream`, `Infermatic`, `Io Net`, `Inflection`, `Liquid`, `Mara`, `Mancer 2`, `Minimax`, `ModelRun`, `Mistral`, `Modular`, `Moonshot AI`, `Morph`, `NCompass`, `Nebius`, `Nex AGI`, `NextBit`, `Novita`, `Nvidia`, `OpenAI`, `OpenInference`, `Parasail`, `Poolside`, `Perceptron`, `Perplexity`, `Phala`, `Recraft`, `Reka`, `Relace`, `SambaNova`, `Seed`, `SiliconFlow`, `Sourceful`, `StepFun`, `Stealth`, `StreamLake`, `Switchpoint`, `Together`, `Upstage`, `Venice`, `WandB`, `Xiaomi`, `xAI`, `Z.AI`, `FakeProvider` | string[]

Una lista ordenada de slugs de proveedores. El router intentará usar el primer proveedor del subconjunto de esta lista que soporte el modelo que solicitaste, y pasará al siguiente si no está disponible. Si no hay proveedores disponibles, la solicitud fallará con un mensaje de error.

provider.preferred_max_latency

number | object

Latencia máxima preferida (en segundos). Puede ser un número (se aplica a p50) o un objeto con límites específicos por percentil. Los endpoints que superen el umbral o los umbrales todavía pueden usarse, pero tienen menor prioridad en el enrutamiento. Al usar modelos de respaldo, esto puede hacer que se use un modelo de respaldo en lugar del modelo principal si cumple el umbral.

provider.preferred_min_throughput

number | object

Rendimiento mínimo preferido (en tokens por segundo). Puede ser un número (se aplica a p50) o un objeto con límites específicos por percentil. Los endpoints que queden por debajo del umbral o los umbrales todavía pueden usarse, pero tienen menor prioridad en el enrutamiento. Al usar modelos de respaldo, esto puede hacer que se use un modelo de respaldo en lugar del modelo principal si cumple el umbral.

provider.quantizations

`int4`, `int8`, `fp4`, `fp6`, `fp8`, `fp16`, `bf16`, `fp32`, `unknown`[]

Una lista de niveles de cuantización con los que filtrar los proveedores.

provider.require_parameters

boolean

Si se deben filtrar los proveedores para dejar solo aquellos que soportan los parámetros que proporcionaste. Si omites esta opción o la estableces en false, los proveedores recibirán solo los parámetros que soportan e ignorarán el resto.

provider.sort

`price`, `throughput`, `latency`, `exacto` | object

La estrategia de ordenamiento que se usará para esta solicitud, si no se especifica “order”. Cuando se establece, no se realiza balanceo de carga.

provider.zdr

boolean

Si se debe restringir el enrutamiento solo a endpoints ZDR (Zero Data Retention). Cuando es true, solo se usan endpoints que no retienen los prompts.

quality

string

Preajuste de calidad de salida

resolution

string

Preajuste de resolución de salida

seed

integer

Semilla para la generación determinista

size

string

Tamaño de la imagen de salida

stream

boolean

Habilitar el streaming SSE para imágenes parciales. La ruta `/proxy/` rechaza `stream: true` con un 400. Comfy Router lo establece en false y atiende la solicitud.

user

string

Identificador estable del usuario final

Generado a partir del esquema que Router sirve en `GET /v2/models/openrouter/images/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.### Salida

### Salida

created

integer

Marca de tiempo Unix de creación

data

object[]

Imágenes generadas

data[].b64_json

string

Datos de imagen codificados en Base64. Cuando la respuesta supera 1,048,576 bytes, Comfy Router responde `url` en su lugar. La imagen permanece aquí cuando la respuesta no supera ese tamaño o cuando falla su carga a Comfy storage.

data[].media_type

string

Tipo MIME de la imagen

data[].url

string

Una URL firmada alojada por Comfy para la imagen, que se entrega en lugar de `b64_json` cuando la respuesta supera 1,048,576 bytes. Comfy Router siempre la solicita; la ruta `/proxy/` solo la solicita cuando la solicitud envía `Comfy-Asset-Format: url`. Un espacio de trabajo con retención de datos cero nunca la recibe: sus imágenes permanecen en `b64_json`. La URL vence 24 horas después de la llamada.

usage

object

Uso de generación de imágenes

usage.completion_tokens

integer

Tokens generados

usage.cost

number

Costo total en USD de la solicitudFormato: `double`

usage.prompt_tokens

integer

Tokens usados para la entrada

usage.total_tokens

integer

Tokens totales de la solicitud

## Ejemplos

### Salida
    
    
    {
      "created": 1767225600,
      "data": [
        {
          "media_type": "image/png",
          "url": "https://storage.googleapis.com/example-bucket/openrouter-images/example.png"
        }
      ],
      "usage": {
        "completion_tokens": 1024,
        "cost": 0.03,
        "prompt_tokens": 12,
        "total_tokens": 1036
      }
    }
    

## Antes de lanzar

Los SDK crean una `Idempotency-Key` y la reutilizan para los reintentos automáticos. Para los reintentos manuales, reutiliza la clave original. Router puede mantener la conexión abierta hasta 10 minutos. Cuando una solicitud falla, Router envía un encabezado de respuesta `X-Comfy-Error-Type` que explica el motivo. Un `422` significa que Router rechazó la entrada antes de llamar al proveedor, y un `413` significa que el cuerpo de la solicitud era más grande de lo que Router acepta. Descarga los recursos generados de inmediato, porque [las URL de resultados pueden caducar](https://docs.comfy.org/es/development/comfy-router/reference#recursos-del-resultado). Cualquier límite de tamaño mencionado en la descripción de un campo más arriba es el límite propio del proveedor para ese campo, citado de la especificación del proveedor. Router aplica un tope aparte al cuerpo completo de la solicitud, con el que cuentan los medios codificados en base64: consulta [tamaño del cuerpo de la solicitud](https://docs.comfy.org/es/development/comfy-router/limitations#los-cuerpos-de-las-solicitudes-tienen-un-l%C3%ADmite). Esta página documenta un modelo socio al que se llama a través de Comfy Router. El mismo paquete `comfy-sdk` / `@comfyorg/sdk` también incluye un segundo cliente, para ejecutar todo un gráfico de flujo de trabajo de ComfyUI en Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, con `client.workflows`, `client.assets` y `client.jobs`. Consulta [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks).

## Encabezados

Autenticación, idempotencia, IDs de solicitud, agrupaciones de errores, ritmo de reintentos y límites de gasto.

## Uso de la API de Router

Descubrimiento de modelos, errores de validación, reintentos y facturación.

## Limitaciones

Lo que Router no hace hoy y qué usar en su lugar.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/openrouter/images/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/openrouter/images/code)

[Chat Completions](https://docs.comfy.org/es/development/comfy-router/models/openrouter/chat-completions/code)[Pika 2.5 Image To Video](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-2-5-image-to-video/code)
