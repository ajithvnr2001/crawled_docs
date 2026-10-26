---
url: https://docs.comfy.org/es/development/comfy-router/models/xai/grok-imagine-image-2-0/code/
title: Usa Grok Imagine Image 2.0 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:25.088703+00:00
---

# Usa Grok Imagine Image 2.0 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/xai/grok-imagine-image-2-0/code/

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



xAI

# Usa Grok Imagine Image 2.0 con Comfy Router

Copiar páginaCopiar página

Llama a xai/grok-imagine-image-2.0 mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `xai/grok-imagine-image-2.0`, servida por Comfy Router desde xAI. **Entrada:** Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `xai/grok-imagine-image-2.0` **Endpoint:** `POST https://api.comfy.org/v2/models/xai/grok-imagine-image-2.0`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    with Comfy() as client:
        result = client.models.run(
            "xai/grok-imagine-image-2.0",
            {
                "n": 1,
                "prompt": "A single red maple leaf on a plain white background.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("xai/grok-imagine-image-2.0", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/xai/grok-imagine-image-2.0 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    

The same body, sent to `POST https://api.comfy.org/v2/models/xai/grok-imagine-image-2.0/requests`. Router answers `201` with a `request_id` as soon as the run is admitted, and the result is collected once it is ready, from this process or another one. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) walks through status, cancellation and collection.

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
                "xai/grok-imagine-image-2.0",
                {
                    "n": 1,
                    "prompt": "A single red maple leaf on a plain white background.",
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
    const handle = await comfy.models.submit("xai/grok-imagine-image-2.0", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
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
    curl https://api.comfy.org/v2/models/xai/grok-imagine-image-2.0/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/xai/grok-imagine-image-2.0/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/xai/grok-imagine-image-2.0/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

aspect_ratio

string

predeterminado:"\"auto\""

Relación de aspecto de la imagen generada. El valor predeterminado es auto, que selecciona automáticamente la mejor relación para el prompt.Valores posibles: `1:1`, `3:4`, `4:3`, `9:16`, `16:9`, `2:3`, `3:2`, `9:19.5`, `19.5:9`, `9:20`, `20:9`, `1:2`, `2:1`, `auto`

​

model

string

predeterminado:"\"grok-imagine-image\""

Modelo que se va a usar. Compatibles: grok-imagine-image (predeterminado), grok-imagine-image-pro, grok-imagine-image-quality, grok-imagine-image-2.0. Los ids -beta obsoletos son alias de su modelo GA.

​

n

integer

predeterminado:"1"

Cantidad de imágenes a generarRango: `1` a `10`

​

prompt

string

requerido

Prompt para la generación de imágenes

​

quality

string

Calidad de la imagen de salida. Para grok-imagine-image-2.0 esto selecciona el nivel de precio (low/medium; medium es el predeterminado); los demás modelos actualmente lo ignoran.Valores posibles: `low`, `medium`, `high`

​

resolution

string

predeterminado:"\"1k\""

Resolución de la imagen generada. El valor predeterminado es 1k.Valores posibles: `1k`, `2k`

​

response_format

string

predeterminado:"\"url\""

Formato de respuesta en el que se devuelve la imagen. Puede ser url o b64_json. Comfy lo fuerza a `url` en la solicitud saliente (tanto en el despacho de Comfy Router `POST /v2/models/xai/{model}` como en esta ruta `/proxy/`) porque los resultados de imagen se sirven como URLs rehospedadas de cualquier manera. Por lo tanto, un valor DENTRO del enum se acepta y se ignora: envía `url` o `b64_json` u omite el campo, y la respuesta es la misma. Un valor FUERA del enum, excluyendo las grafías UNSET que reconoce cada superficie (descritas a continuación), se RECHAZA en lugar de forzarse en AMBAS superficies, y solo cambia la forma del rechazo: esta ruta `/proxy/` responde con un `400` en la entrada, y el despacho del Router `POST /v2/models/xai/{model}` responde con el `422` por campo que debe al enum publicado aquí, antes de realizar cualquier llamada al socio. Las dos superficies difieren en qué cuenta como UNSET. En esta ruta `/proxy/`, un campo omitido, un `null` explícito y `""` significan sin definir y se fuerzan como cualquier valor aceptado. El despacho del Router aplica el enum exactamente como se publica, así que `null` y `""` no son miembros allí como cualquier otro: OMITE el campo para dejarlo sin definir en esa superficie.Valores posibles: `url`, `b64_json`

​

size

string

Tamaño de la imagen (no compatible)

​

style

string

Estilo de la imagen (no compatible)

​

user

string

Un identificador único que representa a tu usuario final, lo que puede ayudar a xAI a monitorear y detectar abusos

Generado a partir del esquema que Router sirve en `GET /v2/models/xai/grok-imagine-image-2.0/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

block_reason

string

Si la solicitud fue bloqueada por la moderación de entrada, contiene el motivo del bloqueo

​

data

object[]

Una lista de objetos de imagen generados

​

data[].b64_json

string

Una representación en cadena codificada en base64 de la imagen generada con codificación jpeg (si response_format es b64_json)

​

data[].mime_type

string

El tipo MIME de la imagen generada (p. ej., image/png, image/jpeg, image/webp).

​

data[].url

string

Una URL de la imagen generada (si response_format es url)

​

usage

object

Información de uso de la solicitud de generación de imágenes

​

usage.cost_in_usd_ticks

integer

Costo exacto de esta solicitud en ticks de USD (10,000,000,000 ticks = 1 USD)

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "n": 1,
      "prompt": "A single red maple leaf on a plain white background."
    }
    

### 

​

Salida
    
    
    {
      "data": [
        {
          "mime_type": "image/jpeg",
          "url": "https://example.invalid/xai/grok-imagine-image/generated.jpg"
        },
        {
          "mime_type": "image/jpeg",
          "url": "https://example.invalid/xai/grok-imagine-image/generated-2.jpg"
        }
      ],
      "usage": {
        "cost_in_usd_ticks": 200000000
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/xai/grok-imagine-image-2-0/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/xai/grok-imagine-image-2-0/code)

[Ultimate Image Upscaler](https://docs.comfy.org/es/development/comfy-router/models/wavespeed/ultimate-image-upscaler/code)[Grok Imagine Image Pro](https://docs.comfy.org/es/development/comfy-router/models/xai/grok-imagine-image-pro/code)
