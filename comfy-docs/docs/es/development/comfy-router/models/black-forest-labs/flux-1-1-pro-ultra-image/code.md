---
url: https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-1-1-pro-ultra-image/code/
title: Usa Flux 1.1 Pro Ultra Image con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:55.855157+00:00
---

# Usa Flux 1.1 Pro Ultra Image con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-1-1-pro-ultra-image/code/

## En esta página

Volver arriba

  * Inicio rápido
  * Antes de lanzar



Black Forest Labs

# Usa Flux 1.1 Pro Ultra Image con Comfy Router

Copiar páginaCopiar página

Ejemplos en Python, TypeScript y cURL para llamar a FLUX 1.1 [pro] Ultra y FLUX 1.1 [pro] vía Comfy Router, con campos y estructura del resultado

Copiar páginaCopiar página

API Reference for Flux 1.1 Pro Ultra Image. FLUX 1.1 [pro] es un modelo de texto a imagen de Black Forest Labs. El modo Ultra genera imágenes de hasta 4MP de resolución. **Entrada:** Texto, Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. Elige el modelo que quieres llamar. Todo lo que sigue, desde los fragmentos hasta el esquema y los ejemplos, depende de tu elección.

  * FLUX 1.1 [pro] Ultra

  * FLUX 1.1 [pro]




