---
url: https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/video-edit-v1/code/
title: Usa Video Edit V1 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:57.281438+00:00
---

# Usa Video Edit V1 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/video-edit-v1/code/

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



Black Forest Labs

# Usa Video Edit V1 con Comfy Router

Copiar páginaCopiar página

Llama a bfl/video-edit-v1 desde Comfy Router: endpoint, forma de la solicitud y respuesta del Router.

Copiar páginaCopiar página

Referencia de API para `bfl/video-edit-v1`, servida por Comfy Router de Black Forest Labs. **Entrada:** Video, Texto · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `bfl/video-edit-v1` **Endpoint:** `POST https://api.comfy.org/v2/models/bfl/video-edit-v1`

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
            "bfl/video-edit-v1",
            {
                "prompt": "Remove the orange bucket.",
                "video": "https://example.com/clip.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("bfl/video-edit-v1", {
      prompt: "Remove the orange bucket.",
      video: "https://example.com/clip.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/bfl/video-edit-v1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"Remove the orange bucket.\", \"video\": \"https://example.com/clip.mp4\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/bfl/video-edit-v1/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge una vez que está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "bfl/video-edit-v1",
                {
                    "prompt": "Remove the orange bucket.",
                    "video": "https://example.com/clip.mp4",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que otro proceso necesita
    
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
    const handle = await comfy.models.submit("bfl/video-edit-v1", {
      prompt: "Remove the orange bucket.",
      video: "https://example.com/clip.mp4",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/bfl/video-edit-v1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"Remove the orange bucket.\", \"video\": \"https://example.com/clip.mp4\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bfl/video-edit-v1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/bfl/video-edit-v1/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

prompt

string

requerido

Instrucción de edición. Nombra los objetos, el escenario, el estilo, el texto en pantalla o el diálogo que hay que cambiar; todo lo que no se nombra se conserva.

​

safety_tolerance

integer

predeterminado:"2"

Nivel de tolerancia para la moderación de la entrada y de la salida, donde 0 es el más estricto.Rango: `0` a `4`

​

video

string

requerido

Video a editar, ya sea una URL HTTP(S) o un MP4 codificado en base64. El material de origen puede durar como máximo 15 segundos y pesar 50 MiB, y cada lado debe medir al menos 160 píxeles; las fuentes de más de 720p se reducen a 720p.

Generado a partir del esquema que Router publica en `GET /v2/models/bfl/video-edit-v1/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

cost

number

Costo informado por el proveedor en créditos, que se completa en cuanto la tarea está en estado Ready.Formato: `float`

​

id

string

requerido

Identificador de la tarea de BFL.

​

progress

number

Progreso de generación opcional informado por BFL.Rango: `0` a `1`Formato: `float`

​

result

object

requerido

La generación finalizada. Aquí no puede ser null: la entrada `required` de este componente es la promesa de que un `200` trae el resultado, y un `result` que admitiera null la reduciría a una simple comprobación de presencia de la clave.

​

result.cost

number

Costo de la generación informado por el proveedor. Es la cifra de BFL, no el cargo de Comfy.Formato: `double`

​

result.duration

number

Duración de la generación informada por el proveedor, en segundos.Formato: `double`

​

result.end_time

number

Hora de finalización de la generación informada por el proveedor, en segundos desde la época Unix. `double` por la misma razón que `start_time`.Formato: `double`

​

result.prompt

string

El prompt con el que realmente se ejecutó la generación, después de cualquier upsampling de prompt.

​

result.sample

string (uri)

URL firmada del recurso generado. Router vuelve a alojar el recurso en el almacenamiento de Comfy y reescribe este campo, así que normalmente es una URL alojada en Comfy válida por un máximo de 24 horas: se firma por 24 horas al emitirse y se reproduce desde una memoización de 23 horas, por lo que una consulta posterior puede devolver una a la que le queda tan solo una hora. En cambio, una hoja cuyo realojamiento no se pudo realizar conserva la propia URL de entrega de corta duración de BFL, de unas dos horas para video y unos diez minutos para imágenes. En cualquier caso, el enlace caduca, así que descarga el recurso en lugar de guardar la URL.Formato: `uri`

​

result.seed

integer

La semilla que usó la generación, ya sea aportada o elegida por el proveedor. Se declara `int64` porque BFL devuelve semillas por encima de 2^31 (por ejemplo, 2784347701), que un `integer` sin formato genera como un campo de 32 bits en muchos generadores de SDK.Formato: `int64`

​

result.start_time

number

Hora de inicio de la generación informada por el proveedor, en segundos desde la época Unix. `double`, no `float`: el espaciado de float32 cerca de un valor de época actual es de ~128 segundos, lo que colapsa el lapso de toda una generación en un único valor decodificado.Formato: `double`

​

status

string

requerido

Estado de la tarea: Pending, Reasoning, Generating, Ready, Request Moderated, Content Moderated, Error o Task not found.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "prompt": "Remove the orange bucket.",
      "video": "https://example.com/clip.mp4"
    }
    

### 

​

Salida
    
    
    {
      "cost": null,
      "id": "b2e0c1a4-0f2f-4a55-9f2e-2f9a1c0d4e77",
      "progress": null,
      "result": {
        "cost": null,
        "duration": 3.4,
        "end_time": 1767225603.4,
        "prompt": "A watercolor painting of a lighthouse at dawn, soft light on the water",
        "sample": "https://example.invalid/bfl/flux-pro-1.1/sample.png",
        "seed": 2784347701,
        "start_time": 1767225600
      },
      "status": "Ready"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/black-forest-labs/video-edit-v1/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/black-forest-labs/video-edit-v1/code)

[FLUX Video Upscale](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-video-upscale/code)[VTO V1](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/vto-v1/code)
