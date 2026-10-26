---
url: https://docs.comfy.org/es/development/comfy-router/models/openai/o4-mini/code/
title: Usa o4-mini con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:16.314576+00:00
---

# Usa o4-mini con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/openai/o4-mini/code/

## En esta página

Volver arriba

  * Inicio rápido
  * Esquema
    * Entrada
    * Salida
  * Ejemplos
    * Entrada
    * Salida
  * Antes de lanzar



OpenAI

# Usa o4-mini con Comfy Router

Copiar páginaCopiar página

Llama a openai/o4-mini mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `openai/o4-mini`, servida por Comfy Router de OpenAI. **Entrada:** Texto, Imagen · **Salida:** Texto

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `openai/o4-mini` **Endpoint:** `POST https://api.comfy.org/v2/models/openai/o4-mini`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "openai/o4-mini",
            {
                "input": "Reply with the single word: ok",
                "max_output_tokens": 1024,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("openai/o4-mini", {
      input: "Reply with the single word: ok",
      max_output_tokens: 1024,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/openai/o4-mini \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\", \"max_output_tokens\": 1024}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/openai/o4-mini/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recopila cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recopilación.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "openai/o4-mini",
                {
                    "input": "Reply with the single word: ok",
                    "max_output_tokens": 1024,
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("openai/o4-mini", {
      input: "Reply with the single word: ok",
      max_output_tokens: 1024,
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/openai/o4-mini/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\", \"max_output_tokens\": 1024}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/openai/o4-mini/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recopila. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/openai/o4-mini/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

include

string[]

Datos de salida adicionales que se incluyen en la respuesta del modelo.

​

input

string | object[]

requerido

Entradas de texto, imagen o archivo al modelo, usadas para generar una respuesta. Es el único campo de este contrato que Router no puede suministrar, y la única entrada en `required` más abajo.

​

instructions

string

Inserta un mensaje de sistema (o de desarrollador) como el primer elemento del contexto del modelo.

​

max_output_tokens

integer

Un límite superior para la cantidad de tokens generados en una respuesta, incluidos los tokens de salida visibles y los tokens de razonamiento. En un id de razonamiento este techo se comparte con los tokens de razonamiento ocultos, así que un valor pequeño puede consumir todo el presupuesto antes de cualquier texto visible: por eso los casos de prueba de humo de razonamiento envían 1024 donde los de chat envían 16.Rango: `1` a `…`

​

model

string

Identificador de modelo de OpenAI. En Comfy Router este campo es OPCIONAL y Router lo rellena a partir del segmento de ruta `{model}`; un `null` explícito se reemplaza de la misma manera. Se rechaza el envío de un valor que no coincida con la ruta.

​

parallel_tool_calls

boolean

Si se permite que el modelo ejecute llamadas a herramientas en paralelo.

​

previous_response_id

string

El ID de una respuesta anterior, para conversaciones de varios turnos.

​

reasoning

object

SOLO NIVEL DE RAZONAMIENTO. Configuración para modelos de razonamiento, por ejemplo `{"effort": "medium"}`. Se reenvía sin cambios; consulta la guía de razonamiento de OpenAI para conocer las claves aceptadas. Un id de nivel chat la ignora.

​

store

boolean

Si OpenAI almacena la respuesta generada para recuperarla más tarde.

​

stream

boolean

Se declara para que quien lo envíe no sea rechazado, pero es INERTE en esta superficie: Router lo FIJA en `false` antes del despacho, porque captura la respuesta del proveedor en lugar de retransmitir un `text/event-stream`, el cual no puede decodificar, así que una generación en streaming sería facturada por OpenAI y medida por nadie. Ninguna superficie de Comfy sirve el stream: la entrada `POST /proxy/openai/v1/responses` de v1 rechaza `stream: true` con un 400 y nunca reenvía la solicitud al proveedor, así que omite el campo o envía `false` en cualquiera de las dos superficies y lee la respuesta completada como un solo cuerpo JSON.

​

temperature

number

Temperatura de muestreo. SOLO NIVEL DE CHAT: los ids de razonamiento de la serie o (`o1`, `o1-pro`, `o3`, `o4-mini`) rechazan este parámetro en OpenAI. Router no lo rechaza por ellos (consulta la nota de este componente sobre por qué los dos niveles comparten un esquema), así que OpenAI responde a una llamada de razonamiento que lo envía con su propio error.Rango: `0` a `2`

​

text

object

Configuración del formato de salida, por ejemplo `{"format": {"type": "json_schema", ...}}` para Structured Outputs. Se reenvía sin cambios.

​

tool_choice

string | object

Cómo debe seleccionar el modelo qué herramienta usar. Ya sea un modo de tipo cadena o un objeto que nombra una herramienta.

​

tools

object[]

Definiciones de herramientas que el modelo puede llamar. Router no restringe la taxonomía de herramientas; consulta la referencia de la API Responses de OpenAI para las formas aceptadas.

​

top_p

number

Corte del muestreo de núcleo. SOLO NIVEL DE CHAT, en los mismos términos que `temperature`.Rango: `0` a `1`

​

truncation

string

Estrategia de truncamiento cuando el contexto supera la ventana del modelo. La enumeración SÍ se aplica aquí, a diferencia de los tres vocabularios anteriores, porque estos dos valores son el conjunto completo que OpenAI documenta y no ha crecido. Un `null` explícito sigue aceptándose, en los mismos términos que los campos anteriores.Valores posibles: `auto`, `disabled`

​

usage

object

Envolvente de uso de tokens. Está presente en este contrato porque la operación de v1 la declara en el cuerpo de la solicitud; OpenAI la rellena en la RESPUESTA, así que quien llama no tiene motivo para enviarla.

Generado a partir del esquema que Router sirve en `GET /v2/models/openai/o4-mini/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

instructions

string

Inserta un mensaje de sistema (o de desarrollador) como primer elemento en el contexto del modelo.Cuando se usa junto con `previous_response_id`, las instrucciones de una respuesta anterior no se trasladan a la siguiente respuesta. Esto facilita cambiar los mensajes de sistema (o de desarrollador) en las nuevas respuestas.

​

max_output_tokens

integer

Un límite superior para la cantidad de tokens que se pueden generar en una respuesta, incluidos los tokens de salida visibles y los [tokens de razonamiento](https://platform.openai.com/docs/guides/reasoning).

​

model

string

El modelo que se usa para generar la respuesta

​

temperature

number

predeterminado:"1"

Controla la aleatoriedad de la respuestaRango: `0` a `2`

​

top_p

number

predeterminado:"1"

Controla la diversidad de la respuesta mediante muestreo de núcleoRango: `0` a `1`

​

truncation

string

predeterminado:"\"disabled\""

La estrategia de truncamiento que se usa para la respuesta del modelo.

  * `auto`: si el contexto de esta respuesta y de las anteriores supera el tamaño de la ventana de contexto del modelo, el modelo truncará la respuesta para ajustarla a la ventana de contexto descartando elementos de entrada en medio de la conversación.
  * `disabled` (predeterminado): si una respuesta del modelo supera el tamaño de la ventana de contexto de un modelo, la solicitud fallará con un error 400. Valores posibles: `auto`, `disabled`



​

previous_response_id

string

El ID único de la respuesta anterior del modelo. Úsalo para crear conversaciones de varios turnos. Aprende más sobre el [estado de la conversación](https://platform.openai.com/docs/guides/conversation-state).

​

reasoning

object

**Solo para modelos de la serie o** Opciones de configuración para los [modelos de razonamiento](https://platform.openai.com/docs/guides/reasoning).

​

reasoning.context

string

Controla qué elementos de razonamiento se devuelven al modelo en turnos posteriores, por ejemplo `auto`, `current_turn` o `all_turns`.

​

reasoning.effort

string

predeterminado:"\"medium\""

**Solo para modelos de la serie o** Limita el esfuerzo de razonamiento de los [modelos de razonamiento](https://platform.openai.com/docs/guides/reasoning). Los valores admitidos actualmente son `low`, `medium` y `high`. Reducir el esfuerzo de razonamiento puede dar respuestas más rápidas y usar menos tokens en razonamiento dentro de una respuesta.Valores posibles: `low`, `medium`, `high`

​

reasoning.generate_summary

string

**Obsoleto:** usa `summary` en su lugar.Un resumen del razonamiento que realizó el modelo. Puede ser útil para depurar y entender el proceso de razonamiento del modelo. Uno de `auto`, `concise` o `detailed`.Valores posibles: `auto`, `concise`, `detailed`

​

reasoning.mode

string

El modo de razonamiento que se usa para la respuesta.

​

reasoning.summary

string

Un resumen del razonamiento que realizó el modelo. Puede ser útil para depurar y entender el proceso de razonamiento del modelo. Uno de `auto`, `concise` o `detailed`.Valores posibles: `auto`, `concise`, `detailed`

​

text

object

​

text.format

object

Un objeto que especifica el formato que el modelo debe generar.Configurar `{ "type": "json_schema" }` habilita las salidas estructuradas, lo que garantiza que el modelo coincida con el esquema JSON que proporciones. Aprende más en la [guía de salidas estructuradas](https://platform.openai.com/docs/guides/structured-outputs).El formato predeterminado es `{ "type": "text" }` sin opciones adicionales.**No recomendado para gpt-4o y modelos más nuevos:** Establecerlo en `{ "type": "json_object" }` habilita el modo JSON anterior, que garantiza que el mensaje que genera el modelo sea JSON válido. Se prefiere usar `json_schema` en los modelos que lo admiten.

​

text.verbosity

string

Limita la verbosidad de la respuesta del modelo. Uno de `low`, `medium` o `high`.

​

tool_choice

`none`, `auto`, `required` | object

Cómo debe elegir el modelo qué herramienta (o herramientas) usar al generar una respuesta. Consulta el parámetro `tools` para ver cómo especificar qué herramientas puede llamar el modelo.

​

tools

object[]

​

background

boolean

Indica si la respuesta del modelo se ejecuta en segundo plano.

​

billing

object

Información de facturación de la respuesta.

​

billing.payer

string

La parte responsable de pagar la respuesta.

​

completed_at

number

Marca de tiempo Unix (en segundos) de cuándo se completó esta respuesta. Solo está presente cuando el estado es `completed`.

​

created_at

number

Marca de tiempo Unix (en segundos) de cuándo se creó esta respuesta.

​

error

object

Un objeto de error que se devuelve cuando el modelo no logra generar una respuesta.

​

error.code

string

requerido

El código de error de la respuesta.Valores posibles: `server_error`, `rate_limit_exceeded`, `invalid_prompt`, `vector_store_timeout`, `invalid_image`, `invalid_image_format`, `invalid_base64_image`, `invalid_image_url`, `image_too_large`, `image_too_small`, `image_parse_error`, `image_content_policy_violation`, `invalid_image_mode`, `image_file_too_large`, `unsupported_image_media_type`, `empty_image_file`, `failed_to_download_image`, `image_file_not_found`

​

error.message

string

requerido

Una descripción del error legible para humanos.

​

frequency_penalty

number

Penaliza los tokens nuevos según su frecuencia existente en el texto hasta el momento.

​

id

string

Identificador único para esta respuesta.

​

incomplete_details

object

Detalles sobre por qué la respuesta está incompleta.

​

incomplete_details.reason

string

El motivo por el que la respuesta está incompleta.Valores posibles: `max_output_tokens`, `content_filter`

​

max_tool_calls

integer

El número máximo de llamadas totales a herramientas integradas que puede procesar una respuesta.

​

metadata

object

Conjunto de pares clave-valor que puedes adjuntar a la respuesta.

​

moderation

object

Resultados de moderación para la entrada y salida de la respuesta, si se solicitaron completaciones moderadas.

​

object

string

El tipo de objeto de este recurso, siempre establecido en `response`.Valores posibles: `response`

​

output

object[]

Un arreglo de elementos de contenido generados por el modelo.

  * La longitud y el orden de los elementos en el arreglo `output` depende de la respuesta del modelo.
  * En lugar de acceder al primer elemento del arreglo `output` y asumir que es un mensaje de `assistant` con el contenido generado por el modelo, considera usar la propiedad `output_text` donde sea compatible en los SDK.



​

output_text

string

Propiedad de conveniencia solo para SDK que contiene la salida de texto agregada de todos los elementos `output_text` en el arreglo `output`, si los hay. Compatible con los SDK de Python y JavaScript.

​

parallel_tool_calls

boolean

predeterminado:"true"

Si se permite que el modelo ejecute llamadas a herramientas en paralelo.

​

presence_penalty

number

Penaliza los tokens nuevos según si aparecen en el texto hasta el momento.

​

prompt_cache_key

string

Usado por OpenAI para almacenar en caché las respuestas de solicitudes similares y optimizar las tasas de aciertos de caché. Reemplaza el campo `user`.

​

prompt_cache_retention

string

La política de retención para la caché de prompts, por ejemplo, `in_memory` o `24h`.

​

safety_identifier

string

Un identificador estable que se usa para ayudar a detectar usuarios de tu aplicación que puedan estar violando las políticas de uso de OpenAI.

​

service_tier

string

El nivel de procesamiento usado para atender la solicitud, por ejemplo, `auto`, `default`, `flex`, `scale` o `priority`.

​

status

string

El estado de la generación de la respuesta. Uno de `completed`, `failed`, `in_progress`, `cancelled`, `queued` o `incomplete`.Valores posibles: `completed`, `failed`, `in_progress`, `cancelled`, `queued`, `incomplete`

​

store

boolean

Si la respuesta se almacena para recuperarla más tarde a través de la API.

​

tool_usage

object

Uso de tokens y solicitudes desglosado por herramienta integrada.

​

tool_usage.image_gen

object

Uso de tokens de la herramienta de generación de imágenes.

​

tool_usage.image_gen.input_tokens

integer

​

tool_usage.image_gen.input_tokens_details

object

​

tool_usage.image_gen.input_tokens_details.image_tokens

integer

​

tool_usage.image_gen.input_tokens_details.text_tokens

integer

​

tool_usage.image_gen.output_tokens

integer

​

tool_usage.image_gen.output_tokens_details

object

​

tool_usage.image_gen.output_tokens_details.image_tokens

integer

​

tool_usage.image_gen.output_tokens_details.text_tokens

integer

​

tool_usage.image_gen.total_tokens

integer

​

tool_usage.web_search

object

Uso de la herramienta de búsqueda web.

​

tool_usage.web_search.num_requests

integer

​

top_logprobs

integer

El número máximo de tokens más probables que se devolverán en cada posición de token, cada uno con una probabilidad logarítmica asociada.

​

usage

object

Representa los detalles de uso de tokens, incluidos los tokens de entrada, los tokens de salida, un desglose de los tokens de salida y el total de tokens usados.

​

usage.input_tokens

integer

requerido

El número de tokens de entrada.

​

usage.input_tokens_details

object

requerido

Un desglose detallado de los tokens de entrada.

​

usage.input_tokens_details.cache_write_tokens

integer

El número de tokens de entrada que se escribieron en la caché.

​

usage.input_tokens_details.cached_tokens

integer

requerido

El número de tokens que se recuperaron de la caché. [Más información sobre la caché de prompts](https://platform.openai.com/docs/guides/prompt-caching).

​

usage.output_tokens

integer

requerido

El número de tokens de salida.

​

usage.output_tokens_details

object

requerido

Un desglose detallado de los tokens de salida.

​

usage.output_tokens_details.reasoning_tokens

integer

requerido

El número de tokens de razonamiento.

​

usage.total_tokens

integer

requerido

El número total de tokens utilizados.

​

user

string

Identificador obsoleto para el usuario final. Reemplazado por `safety_identifier` y `prompt_cache_key`.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "input": "Reply with the single word: ok",
      "max_output_tokens": 1024
    }
    

### 

​

Salida
    
    
    {
      "completed_at": 1767225601,
      "created_at": 1767225600,
      "id": "resp_0a1b2c3d4e5f6a7b8c9d0e1f",
      "object": "response",
      "output": [
        {
          "content": [
            {
              "annotations": [],
              "text": "ok",
              "type": "output_text"
            }
          ],
          "id": "msg_0a1b2c3d4e5f6a7b8c9d0e1f",
          "role": "assistant",
          "status": "completed",
          "type": "message"
        }
      ],
      "output_text": "ok",
      "status": "completed",
      "usage": {
        "input_tokens": 14,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 2,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 16
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/openai/o4-mini/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/openai/o4-mini/code)

[o3](https://docs.comfy.org/es/development/comfy-router/models/openai/o3/code)[Chat Completions](https://docs.comfy.org/es/development/comfy-router/models/openrouter/chat-completions/code)
