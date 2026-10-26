---
url: https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-video-upscale/code/
title: Usa FLUX Video Upscale con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:57.179418+00:00
---

# Usa FLUX Video Upscale con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-video-upscale/code/

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

# Usa FLUX Video Upscale con Comfy Router

Copiar páginaCopiar página

Fragmentos de Python, TypeScript y cURL para ampliar un video con FLUX Video Upscale mediante Comfy Router, más los campos de solicitud y la forma del resultado.

Copiar páginaCopiar página

Referencia de API para FLUX Video Upscale. FLUX Video Upscale es el ampliador de video de Black Forest Labs: envía un video y recibes una versión con mayor resolución. **Entrada:** Video · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada con HTTP directo. **ID del modelo:** `bfl/video-upscale-v1` **Endpoint:** `POST https://api.comfy.org/v2/models/bfl/video-upscale-v1`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY desde el entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "bfl/video-upscale-v1",
                {
                    "input_video": "https://your-host.example/clip.mp4",
                    "upscale_factor": 2,
                    "creativity": 1,
                },
            )
    
        print("video:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY desde el entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    type Result = { result: { sample: string } };
    const result = await comfy.models.run<Result>("bfl/video-upscale-v1", {
      input_video: "https://your-host.example/clip.mp4",
      upscale_factor: 2,
      creativity: 1,
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("video:", result.data.result.sample);
    
    
    
    curl https://api.comfy.org/v2/models/bfl/video-upscale-v1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input_video\": \"https://your-host.example/clip.mp4\", \"upscale_factor\": 2, \"creativity\": 1}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/bfl/video-upscale-v1/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY desde el entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "bfl/video-upscale-v1",
                {
                    "input_video": "https://your-host.example/clip.mp4",
                    "upscale_factor": 2,
                    "creativity": 1,
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta periódicamente hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló genera aquí el error tipado de Router.
            result = await handle.get()
    
        print("video:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY desde el entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    type Result = { result: { sample: string } };
    const handle = await comfy.models.submit<Result>("bfl/video-upscale-v1", {
      input_video: "https://your-host.example/clip.mp4",
      upscale_factor: 2,
      creativity: 1,
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta periódicamente hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló genera aquí un rechazo.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("video:", result.data.result.sample);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/bfl/video-upscale-v1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input_video\": \"https://your-host.example/clip.mp4\", \"upscale_factor\": 2, \"creativity\": 1}"
    
    # 2. Consulta periódicamente hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bfl/video-upscale-v1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/bfl/video-upscale-v1/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

creativity

integer

predeterminado:"1"

0 conserva la fuente con precisión y la hace más nítida; 1 permite una mejora creativa del detalle, que no preserva estrictamente los rostros ni los productos.Rango: `0` a `1`

​

input_video

string

requerido

Video a escalar, ya sea una URL HTTP(S) o un MP4 codificado en base64. Como máximo 20 segundos de material de origen y 50MB.

​

prompt

string

Descripción opcional del contenido del clip, que orienta el detalle mejorado. Déjala vacía para un escalado neutro.

​

safety_tolerance

integer

predeterminado:"2"

Nivel de tolerancia para la moderación del prompt y de los fotogramas de salida, donde 0 es el más estricto.Rango: `0` a `4`

​

upscale_factor

number

predeterminado:"2"

Escalado de salida en relación con la resolución de origen. La salida conserva la relación de aspecto de la fuente y está limitada a unos 14.4 megapíxeles por fotograma, así que las fuentes muy grandes se escalan por menos del factor solicitado.Rango: `1.5` a `3`Formato: `float`

​

webhook_secret

string

Secreto opcional para la verificación de la firma del webhook.

​

webhook_url

string (uri)

URL que recibe las notificaciones del webhook.Formato: `uri`

Generado a partir del esquema que Router sirve en `GET /v2/models/bfl/video-upscale-v1/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

cost

number

Costo en créditos informado por el proveedor, disponible una vez que la tarea está en estado Listo.Formato: `float`

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

La generación finalizada. Aquí no admite nulos: la entrada `required` de este componente es la promesa de que un `200` trae el resultado, y un `result` que admitiera nulos lo reduciría a una comprobación de presencia de la clave.

​

result.cost

number

Costo de la generación informado por el proveedor. Es la cifra de BFL, no el cargo de Comfy.Formato: `double`

​

result.duration

number

Duración de la generación en segundos, informada por el proveedor.Formato: `double`

​

result.end_time

number

Hora de finalización de la generación informada por el proveedor, en segundos desde la época Unix. Es `double` por la misma razón que `start_time`.Formato: `double`

​

result.prompt

string

El prompt con el que realmente se ejecutó la generación, después de cualquier aumento del prompt.

​

result.sample

string (uri)

URL firmada del recurso generado. Router vuelve a alojar el recurso en el almacenamiento de Comfy y reescribe este campo, así que normalmente es una URL alojada en Comfy válida hasta 24 horas: firmada por 24 horas al generarse y reproducida desde una memoria de 23 horas, de modo que una consulta posterior puede devolver una a la que le quede tan solo una hora; una hoja cuyo re-alojamiento no se pudo realizar conserva en su lugar la URL de entrega de corta duración de BFL, de unas dos horas para video y unos diez minutos para imágenes. En cualquier caso el enlace caduca, así que descarga el recurso en lugar de guardar la URL.Formato: `uri`

​

result.seed

integer

La semilla que usó la generación, ya sea proporcionada o elegida por el proveedor. Se declara como `int64` porque BFL devuelve semillas por encima de 2^31 (por ejemplo, 2784347701), que un `integer` sin formato genera como un campo de 32 bits en muchos generadores de SDK.Formato: `int64`

​

result.start_time

number

Hora de inicio de la generación informada por el proveedor, en segundos desde la época Unix. Es `double`, no `float`: el espaciado de float32 cerca de un valor de época actual es de ~128 segundos, lo que colapsa todo el intervalo de una generación en un único valor decodificado.Formato: `double`

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
      "input_video": "https://your-host.example/clip.mp4",
      "upscale_factor": 2,
      "creativity": 1
    }
    

### 

​

Salida
    
    
    {
      "id": "0a1b2c3d-...",
      "status": "Ready",
      "result": {
        "sample": "https://.../upscaled.mp4"
      }
    }
    

`result.sample` suele ser una URL firmada alojada por Comfy, válida hasta 24 horas desde su creación. Una repetición puede devolver una URL más antigua, y un recurso que no se pudo volver a alojar conserva su URL del proveedor, que tiene una vigencia más corta. Descarga el MP4 de inmediato en lugar de almacenar el enlace.

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/black-forest-labs/flux-video-upscale/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/black-forest-labs/flux-video-upscale/code)

[FLUX Pro 1.0 Fill](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-pro-1-0-fill/code)[Video Edit V1](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/video-edit-v1/code)
