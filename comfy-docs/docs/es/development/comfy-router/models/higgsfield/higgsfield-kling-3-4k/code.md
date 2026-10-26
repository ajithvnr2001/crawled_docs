---
url: https://docs.comfy.org/es/development/comfy-router/models/higgsfield/higgsfield-kling-3-4k/code/
title: Usa Higgsfield Kling 3.4k con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:07.065774+00:00
---

# Usa Higgsfield Kling 3.4k con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/higgsfield/higgsfield-kling-3-4k/code/

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



Higgsfield

# Usa Higgsfield Kling 3.4k con Comfy Router

Copiar páginaCopiar página

Llama a higgsfield/higgsfield-kling-3-4k con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `higgsfield/higgsfield-kling-3-4k`, servida por Comfy Router desde Higgsfield. **Entrada:** Texto · **Salida:** Video + Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `higgsfield/higgsfield-kling-3-4k` **Endpoint:** `POST https://api.comfy.org/v2/models/higgsfield/higgsfield-kling-3-4k`

  * Esperar el resultado

  * Encolar y recoger el resultado más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "higgsfield/higgsfield-kling-3-4k",
            {
                "aspect_ratio": "16:9",
                "cfg_scale": 0.5,
                "duration": 5,
                "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
                "sound": "on",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("higgsfield/higgsfield-kling-3-4k", {
      aspect_ratio: "16:9",
      cfg_scale: 0.5,
      duration: 5,
      prompt: "A cinematic glass pavilion in a misty pine forest at sunrise",
      sound: "on",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/higgsfield/higgsfield-kling-3-4k \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"cfg_scale\": 0.5, \"duration\": 5, \"prompt\": \"A cinematic glass pavilion in a misty pine forest at sunrise\", \"sound\": \"on\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/higgsfield/higgsfield-kling-3-4k/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida del resultado.

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
                "higgsfield/higgsfield-kling-3-4k",
                {
                    "aspect_ratio": "16:9",
                    "cfg_scale": 0.5,
                    "duration": 5,
                    "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
                    "sound": "on",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("higgsfield/higgsfield-kling-3-4k", {
      aspect_ratio: "16:9",
      cfg_scale: 0.5,
      duration: 5,
      prompt: "A cinematic glass pavilion in a misty pine forest at sunrise",
      sound: "on",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud fallida o cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/higgsfield/higgsfield-kling-3-4k/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"cfg_scale\": 0.5, \"duration\": 5, \"prompt\": \"A cinematic glass pavilion in a misty pine forest at sunrise\", \"sound\": \"on\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/higgsfield/higgsfield-kling-3-4k/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/higgsfield/higgsfield-kling-3-4k/requests/$REQUEST_ID \
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

predeterminado:"\"16:9\""

Relación de aspecto de la salida.Valores posibles: `16:9`, `9:16`, `1:1`

​

cfg_scale

number

predeterminado:"0.5"

Qué tan fielmente sigue la generación al prompt. Higgsfield documenta 0-1 en incrementos de 0.01, pero aquí solo se declara el límite 0-1: un `multipleOf: 0.01` se evaluaría en punto flotante binario y rechazaría valores ordinarios como 0.3, así que un valor de mayor precisión se ACEPTA y se reenvía en lugar de rechazarse, del mismo modo que `prompt` advierte sobre su límite de longitud no declarado.Rango: `0` a `1`

​

duration

integer

predeterminado:"5"

Duración de la salida en segundos. Alcance admitido: 3-15.Rango: `3` a `15`

​

elements

string[]

Ids de elementos Kling reutilizables, para mantener la consistencia del sujeto entre generaciones.

​

multi_prompt

object[]

Definiciones de tomas ordenadas, usadas cuando `multi_shots` es verdadero. De 1 a 6 tomas; las duraciones de cada toma están acotadas por la duración total de la tarea, lo cual no se puede expresar aquí.

​

multi_prompt[].duration

integer

Duración de esta toma en segundos, 1-15. La suma de todas las tomas no debe superar la duración total de la tarea, algo que JSON Schema no puede expresar; Higgsfield lo aplica.Rango: `1` a `15`

​

multi_prompt[].prompt

string

Prompt para esta toma. Higgsfield documenta un límite de 512 caracteres.

​

multi_shots

boolean

predeterminado:"false"

Activa una secuencia de varias tomas. Cuando es verdadero, `multi_prompt` contiene las definiciones de cada toma.

​

prompt

string

Prompt que describe la salida deseada. Higgsfield documenta que Kling usa solo los primeros 2,500 caracteres y trunca el resto, por lo que no se declara ningún maxLength: un cuerpo más largo se acepta, no se rechaza.

​

sound

string

predeterminado:"\"on\""

Activa o desactiva el sonido generado.Valores posibles: `on`, `off`

Generado a partir del esquema que Router sirve en `GET /v2/models/higgsfield/higgsfield-kling-3-4k/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

cancel_url

string

URL absoluta usada para cancelar una solicitud antes de que comience el procesamiento.

​

error

string

Detalle del fallo, definido cuando `status` es `failed`.

​

request_id

string

requerido

Identificador estable usado para consultar el estado, cancelar y solicitar soporte.

​

status

string

requerido

Estado actual de la solicitud.Valores posibles: `queued`, `in_progress`, `nsfw`, `failed`, `completed`, `canceled`

​

status_url

string

URL absoluta para consultar el estado hasta que la solicitud alcance un estado terminal.

​

video

object

Una salida de medios de Higgsfield.

​

video.url

string

requerido

URL de descarga de los medios generados.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "aspect_ratio": "16:9",
      "cfg_scale": 0.5,
      "duration": 5,
      "prompt": "A cinematic glass pavilion in a misty pine forest at sunrise",
      "sound": "on"
    }
    

### 

​

Salida
    
    
    {
      "cancel_url": "https://api.higgsfield.ai/requests/4b1f8ac2-0d35-4f2e-9c77-1e5a6b0c93d4/cancel",
      "request_id": "4b1f8ac2-0d35-4f2e-9c77-1e5a6b0c93d4",
      "status": "completed",
      "status_url": "https://api.higgsfield.ai/requests/4b1f8ac2-0d35-4f2e-9c77-1e5a6b0c93d4/status",
      "video": {
        "url": "https://example.invalid/higgsfield/higgsfield-kling-3-4k/generated.mp4"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/higgsfield/higgsfield-kling-3-4k/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/higgsfield/higgsfield-kling-3-4k/code)

[Higgsfield Genjutsu Motion Transfer V1.0](https://docs.comfy.org/es/development/comfy-router/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1-0/code)[Higgsfield Kling 3 Pro](https://docs.comfy.org/es/development/comfy-router/models/higgsfield/higgsfield-kling-3-pro/code)
