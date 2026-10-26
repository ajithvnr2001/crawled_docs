---
url: https://docs.comfy.org/es/development/comfy-router/models/luma/ray-flash-2/code/
title: Usa Ray Flash 2 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:09.932536+00:00
---

# Usa Ray Flash 2 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/luma/ray-flash-2/code/

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



Luma

# Usa Ray Flash 2 con Comfy Router

Copiar páginaCopiar página

Llama a luma/ray-flash-2 con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `luma/ray-flash-2`, servida por Comfy Router desde Luma. **Entrada:** Texto, Imagen · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `luma/ray-flash-2` **Endpoint:** `POST https://api.comfy.org/v2/models/luma/ray-flash-2`

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
            "luma/ray-flash-2",
            {
                "aspect_ratio": "16:9",
                "duration": "5s",
                "prompt": "a single red maple leaf resting on a plain white background",
                "resolution": "540p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("luma/ray-flash-2", {
      aspect_ratio: "16:9",
      duration: "5s",
      prompt: "a single red maple leaf resting on a plain white background",
      resolution: "540p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/luma/ray-flash-2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5s\", \"prompt\": \"a single red maple leaf resting on a plain white background\", \"resolution\": \"540p\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/luma/ray-flash-2/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "luma/ray-flash-2",
                {
                    "aspect_ratio": "16:9",
                    "duration": "5s",
                    "prompt": "a single red maple leaf resting on a plain white background",
                    "resolution": "540p",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
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
    const handle = await comfy.models.submit("luma/ray-flash-2", {
      aspect_ratio: "16:9",
      duration: "5s",
      prompt: "a single red maple leaf resting on a plain white background",
      resolution: "540p",
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
    curl https://api.comfy.org/v2/models/luma/ray-flash-2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"duration\": \"5s\", \"prompt\": \"a single red maple leaf resting on a plain white background\", \"resolution\": \"540p\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/luma/ray-flash-2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/luma/ray-flash-2/requests/$REQUEST_ID \
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

requerido

La relación de aspecto de la generaciónValores posibles: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `21:9`, `9:21`

​

callback_url

string (uri)

La URL de callback de la generación. Se enviará una solicitud POST con el objeto Generation a la URL de callback cuando la generación esté en proceso, se haya completado o haya falladoFormato: `uri`

​

duration

`5s`, `9s` | string

requerido

​

generation_type

string

predeterminado:"\"video\""

Valores posibles: `video`

​

keyframes

object

Los fotogramas clave de la generación

​

keyframes.frame0

object

Un fotograma clave puede ser una referencia a Generation, una imagen o un video

​

keyframes.frame1

object

Un fotograma clave puede ser una referencia a Generation, una imagen o un video

​

loop

boolean

Indica si el video se repite en bucle

​

model

string

El modelo de video utilizado para la generación. En la ruta de Comfy Router `POST /v2/models/luma/{model}` este campo se obtiene de la ruta y NO DEBE enviarse; en la ruta v1 `POST /proxy/luma/generations` es requerido y está restringido a la enumeración LumaVideoModel (`ray-2`, `ray-flash-2`).

​

prompt

string

requerido

El prompt de la generación

​

resolution

`540p`, `720p`, `1080p`, `4k` | string

requerido

Generado a partir del esquema que Router sirve en `GET /v2/models/luma/ray-flash-2/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

assets

object

Los recursos de la generación

​

assets.image

string (uri)

La URL de la imagenFormato: `uri`

​

assets.progress_video

string (uri)

La URL del video de progresoFormato: `uri`

​

assets.video

string (uri)

La URL del videoFormato: `uri`

​

created_at

string (date-time)

La fecha y hora en que se creó la generaciónFormato: `date-time`

​

failure_reason

string

El motivo del estado de la generación

​

generation_type

string

Valores posibles: `video`, `image`

​

id

string (uuid)

El ID de la generaciónFormato: `uuid`

​

model

string

El modelo utilizado para la generación

​

request

object

La solicitud de la generación

​

state

string

El estado de la generaciónValores posibles: `queued`, `dreaming`, `completed`, `failed`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "aspect_ratio": "16:9",
      "duration": "5s",
      "prompt": "a single red maple leaf resting on a plain white background",
      "resolution": "540p"
    }
    

### 

​

Salida
    
    
    {
      "assets": {
        "video": "https://example.invalid/luma/ray-flash-2/generated.mp4"
      },
      "created_at": "2027-01-01T00:00:00Z",
      "generation_type": "video",
      "id": "8c41d0b6-2e7a-4f35-b1d8-9a0e6f3c2b71",
      "model": "ray-flash-2",
      "state": "completed"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/luma/ray-flash-2/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/luma/ray-flash-2/code)

[Ray 2](https://docs.comfy.org/es/development/comfy-router/models/luma/ray-2/code)[Ray 3.2](https://docs.comfy.org/es/development/comfy-router/models/luma_2/ray-3-2/code)
