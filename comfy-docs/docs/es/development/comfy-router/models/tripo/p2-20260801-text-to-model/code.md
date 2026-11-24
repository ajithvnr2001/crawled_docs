---
url: https://docs.comfy.org/es/development/comfy-router/models/tripo/p2-20260801-text-to-model/code/
title: Usar P2 20260801 Text To Model con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:27.515370+00:00
---

# Usar P2 20260801 Text To Model con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/tripo/p2-20260801-text-to-model/code/

## En esta página

Volver arriba

  * Quick start
  * Esquema
    * Entrada
    * Salida
  * Ejemplos
    * Entrada
    * Salida
  * Antes de lanzar



Tripo

# Usar P2 20260801 Text To Model con Comfy Router

Copiar páginaCopiar página

Llama a tripo/p2-20260801-text-to-model mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `tripo/p2-20260801-text-to-model`, servida por Comfy Router desde Tripo. **Entrada:** Texto · **Salida:** 3D

## Quick start

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **Model ID:** `tripo/p2-20260801-text-to-model` **Endpoint:** `POST https://api.comfy.org/v2/models/tripo/p2-20260801-text-to-model`

  * Wait for the result

  * Queue and collect later




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    with Comfy() as client:
        result = client.models.run(
            "tripo/p2-20260801-text-to-model",
            {
                "prompt": "a red chair",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("tripo/p2-20260801-text-to-model", {
      prompt: "a red chair",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/tripo/p2-20260801-text-to-model \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a red chair\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/tripo/p2-20260801-text-to-model/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y puedes recopilar el resultado cuando esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recopilación.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Reads COMFY_API_KEY from the environment.
    # Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "tripo/p2-20260801-text-to-model",
                {
                    "prompt": "a red chair",
                },
            )
            print("request_id:", handle.request_id)  # with the model ID, all another process needs
    
            # Poll until the request completes, waiting the Retry-After the server names.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # The provider's own payload, the same value models.run() returns.
            # A request that failed or was cancelled raises the typed Router error here.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    const handle = await comfy.models.submit("tripo/p2-20260801-text-to-model", {
      prompt: "a red chair",
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/tripo/p2-20260801-text-to-model/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a red chair\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/tripo/p2-20260801-text-to-model/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/tripo/p2-20260801-text-to-model/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

auto_size

boolean

predeterminado:"false"

compress

string

export_orientation

string

predeterminado:"\"+x\""

export_uv

boolean

predeterminado:"true"

face_limit

integer

generate_parts

boolean

predeterminado:"false"

geometry_quality

string

predeterminado:"\"standard\""

image_seed

integer

model

string

Versión del modelo de Tripo. Omítela o envía null cuando uses Comfy Router; la versión se selecciona por el id del modelo (por ejemplo, `v3.1-20260211` para `tripo/v3.1-20260211-text-to-model`). Se recomienda omitirla. Una versión proporcionada debe nombrar la versión del id con el uso de mayúsculas y minúsculas propio de Tripo (por ejemplo, `P2-20260801` para `tripo/p2-20260801-text-to-model`), no con la grafía en minúsculas que usa el id.

model_seed

integer

negative_prompt

string

pbr

boolean

predeterminado:"true"

prompt

string

requerido

El prompt de texto que describe el modelo 3D a generar.

quad

boolean

predeterminado:"false"

smart_low_poly

boolean

predeterminado:"false"

texture

boolean

predeterminado:"true"

texture_quality

string

predeterminado:"\"standard\""

texture_seed

integer

Generado a partir del esquema que Router sirve en `GET /v2/models/tripo/p2-20260801-text-to-model/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

code

integer

requerido

Código de envoltura de Tripo; 0 en caso de éxito.Valores posibles: `0`

data

object

requerido

data.completed_at

string

data.created_at

string

requerido

data.credits_consumed

number

Créditos reales consumidos por la tarea. Presente una vez que el estado es definitivo; 0 para las tareas fallidas.

data.error_code

integer

data.error_message

string

data.output

object

requerido

data.progress

integer

requerido

Alcance: `0` a `100`

data.status

string

requerido

Valores posibles: `success`

data.task_id

string

requerido

data.type

string

requerido

## Ejemplos

### Entrada
    
    
    {
      "prompt": "a red chair"
    }
    

### Salida
    
    
    {
      "code": 0,
      "data": {
        "completed_at": "2026-01-01T00:01:00Z",
        "created_at": "2026-01-01T00:00:00Z",
        "credits_consumed": 30,
        "output": {
          "model_url": "https://example.invalid/tripo/out.glb",
          "rendered_image_url": "https://example.invalid/tripo/preview.webp"
        },
        "progress": 100,
        "status": "success",
        "task_id": "t-1",
        "type": "text_to_model"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/tripo/p2-20260801-text-to-model/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/tripo/p2-20260801-text-to-model/code)

[P2 20260801 Multiview To Model](https://docs.comfy.org/es/development/comfy-router/models/tripo/p2-20260801-multiview-to-model/code)[V3.0 20250812 Image To Model](https://docs.comfy.org/es/development/comfy-router/models/tripo/v3-0-20250812-image-to-model/code)
