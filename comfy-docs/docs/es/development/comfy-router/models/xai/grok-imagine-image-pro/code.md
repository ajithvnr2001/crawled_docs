---
url: https://docs.comfy.org/es/development/comfy-router/models/xai/grok-imagine-image-pro/code/
title: Usa Grok Imagine Image Pro con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:25.512563+00:00
---

# Usa Grok Imagine Image Pro con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/xai/grok-imagine-image-pro/code/

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

# Usa Grok Imagine Image Pro con Comfy Router

Copiar páginaCopiar página

Llama a xai/grok-imagine-image-pro mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `xai/grok-imagine-image-pro`, servida por Comfy Router desde xAI. **Entrada:** Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP directo. **ID del modelo:** `xai/grok-imagine-image-pro` **Endpoint:** `POST https://api.comfy.org/v2/models/xai/grok-imagine-image-pro`

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
            "xai/grok-imagine-image-pro",
            {
                "n": 1,
                "prompt": "A single red maple leaf on a plain white background.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("xai/grok-imagine-image-pro", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/xai/grok-imagine-image-pro \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/xai/grok-imagine-image-pro/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "xai/grok-imagine-image-pro",
                {
                    "n": 1,
                    "prompt": "A single red maple leaf on a plain white background.",
                },
            )
            print("request_id:", handle.request_id)  # junto con el model ID, es todo lo que otro proceso necesita
    
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
    const handle = await comfy.models.submit("xai/grok-imagine-image-pro", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
    });
    console.log("requestId:", handle.requestId); // junto con el model ID, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/xai/grok-imagine-image-pro/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/xai/grok-imagine-image-pro/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/xai/grok-imagine-image-pro/requests/$REQUEST_ID \
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

Modelo que se va a usar. Compatibles: grok-imagine-image (predeterminado), grok-imagine-image-pro, grok-imagine-image-quality, grok-imagine-image-2.0. Los ids -beta obsoletos se tratan como alias de su modelo GA.

​

n

integer

predeterminado:"1"

Número de imágenes que se van a generarRango: `1` a `10`

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

Formato de respuesta en el que se devuelve la imagen. Puede ser url o b64_json. Comfy fuerza este valor a `url` en la solicitud saliente (tanto en el dispatch de Comfy Router: `POST /v2/models/xai/{model}`, como en esta ruta `/proxy/`), porque los resultados de imagen se sirven como URL re-alojadas de cualquier forma. Por lo tanto, un valor DENTRO del enum se acepta y se ignora: envía `url` o `b64_json` u omite el campo, y la respuesta es la misma. Un valor FUERA del enum, excluyendo las formas de UNSET que reconoce cada superficie y que se describen a continuación, se RECHAZA en lugar de forzarse en AMBAS superficies, y solo difiere la forma del rechazo: esta ruta `/proxy/` responde con un `400` en la entrada, y el dispatch de Router `POST /v2/models/xai/{model}` responde con el `422` por campo que debe al enum publicado aquí, antes de realizar cualquier llamada al socio. Las dos superficies difieren en lo que cuenta como UNSET. En esta ruta `/proxy/`, un campo omitido, un `null` explícito y `""` significan todos no establecido y se fuerzan como cualquier valor aceptado. El dispatch de Router aplica el enum exactamente como se publica, así que `null` y `""` no son miembros allí como cualquier otro: OMITE el campo para dejarlo sin establecer en esa superficie.Valores posibles: `url`, `b64_json`

​

size

string

Tamaño de la imagen (no admitido)

​

style

string

Estilo de la imagen (no admitido)

​

user

string

Un identificador único que representa a tu usuario final, lo que puede ayudar a xAI a monitorear y detectar abusos

Generado a partir del esquema que Router sirve en `GET /v2/models/xai/grok-imagine-image-pro/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

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

Una url de la imagen generada (si response_format es url)

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/xai/grok-imagine-image-pro/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/xai/grok-imagine-image-pro/code)

[Grok Imagine Image 2.0](https://docs.comfy.org/es/development/comfy-router/models/xai/grok-imagine-image-2-0/code)[Grok Imagine Image Quality](https://docs.comfy.org/es/development/comfy-router/models/xai/grok-imagine-image-quality/code)
