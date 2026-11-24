---
url: https://docs.comfy.org/es/development/comfy-router/models/tripo/v3-1-20260211-multiview-to-model/code/
title: Usa V3.1 20260211 Multiview To Model con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:28.420980+00:00
---

# Usa V3.1 20260211 Multiview To Model con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/tripo/v3-1-20260211-multiview-to-model/code/

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



Tripo

# Usa V3.1 20260211 Multiview To Model con Comfy Router

Copiar páginaCopiar página

Llama a tripo/v3.1-20260211-multiview-to-model mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `tripo/v3.1-20260211-multiview-to-model`, servida por Comfy Router desde Tripo. **Entrada:** Image · **Salida:** 3D

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada con HTTP directo. **Model ID:** `tripo/v3.1-20260211-multiview-to-model` **Endpoint:** `POST https://api.comfy.org/v2/models/tripo/v3.1-20260211-multiview-to-model`

  * Esperar el resultado

  * Encolar y obtener más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "tripo/v3.1-20260211-multiview-to-model",
            {
                "inputs": ["https://example.invalid/tripo/front.png", "", "https://example.invalid/tripo/back.png", ""],
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("tripo/v3.1-20260211-multiview-to-model", {
      inputs: ["https://example.invalid/tripo/front.png", "", "https://example.invalid/tripo/back.png", ""],
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/tripo/v3.1-20260211-multiview-to-model \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"inputs\": [\"https://example.invalid/tripo/front.png\",\"\",\"https://example.invalid/tripo/back.png\",\"\"]}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/tripo/v3.1-20260211-multiview-to-model/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y obtienes el resultado cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la obtención del resultado.

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
                "tripo/v3.1-20260211-multiview-to-model",
                {
                    "inputs": ["https://example.invalid/tripo/front.png", "", "https://example.invalid/tripo/back.png", ""],
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que necesita otro proceso
    
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
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("tripo/v3.1-20260211-multiview-to-model", {
      inputs: ["https://example.invalid/tripo/front.png", "", "https://example.invalid/tripo/back.png", ""],
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/tripo/v3.1-20260211-multiview-to-model/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"inputs\": [\"https://example.invalid/tripo/front.png\",\"\",\"https://example.invalid/tripo/back.png\",\"\"]}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/tripo/v3.1-20260211-multiview-to-model/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Obtén el resultado. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/tripo/v3.1-20260211-multiview-to-model/requests/$REQUEST_ID \
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

inputs

object[]

requerido

Las imágenes de las vistas, como objetos con clave de vista o como cuatro entradas posicionales en el orden frente, izquierda, atrás, derecha.

model

string

Versión del modelo Tripo. Omítela o envía null cuando uses Comfy Router; la versión la determina el id del modelo (por ejemplo `v3.1-20260211` para `tripo/v3.1-20260211-multiview-to-model`). Se recomienda omitirla. Si envías una versión, debe escribir la versión del id con el uso de mayúsculas y minúsculas propio de Tripo (por ejemplo `P2-20260801` para `tripo/p2-20260801-multiview-to-model`), no la forma en minúsculas que usa el id.

model_seed

integer

orientation

string

predeterminado:"\"default\""

pbr

boolean

predeterminado:"true"

quad

boolean

predeterminado:"false"

smart_low_poly

boolean

predeterminado:"false"

texture

boolean

predeterminado:"true"

texture_alignment

string

predeterminado:"\"original_image\""

texture_quality

string

predeterminado:"\"standard\""

texture_seed

integer

Generado a partir del esquema que Router publica en `GET /v2/models/tripo/v3.1-20260211-multiview-to-model/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

code

integer

requerido

Código de envoltura de Tripo; 0 cuando la llamada tiene éxito.Valores posibles: `0`

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

Créditos reales consumidos por la tarea. Aparece cuando el estado ya está finalizado; 0 en las tareas fallidas.

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

Rango: `0` a `100`

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
      "inputs": [
        "https://example.invalid/tripo/front.png",
        "",
        "https://example.invalid/tripo/back.png",
        ""
      ]
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/tripo/v3-1-20260211-multiview-to-model/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/tripo/v3-1-20260211-multiview-to-model/code)

[V3.1 20260211 Image To Model](https://docs.comfy.org/es/development/comfy-router/models/tripo/v3-1-20260211-image-to-model/code)[V3.1 20260211 Text To Model](https://docs.comfy.org/es/development/comfy-router/models/tripo/v3-1-20260211-text-to-model/code)
