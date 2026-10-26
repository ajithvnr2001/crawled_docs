---
url: https://docs.comfy.org/es/development/comfy-router/models/gemini-interactions/gemini-omni-flash-preview/code/
title: Usa Gemini Omni Flash Preview con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:04.627037+00:00
---

# Usa Gemini Omni Flash Preview con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/gemini-interactions/gemini-omni-flash-preview/code/

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



Gemini Interactions

# Usa Gemini Omni Flash Preview con Comfy Router

Copiar páginaCopiar página

Llama a gemini-interactions/gemini-omni-flash-preview mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `gemini-interactions/gemini-omni-flash-preview`, servida por Comfy Router desde Gemini Interactions. **Entrada:** texto, imagen, audio, video · **Salida:** texto + imagen + audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de código de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `gemini-interactions/gemini-omni-flash-preview` **Endpoint:** `POST https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "gemini-interactions/gemini-omni-flash-preview",
            {
                "input": "Reply with the single word: ok",
                "stream": False,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("gemini-interactions/gemini-omni-flash-preview", {
      input: "Reply with the single word: ok",
      stream: false,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\", \"stream\": false}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview/requests`. El Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge una vez que está listo, desde este proceso o desde otro. La [entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "gemini-interactions/gemini-omni-flash-preview",
                {
                    "input": "Reply with the single word: ok",
                    "stream": False,
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada lanza aquí el error tipado del Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("gemini-interactions/gemini-omni-flash-preview", {
      input: "Reply with the single word: ok",
      stream: false,
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud fallida o cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. El Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\", \"stream\": false}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge el resultado. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/gemini-interactions/gemini-omni-flash-preview/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

input

object

requerido

Un prompt en forma de cadena o un arreglo de partes de contenido tipadas (texto, imagen, audio, video, documento).

​

model

string

Identificador del modelo Gemini: `gemini-omni-1.1-flash` (disponible de forma general), o el obsoleto `gemini-omni-flash-preview`. En la ruta de Comfy Router `POST /v2/models/gemini-interactions/{model}` se toma de la ruta y puede omitirse. Esas dos grafías, el conjunto al que Comfy Router se dirige como `gemini-interactions/<model>`, son las que atiende esta operación (supportedGeminiInteractionModels); se escriben aquí en lugar de restringirlas a un enum, porque el proxy valida el modelo por sí mismo y responde con su propio 400 ante una grafía que no atiende.

​

previous_interaction_id

string

ID de una interacción almacenada previa, que habilita la edición de video multiturno con estado.

Generado a partir del esquema que Router sirve en `GET /v2/models/gemini-interactions/gemini-omni-flash-preview/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

id

string

​

model

string

​

object

string

​

status

string

requerido

Siempre `completed` en una respuesta de Router. Los demás estados del proveedor (`in_progress`, `requires_action`, `failed`, `cancelled`, `incomplete`, `budget_exceeded`) no llegan a quien llama a través de Router como un 200; se devuelven como un error de Comfy Router que incluye el cuerpo del proveedor.Valores posibles: `completed`

​

steps

object[]

requerido

La línea de tiempo de la interacción, en orden. Aquí se restringe a partir del `steps` sin tipo de `GeminiInteraction` para que el campo hoja de la salida sea direccionable; el proveedor sigue agregando tipos de paso, así que un elemento es `additionalProperties: true` y solo se declaran los campos que lee quien llama a Router.

​

steps[].content

object[]

Los bloques de contenido tipados de este paso.

​

steps[].content[].data

string

Medios en línea codificados en Base64, en un bloque de medios entregado en línea. Google limita los medios en línea a 4 MB y exige `delivery: uri` por encima de ese tamaño.

​

steps[].content[].mime_type

string

Tipo de medio de `data` o `uri`, en un bloque de medios.

​

steps[].content[].text

string

El texto generado. Está presente en un bloque `text`, y esta es la hoja que verifica el caso nocturno del SDK de Router, concretamente en un paso `model_output` (`steps[type=model_output].content[].text`).

​

steps[].content[].type

string

Tipo de bloque: `text`, `image`, `audio`, `video` o `document`.

​

steps[].content[].uri

string

Referencia a medios entregados fuera de banda, que quien llama obtiene del URI que se indica.

​

steps[].type

string

Tipo de paso. `model_output` es la respuesta generada; `user_input` es el turno del propio llamador devuelto por la ruta de recuperación; `thought` es razonamiento interno. Los pasos de herramienta (`function_call`, `function_result`, `code_execution_call`, `google_search_call`, …) son abiertos y Google los amplía.

​

usage

object

Uso de tokens de una interacción de Gemini.

​

usage.input_tokens_by_modality

object[]

Recuento de tokens de una modalidad.

​

usage.input_tokens_by_modality[].modality

string

Uno de `text`, `image`, `audio`, `video`, `document`.

​

usage.input_tokens_by_modality[].tokens

integer

​

usage.output_tokens_by_modality

object[]

Recuento de tokens de una modalidad.

​

usage.output_tokens_by_modality[].modality

string

Uno de `text`, `image`, `audio`, `video`, `document`.

​

usage.output_tokens_by_modality[].tokens

integer

​

usage.total_cached_tokens

integer

​

usage.total_input_tokens

integer

​

usage.total_output_tokens

integer

​

usage.total_thought_tokens

integer

​

usage.total_tokens

integer

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "input": "Reply with the single word: ok",
      "stream": false
    }
    

### 

​

Salida
    
    
    {
      "id": "interactions/3f6c1a90-2b47-4d18-9a55-7c0e8b21d4f3",
      "object": "interaction",
      "status": "completed",
      "steps": [
        {
          "content": [
            {
              "text": "ok",
              "type": "text"
            }
          ],
          "type": "model_output"
        }
      ],
      "usage": {
        "input_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 9
          }
        ],
        "output_tokens_by_modality": [
          {
            "modality": "text",
            "tokens": 2
          }
        ],
        "total_cached_tokens": 0,
        "total_input_tokens": 9,
        "total_output_tokens": 2,
        "total_thought_tokens": 0,
        "total_tokens": 11
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/gemini-interactions/gemini-omni-flash-preview/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/gemini-interactions/gemini-omni-flash-preview/code)

[Gemini Omni 1.1 Flash](https://docs.comfy.org/es/development/comfy-router/models/gemini-interactions/gemini-omni-1-1-flash/code)[Gemini 2.5 Flash Image](https://docs.comfy.org/es/development/comfy-router/models/google/gemini-2-5-flash-image/code)
