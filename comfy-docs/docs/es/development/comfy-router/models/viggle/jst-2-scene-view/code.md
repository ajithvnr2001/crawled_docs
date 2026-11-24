---
url: https://docs.comfy.org/es/development/comfy-router/models/viggle/jst-2-scene-view/code/
title: Usar Jst 2 Scene View con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:28.679944+00:00
---

# Usar Jst 2 Scene View con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/viggle/jst-2-scene-view/code/

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



Viggle

# Usar Jst 2 Scene View con Comfy Router

Copiar páginaCopiar página

Llama a viggle/jst-2-scene-view desde Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API de `viggle/jst-2-scene-view`, servida por Comfy Router desde Viggle. **Entrada:** 3D · **Salida:** Image

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP sin procesar. **Model ID:** `viggle/jst-2-scene-view` **Endpoint:** `POST https://api.comfy.org/v2/models/viggle/jst-2-scene-view`

  * Esperar el resultado

  * Enviar a la cola y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "viggle/jst-2-scene-view",
            {
                "projection": "perspective",
                "referenceBatchIds": ["3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f"],
                "sessionId": "replace-with-a-new-random-id",
                "targetPosition": {
                    "pitch": 0,
                    "position": [0.3, 0, 0],
                    "yaw": 30,
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("viggle/jst-2-scene-view", {
      projection: "perspective",
      referenceBatchIds: ["3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f"],
      sessionId: "replace-with-a-new-random-id",
      targetPosition: {
        pitch: 0,
        position: [0.3, 0, 0],
        yaw: 30,
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/viggle/jst-2-scene-view \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"projection\": \"perspective\", \"referenceBatchIds\": [\"3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f\"], \"sessionId\": \"replace-with-a-new-random-id\", \"targetPosition\": {\"pitch\":0,\"position\":[0.3,0,0],\"yaw\":30}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/viggle/jst-2-scene-view/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "viggle/jst-2-scene-view",
                {
                    "projection": "perspective",
                    "referenceBatchIds": ["3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f"],
                    "sessionId": "replace-with-a-new-random-id",
                    "targetPosition": {
                        "pitch": 0,
                        "position": [0.3, 0, 0],
                        "yaw": 30,
                    },
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta el estado hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
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
    const handle = await comfy.models.submit("viggle/jst-2-scene-view", {
      projection: "perspective",
      referenceBatchIds: ["3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f"],
      sessionId: "replace-with-a-new-random-id",
      targetPosition: {
        pitch: 0,
        position: [0.3, 0, 0],
        yaw: 30,
      },
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta el estado hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/viggle/jst-2-scene-view/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"projection\": \"perspective\", \"referenceBatchIds\": [\"3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f\"], \"sessionId\": \"replace-with-a-new-random-id\", \"targetPosition\": {\"pitch\":0,\"position\":[0.3,0,0],\"yaw\":30}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/viggle/jst-2-scene-view/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/viggle/jst-2-scene-view/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

fov

number

Campo de visión en grados, de 20 a 140.

projection

string

perspective (el valor predeterminado, 1 vista) o pano (un panorama de 360°, 6 vistas).

referenceBatchIds

string[]

requerido

De 1 a 35 ids de lote de la sesión, desde `result.outputBatch.batchId`.

seed

integer

Semilla de generación.Formato: `int64`

sessionId

string

requerido

La sesión de la escena.

targetPosition

object

requerido

La cámara como una posición y dos ángulos.

targetPosition.pitch

number

Grados hacia arriba o hacia abajo, de -90 a 90; un valor positivo mira hacia arriba.

targetPosition.position

number[]

requerido

Posición de la cámara `[x, y, z]`.

targetPosition.yaw

number

Grados alrededor del eje +Y del mundo; un valor positivo gira hacia la izquierda.

Generado a partir del esquema que Router expone en `GET /v2/models/viggle/jst-2-scene-view/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

completedAt

integer

Formato: `int64`

createdAt

integer

Formato: `int64`

credits

number

Créditos de Viggle que se cobran por la tarea; 0 cuando se reembolsa una tarea que no finalizó en estado listo.

error

object

Objeto de error de Viggle, que se establece cuando la tarea falla.

error.code

string

error.message

string

error.request_id

string

error.retryable

boolean

id

string

ID de la tarea de escena (prefijo `scn_`).

operation

string

Tipo de tarea: pano, generate o reconstruct.

queuePosition

integer

Tareas por delante de esta mientras está en cola.

result

object

La salida de la escena, que solo se establece cuando la tarea está lista.

result.newViewCount

integer

result.operation

string

result.outputBatch

object

El lote de imágenes que la tarea agregó a la sesión.

result.outputBatch.batchId

string

result.outputBatch.createdAt

number

result.outputBatch.kind

string

result.outputBatch.manifest

object

result.outputBatch.manifest.url

string

URL de descarga, válida durante 3 horas.

result.outputBatch.views

object[]

result.outputBatch.views[].c2w

number[][]

Matriz de cámara a mundo de 4 × 4.

result.outputBatch.views[].index

integer

result.outputBatch.views[].intrinsic

number[]

Parámetros intrínsecos de la cámara.

result.outputBatch.views[].url

string

URL de descarga de la imagen de la vista, válida durante 3 horas.

result.panorama

object

result.panorama.url

string

URL de descarga, válida durante 3 horas.

result.preview

object

result.preview.url

string

URL de descarga, válida durante 3 horas.

result.referenceViewCount

integer

result.sessionId

string

result.spz

object

result.spz.url

string

URL de descarga, válida durante 3 horas.

sessionId

string

status

string

Estado: queued, processing, ready, failed o cancelled.

## Ejemplos

### Entrada
    
    
    {
      "projection": "perspective",
      "referenceBatchIds": [
        "3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f"
      ],
      "sessionId": "replace-with-a-new-random-id",
      "targetPosition": {
        "pitch": 0,
        "position": [
          0.3,
          0,
          0
        ],
        "yaw": 30
      }
    }
    

### Salida
    
    
    {
      "credits": 6,
      "error": null,
      "id": "scn_0199f0c2-6a1e-7c3d-9b2a-4f5e6d7c8b9a.replace-with-a-new-random-id",
      "operation": "pano",
      "result": {
        "newViewCount": 6,
        "operation": "pano",
        "outputBatch": {
          "batchId": "3f0a6c1e-8d2b-4b7a-9e5c-1a2b3c4d5e6f",
          "kind": "initial",
          "views": [
            {
              "index": 0,
              "url": "https://example.invalid/viggle/view-0.png"
            }
          ]
        },
        "panorama": {
          "url": "https://example.invalid/viggle/panorama.png"
        },
        "referenceViewCount": 0,
        "sessionId": "replace-with-a-new-random-id",
        "spz": {
          "url": "https://example.invalid/viggle/scene.spz"
        }
      },
      "sessionId": "replace-with-a-new-random-id",
      "status": "ready"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/viggle/jst-2-scene-view/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/viggle/jst-2-scene-view/code)

[Veo 3.1 Lite Generate 001](https://docs.comfy.org/es/development/comfy-router/models/veo/veo-3-1-lite-generate-001/code)[Jst 2 Scene](https://docs.comfy.org/es/development/comfy-router/models/viggle/jst-2-scene/code)
