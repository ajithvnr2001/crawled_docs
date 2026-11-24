---
url: https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2-pro-reference/code/
title: Usar P Video 2 Pro Reference con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:26.648370+00:00
---

# Usar P Video 2 Pro Reference con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2-pro-reference/code/

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



Pruna

# Usar P Video 2 Pro Reference con Comfy Router

Copiar páginaCopiar página

Llama a pruna/p-video-2-pro-reference mediante Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `pruna/p-video-2-pro-reference`, servida por Comfy Router desde Pruna. **Entrada:** Texto, Imagen, Video, Audio · **Salida:** Video + Audio

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `pruna/p-video-2-pro-reference` **Endpoint:** `POST https://api.comfy.org/v2/models/pruna/p-video-2-pro-reference`

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
            "pruna/p-video-2-pro-reference",
            {
                "input": {
                    "duration": 5,
                    "image": ["https://example.com/woman.png"],
                    "mode": "speed",
                    "prompt": "The woman from the image walks through the market.",
                    "resolution": "768p",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("pruna/p-video-2-pro-reference", {
      input: {
        duration: 5,
        image: ["https://example.com/woman.png"],
        mode: "speed",
        prompt: "The woman from the image walks through the market.",
        resolution: "768p",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pruna/p-video-2-pro-reference \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"duration\":5,\"image\":[\"https://example.com/woman.png\"],\"mode\":\"speed\",\"prompt\":\"The woman from the image walks through the market.\",\"resolution\":\"768p\"}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/pruna/p-video-2-pro-reference/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "pruna/p-video-2-pro-reference",
                {
                    "input": {
                        "duration": 5,
                        "image": ["https://example.com/woman.png"],
                        "mode": "speed",
                        "prompt": "The woman from the image walks through the market.",
                        "resolution": "768p",
                    },
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("pruna/p-video-2-pro-reference", {
      input: {
        duration: 5,
        image: ["https://example.com/woman.png"],
        mode: "speed",
        prompt: "The woman from the image walks through the market.",
        resolution: "768p",
      },
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
    curl https://api.comfy.org/v2/models/pruna/p-video-2-pro-reference/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"duration\":5,\"image\":[\"https://example.com/woman.png\"],\"mode\":\"speed\",\"prompt\":\"The woman from the image walks through the market.\",\"resolution\":\"768p\"}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pruna/p-video-2-pro-reference/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/pruna/p-video-2-pro-reference/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

input

object

requerido

Parámetros de P-Video-2-Pro Reference. La tarea se factura por segundo del video devuelto, medido a partir del archivo devuelto y redondeado hacia abajo a un segundo entero, según la tarifa de `resolution` y `mode`. Cada referencia también se factura: cada imagen (incluidas `first_frame_image` y `last_frame_image`) una vez, y cada clip de video y audio por segundo de su duración real, como máximo `duration` \+ 0.5 segundos por clip. Las referencias de video y audio deben ser URLs http(s) accesibles públicamente, porque sus duraciones se leen antes de enviar la tarea. El filtro de seguridad siempre está activo; cualquier valor de `enable_safety_filter` en la solicitud se ignora.

input.aspect_ratio

string

predeterminado:"\"16:9\""

adaptive, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3 o 1:1.

input.audio

string[]

URIs de audio de referencia. Como máximo 3, 15 segundos en total.

input.duration

integer

predeterminado:"5"

Duración de salida en segundos.Alcance: `5` a `15`

input.first_frame_image

string

URI de la imagen del fotograma inicial. Se factura como imagen de referencia.

input.image

string[]

URIs de imágenes de referencia. Como máximo 9, incluidas las del primer y el último fotograma.

input.keep_audio

boolean

predeterminado:"false"

Usa la única referencia de `audio` como banda sonora del video. Requiere exactamente una referencia de audio, que se sigue facturando.

input.last_frame_image

string

URI de la imagen del fotograma final. Se factura como imagen de referencia.

input.mode

string

predeterminado:"\"speed\""

`speed` o `cost`. El modo define las tarifas.

input.prompt

string

requerido

Prompt de texto. También se requiere al menos una referencia de imagen o de video.

input.prompt_upsampler

string

predeterminado:"\"turbo\""

turbo, max u off.

input.resolution

string

predeterminado:"\"768p\""

Resolución de salida: 480p, 768p, 1080p, 2k o 4k. 1080p, 2k y 4k aplican upscale al video de 768p.

input.seed

integer

Semilla para una generación reproducible.

input.video

string[]

URIs de videos de referencia. Como máximo 3, de 2 a 15 segundos cada uno, 15 segundos en total.

Generado a partir del esquema que Router sirve en `GET /v2/models/pruna/p-video-2-pro-reference/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

error

string

Mensaje de error. Presente cuando el estado es failed.

generation_url

string

URL del video finalizado. Presente cuando el estado es succeeded.

message

string

Mensaje de progreso legible.

moderation

object

Veredicto del verificador de seguridad de Pruna. Presente cuando el estado es failed y la moderación de contenido bloqueó la predicción.

moderation.blocked

boolean

Indica si el verificador de seguridad bloqueó la predicción.

moderation.can_disable

boolean

Indica si el bloqueo proviene de un filtro de seguridad que la solicitud podría desactivar.

moderation.categories

string[]

Categorías de las políticas de contenido que activaron el bloqueo, por ejemplo sexual.

moderation.message

string

Resumen legible del bloqueo.

moderation.phase

string

Qué se analizó: input (la solicitud enviada) u output (el video generado).

moderation.reason

string

Motivo legible del bloqueo.

status

string

Estado de la predicción: starting, processing, succeeded, failed o canceled.

## Ejemplos

### Entrada
    
    
    {
      "input": {
        "duration": 5,
        "image": [
          "https://example.com/woman.png"
        ],
        "mode": "speed",
        "prompt": "The woman from the image walks through the market.",
        "resolution": "768p"
      }
    }
    

### Salida
    
    
    {
      "generation_url": "https://example.invalid/pruna/p-video-2/output.mp4",
      "status": "succeeded"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/pruna/p-video-2-pro-reference/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/pruna/p-video-2-pro-reference/code)

[P Video 2 Pro Avatar](https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2-pro-avatar/code)[P Video 2](https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2/code)