**ID del modelo:** `bfl/flux-pro-1.1-ultra`**Endpoint:** `POST https://api.comfy.org/v2/models/bfl/flux-pro-1.1-ultra`

  * Esperar el resultado

  * Poner en cola y recoger después




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "bfl/flux-pro-1.1-ultra",
                {
                    "prompt": "a single red maple leaf on a plain white background, studio lighting",
                    "aspect_ratio": "16:9",
                    "raw": False,
                },
            )
    
        print("image:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    type Result = { result: { sample: string } };
    const result = await comfy.models.run<Result>("bfl/flux-pro-1.1-ultra", {
      prompt: "a single red maple leaf on a plain white background, studio lighting",
      aspect_ratio: "16:9",
      raw: false,
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.result.sample);
    
    
    
    curl https://api.comfy.org/v2/models/bfl/flux-pro-1.1-ultra \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a single red maple leaf on a plain white background, studio lighting\", \"aspect_ratio\": \"16:9\", \"raw\": false}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/bfl/flux-pro-1.1-ultra/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "bfl/flux-pro-1.1-ultra",
                {
                    "prompt": "a single red maple leaf on a plain white background, studio lighting",
                    "aspect_ratio": "16:9",
                    "raw": False,
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil del propio proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print("image:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    type Result = { result: { sample: string } };
    const handle = await comfy.models.submit<Result>("bfl/flux-pro-1.1-ultra", {
      prompt: "a single red maple leaf on a plain white background, studio lighting",
      aspect_ratio: "16:9",
      raw: false,
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.result.sample);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/bfl/flux-pro-1.1-ultra/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a single red maple leaf on a plain white background, studio lighting\", \"aspect_ratio\": \"16:9\", \"raw\": false}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bfl/flux-pro-1.1-ultra/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/bfl/flux-pro-1.1-ultra/requests/$REQUEST_ID \
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

Relación de aspecto de la imagen, entre 21:9 y 9:21; por ejemplo, 16:9.

​

image_prompt

string

Imagen opcional codificada en base64 para hacer un remix.

​

image_prompt_strength

number

predeterminado:"0.1"

Mezcla entre el prompt y el image prompt, de 0 (solo el prompt) a 1 (solo el image prompt).Rango: `0` a `1`

​

output_format

string

predeterminado:"\"jpeg\""

Formato de la imagen de salida.Valores posibles: `jpeg`, `png`, `webp`

​

prompt

string

requerido

Prompt de texto para la generación de la imagen.

​

prompt_upsampling

boolean

predeterminado:"false"

Indica si se aplica upsampling al prompt. Si está activo, el prompt se modifica automáticamente para una generación más creativa.

​

raw

boolean

predeterminado:"false"

Genera imágenes con menos procesamiento y un aspecto más natural.

​

safety_tolerance

integer

predeterminado:"2"

Nivel de tolerancia para la moderación de entrada y salida, entre 0 (el más estricto) y 6 (el menos estricto).Rango: `0` a `6`

​

seed

integer

Semilla opcional para reproducibilidad. Si se omite, se usa una semilla aleatoria.

​

webhook_secret

string

Secreto opcional para la verificación de la firma del webhook.

​

webhook_url

string (uri)

URL que recibe las notificaciones del webhook.Formato: `uri`

Generado a partir del esquema que Router sirve en `GET /v2/models/bfl/flux-pro-1.1-ultra/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

cost

number

Costo informado por el proveedor, en créditos, que se completa cuando la tarea pasa a Ready.Formato: `float`

​

id

string

requerido

Identificador de la tarea de BFL.

​

progress

number

Progreso de la generación notificado por BFL, opcional.Rango: `0` a `1`Formato: `float`

​

result

object

requerido

La generación finalizada. Aquí no admite nulos: la entrada `required` de este componente es una promesa de que un `200` lleva el resultado, y un `result` que admitiera nulos lo reduciría a una simple comprobación de presencia de clave.

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

Hora de finalización de la generación informada por el proveedor, en segundos desde la época Unix. `double` por la misma razón que `start_time`.Formato: `double`

​

result.prompt

string

El prompt con el que realmente se ejecutó la generación, después de cualquier upsampling del prompt.

​

result.sample

string (uri)

URL firmada del recurso generado. Router vuelve a alojar el recurso en el almacenamiento de Comfy y reescribe este campo, así que normalmente es una URL alojada en Comfy válida hasta 24 horas: se firma por 24 horas al generarse y se reproduce desde una memo de 23 horas, de modo que una consulta posterior puede devolver una con tan solo una hora de vigencia; un leaf cuyo realojamiento no se pudo realizar conserva en su lugar la URL de entrega de corta duración de BFL: unas dos horas para video y unos diez minutos para imágenes. En cualquier caso el enlace caduca, así que descarga el recurso en lugar de guardar la URL.Formato: `uri`

​

result.seed

integer

La semilla que usó la generación, ya sea proporcionada o elegida por el proveedor. Se declara como `int64` porque BFL devuelve semillas superiores a 2^31 (por ejemplo, 2784347701), que un `integer` sin formato genera como un campo de 32 bits en muchos generadores de SDK.Formato: `int64`

​

result.start_time

number

Hora de inicio de la generación informada por el proveedor, en segundos desde la época Unix. `double`, no `float`: el espaciado de float32 cerca de un valor epoch actual es de ~128 segundos, lo que colapsa el lapso de toda una generación a un único valor decodificado.Formato: `double`

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
      "prompt": "a single red maple leaf on a plain white background, studio lighting",
      "aspect_ratio": "16:9",
      "raw": false
    }
    

### 

​

Salida
    
    
    {
      "id": "0a1b2c3d-...",
      "status": "Ready",
      "result": {
        "sample": "https://.../out.jpeg",
        "prompt": "a single red maple leaf on a plain white background, studio lighting",
        "seed": 1234567890
      }
    }
    

La URL es temporal. Descarga la imagen cuanto antes si necesitas conservarla.

**ID del modelo:** `bfl/flux-pro-1.1`**Endpoint:** `POST https://api.comfy.org/v2/models/bfl/flux-pro-1.1`

  * Esperar el resultado

  * Poner en cola y recoger después




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "bfl/flux-pro-1.1",
                {
                    "prompt": "a single red maple leaf on a plain white background, studio lighting",
                    "width": 1024,
                    "height": 768,
                },
            )
    
        print("image:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    type Result = { result: { sample: string } };
    const result = await comfy.models.run<Result>("bfl/flux-pro-1.1", {
      prompt: "a single red maple leaf on a plain white background, studio lighting",
      width: 1024,
      height: 768,
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.result.sample);
    
    
    
    curl https://api.comfy.org/v2/models/bfl/flux-pro-1.1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a single red maple leaf on a plain white background, studio lighting\", \"width\": 1024, \"height\": 768}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "bfl/flux-pro-1.1",
                {
                    "prompt": "a single red maple leaf on a plain white background, studio lighting",
                    "width": 1024,
                    "height": 768,
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil del propio proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print("image:", result["result"]["sample"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    type Result = { result: { sample: string } };
    const handle = await comfy.models.submit<Result>("bfl/flux-pro-1.1", {
      prompt: "a single red maple leaf on a plain white background, studio lighting",
      width: 1024,
      height: 768,
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("image:", result.data.result.sample);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a single red maple leaf on a plain white background, studio lighting\", \"width\": 1024, \"height\": 768}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/bfl/flux-pro-1.1/requests/$REQUEST_ID \
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

predeterminado:"768"

Alto de la imagen generada en píxeles. Debe ser múltiplo de 32.Rango: `256` a `1440`

​

image_prompt

string

Imagen opcional codificada en base64 para usar con FLUX Redux.

​

output_format

string

predeterminado:"\"jpeg\""

Formato de la imagen de salida.Valores posibles: `jpeg`, `png`, `webp`

​

prompt

string

requerido

Prompt de texto para la generación de la imagen.

​

prompt_upsampling

boolean

predeterminado:"false"

Indica si se aplica upsampling al prompt. Si está activo, el prompt se modifica automáticamente para una generación más creativa.

​

safety_tolerance

integer

predeterminado:"2"

Nivel de tolerancia para la moderación de entrada y salida, entre 0 (el más estricto) y 6 (el menos estricto).Rango: `0` a `6`

​

seed

integer

Semilla opcional para reproducibilidad. Si se omite, se usa una semilla aleatoria.

​

webhook_secret

string

Secreto opcional para la verificación de la firma del webhook.

​

webhook_url

string (uri)

URL que recibe las notificaciones del webhook.Formato: `uri`

​

width

integer

predeterminado:"1024"

Ancho de la imagen generada en píxeles. Debe ser múltiplo de 32.Rango: `256` a `1440`

Generado a partir del esquema que Router sirve en `GET /v2/models/bfl/flux-pro-1.1/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

cost

number

Costo informado por el proveedor, en créditos, que se completa cuando la tarea pasa a Ready.Formato: `float`

​

id

string

requerido

Identificador de la tarea de BFL.

​

progress

number

Progreso de la generación notificado por BFL, opcional.Rango: `0` a `1`Formato: `float`

​

result

object

requerido

La generación finalizada. Aquí no admite nulos: la entrada `required` de este componente es una promesa de que un `200` lleva el resultado, y un `result` que admitiera nulos lo reduciría a una simple comprobación de presencia de clave.

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

Hora de finalización de la generación informada por el proveedor, en segundos desde la época Unix. `double` por la misma razón que `start_time`.Formato: `double`

​

result.prompt

string

El prompt con el que realmente se ejecutó la generación, después de cualquier upsampling del prompt.

​

result.sample

string (uri)

URL firmada del recurso generado. Router vuelve a alojar el recurso en el almacenamiento de Comfy y reescribe este campo, así que normalmente es una URL alojada en Comfy válida hasta 24 horas: se firma por 24 horas al generarse y se reproduce desde una memo de 23 horas, de modo que una consulta posterior puede devolver una con tan solo una hora de vigencia; un leaf cuyo realojamiento no se pudo realizar conserva en su lugar la URL de entrega de corta duración de BFL: unas dos horas para video y unos diez minutos para imágenes. En cualquier caso el enlace caduca, así que descarga el recurso en lugar de guardar la URL.Formato: `uri`

​

result.seed

integer

La semilla que usó la generación, ya sea proporcionada o elegida por el proveedor. Se declara como `int64` porque BFL devuelve semillas superiores a 2^31 (por ejemplo, 2784347701), que un `integer` sin formato genera como un campo de 32 bits en muchos generadores de SDK.Formato: `int64`

​

result.start_time

number

Hora de inicio de la generación informada por el proveedor, en segundos desde la época Unix. `double`, no `float`: el espaciado de float32 cerca de un valor epoch actual es de ~128 segundos, lo que colapsa el lapso de toda una generación a un único valor decodificado.Formato: `double`

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
      "prompt": "a single red maple leaf on a plain white background, studio lighting",
      "width": 1024,
      "height": 768
    }
    

### 

​

Salida
    
    
    {
      "id": "0a1b2c3d-...",
      "status": "Ready",
      "result": {
        "sample": "https://.../out.jpeg",
        "prompt": "a single red maple leaf on a plain white background, studio lighting",
        "seed": 1234567890
      }
    }
    

La URL es temporal. Descarga la imagen cuanto antes si necesitas conservarla.

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/black-forest-labs/flux-1-1-pro-ultra-image/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/black-forest-labs/flux-1-1-pro-ultra-image/code)

[Erase V1](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/erase-v1/code)[FLUX.1 Kontext](https://docs.comfy.org/es/development/comfy-router/models/black-forest-labs/flux-1-kontext/code)
