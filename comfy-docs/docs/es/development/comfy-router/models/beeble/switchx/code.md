---
url: https://docs.comfy.org/es/development/comfy-router/models/beeble/switchx/code/
title: Usa SwitchX con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:56.134928+00:00
---

# Usa SwitchX con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/beeble/switchx/code/

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



Beeble

# Usa SwitchX con Comfy Router

Copiar páginaCopiar página

Llama a beeble/switchx a través de Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `beeble/switchx`, servida por Comfy Router desde Beeble. **Entrada:** Imagen, Video, Texto · **Salida:** Imagen + Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `beeble/switchx` **Endpoint:** `POST https://api.comfy.org/v2/models/beeble/switchx`

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
            "beeble/switchx",
            {
                "alpha_mode": "auto",
                "generation_type": "image",
                "max_resolution": 720,
                "prompt": "A cinematic product photo of a glass lamp on a marble table",
                "source_uri": "https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("beeble/switchx", {
      alpha_mode: "auto",
      generation_type: "image",
      max_resolution: 720,
      prompt: "A cinematic product photo of a glass lamp on a marble table",
      source_uri: "https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/beeble/switchx \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"alpha_mode\": \"auto\", \"generation_type\": \"image\", \"max_resolution\": 720, \"prompt\": \"A cinematic product photo of a glass lamp on a marble table\", \"source_uri\": \"https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/beeble/switchx/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "beeble/switchx",
                {
                    "alpha_mode": "auto",
                    "generation_type": "image",
                    "max_resolution": 720,
                    "prompt": "A cinematic product photo of a glass lamp on a marble table",
                    "source_uri": "https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
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
    const handle = await comfy.models.submit("beeble/switchx", {
      alpha_mode: "auto",
      generation_type: "image",
      max_resolution: 720,
      prompt: "A cinematic product photo of a glass lamp on a marble table",
      source_uri: "https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/beeble/switchx/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"alpha_mode\": \"auto\", \"generation_type\": \"image\", \"max_resolution\": 720, \"prompt\": \"A cinematic product photo of a glass lamp on a marble table\", \"source_uri\": \"https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/beeble/switchx/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/beeble/switchx/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

alpha_mode

string

requerido

Modo alfa: auto, fill, custom o selectValores posibles: `auto`, `fill`, `custom`, `select`

​

alpha_uri

string

URI de una máscara alfa personalizada. Requerido cuando alpha_mode es custom o select. Se ignora para auto o fill.

​

callback_url

string

URL HTTPS para la notificación por webhook al completarse o fallar.

​

generation_type

string

requerido

Tipo de salida: image o videoValores posibles: `image`, `video`

​

idempotency_key

string

Clave de idempotencia para reintentos seguros. Si ya existe una tarea con la misma clave en tu cuenta, la API devuelve el estado de la tarea existente en lugar de crear un duplicado.

​

max_resolution

integer

predeterminado:"1080"

Resolución máxima de salida: 720 o 1080 (predeterminado: 1080).

​

prompt

string

Descripción de texto del resultado deseado (máx. 2,000 caracteres). Se requiere al menos uno de prompt o reference_image_uri.

​

reference_image_uri

string

URI de la imagen de referencia para la transferencia de estilo. Acepta los mismos tipos de URI que source_uri.

​

source_uri

string

requerido

URI de la imagen o el video de origen. Acepta beeble://uploads/{id}/{filename}, URL https o URI data:{mime};base64 (máx. 50 MB).

Generado a partir del esquema que Router sirve en `GET /v2/models/beeble/switchx/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

alpha_mode

string

auto, fill, custom o select

​

completed_at

string

Marca de tiempo ISO 8601 de cuándo se completó o falló la tarea.

​

created_at

string

Marca de tiempo ISO 8601 de cuándo se creó la tarea.

​

error

string

Mensaje de error (presente cuando el estado es failed).

​

generation_type

string

image o video

​

id

string

requerido

Identificador de la tarea (swx_…)

​

modified_at

string

Marca de tiempo ISO 8601 del último cambio de estado.

​

output

object

URL firmadas de las salidas de la tarea de SwitchX.

​

output.alpha

string

URL de la máscara alfa.

​

output.render

string

URL de la salida compuesta.

​

output.source

string

URL de la fuente preprocesada.

​

progress

integer

Porcentaje de progreso (0-100).

​

status

string

requerido

Estado actual de la tarea.Valores posibles: `in_queue`, `processing`, `completed`, `failed`

​

webhook

object

Estado de entrega del webhook de una tarea de SwitchX.

​

webhook.attempts

integer

Número de intentos de entrega realizados hasta ahora.

​

webhook.last_error

string

Mensaje de error del último intento de entrega fallido.

​

webhook.status

string

pending, delivered o failed

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "alpha_mode": "auto",
      "generation_type": "image",
      "max_resolution": 720,
      "prompt": "A cinematic product photo of a glass lamp on a marble table",
      "source_uri": "https://img.freepik.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80"
    }
    

### 

​

Salida
    
    
    {
      "alpha_mode": "auto",
      "completed_at": "2027-01-01T00:01:04Z",
      "created_at": "2027-01-01T00:00:00Z",
      "generation_type": "image",
      "id": "swx_1a2b3c4d5e6f7a8b",
      "modified_at": "2027-01-01T00:01:04Z",
      "output": {
        "alpha": "https://example.invalid/beeble/switchx/alpha.png",
        "render": "https://example.invalid/beeble/switchx/render.png",
        "source": "https://example.invalid/beeble/switchx/source.png"
      },
      "progress": 100,
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/beeble/switchx/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/beeble/switchx/code)

[Claude Sonnet 5](https://docs.comfy.org/es/development/comfy-router/models/anthropic/claude-sonnet-5/code)[Erase V1](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/erase-v1/code)
