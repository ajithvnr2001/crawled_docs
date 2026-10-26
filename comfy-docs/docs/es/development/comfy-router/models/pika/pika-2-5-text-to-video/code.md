---
url: https://docs.comfy.org/es/development/comfy-router/models/pika/pika-2-5-text-to-video/code/
title: Usa Pika 2.5 Text To Video con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:16.735680+00:00
---

# Usa Pika 2.5 Text To Video con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/pika/pika-2-5-text-to-video/code/

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



Pika

# Usa Pika 2.5 Text To Video con Comfy Router

Copiar páginaCopiar página

Llama a pika/pika-2.5-text-to-video con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `pika/pika-2.5-text-to-video`, servida por Comfy Router desde Pika. **Entrada:** Texto · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `pika/pika-2.5-text-to-video` **Endpoint:** `POST https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video`

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
            "pika/pika-2.5-text-to-video",
            {
                "duration_s": 5,
                "prompt": "A paper boat drifting down a rain-soaked city street at dusk",
                "resolution": "720p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("pika/pika-2.5-text-to-video", {
      duration_s: 5,
      prompt: "A paper boat drifting down a rain-soaked city street at dusk",
      resolution: "720p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration_s\": 5, \"prompt\": \"A paper boat drifting down a rain-soaked city street at dusk\", \"resolution\": \"720p\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video/requests`. Router responde `201` con un `request_id` en cuanto admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "pika/pika-2.5-text-to-video",
                {
                    "duration_s": 5,
                    "prompt": "A paper boat drifting down a rain-soaked city street at dusk",
                    "resolution": "720p",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("pika/pika-2.5-text-to-video", {
      duration_s: 5,
      prompt: "A paper boat drifting down a rain-soaked city street at dusk",
      resolution: "720p",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration_s\": 5, \"prompt\": \"A paper boat drifting down a rain-soaked city street at dusk\", \"resolution\": \"720p\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/pika/pika-2.5-text-to-video/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

duration_s

integer

predeterminado:"5"

Duración del video en segundos. Texto a video genera únicamente clips de cinco segundos.Valores posibles: `5`

​

negative_prompt

string

Texto que describe lo que se debe evitar en el video.

​

prompt

string

requerido

Prompt de texto que describe el video a generar.

​

resolution

string

predeterminado:"\"1080p\""

Resolución de salida.Valores posibles: `720p`, `1080p`

​

seed

integer

Semilla para una generación reproducible. Omítela (o envía null) para obtener una semilla aleatoria.

Generado a partir del esquema que Router sirve en `GET /v2/models/pika/pika-2.5-text-to-video/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

error

object

Registro de fallo estructurado de Pika, establecido en una tarea `failed`. Router responde a una tarea fallida con su propia respuesta de error, así que un cuerpo que devuelve Router no lo incluye; se declara porque forma parte del documento de tarea de Pika.

​

error.code

string

requerido

Valores posibles: `invalid_input`, `content_moderation`, `provider_error`, `provider_timeout`, `provider_unavailable`, `rate_limited`, `insufficient_balance`, `membership_required`, `cycle_limit_exceeded`, `admission_suspended`, `usage_limit_exceeded`, `timed_out`, `internal`

​

error.message

string

requerido

​

id

string

requerido

ID de trabajo de Pika.

​

model_id

string

La entrada del catálogo de Pika que ejecutó la tarea.

​

output

object

Los medios de la tarea finalizada, establecidos cuando `status` es `completed`. `media_type` indica qué campo los contiene: `image` llena `images`, `video` llena `video` y `videos` llena `videos`.

​

output.images

object[]

Imágenes generadas, para un modelo de imágenes.

​

output.images[].content_type

string

Tipo MIME del archivo.

​

output.images[].height

integer

Alto en píxeles.

​

output.images[].url

string

URL de descarga del archivo generado.

​

output.images[].width

integer

Ancho en píxeles.

​

output.media_type

string

Valores posibles: `image`, `video`, `videos`

​

output.seed

integer

La semilla que realmente usó la tarea de video, cuando se informa.

​

output.video

object

Un archivo de medios generado.

​

output.video.content_type

string

Tipo MIME del archivo.

​

output.video.height

integer

Alto en píxeles.

​

output.video.url

string

URL de descarga del archivo generado.

​

output.video.width

integer

Ancho en píxeles.

​

output.videos

object[]

Videos generados, para una entrega de varios videos.

​

output.videos[].content_type

string

Tipo MIME del archivo.

​

output.videos[].height

integer

Alto en píxeles.

​

output.videos[].url

string

URL de descarga del archivo generado.

​

output.videos[].width

integer

Ancho en píxeles.

​

runtime_s

number

Segundos que tardó la generación, desde el despacho hasta el estado terminal. Es un valor aproximado; puede ser null.

​

status

string

requerido

Estado del ciclo de vida. Un cuerpo que devuelve Router siempre indica `completed`; una tarea `failed` se responde con la respuesta de error de Router.Valores posibles: `queued`, `running`, `completed`, `failed`

​

usage

object

Unidades de la tarea informadas por el proveedor. Las claves son dispersas; solo están presentes las unidades que informa la tarea.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "duration_s": 5,
      "prompt": "A paper boat drifting down a rain-soaked city street at dusk",
      "resolution": "720p"
    }
    

### 

​

Salida
    
    
    {
      "id": "6f1c2a9e-3b47-4d8a-9e21-7c5b0f4d8a13",
      "model_id": "pika/pika-2.5/text-to-video",
      "output": {
        "media_type": "video",
        "seed": 42,
        "video": {
          "content_type": "video/mp4",
          "height": 720,
          "url": "https://example.invalid/pika/pika-2.5-text-to-video/generated.mp4",
          "width": 1280
        }
      },
      "status": "completed"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/pika/pika-2-5-text-to-video/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/pika/pika-2-5-text-to-video/code)

[Pika 2.5 Image To Video](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-2-5-image-to-video/code)[P Video 2](https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2/code)
