---
url: https://docs.comfy.org/es/development/comfy-router/models/wan/wan2-5-i2i-preview/code/
title: Usa Wan 2.5 I2I Preview con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:22.737741+00:00
---

# Usa Wan 2.5 I2I Preview con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/wan/wan2-5-i2i-preview/code/

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



Wan

# Usa Wan 2.5 I2I Preview con Comfy Router

Copiar páginaCopiar página

Llama a wan/wan2.5-i2i-preview mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `wan/wan2.5-i2i-preview`, servida por Comfy Router de Wan. **Entrada:** Imagen, Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `wan/wan2.5-i2i-preview` **Endpoint:** `POST https://api.comfy.org/v2/models/wan/wan2.5-i2i-preview`

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
            "wan/wan2.5-i2i-preview",
            {
                "input": {
                    "images": ["https://example.invalid/red-maple-leaf.png"],
                    "prompt": "Make the leaf golden.",
                },
                "parameters": {
                    "n": 1,
                    "size": "768*768",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("wan/wan2.5-i2i-preview", {
      input: {
        images: ["https://example.invalid/red-maple-leaf.png"],
        prompt: "Make the leaf golden.",
      },
      parameters: {
        n: 1,
        size: "768*768",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/wan/wan2.5-i2i-preview \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"images\":[\"https://example.invalid/red-maple-leaf.png\"],\"prompt\":\"Make the leaf golden.\"}, \"parameters\": {\"n\":1,\"size\":\"768*768\"}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/wan/wan2.5-i2i-preview/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) repasa el estado, la cancelación y la recogida.

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
                "wan/wan2.5-i2i-preview",
                {
                    "input": {
                        "images": ["https://example.invalid/red-maple-leaf.png"],
                        "prompt": "Make the leaf golden.",
                    },
                    "parameters": {
                        "n": 1,
                        "size": "768*768",
                    },
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("wan/wan2.5-i2i-preview", {
      input: {
        images: ["https://example.invalid/red-maple-leaf.png"],
        prompt: "Make the leaf golden.",
      },
      parameters: {
        n: 1,
        size: "768*768",
      },
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/wan/wan2.5-i2i-preview/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"images\":[\"https://example.invalid/red-maple-leaf.png\"],\"prompt\":\"Make the leaf golden.\"}, \"parameters\": {\"n\":1,\"size\":\"768*768\"}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/wan/wan2.5-i2i-preview/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/wan/wan2.5-i2i-preview/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

input

object

requerido

Ingresa información básica, como palabras del prompt, imágenes, etc.

​

input.images

string[]

requerido

Arreglo de URLs de imágenes para la generación de imagen a imagen

​

input.negative_prompt

string

Palabras del prompt inverso para describir el contenido que no quieres ver en la imagen

​

input.prompt

string

requerido

Palabras del prompt positivo para describir los elementos esperados de la imagen y sus características visuales. Admite chino e inglés, con una longitud no mayor a 2000 caracteres

​

model

string

El ID del modelo a llamar para la generación de imagen a imagen. NO está restringido en este componente: Comfy Router lo completa a partir del segmento de ruta `{model}` de `POST /v2/models/wan/{model}`. Una llamada directa a v1 a `POST /proxy/wan/api/v1/services/aigc/image2image/image-synthesis` DEBE proporcionarlo, y el enum de grafías aceptadas se encuentra en el componente propio de esa operación, `WanImage2ImageGenerationRequest`.

​

parameters

object

Parámetros de procesamiento de la imagen

​

parameters.n

integer

predeterminado:"4"

Número de imágenes generadas. Rango de 1 a 4, el valor predeterminado es 4Rango: `1` a `4`

​

parameters.seed

integer

Semilla de número aleatorio para controlar la aleatoriedad. Rango [0, 2147483647]Rango: `0` a `2147483647`

​

parameters.size

string

predeterminado:"\"1280*1280\""

La resolución de la imagen de salida en el formato ancho _alto. El valor predeterminado es 1280_ 1280\. La API acepta un área en píxeles entre 589824 (768 _768) y 1638400 (1280_ 1280) con una relación de aspecto entre 1:4 y 4:1

​

parameters.watermark

boolean

predeterminado:"false"

Si se agrega el logotipo de marca de agua en la esquina inferior derecha

Generado a partir del esquema que Router publica en `GET /v2/models/wan/wan2.5-i2i-preview/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

output

object

requerido

​

output.actual_prompt

string

Prompt real después de la reescritura inteligente (para tareas de video)

​

output.check_audio

string

URL de audio para tareas I2V con generación de audio

​

output.code

string

El código de error de la solicitud fallida (no se devuelve si la solicitud es exitosa)

​

output.end_time

string

Hora de finalización de la tarea

​

output.message

string

Información detallada sobre la solicitud fallida (no se devuelve si la solicitud es exitosa)

​

output.orig_prompt

string

Prompt de entrada original (para tareas de video)

​

output.results

object[]

Lista de resultados de la tarea para tareas de generación de imágenes

​

output.results[].actual_prompt

string

Prompt real después de la reescritura inteligente (si está habilitada)

​

output.results[].code

string

Código de error de la imagen (se devuelve cuando fallan algunas tareas)

​

output.results[].message

string

Información de error de la imagen (se devuelve cuando fallan algunas tareas)

​

output.results[].orig_prompt

string

Prompt de entrada original

​

output.results[].url

string

Dirección URL de la imagen generada

​

output.scheduled_time

string

Hora de ejecución de la tarea

​

output.submit_time

string

Hora de envío de la tarea

​

output.task_id

string

requerido

ID de la tarea

​

output.task_metrics

object

Estadísticas de resultados de la tarea para tareas de generación de imágenes

​

output.task_metrics.FAILED

integer

Número de tareas fallidas

​

output.task_metrics.SUCCEEDED

integer

Número de tareas exitosas

​

output.task_metrics.TOTAL

integer

Número total de tareas

​

output.task_status

string

requerido

Estado de la tareaValores posibles: `PENDING`, `RUNNING`, `SUCCEEDED`, `FAILED`, `CANCELED`, `UNKNOWN`

​

output.video_url

string

URL del video para tareas de generación de video completadas. El enlace es válido durante 24 horas

​

request_id

string

requerido

Identificador único de la solicitud

​

usage

object

Estadísticas de la información de salida. Solo se cuentan los resultados exitosos

​

usage.SR

integer

Nivel de resolución del video (tareas I2V y wan3.0-video)

​

usage.duration

number

Duración del video generado en segundos (tareas I2V y wan3.0-video)

​

usage.fps

integer

Frecuencia de cuadros del video generado (tareas wan3.0-video)

​

usage.image_count

integer

Número de imágenes generadas (tareas T2I e I2I)

​

usage.input_video_duration

number

Duración del video de entrada en segundos, 0.0 cuando no hay video de entrada (tareas wan3.0-video)

​

usage.output_video_duration

number

Duración del video de salida en segundos (tareas wan3.0-video)

​

usage.ratio

string

Relación de aspecto del video generado, por ejemplo 16:9 (tareas wan3.0-video)

​

usage.size

string

Resolución de la imagen (tareas T2I e I2I)

​

usage.video_count

integer

Número de videos generados (tareas T2V)

​

usage.video_duration

number

Duración del video generado en segundos (tareas T2V)

​

usage.video_ratio

string

Relación de resolución del video (tareas T2V)

​

code

string

Código de error de una solicitud fallida, informado en la RAÍZ del envelope y no bajo `output` (no se devuelve si la solicitud fue exitosa).

​

message

string

Información detallada sobre una solicitud fallida, informada en la RAÍZ del envelope y no bajo `output` (no se devuelve si la solicitud fue exitosa). Léela antes de recurrir a `output.message`.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "input": {
        "images": [
          "https://example.invalid/red-maple-leaf.png"
        ],
        "prompt": "Make the leaf golden."
      },
      "parameters": {
        "n": 1,
        "size": "768*768"
      }
    }
    

### 

​

Salida
    
    
    {
      "output": {
        "end_time": "2027-01-01T00:00:12.000Z",
        "results": [
          {
            "actual_prompt": "a single red maple leaf resting on still water, shallow depth of field, soft morning light",
            "orig_prompt": "a single red maple leaf resting on still water",
            "url": "https://example.invalid/wan/generated-1.png"
          },
          {
            "code": "DataInspectionFailed",
            "message": "This candidate was rejected; the task as a whole succeeded.",
            "orig_prompt": "a single red maple leaf resting on still water"
          }
        ],
        "scheduled_time": "2027-01-01T00:00:01.000Z",
        "submit_time": "2027-01-01T00:00:00.000Z",
        "task_id": "0385dc79-5ff8-4d82-bcb6-7c1a9f2e4d60",
        "task_metrics": {
          "FAILED": 1,
          "SUCCEEDED": 1,
          "TOTAL": 2
        },
        "task_status": "SUCCEEDED"
      },
      "request_id": "7574ee8f-38a3-4b1e-9280-11c33ab46e51",
      "usage": {
        "image_count": 1,
        "size": "1280*1280"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/wan/wan2-5-i2i-preview/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/wan/wan2-5-i2i-preview/code)

[HappyHorse 1.1 T2V](https://docs.comfy.org/es/development/comfy-router/models/wan/happyhorse-1-1-t2v/code)[Wan 2.5 I2V Preview](https://docs.comfy.org/es/development/comfy-router/models/wan/wan2-5-i2v-preview/code)
