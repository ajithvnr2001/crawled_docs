---
url: https://docs.comfy.org/es/development/comfy-router/models/veed/video-background-removal/code/
title: Usa Video Background Removal con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:21.247492+00:00
---

# Usa Video Background Removal con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/veed/video-background-removal/code/

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



Veed

# Usa Video Background Removal con Comfy Router

Copiar páginaCopiar página

Llama a veed/video-background-removal con Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API de `veed/video-background-removal`, servida por Comfy Router desde Veed. **Entrada:** video · **Salida:** video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `veed/video-background-removal` **Endpoint:** `POST https://api.comfy.org/v2/models/veed/video-background-removal`

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
            "veed/video-background-removal",
            {
                "output_codec": "vp9",
                "refine_foreground_edges": True,
                "subject_is_person": True,
                "video_url": "https://static-assets.veed.io/api-examples/bg-v2v-input.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("veed/video-background-removal", {
      output_codec: "vp9",
      refine_foreground_edges: true,
      subject_is_person: true,
      video_url: "https://static-assets.veed.io/api-examples/bg-v2v-input.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/veed/video-background-removal \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"output_codec\": \"vp9\", \"refine_foreground_edges\": true, \"subject_is_person\": true, \"video_url\": \"https://static-assets.veed.io/api-examples/bg-v2v-input.mp4\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/veed/video-background-removal/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "veed/video-background-removal",
                {
                    "output_codec": "vp9",
                    "refine_foreground_edges": True,
                    "subject_is_person": True,
                    "video_url": "https://static-assets.veed.io/api-examples/bg-v2v-input.mp4",
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
    const handle = await comfy.models.submit("veed/video-background-removal", {
      output_codec: "vp9",
      refine_foreground_edges: true,
      subject_is_person: true,
      video_url: "https://static-assets.veed.io/api-examples/bg-v2v-input.mp4",
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
    curl https://api.comfy.org/v2/models/veed/video-background-removal/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"output_codec\": \"vp9\", \"refine_foreground_edges\": true, \"subject_is_person\": true, \"video_url\": \"https://static-assets.veed.io/api-examples/bg-v2v-input.mp4\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/veed/video-background-removal/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/veed/video-background-removal/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

output_codec

string

predeterminado:"\"vp9\""

Codificación de salida: vp9 (un WebM con alfa) o h264 (el video RGB y una máscara alfa).

​

refine_foreground_edges

boolean

predeterminado:"true"

Mejora la calidad de los bordes del sujeto.

​

subject_is_person

boolean

predeterminado:"true"

Establécelo en falso cuando el sujeto no sea una persona.

​

video_url

string

requerido

URL http(s) pública del video de origen.

Generado a partir del esquema que Router sirve en `GET /v2/models/veed/video-background-removal/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

data

object

​

data.credits_charged

integer

Créditos que VEED cobró por la tarea. Presente una vez que la tarea está COMPLETED.

​

data.credits_estimated

integer

Créditos que VEED cotizó antes de ejecutar la tarea. Presente solo en la respuesta de envío.

​

data.error

object

Información del fallo. Presente una vez que la tarea está FAILED.

​

data.error.code

string

Código de fallo legible por máquina.

​

data.error.details

object[]

​

data.error.message

string

Mensaje de fallo legible por humanos.

​

data.job_id

string

ID de trabajo usado para consultar el estado.

​

data.result

object

Los medios producidos. Presente una vez que la tarea está COMPLETED. Las rutas de video responden `video`, Clean Audio responde `audio` y Video Background Removal responde `files`.

​

data.result.audio

object

​

data.result.audio.content_type

string

Tipo MIME del archivo.

​

data.result.audio.file_name

string

Nombre del archivo.

​

data.result.audio.file_size

integer

Tamaño del archivo en bytes.Formato: `int64`

​

data.result.audio.url

string

URL desde la que se puede descargar el archivo.

​

data.result.files

object[]

Salida de Video Background Removal. Un WebM con alfa para `vp9`, o el video RGB y una máscara alfa para `h264`.

​

data.result.files[].content_type

string

Tipo MIME del archivo.

​

data.result.files[].file_name

string

Nombre del archivo.

​

data.result.files[].file_size

integer

Tamaño del archivo en bytes.Formato: `int64`

​

data.result.files[].url

string

URL desde la que se puede descargar el archivo.

​

data.result.video

object

​

data.result.video.content_type

string

Tipo MIME del archivo.

​

data.result.video.file_name

string

Nombre del archivo.

​

data.result.video.file_size

integer

Tamaño del archivo en bytes.Formato: `int64`

​

data.result.video.url

string

URL desde la que se puede descargar el archivo.

​

data.status

string

Estado de la tarea: PROCESSING, COMPLETED, FAILED o CANCELLED.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "output_codec": "vp9",
      "refine_foreground_edges": true,
      "subject_is_person": true,
      "video_url": "https://static-assets.veed.io/api-examples/bg-v2v-input.mp4"
    }
    

### 

​

Salida
    
    
    {
      "data": {
        "credits_charged": 23,
        "job_id": "2a8065b6-9f4e-4132-bb7f-e99db65726bd",
        "result": {
          "files": [
            {
              "content_type": "application/octet-stream",
              "url": "https://example.invalid/veed/foreground.webm"
            }
          ]
        },
        "status": "COMPLETED"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/veed/video-background-removal/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/veed/video-background-removal/code)

[Video Background Removal Green Screen](https://docs.comfy.org/es/development/comfy-router/models/veed/video-background-removal-green-screen/code)[Veo 3.1 Fast Generate 001](https://docs.comfy.org/es/development/comfy-router/models/veo/veo-3-1-fast-generate-001/code)
