---
url: https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-2-max/code/
title: Usa FLUX 2 Max con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:56.683574+00:00
---

# Usa FLUX 2 Max con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-2-max/code/

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

# Usa FLUX 2 Max con Comfy Router

Copiar páginaCopiar página

Llama a bfl/flux-2-max mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `bfl/flux-2-max`, servida por Comfy Router de Black Forest Labs. **Entrada:** Texto, Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `bfl/flux-2-max` **Endpoint:** `POST https://api.comfy.org/v2/models/bfl/flux-2-max`

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
            "bfl/flux-2-max",
            {
                "prompt": "A single red maple leaf on a plain white background.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("bfl/flux-2-max", {
      prompt: "A single red maple leaf on a plain white background.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/bfl/flux-2-max \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A single red maple leaf on a plain white background.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/bfl/flux-2-max/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "bfl/flux-2-max",
                {
                    "prompt": "A single red maple leaf on a plain white background.",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
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
    const handle = await comfy.models.submit("bfl/flux-2-max", {
      prompt: "A single red maple leaf on a plain white background.",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/bfl/flux-2-max/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A single red maple leaf on a plain white background.\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bfl/flux-2-max/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/bfl/flux-2-max/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

height

integer

predeterminado:"1024"

Alto de la imagen.Rango: `256` a `2048`

​

input_image

string

Imagen codificada en Base64 para generación de imagen a imagen.

​

input_image_2

string

Imagen codificada en Base64 para generación de imagen a imagen.

​

input_image_3

string

Imagen codificada en Base64 para generación de imagen a imagen.

​

input_image_4

string

Imagen codificada en Base64 para generación de imagen a imagen.

​

input_image_5

string

Imagen codificada en Base64 para generación de imagen a imagen.

​

input_image_6

string

Imagen codificada en Base64 para generación de imagen a imagen.

​

input_image_7

string

Imagen codificada en Base64 para generación de imagen a imagen.

​

input_image_8

string

Imagen codificada en Base64 para generación de imagen a imagen.

​

input_image_9

string

Imagen codificada en Base64 para generación de imagen a imagen.

​

output_format

string

predeterminado:"\"jpeg\""

Formato de salida de la imagen generada.Valores posibles: `jpeg`, `png`

​

prompt

string

requerido

Descripción de texto de la imagen que se va a generar.

​

prompt_upsampling

boolean

predeterminado:"true"

Modifica automáticamente el prompt para la generación.

​

safety_tolerance

integer

predeterminado:"2"

Nivel de tolerancia de moderación (solo Flux 2 Max).Rango: `0` a `5`

​

seed

integer

Semilla para la reproducibilidad.

​

width

integer

predeterminado:"1024"

Ancho de la imagen.Rango: `256` a `2048`

Generado a partir del esquema que Router sirve en `GET /v2/models/bfl/flux-2-max/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

cost

number

Costo informado por el proveedor, en créditos, que se completa cuando la tarea está Ready.Formato: `float`

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

La generación finalizada. Aquí no admite nulos: la entrada `required` de este componente es la promesa de que un `200` trae el resultado, y un `result` que admita nulos lo reduciría a una simple comprobación de presencia de clave.

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

El prompt que la generación ejecutó realmente, después de aplicar cualquier upsampling al prompt.

​

result.sample

string (uri)

URL firmada del recurso generado. Router vuelve a alojar el recurso en el almacenamiento de Comfy y reescribe este campo, así que normalmente es una URL alojada en Comfy válida hasta 24 horas: se firma por 24 horas al emitirse y se reproduce desde una memo de 23 horas, por lo que una consulta posterior puede devolver una a la que le queda tan solo una hora de vigencia; una hoja cuyo re-alojamiento no se pudo realizar conserva en su lugar la URL de entrega de corta duración de BFL: unas dos horas para video y unos diez minutos para imágenes. En cualquier caso el enlace caduca, así que descarga el recurso en lugar de guardar la URL.Formato: `uri`

​

result.seed

integer

La semilla que usó la generación, ya sea proporcionada o elegida por el proveedor. Se declara `int64` porque BFL devuelve semillas por encima de 2^31 (por ejemplo, 2784347701), que un `integer` sin formato genera como un campo de 32 bits en muchos generadores de SDK.Formato: `int64`

​

result.start_time

number

Hora de inicio de la generación informada por el proveedor, en segundos desde la época Unix. `double`, no `float`: el espaciado de float32 cerca de un valor de época actual es de ~128 segundos, lo que colapsa todo el intervalo de una generación a un único valor decodificado.Formato: `double`

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
      "prompt": "A single red maple leaf on a plain white background."
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/black-forest-labs/flux-2-max/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/black-forest-labs/flux-2-max/code)

[FLUX.1 Kontext](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-1-kontext/code)[FLUX 2 Pro](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-2-pro/code)
