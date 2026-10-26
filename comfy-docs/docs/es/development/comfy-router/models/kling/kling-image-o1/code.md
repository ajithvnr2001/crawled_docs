---
url: https://docs.comfy.org/es/development/comfy-router/models/kling/kling-image-o1/code/
title: Usa Kling Image O1 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:07.740935+00:00
---

# Usa Kling Image O1 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/kling/kling-image-o1/code/

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



Kling

# Usa Kling Image O1 con Comfy Router

Copiar páginaCopiar página

Llama a kling/kling-image-o1 mediante Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `kling/kling-image-o1`, servida por Comfy Router desde Kling. **Entrada:** Texto, Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `kling/kling-image-o1` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/kling-image-o1`

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
            "kling/kling-image-o1",
            {
                "aspect_ratio": "1:1",
                "n": 1,
                "prompt": "A watercolour koi pond at dawn, soft light.",
                "resolution": "1k",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("kling/kling-image-o1", {
      aspect_ratio: "1:1",
      n: 1,
      prompt: "A watercolour koi pond at dawn, soft light.",
      resolution: "1k",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/kling-image-o1 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"1:1\", \"n\": 1, \"prompt\": \"A watercolour koi pond at dawn, soft light.\", \"resolution\": \"1k\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/kling/kling-image-o1/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "kling/kling-image-o1",
                {
                    "aspect_ratio": "1:1",
                    "n": 1,
                    "prompt": "A watercolour koi pond at dawn, soft light.",
                    "resolution": "1k",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
            # Consulta el estado hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("kling/kling-image-o1", {
      aspect_ratio: "1:1",
      n: 1,
      prompt: "A watercolour koi pond at dawn, soft light.",
      resolution: "1k",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que necesita otro proceso
    
    // Consulta el estado hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/kling/kling-image-o1/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"1:1\", \"n\": 1, \"prompt\": \"A watercolour koi pond at dawn, soft light.\", \"resolution\": \"1k\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/kling-image-o1/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/kling/kling-image-o1/requests/$REQUEST_ID \
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

predeterminado:"\"auto\""

Relación de aspecto de las imágenes generadas (ancho:alto). auto genera imágenes de forma inteligente según el contenido de entrada.Valores posibles: `16:9`, `9:16`, `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `21:9`, `auto`

​

callback_url

string (uri)

Dirección de notificación de callback para el resultado de esta tarea. Si se configura, el servidor notificará activamente cuando cambie el estado de la tarea.Formato: `uri`

​

element_list

object[]

Lista de elementos de referencia configurada según el ID de elemento. La suma de elementos de referencia e imágenes de referencia no debe superar 10.

​

element_list[].element_id

integer

requerido

ID de elementoFormato: `int64`

​

external_task_id

string

ID de tarea personalizado. Debe ser único dentro de una misma cuenta de usuario.

​

image_list

object[]

Lista de imágenes de referencia. Admite la introducción de la codificación Base64 de la imagen o la URL de la imagen (asegúrate de que sea accesible). Los formatos admitidos incluyen .jpg/.jpeg/.png. El tamaño del archivo no puede superar 10 MB. Las dimensiones de ancho y alto no deben ser inferiores a 300 px, con una relación de aspecto entre 1:2.5 y 2.5:1. La suma de elementos de referencia e imágenes de referencia no debe superar 10.

​

image_list[].image

string

requerido

Codificación Base64 de la imagen o URL de la imagen (asegúrate de que sea accesible)

​

model_name

string

Nombre del modelo. Omítelo o envía null cuando uses Comfy Router; el modelo se selecciona mediante la ruta de la solicitud. Un nombre proporcionado debe coincidir con esa ruta.

​

n

integer

predeterminado:"1"

Número de imágenes generadas. Rango de valores [1,9].Rango: `1` a `9`

​

prompt

string

requerido

Palabras del prompt de texto, que pueden incluir descripciones positivas y negativas. No debe superar los 2500 caracteres. El modelo Omni puede lograr diversas capacidades mediante el prompt con elementos e imágenes. Especifica una imagen con el formato <<<>>>, por ejemplo <<<image_1>>>.

​

resolution

string

predeterminado:"\"1k\""

Resolución de generación de imágenes. 1k es el estándar 1K, 2k es alta resolución 2K y 4k es alta resolución 4K.Valores posibles: `1k`, `2k`, `4k`

​

result_type

string

predeterminado:"\"single\""

Controla si se genera una sola imagen o una serie de imágenes.Valores posibles: `single`, `series`

​

series_amount

integer

predeterminado:"4"

Número de imágenes de una serie. Rango de valores [2,9].Rango: `2` a `9`

Generado a partir del esquema que Router sirve en `GET /v2/models/kling/kling-image-o1/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

code

integer

Código de error

​

data

object

​

data.created_at

integer

Hora de creación de la tarea, marca de tiempo Unix en milisegundos

​

data.final_unit_deduction

string

Unidades de deducción de la tarea

​

data.task_id

string

ID de la tarea

​

data.task_info

object

​

data.task_info.external_task_id

string

ID de tarea definido por el cliente

​

data.task_result

object

​

data.task_result.images

object[]

​

data.task_result.images[].index

integer

Número de imagen (0-9)

​

data.task_result.images[].url

string (uri)

URL de la imagen generadaFormato: `uri`

​

data.task_result.result_type

string

Indica si el resultado es una sola imagen o una serie de imágenesValores posibles: `single`, `series`

​

data.task_result.series_images

object[]

Lista de resultados de imágenes de la serie

​

data.task_result.series_images[].index

integer

Número de secuencia de la imagen de la serie

​

data.task_result.series_images[].url

string (uri)

URL de la imagen generadaFormato: `uri`

​

data.task_status

string

Estado de la tareaValores posibles: `submitted`, `processing`, `succeed`, `failed`

​

data.task_status_msg

string

Información del estado de la tarea, que muestra el motivo del fallo cuando la tarea falla (como la activación del control de riesgo de contenido de la plataforma, etc.)

​

data.updated_at

integer

Hora de actualización de la tarea, marca de tiempo Unix en milisegundos

​

message

string

Mensaje de error

​

request_id

string

ID de la solicitud

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "aspect_ratio": "1:1",
      "n": 1,
      "prompt": "A watercolour koi pond at dawn, soft light.",
      "resolution": "1k"
    }
    

### 

​

Salida
    
    
    {
      "code": 0,
      "data": {
        "created_at": 1798761600000,
        "task_id": "kling-image-task-3c4d5e6f7a8b",
        "task_result": {
          "images": [
            {
              "index": 0,
              "url": "https://example.invalid/kling/kling-image-o1/generated.png"
            }
          ],
          "result_type": "single"
        },
        "task_status": "succeed",
        "task_status_msg": "",
        "updated_at": 1798761660000
      },
      "message": "SUCCEED",
      "request_id": "6a4b2c80-1e93-4d57-b8f2-05c7e9a3d146"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/kling/kling-image-o1/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/kling/kling-image-o1/code)

[Kling 3.0 Turbo](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-3-0-turbo/code)[Kling V2.5 Turbo](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-v2-5-turbo/code)
