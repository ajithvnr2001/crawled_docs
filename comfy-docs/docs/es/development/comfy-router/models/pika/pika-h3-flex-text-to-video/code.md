---
url: https://docs.comfy.org/es/development/comfy-router/models/pika/pika-h3-flex-text-to-video/code/
title: Usa Pika H3 Flex Text To Video con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:54.134524+00:00
---

# Usa Pika H3 Flex Text To Video con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/pika/pika-h3-flex-text-to-video/code/

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

# Usa Pika H3 Flex Text To Video con Comfy Router

Copiar páginaCopiar página

Llama a pika/pika-h3-flex-text-to-video mediante Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `pika/pika-h3-flex-text-to-video`, servida por Comfy Router desde Pika. **Entrada:** Texto · **Salida:** video + audio

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP sin procesar. **ID del modelo:** `pika/pika-h3-flex-text-to-video` **Endpoint:** `POST https://api.comfy.org/v2/models/pika/pika-h3-flex-text-to-video`

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
            "pika/pika-h3-flex-text-to-video",
            {
                "duration": 5,
                "prompt": "A paper boat drifts down a rain-soaked street at dusk while thunder rolls in the distance",
                "resolution": "480p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("pika/pika-h3-flex-text-to-video", {
      duration: 5,
      prompt: "A paper boat drifts down a rain-soaked street at dusk while thunder rolls in the distance",
      resolution: "480p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pika/pika-h3-flex-text-to-video \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"A paper boat drifts down a rain-soaked street at dusk while thunder rolls in the distance\", \"resolution\": \"480p\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/pika/pika-h3-flex-text-to-video/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "pika/pika-h3-flex-text-to-video",
                {
                    "duration": 5,
                    "prompt": "A paper boat drifts down a rain-soaked street at dusk while thunder rolls in the distance",
                    "resolution": "480p",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que otro proceso necesita
    
            # Sondea hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
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
    const handle = await comfy.models.submit("pika/pika-h3-flex-text-to-video", {
      duration: 5,
      prompt: "A paper boat drifts down a rain-soaked street at dusk while thunder rolls in the distance",
      resolution: "480p",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que otro proceso necesita
    
    // Sondea hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/pika/pika-h3-flex-text-to-video/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"A paper boat drifts down a rain-soaked street at dusk while thunder rolls in the distance\", \"resolution\": \"480p\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pika/pika-h3-flex-text-to-video/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/pika/pika-h3-flex-text-to-video/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

aspect_ratio

string

Relación de aspecto de salida. `auto` elige una a partir del prompt y de las entradas de medios. Omítela para que Pika elija: `auto` cuando `rewrite` está activado; si no, la relación de la primera entrada de medios; si no, 16:9.Valores posibles: `auto`, `21:9`, `16:9`, `3:2`, `4:3`, `5:4`, `1:1`, `4:5`, `3:4`, `2:3`, `9:16`, `9:21`

channel_mode

string

predeterminado:"\"mono\""

Solo afecta a los stems de audio. `mono` hace una mezcla descendente antes de la separación; `stereo` conserva ambos canales. El audio del video no cambia.Valores posibles: `stereo`, `mono`

duration

integer

predeterminado:"5"

Duración del video en segundos enteros, de 5 a 15.Alcance: `5` a `15`

output_mode

string

predeterminado:"\"video\""

`video` devuelve solo el video. `audio-stems` también devuelve los stems WAV de diálogo, música y efectos en `output.stems`, y añade el cargo por segundo de separación de stems de Pika.Valores posibles: `video`, `audio-stems`

prompt

string

requerido

Prompt de texto que describe el video y su audio.

resolution

string

predeterminado:"\"768p\""

Resolución de salida. 480p y 768p son nativas. 1080p, 2k y 4k generan a 768p y luego aplican upscale, manteniendo el audio y la frecuencia de cuadros.Valores posibles: `480p`, `768p`, `1080p`, `2k`, `4k`

rewrite

boolean

predeterminado:"true"

Mejora el prompt antes de la generación. Ponlo en `false` para usar el prompt tal como está escrito.

seed

integer

predeterminado:"0"

Semilla del video, 0 o más.Alcance: `0` a `…`Formato: `int64`

Generado a partir del esquema que Router sirve en `GET /v2/models/pika/pika-h3-flex-text-to-video/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

error

object

Se define en una tarea con estado `failed`.

error.code

string

Código de fallo legible por máquina, como invalid_input, content_moderation o provider_error.

error.message

string

Texto de diagnóstico.

id

string

ID de trabajo que se usa para consultar el estado.

model_id

string

La entrada del catálogo de Pika con la que se ejecutó la tarea.

output

object

Los medios de la tarea finalizada; se define cuando `status` es `completed`.

output.audio

object

Un archivo de medios generado.

output.audio.content_type

string

Tipo MIME del archivo.

output.audio.url

string

URL de descarga del archivo generado.

output.media_type

string

Qué campo lleva el archivo: video o audio.

output.video

object

Un archivo de medios generado.

output.video.content_type

string

Tipo MIME del archivo.

output.video.url

string

URL de descarga del archivo generado.

status

string

Estado de la tarea: queued, running, completed o failed.

usage

object

Unidades que Pika reportó para la tarea.

## Ejemplos

### Entrada
    
    
    {
      "duration": 5,
      "prompt": "A paper boat drifts down a rain-soaked street at dusk while thunder rolls in the distance",
      "resolution": "480p"
    }
    

### Salida
    
    
    {
      "id": "media_8f3a2c91-5b7d-4e0a-9c26-31d4f2a8e6b0",
      "output": {
        "media_type": "video",
        "video": {
          "content_type": "video/mp4",
          "url": "https://example.invalid/pika/video.mp4"
        }
      },
      "status": "completed"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/pika/pika-h3-flex-text-to-video/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/pika/pika-h3-flex-text-to-video/code)

[Pika H3 Flex Reference To Video](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-h3-flex-reference-to-video/code)[Pika Music](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-music/code)
