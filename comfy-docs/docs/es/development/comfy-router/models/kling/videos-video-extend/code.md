---
url: https://docs.comfy.org/es/development/comfy-router/models/kling/videos-video-extend/code/
title: Usa Videos Video Extend con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:08.992930+00:00
---

# Usa Videos Video Extend con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/kling/videos-video-extend/code/

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

# Usa Videos Video Extend con Comfy Router

Copiar páginaCopiar página

Llama a kling/videos-video-extend mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `kling/videos-video-extend`, servida por Comfy Router de Kling. **Entrada:** Video, Texto · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP sin procesar. **ID del modelo:** `kling/videos-video-extend` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/videos-video-extend`

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
            "kling/videos-video-extend",
            {
                "cfg_scale": 0.5,
                "prompt": "The camera keeps drifting forward down the alley.",
                "video_id": "kling-video-6f5e4d3c2b1a",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("kling/videos-video-extend", {
      cfg_scale: 0.5,
      prompt: "The camera keeps drifting forward down the alley.",
      video_id: "kling-video-6f5e4d3c2b1a",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/videos-video-extend \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"cfg_scale\": 0.5, \"prompt\": \"The camera keeps drifting forward down the alley.\", \"video_id\": \"kling-video-6f5e4d3c2b1a\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/kling/videos-video-extend/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "kling/videos-video-extend",
                {
                    "cfg_scale": 0.5,
                    "prompt": "The camera keeps drifting forward down the alley.",
                    "video_id": "kling-video-6f5e4d3c2b1a",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
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
    const handle = await comfy.models.submit("kling/videos-video-extend", {
      cfg_scale: 0.5,
      prompt: "The camera keeps drifting forward down the alley.",
      video_id: "kling-video-6f5e4d3c2b1a",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/kling/videos-video-extend/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"cfg_scale\": 0.5, \"prompt\": \"The camera keeps drifting forward down the alley.\", \"video_id\": \"kling-video-6f5e4d3c2b1a\"}"
    
    # 2. Sondea hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/videos-video-extend/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras todavía se está ejecutando.
    curl https://api.comfy.org/v2/models/kling/videos-video-extend/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

callback_url

string (uri)

La dirección de notificación de callback. El servidor notificará cuando cambie el estado de la tarea.Formato: `uri`

​

cfg_scale

number

predeterminado:"0.5"

Flexibilidad en la generación de video. Cuanto mayor sea el valor, menor será el grado de flexibilidad del modelo y mayor la relevancia respecto al prompt del usuario.Rango: `0` a `1`Formato: `float`

​

negative_prompt

string

Prompt de texto negativo para los elementos que se deben evitar en el video extendido

​

prompt

string

Prompt de texto positivo para guiar la extensión del video

​

video_id

string

requerido

El ID del video que se va a extender. Admite videos generados mediante operaciones de texto a video, imagen a video y extensiones de video anteriores. La duración total no puede superar los 3 minutos después de la extensión.

Generado a partir del esquema que Router sirve en `GET /v2/models/kling/videos-video-extend/openapi.json`, el mismo documento con el que valida cada llamada antes de que la solicitud llegue al proveedor.

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

Hora de creación de la tarea

​

data.final_unit_deduction

string

Las unidades de deducción de la tarea

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

​

data.task_result

object

​

data.task_result.videos

object[]

​

data.task_result.videos[].duration

string

Duración total del video en segundos

​

data.task_result.videos[].id

string

ID del video generado

​

data.task_result.videos[].url

string (uri)

URL del video generadoFormato: `uri`

​

data.task_result.videos[].watermark_url

string (uri)

URL del video generado con marca de agua, en formato de protección contra hotlinkingFormato: `uri`

​

data.task_status

string

Estado de la tareaValores posibles: `submitted`, `processing`, `succeed`, `failed`

​

data.updated_at

integer

Hora de actualización de la tarea

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
      "cfg_scale": 0.5,
      "prompt": "The camera keeps drifting forward down the alley.",
      "video_id": "kling-video-6f5e4d3c2b1a"
    }
    

### 

​

Salida
    
    
    {
      "code": 0,
      "data": {
        "created_at": 1798761600000,
        "final_unit_deduction": "1.00",
        "task_id": "kling-video-extend-task-0a1b2c3d4e5f",
        "task_result": {
          "videos": [
            {
              "duration": "10",
              "id": "kling-video-5f4e3d2c1b0a",
              "url": "https://example.invalid/kling/videos-video-extend/generated.mp4"
            }
          ]
        },
        "task_status": "succeed",
        "updated_at": 1798762020000
      },
      "message": "SUCCEED",
      "request_id": "c7b6a504-3f2e-41d0-8a9c-6b5d4e3f2a10"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/kling/videos-video-extend/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/kling/videos-video-extend/code)

[Videos Lip Sync](https://docs.comfy.org/es/development/comfy-router/models/kling/videos-lip-sync/code)[Krea 2 Large](https://docs.comfy.org/es/development/comfy-router/models/krea/krea-2-large/code)
