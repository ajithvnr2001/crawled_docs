---
url: https://docs.comfy.org/es/development/comfy-router/models/anthropic/claude-sonnet-5/code/
title: Usa Claude Sonnet 5 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:55.549275+00:00
---

# Usa Claude Sonnet 5 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/anthropic/claude-sonnet-5/code/

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



Anthropic

# Usa Claude Sonnet 5 con Comfy Router

Copiar páginaCopiar página

Llama a anthropic/claude-sonnet-5 mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `anthropic/claude-sonnet-5`, servida por Comfy Router desde Anthropic. **Entrada:** Texto, Imagen · **Salida:** Texto

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `anthropic/claude-sonnet-5` **Endpoint:** `POST https://api.comfy.org/v2/models/anthropic/claude-sonnet-5`

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
            "anthropic/claude-sonnet-5",
            {
                "max_tokens": 16,
                "messages": [
                    {
                        "content": "Reply with the single word: ok",
                        "role": "user",
                    },
                ],
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("anthropic/claude-sonnet-5", {
      max_tokens: 16,
      messages: [
        {
          content: "Reply with the single word: ok",
          role: "user",
        },
      ],
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/anthropic/claude-sonnet-5 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"max_tokens\": 16, \"messages\": [{\"content\":\"Reply with the single word: ok\",\"role\":\"user\"}]}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/anthropic/claude-sonnet-5/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "anthropic/claude-sonnet-5",
                {
                    "max_tokens": 16,
                    "messages": [
                        {
                            "content": "Reply with the single word: ok",
                            "role": "user",
                        },
                    ],
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("anthropic/claude-sonnet-5", {
      max_tokens: 16,
      messages: [
        {
          content: "Reply with the single word: ok",
          role: "user",
        },
      ],
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/anthropic/claude-sonnet-5/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"max_tokens\": 16, \"messages\": [{\"content\":\"Reply with the single word: ok\",\"role\":\"user\"}]}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/anthropic/claude-sonnet-5/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/anthropic/claude-sonnet-5/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

max_tokens

integer

requerido

Número máximo de tokens a generar antes de detenerse.

​

messages

object[]

requerido

Turnos de la conversación. Consulta la documentación de la API de Messages de Anthropic para ver la taxonomía completa de bloques de contenido.

​

messages[].content

object

requerido

Ya sea una cadena abreviada o un arreglo de bloques de contenido (text, image, document, tool_use, tool_result, …).

​

messages[].role

string

requerido

Valores posibles: `user`, `assistant`

​

model

string

Identificador del modelo de Anthropic (por ejemplo, `claude-sonnet-4-5`, `claude-opus-4-7`).

​

stream

boolean

Cuando es verdadero, la respuesta es un `text/event-stream` de eventos de mensaje de Anthropic en lugar de un único cuerpo JSON.

​

system

object

Prompt de sistema de nivel superior. Ya sea una cadena o un arreglo de bloques de contenido; ambos llegan a Anthropic sin cambios.

Generado a partir del esquema que Router sirve en `GET /v2/models/anthropic/claude-sonnet-5/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

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

role

string

​

stop_reason

string

​

stop_sequence

string

​

type

string

​

usage

object

Uso de tokens de una llamada a la API de Messages de Anthropic.

​

usage.cache_creation

object

Desglose por TTL de los tokens de entrada de escritura en caché de una llamada a la API de Messages de Anthropic.

​

usage.cache_creation.ephemeral_1h_input_tokens

integer

​

usage.cache_creation.ephemeral_5m_input_tokens

integer

​

usage.cache_creation_input_tokens

integer

​

usage.cache_read_input_tokens

integer

​

usage.input_tokens

integer

​

usage.output_tokens

integer

​

content

object[]

requerido

Los bloques de contenido de la respuesta, en orden. Presentes en todo mensaje completado; vacíos cuando el turno no produjo nada.

​

content[].text

string

El texto del bloque. Presente en los bloques `text` y ausente en cualquier otro tipo.

​

content[].type

string

El tipo de bloque. `text` es el que lleva `text`; `thinking`, `redacted_thinking`, `tool_use`, `server_tool_use` y los bloques de resultado de herramienta son los otros que Anthropic envía hoy, y la lista está abierta.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "max_tokens": 16,
      "messages": [
        {
          "content": "Reply with the single word: ok",
          "role": "user"
        }
      ]
    }
    

### 

​

Salida
    
    
    {
      "content": [
        {
          "text": "ok",
          "type": "text"
        }
      ],
      "id": "msg_01ExampleInvalidPlaceholder",
      "model": "claude-sonnet-5",
      "role": "assistant",
      "stop_reason": "end_turn",
      "stop_sequence": null,
      "type": "message",
      "usage": {
        "input_tokens": 16,
        "output_tokens": 3
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/anthropic/claude-sonnet-5/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/anthropic/claude-sonnet-5/code)

[Claude Sonnet 5.5](https://docs.comfy.org/es/development/comfy-router/models/anthropic/claude-sonnet-5-5/code)[SwitchX](https://docs.comfy.org/es/development/comfy-router/models/beeble/switchx/code)
