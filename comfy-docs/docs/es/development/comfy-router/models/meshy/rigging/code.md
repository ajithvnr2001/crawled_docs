---
url: https://docs.comfy.org/es/development/comfy-router/models/meshy/rigging/code/
title: Usa Rigging con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:11.634003+00:00
---

# Usa Rigging con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/meshy/rigging/code/

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



Meshy

# Usa Rigging con Comfy Router

Copiar páginaCopiar página

Llama a meshy/rigging con Comfy Router: endpoint, forma de la solicitud y respuesta del Router.

Copiar páginaCopiar página

Referencia de la API para `meshy/rigging`, servida por Comfy Router desde Meshy. **Entrada:** 3D · **Salida:** 3D

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `meshy/rigging` **Endpoint:** `POST https://api.comfy.org/v2/models/meshy/rigging`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    with Comfy() as client:
        result = client.models.run(
            "meshy/rigging",
            {
                "height_meters": 1.8,
                "input_task_id": "0193abcd-0000-0000-0000-000000000000",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("meshy/rigging", {
      height_meters: 1.8,
      input_task_id: "0193abcd-0000-0000-0000-000000000000",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/meshy/rigging \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"height_meters\": 1.8, \"input_task_id\": \"0193abcd-0000-0000-0000-000000000000\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/meshy/rigging/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Reads COMFY_API_KEY from the environment.
    # Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "meshy/rigging",
                {
                    "height_meters": 1.8,
                    "input_task_id": "0193abcd-0000-0000-0000-000000000000",
                },
            )
            print("request_id:", handle.request_id)  # with the model ID, all another process needs
    
            # Poll until the request completes, waiting the Retry-After the server names.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # The provider's own payload, the same value models.run() returns.
            # A request that failed or was cancelled raises the typed Router error here.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    const handle = await comfy.models.submit("meshy/rigging", {
      height_meters: 1.8,
      input_task_id: "0193abcd-0000-0000-0000-000000000000",
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/meshy/rigging/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"height_meters\": 1.8, \"input_task_id\": \"0193abcd-0000-0000-0000-000000000000\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/meshy/rigging/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/meshy/rigging/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

height_meters

number

predeterminado:"1.7"

La altura aproximada del modelo de personaje en metros. Debe ser un número positivo.Rango: `0` a `…`

​

input_task_id

string

La tarea de entrada que necesita rigging. Requerido si no se proporciona `model_url`.

​

model_url

string

Una URL o Data URI de acceso público a un archivo GLB humanoide con textura. Requerido si no se proporciona `input_task_id`.

​

texture_image_url

string

La imagen de textura de color base del modelo con UV desplegado. URL o Data URI de acceso público. Admite formato .png.

Generado a partir del esquema que Router publica en `GET /v2/models/meshy/rigging/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

created_at

integer

Marca de tiempo de creación de la tarea, en milisegundos.Formato: `int64`

​

expires_at

integer

Marca de tiempo de expiración del resultado de la tarea, en milisegundos.Formato: `int64`

​

finished_at

integer

Marca de tiempo de finalización de la tarea, en milisegundos. 0 si no ha finalizado.Formato: `int64`

​

id

string

requerido

Identificador único de la tarea.

​

preceding_tasks

integer

El número de tareas precedentes. Solo es relevante cuando el estado es PENDING.

​

progress

integer

Progreso de la tarea (0-100). 0 si no ha comenzado, 100 si se completó correctamente.Rango: `0` a `100`

​

result

object

Contiene las URL de los recursos de salida si la tarea finalizó con estado SUCCEEDED.

​

result.basic_animations

object

Contiene las URL de las animaciones predeterminadas.

​

result.basic_animations.running_armature_glb_url

string

URL descargable del esqueleto de la animación de carrera en formato GLB.

​

result.basic_animations.running_fbx_url

string

URL descargable de la animación de carrera en formato FBX (con piel).

​

result.basic_animations.running_glb_url

string

URL descargable de la animación de carrera en formato GLB (con piel).

​

result.basic_animations.walking_armature_glb_url

string

URL descargable del esqueleto de la animación de caminata en formato GLB.

​

result.basic_animations.walking_fbx_url

string

URL descargable de la animación de caminata en formato FBX (con piel).

​

result.basic_animations.walking_glb_url

string

URL descargable de la animación de caminata en formato GLB (con piel).

​

result.rigged_character_fbx_url

string

URL descargable del personaje con rigging en formato FBX.

​

result.rigged_character_glb_url

string

URL descargable del personaje con rigging en formato GLB.

​

started_at

integer

Marca de tiempo de inicio de la tarea, en milisegundos. 0 si no ha comenzado.Formato: `int64`

​

status

string

requerido

Valores posibles: `SUCCEEDED`

​

task_error

object

Objeto de error que contiene el mensaje de error si la tarea falló.

​

task_error.message

string

Mensaje de error detallado.

​

type

string

Tipo de la tarea de Rigging.Valores posibles: `rig`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "height_meters": 1.8,
      "input_task_id": "0193abcd-0000-0000-0000-000000000000"
    }
    

### 

​

Salida
    
    
    {
      "created_at": 1767225600000,
      "expires_at": 1767830400000,
      "finished_at": 1767225712000,
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "progress": 100,
      "result": {
        "basic_animations": {
          "running_glb_url": "https://example.invalid/meshy/rigging/running.glb",
          "walking_glb_url": "https://example.invalid/meshy/rigging/walking.glb"
        },
        "rigged_character_fbx_url": "https://example.invalid/meshy/rigging/character.fbx",
        "rigged_character_glb_url": "https://example.invalid/meshy/rigging/character.glb"
      },
      "started_at": 1767225601000,
      "status": "SUCCEEDED",
      "type": "rig"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/meshy/rigging/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/meshy/rigging/code)

[Remesh](https://docs.comfy.org/es/development/comfy-router/models/meshy/remesh/code)[MiniMax H3](https://docs.comfy.org/es/development/comfy-router/models/minimax/minimax-h3/code)
