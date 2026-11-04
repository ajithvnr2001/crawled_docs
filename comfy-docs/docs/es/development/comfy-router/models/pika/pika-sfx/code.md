---
url: https://docs.comfy.org/es/development/comfy-router/models/pika/pika-sfx/code/
title: Usa Pika Sfx con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:41.394778+00:00
---

# Usa Pika Sfx con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/pika/pika-sfx/code/

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

# Usa Pika Sfx con Comfy Router

Copiar páginaCopiar página

Llama a pika/pika-sfx mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `pika/pika-sfx`, servida por Comfy Router desde Pika. **Entrada:** Texto · **Salida:** Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `pika/pika-sfx` **Endpoint:** `POST https://api.comfy.org/v2/models/pika/pika-sfx`

  * Esperar el resultado

  * Poner en cola y obtener más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "pika/pika-sfx",
            {
                "duration": 2,
                "prompt": "a wooden door creaking open",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("pika/pika-sfx", {
      duration: 2,
      prompt: "a wooden door creaking open",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pika/pika-sfx \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 2, \"prompt\": \"a wooden door creaking open\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/pika/pika-sfx/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se obtiene cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) describe el estado, la cancelación y la obtención del resultado.

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
                "pika/pika-sfx",
                {
                    "duration": 2,
                    "prompt": "a wooden door creaking open",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta repetidamente hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
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
    const handle = await comfy.models.submit("pika/pika-sfx", {
      duration: 2,
      prompt: "a wooden door creaking open",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta repetidamente hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló provoca un rechazo aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/pika/pika-sfx/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 2, \"prompt\": \"a wooden door creaking open\"}"
    
    # 2. Consulta repetidamente hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indique cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pika/pika-sfx/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Obtén. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/pika/pika-sfx/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

duration

number

predeterminado:"10"

Duración del efecto de sonido en segundos, de 1 a 20.Rango: `1` a `20`

​

prompt

string

requerido

Descripción del efecto de sonido.

​

seed

integer

predeterminado:"-1"

Semilla para obtener resultados reproducibles, de -1 a 2147483647. Con -1 se elige una semilla aleatoria.Rango: `-1` a `2147483647`

Generado a partir del esquema que Router publica en `GET /v2/models/pika/pika-sfx/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

error

object

Se asigna cuando la tarea está `failed`.

​

error.code

string

Código de error legible por máquina, como invalid_input, content_moderation o provider_error.

​

error.message

string

Texto de diagnóstico.

​

id

string

ID de trabajo que se usa para consultar el estado.

​

model_id

string

La entrada del catálogo de Pika con la que se ejecutó la tarea.

​

output

object

Los archivos multimedia de la tarea finalizada; se asigna cuando `status` es `completed`.

​

output.audio

object

Un archivo multimedia generado.

​

output.audio.content_type

string

Tipo MIME del archivo.

​

output.audio.url

string

URL de descarga del archivo generado.

​

output.media_type

string

Indica qué campo contiene el archivo: video o audio.

​

output.video

object

Un archivo multimedia generado.

​

output.video.content_type

string

Tipo MIME del archivo.

​

output.video.url

string

URL de descarga del archivo generado.

​

status

string

Estado de la tarea: queued, running, completed o failed.

​

usage

object

Unidades que Pika informó para la tarea.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "duration": 2,
      "prompt": "a wooden door creaking open"
    }
    

### 

​

Salida
    
    
    {
      "id": "media_2d8e4b71-9c05-4f3a-b6d2-81e7a5c09f44",
      "output": {
        "audio": {
          "content_type": "audio/mpeg",
          "url": "https://example.invalid/pika/audio.mp3"
        },
        "media_type": "audio"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/pika/pika-sfx/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/pika/pika-sfx/code)

[Pika Music](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-music/code)[Pika Soundtrack](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-soundtrack/code)
