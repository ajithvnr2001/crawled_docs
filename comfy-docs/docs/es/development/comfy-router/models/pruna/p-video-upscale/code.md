---
url: https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-upscale/code/
title: Usar P Video Upscale con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-27T17:19:27.053159+00:00
---

# Usar P Video Upscale con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-upscale/code/

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

# Usar P Video Upscale con Comfy Router

Copiar páginaCopiar página

Llama a pruna/p-video-upscale desde Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `pruna/p-video-upscale`, servida por Comfy Router desde Pruna. **Entrada:** Video · **Salida:** Video + Audio

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP puro. **ID del modelo:** `pruna/p-video-upscale` **Endpoint:** `POST https://api.comfy.org/v2/models/pruna/p-video-upscale`

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
            "pruna/p-video-upscale",
            {
                "input": {
                    "target": "1080p",
                    "video": "https://example.com/source.mp4",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("pruna/p-video-upscale", {
      input: {
        target: "1080p",
        video: "https://example.com/source.mp4",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pruna/p-video-upscale \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"target\":\"1080p\",\"video\":\"https://example.com/source.mp4\"}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/pruna/p-video-upscale/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "pruna/p-video-upscale",
                {
                    "input": {
                        "target": "1080p",
                        "video": "https://example.com/source.mp4",
                    },
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta en bucle hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("pruna/p-video-upscale", {
      input: {
        target: "1080p",
        video: "https://example.com/source.mp4",
      },
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta en bucle hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/pruna/p-video-upscale/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"target\":\"1080p\",\"video\":\"https://example.com/source.mp4\"}}"
    
    # 2. Consulta en bucle hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pruna/p-video-upscale/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/pruna/p-video-upscale/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

input

object

requerido

Parámetros de P-Video-Upscale. La tarea se factura por segundo del video devuelto, medido a partir del archivo devuelto y redondeado hacia arriba hasta el segundo entero. La tarifa la determinan `target` y si la frecuencia de cuadros de salida supera los 30 fps. Cuando se omite `fps`, la salida conserva la frecuencia de cuadros de `video`, así que esa frecuencia decide el nivel. Una tarea `turbo` se factura a la tarifa turbo de su `target`, sea cual sea la frecuencia de cuadros. El filtro de seguridad siempre está activo; un valor `enable_safety_filter` en la solicitud se ignora.

input.fps

integer

Frecuencia de cuadros de salida (16-60). Una frecuencia superior a la de la fuente se interpola. Cuando se omite, la salida conserva la frecuencia de la fuente.Rango: `16` a `60`

input.target

string

predeterminado:"\"1080p\""

Preajuste de resolución de salida: 720p, 1080p, 2k o 4k. El preajuste define el área en píxeles; un video que no es 16:9 conserva su relación de aspecto. Un video que ya es más grande que el objetivo no se reduce.Valores posibles: `720p`, `1080p`, `2k`, `4k`

input.turbo

boolean

predeterminado:"false"

Tarea más rápida con una calidad ligeramente inferior, facturada a la tarifa turbo (alrededor de un tercio de la tarifa estándar) a cualquier frecuencia de cuadros.

input.video

string

requerido

URI del video de entrada, de 512 MiB como máximo. Debe ser una URL http(s) legible públicamente cuando se omite `fps`, porque su frecuencia de cuadros se lee antes de enviar la tarea.

Generado a partir del esquema que Router sirve en `GET /v2/models/pruna/p-video-upscale/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

error

string

Mensaje de error. Presente cuando el estado es fallido.

generation_url

string

URL del video finalizado. Presente cuando el estado es exitoso.

message

string

Mensaje de progreso legible para las personas.

moderation

object

Veredicto del verificador de seguridad de Pruna. Presente en un estado fallido cuando la moderación de contenido bloqueó la predicción.

moderation.blocked

boolean

Indica si el verificador de seguridad bloqueó la predicción.

moderation.can_disable

boolean

Indica si el bloqueo proviene de un filtro de seguridad que la solicitud podría desactivar.

moderation.categories

string[]

Categorías de política de contenido que activaron el bloqueo, por ejemplo sexual.

moderation.message

string

Resumen del bloqueo legible para las personas.

moderation.phase

string

Qué se examinó: la entrada (la solicitud enviada) o la salida (el video generado).

moderation.reason

string

Motivo del bloqueo legible para las personas.

status

string

Estado de la predicción: iniciando, procesando, exitoso, fallido o cancelado.

## Ejemplos

### Entrada
    
    
    {
      "input": {
        "target": "1080p",
        "video": "https://example.com/source.mp4"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/pruna/p-video-upscale/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/pruna/p-video-upscale/code)

[P Video 2](https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2/code)[Arrow 2 Telos](https://docs.comfy.org/es/development/comfy-router/models/quiver/arrow-2-telos/code)
