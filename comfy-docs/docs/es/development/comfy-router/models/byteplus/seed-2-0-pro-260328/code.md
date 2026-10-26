---
url: https://docs.comfy.org/es/development/comfy-router/models/byteplus/seed-2-0-pro-260328/code/
title: Usa Seed 2.0 Pro 260328 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:01.257585+00:00
---

# Usa Seed 2.0 Pro 260328 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/byteplus/seed-2-0-pro-260328/code/

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



BytePlus

# Usa Seed 2.0 Pro 260328 con Comfy Router

Copiar páginaCopiar página

Llama a byteplus/seed-2-0-pro-260328 con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `byteplus/seed-2-0-pro-260328`, servida por Comfy Router desde BytePlus. **Entrada:** Texto, Imagen · **Salida:** Texto

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `byteplus/seed-2-0-pro-260328` **Endpoint:** `POST https://api.comfy.org/v2/models/byteplus/seed-2-0-pro-260328`

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
            "byteplus/seed-2-0-pro-260328",
            {
                "input": "Reply with the single word: ok",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("byteplus/seed-2-0-pro-260328", {
      input: "Reply with the single word: ok",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/byteplus/seed-2-0-pro-260328 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/byteplus/seed-2-0-pro-260328/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "byteplus/seed-2-0-pro-260328",
                {
                    "input": "Reply with the single word: ok",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta en bucle hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("byteplus/seed-2-0-pro-260328", {
      input: "Reply with the single word: ok",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta en bucle hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/byteplus/seed-2-0-pro-260328/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": \"Reply with the single word: ok\"}"
    
    # 2. Consulta en bucle hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/byteplus/seed-2-0-pro-260328/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/byteplus/seed-2-0-pro-260328/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

caching

object

Configuración de la caché de contexto.

​

caching.prefix

boolean

predeterminado:"false"

Cuando es `true`, solo se crea la caché de prefijo pública; el modelo no responde.

​

caching.type

string

Valores posibles: `enabled`, `disabled`

​

context_management

object

Estrategias de gestión del contexto (`clear_thinking`, `clear_tool_uses`) aplicadas para mantener manejable la ventana de contexto.

​

context_management.edits

object[]

Una única estrategia de edición de contexto, discriminada por `type`.

​

expire_at

integer

Marca de tiempo Unix (segundos, UTC) en la que expiran la respuesta almacenada y la caché. Alcance (creation_time, creation_time + 604800]. Predeterminado: creation_time + 259200 (3 días).

​

include

string[]

Campos de salida adicionales que se deben incluir. Actualmente con soporte: `reasoning.encrypted_content` (razonamiento cifrado y comprimido para reutilización manual en varios turnos).

​

input

string | object[]

requerido

Contenido de texto o lista de elementos de entrada proporcionados al modelo.

​

instructions

string

Mensaje de sistema/desarrollador antepuesto como primera instrucción. No es compatible con `caching`: si `caching.type` es `enabled`, establecer `instructions` devuelve un error.

​

max_output_tokens

integer

Máximo de tokens de salida (respuesta + cadena de pensamiento).

​

max_tool_calls

integer

Rango: `1` a `10`

​

model

string

ID del modelo o ID del endpoint. Consulta <https://docs.byteplus.com/en/docs/ModelArk/1330310> para la lista de modelos y <https://docs.byteplus.com/en/docs/ModelArk/1099522> para los ID de endpoint. Una llamada directa a v1 mediante POST /proxy/byteplus/api/v3/responses DEBE proporcionarlo: el proxy rechaza cualquier valor fuera de su propia lista de permitidos, y también su omisión, con un 400. NO está en las listas `required` de los esquemas de entrada de Comfy Router porque Router lo rellena a partir del segmento de ruta `{model}` de /v2/models/byteplus/{model}, así que quien llama a Router lo omite.

​

previous_response_id

string

ID de la respuesta anterior, usado para continuar una conversación de varios turnos. Inserta ~100 ms entre solicitudes para evitar fallos.

​

reasoning

object

Limita la carga del pensamiento profundo.

​

reasoning.effort

string

`minimal` desactiva el pensamiento por completo. Con `thinking.type = disabled`, solo se permite `minimal`.Valores posibles: `minimal`, `low`, `medium`, `high`

​

store

boolean

predeterminado:"true"

Cuando es `true`, la respuesta se conserva y se puede recuperar por ID para usarla en varios turnos.

​

temperature

number

predeterminado:"1"

Rango: `0` a `2`Formato: `float`

​

text

object

Configuración del formato de salida.

​

text.format

object

Formato de salida de texto discriminado por `type`. `text` devuelve lenguaje natural, `json_object` devuelve un objeto JSON de forma libre y `json_schema` restringe la salida a un JSON Schema proporcionado por quien llama.

​

thinking

object

Controla el modo de pensamiento profundo.

​

thinking.type

string

`enabled`: razona siempre antes de responder. `disabled`: responde sin razonamiento adicional. `auto`: el modelo decide según la consulta.Valores posibles: `enabled`, `disabled`, `auto`

​

tool_choice

`none`, `auto`, `required` | object

Modo de selección de herramientas. Solo los modelos seed-1-6 admiten este campo.

​

tools

object[]

Una herramienta que el modelo puede invocar. Actualmente solo se admite `function`.

​

tools[].description

string

​

tools[].name

string

requerido

​

tools[].parameters

object

requerido

JSON Schema que describe los parámetros de la función.

​

tools[].type

string

predeterminado:"\"function\""

requerido

Valores posibles: `function`

​

top_p

number

predeterminado:"0.7"

Rango: `0` a `1`Formato: `float`

Generado a partir del esquema que Router sirve en `GET /v2/models/byteplus/seed-2-0-pro-260328/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

caching

object

​

caching.prefix

boolean

​

caching.type

string

Valores posibles: `enabled`, `disabled`

​

context_management

object

Estrategias de gestión de contexto que se aplicaron realmente durante esta respuesta. A diferencia de `BytePlusResponseContextManagement` en la solicitud (que configura las estrategias), esto devuelve las estrategias que invocó el servidor, con recuentos de lo que se eliminó.

​

context_management.applied_edits

object[]

Una edición de contexto aplicada, discriminada por `type`.

​

created_at

integer

requerido

Marca de tiempo Unix (en segundos) de cuándo se creó la respuesta.

​

error

object

Detalles del error. Es nulo cuando la respuesta se completó correctamente.

​

error.code

string

requerido

​

error.message

string

requerido

​

expire_at

integer

Marca de tiempo Unix (en segundos) de cuándo expira la respuesta almacenada.

​

id

string

requerido

ID único de la respuesta. Úsalo como `previous_response_id` para continuar la conversación.

​

incomplete_details

object

Se rellena cuando `status` es `incomplete`.

​

incomplete_details.reason

string

p. ej., `max_output_tokens`, `content_filter`.

​

instructions

string

Copia del campo `instructions` de la solicitud.

​

max_output_tokens

integer

​

max_tool_calls

integer

​

metadata

object

​

model

string

requerido

ID del modelo que generó la respuesta.

​

object

string

predeterminado:"\"response\""

requerido

Valores posibles: `response`

​

output

object[]

requerido

Elementos de salida ordenados que generó el modelo.

​

previous_response_id

string

​

reasoning

object

​

reasoning.effort

string

Valores posibles: `minimal`, `low`, `medium`, `high`

​

service_tier

string

Uso del paquete de garantía de TPM. `default` significa ninguno.Valores posibles: `default`

​

status

string

requerido

Valores posibles: `in_progress`, `completed`, `incomplete`, `failed`, `cancelled`

​

store

boolean

​

stream

boolean

​

temperature

number

Formato: `float`

​

text

object

Copia del campo `text` de la solicitud.

​

text.format

object

Formato de salida de texto discriminado por `type`. `text` devuelve lenguaje natural, `json_object` devuelve un objeto JSON de forma libre y `json_schema` restringe la salida a un JSON Schema proporcionado por quien llama.

​

thinking

object

​

thinking.type

string

Valores posibles: `enabled`, `disabled`, `auto`

​

tool_choice

`none`, `auto`, `required` | object

​

tools

object[]

Una herramienta que el modelo puede invocar. Actualmente solo se admite `function`.

​

tools[].description

string

​

tools[].name

string

requerido

​

tools[].parameters

object

requerido

JSON Schema que describe los parámetros de la función.

​

tools[].type

string

predeterminado:"\"function\""

requerido

Valores posibles: `function`

​

top_p

number

Formato: `float`

​

usage

object

Desglose del uso de tokens para facturación y observabilidad.

​

usage.input_tokens

integer

requerido

Total de tokens en la solicitud.

​

usage.input_tokens_details

object

Desglose de los tokens de entrada (aciertos de caché, etc.).

​

usage.input_tokens_details.cached_tokens

integer

Tokens servidos desde la caché de contexto.

​

usage.output_tokens

integer

requerido

Total de tokens generados por el modelo.

​

usage.output_tokens_details

object

Desglose de los tokens de salida (razonamiento, etc.).

​

usage.output_tokens_details.reasoning_tokens

integer

Tokens consumidos por la cadena de razonamiento.

​

usage.tool_usage

object

Recuentos de invocaciones por herramienta.

​

usage.tool_usage.image_process

integer

Número de llamadas a la herramienta de procesamiento de imágenes.

​

usage.tool_usage.mcp

integer

Número de llamadas a herramientas MCP.

​

usage.tool_usage.web_search

integer

Número de invocaciones de la herramienta de búsqueda web.

​

usage.tool_usage_details

object

Desglose por herramienta de los recuentos de invocación de subherramientas.

​

usage.tool_usage_details.image_process

object

p. ej. `{"zoom":1,"point":1,"grounding":1}`.

​

usage.tool_usage_details.mcp

object

p. ej. `{"mcp_server_tos":1,"mcp_server_tls":1}`.

​

usage.tool_usage_details.web_search

object

p. ej. `{"toutiao":1,"moji":1,"search_engine":1}`.

​

usage.total_tokens

integer

requerido

input_tokens + output_tokens.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "input": "Reply with the single word: ok"
    }
    

### 

​

Salida
    
    
    {
      "created_at": 1767225600,
      "id": "resp_0a1b2c3d4e5f6a7b8c9d0e1f",
      "model": "seed-2-0-pro-260328",
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
      "status": "completed",
      "usage": {
        "input_tokens": 14,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 2,
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/byteplus/seed-2-0-pro-260328/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/byteplus/seed-2-0-pro-260328/code)

[Seed 2.0 Mini 260215](https://docs.comfy.org/es/development/comfy-router/models/byteplus/seed-2-0-mini-260215/code)[Seed Audio 1.0 Multilingual](https://docs.comfy.org/es/development/comfy-router/models/byteplus/seed-audio-1-0-multilingual/code)
