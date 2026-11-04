---
url: https://docs.comfy.org/es/development/comfy-router/models/pika/pika-soundtrack/code/
title: Usa Pika Soundtrack con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:41.820125+00:00
---

# Usa Pika Soundtrack con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/pika/pika-soundtrack/code/

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

# Usa Pika Soundtrack con Comfy Router

Copiar páginaCopiar página

Llama a pika/pika-soundtrack mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `pika/pika-soundtrack`, servida por Comfy Router desde Pika. **Entrada:** Video, Texto · **Salida:** Video + Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `pika/pika-soundtrack` **Endpoint:** `POST https://api.comfy.org/v2/models/pika/pika-soundtrack`

  * Esperar el resultado

  * Enviar a la cola y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY desde las variables de entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "pika/pika-soundtrack",
            {
                "seed": -1,
                "video": "https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY desde las variables de entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("pika/pika-soundtrack", {
      seed: -1,
      video: "https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pika/pika-soundtrack \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"seed\": -1, \"video\": \"https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/pika/pika-soundtrack/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY desde las variables de entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "pika/pika-soundtrack",
                {
                    "seed": -1,
                    "video": "https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4",
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
    
    // Lee COMFY_API_KEY desde las variables de entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("pika/pika-soundtrack", {
      seed: -1,
      video: "https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4",
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
    curl https://api.comfy.org/v2/models/pika/pika-soundtrack/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"seed\": -1, \"video\": \"https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pika/pika-soundtrack/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/pika/pika-soundtrack/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

instruction

string

Qué debe ser el audio y cómo acompaña a la acción. Omítelo para hacer diseño de sonido solo a partir del video.

​

seed

integer

predeterminado:"-1"

Semilla de -1 a 2147483647. -1 elige una semilla aleatoria.Rango: `-1` a `2147483647`

​

video

string

requerido

URL del video de origen, H.264 o HEVC, de 1200 segundos y 2 GB como máximo.

Generado a partir del esquema que Router sirve en `GET /v2/models/pika/pika-soundtrack/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

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

Código de fallo legible por máquina, como invalid_input, content_moderation o provider_error.

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

Los medios de la tarea finalizada, asignados cuando `status` es `completed`.

​

output.audio

object

Un archivo de medios generado.

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

Qué campo lleva el archivo: video o audio.

​

output.video

object

Un archivo de medios generado.

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
      "seed": -1,
      "video": "https://cdn.pika.art/v2/media/uploads/a7112d4d-62ed-4a11-8dee-74e89c2ec037/ae79aabfd458427495cf462f49e1cecc.mp4"
    }
    

### 

​

Salida
    
    
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/pika/pika-soundtrack/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/pika/pika-soundtrack/code)

[Pika Sfx](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-sfx/code)[P Video 2](https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2/code)
