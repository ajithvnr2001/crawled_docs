---
url: https://docs.comfy.org/es/development/comfy-router/models/pixverse/v6/code/
title: Usar V6 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:54.648166+00:00
---

# Usar V6 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/pixverse/v6/code/

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



Pixverse

# Usar V6 con Comfy Router

Copiar páginaCopiar página

Llama a pixverse/v6 con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API de `pixverse/v6`, servida por Comfy Router desde Pixverse. **Entrada:** Texto · **Salida:** Video

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **Model ID:** `pixverse/v6` **Endpoint:** `POST https://api.comfy.org/v2/models/pixverse/v6`

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
            "pixverse/v6",
            {
                "aspect_ratio": "16:9",
                "duration": 5,
                "prompt": "a single red maple leaf falling onto still water",
                "quality": "360p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("pixverse/v6", {
      aspect_ratio: "16:9",
      duration: 5,
      prompt: "a single red maple leaf falling onto still water",
      quality: "360p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pixverse/v6 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": 5, \"prompt\": \"a single red maple leaf falling onto still water\", \"quality\": \"360p\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/pixverse/v6/requests`. Router responde `201` con un `request_id` en cuanto admite la ejecución, y recuperas el resultado en cuanto está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "pixverse/v6",
                {
                    "aspect_ratio": "16:9",
                    "duration": 5,
                    "prompt": "a single red maple leaf falling onto still water",
                    "quality": "360p",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
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
    const handle = await comfy.models.submit("pixverse/v6", {
      aspect_ratio: "16:9",
      duration: 5,
      prompt: "a single red maple leaf falling onto still water",
      quality: "360p",
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
    curl https://api.comfy.org/v2/models/pixverse/v6/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": 5, \"prompt\": \"a single red maple leaf falling onto still water\", \"quality\": \"360p\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pixverse/v6/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/pixverse/v6/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

aspect_ratio

string

requerido

Valores posibles: `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9`

duration

integer

requerido

Rango: de `1` a `15`

generate_audio_switch

boolean

predeterminado:"false"

model

string

Identificador del modelo PixVerse de texto a video. En la ruta de Comfy Router `POST /v2/models/pixverse/{model}`, este campo se toma de la ruta y puedes omitirlo.

motion_mode

string

Valores posibles: `normal`, `fast`

negative_prompt

string

prompt

string

requerido

quality

string

requerido

Valores posibles: `360p`, `540p`, `720p`, `1080p`

seed

integer

style

string

Valores posibles: `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`

template_id

integer

water_mark

boolean

Generado a partir del esquema que Router publica en `GET /v2/models/pixverse/v6/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

ErrCode

integer

ErrMsg

string

Resp

object

requerido

Resp.create_time

string

Resp.credits

integer

Resp.id

integer

Resp.modify_time

string

Resp.negative_prompt

string

Resp.outputHeight

integer

Resp.outputWidth

integer

Resp.prompt

string

Resp.resolution_ratio

integer

Resp.seed

integer

Resp.size

integer

Resp.status

integer

requerido

Valores posibles: `1`, `5`, `6`, `7`, `8`

Resp.style

string

Resp.url

string

requerido

## Ejemplos

### Entrada
    
    
    {
      "aspect_ratio": "16:9",
      "duration": 5,
      "prompt": "a single red maple leaf falling onto still water",
      "quality": "360p"
    }
    

### Salida
    
    
    {
      "ErrCode": 0,
      "ErrMsg": "",
      "Resp": {
        "credits": 1,
        "id": 4242,
        "status": 1,
        "url": "https://example.invalid/pixverse/v6/out.mp4"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/pixverse/v6/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/pixverse/v6/code)

[V6 Max](https://docs.comfy.org/es/development/comfy-router/models/pixverse/v6-max/code)[P Video 2](https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2/code)
