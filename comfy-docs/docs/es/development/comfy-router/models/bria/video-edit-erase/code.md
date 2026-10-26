---
url: https://docs.comfy.org/es/development/comfy-router/models/bria/video-edit-erase/code/
title: Usa Video Edit Erase con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:02:59.370887+00:00
---

# Usa Video Edit Erase con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/bria/video-edit-erase/code/

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



Bria

# Usa Video Edit Erase con Comfy Router

Copiar páginaCopiar página

Llama a bria/video-edit-erase con Comfy Router: endpoint, forma de la petición y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `bria/video-edit-erase`, servida por Comfy Router desde Bria. **Entrada:** Video · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP sin procesar. **ID del modelo:** `bria/video-edit-erase` **Endpoint:** `POST https://api.comfy.org/v2/models/bria/video-edit-erase`

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
            "bria/video-edit-erase",
            {
                "auto_trim": True,
                "mask": "https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_mask.mp4",
                "video": "https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_video.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("bria/video-edit-erase", {
      auto_trim: true,
      mask: "https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_mask.mp4",
      video: "https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_video.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/bria/video-edit-erase \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"auto_trim\": true, \"mask\": \"https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_mask.mp4\", \"video\": \"https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_video.mp4\"}"
    

El mismo cuerpo de solicitud, enviado a `POST https://api.comfy.org/v2/models/bria/video-edit-erase/requests`. El Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) detalla el estado, la cancelación y la recogida.

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
                "bria/video-edit-erase",
                {
                    "auto_trim": True,
                    "mask": "https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_mask.mp4",
                    "video": "https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_video.mp4",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
            # Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado del Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("bria/video-edit-erase", {
      auto_trim: true,
      mask: "https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_mask.mp4",
      video: "https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_video.mp4",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que necesita otro proceso
    
    // Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló genera un rechazo aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. El Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/bria/video-edit-erase/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"auto_trim\": true, \"mask\": \"https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_mask.mp4\", \"video\": \"https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_video.mp4\"}"
    
    # 2. Sondea hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/bria/video-edit-erase/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/bria/video-edit-erase/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

auto_trim

boolean

Cuando es verdadero, los videos de más de 5 segundos se recortan a los primeros 5 segundos. Cuando es falso (valor predeterminado), los videos más largos se rechazan.

​

mask

string

requerido

URL de acceso público de un video de máscara que define el área a eliminar. Los píxeles blancos marcan la región que se va a eliminar; los píxeles negros se conservan.

​

output_container_and_codec

string

Preset de contenedor y códec de salida.Valores posibles: `mp4_h264`, `mp4_h265`, `webm_vp9`, `mov_h265`, `mov_proresks`, `mkv_h264`, `mkv_h265`, `mkv_vp9`, `gif`

​

preserve_audio

boolean

Indica si se conserva el audio del video de entrada.

​

video

string

requerido

URL de acceso público del video de entrada. Duración máxima de 5 segundos, a menos que auto_trim sea verdadero. Resolución de entrada admitida hasta 750p; las entradas más grandes se reducen.

Generado a partir del esquema que Router publica en `GET /v2/models/bria/video-edit-erase/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

error

object

Objeto de error (solo presente cuando el estado es ERROR)

​

error.code

integer

Código de error.

​

error.details

string

Detalles adicionales del error.

​

error.message

string

Mensaje de error.

​

request_id

string

Identificador único de la solicitud.

​

result

object

Objeto de resultado (solo presente cuando el estado es COMPLETED)

​

result.image_url

string

URL de la imagen generada o editada.

​

result.prompt

string

Prompt original.

​

result.refined_prompt

string

Versión refinada del prompt, o null en una generación COMPLETED que Bria no refinó. Es nullable porque la clave está PRESENTE y lleva null en lugar de omitirse; se observó en vivo en bria/image-edit-gen-fill.

​

result.seed

integer

Semilla usada para la generación.

​

result.structured_instruction

string

La instrucción estructurada, un documento JSON serializado como cadena, que devuelve `/v2/structured_instruction/generate`. Esa operación no rellena ninguna de las dos URL.

​

result.structured_prompt

string

El prompt estructurado en JSON detallado.

​

result.video_url

string

URL del video generado.

​

status

string

Estado actual de la solicitud.Valores posibles: `IN_PROGRESS`, `COMPLETED`, `ERROR`, `UNKNOWN`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "auto_trim": true,
      "mask": "https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_mask.mp4",
      "video": "https://bria-test-images.s3.us-east-1.amazonaws.com/videos/eraser/video1_video.mp4"
    }
    

### 

​

Salida
    
    
    {
      "request_id": "0b3f9d7e-2c41-4a8b-9f10-6d5c8e2a4b71",
      "result": {
        "video_url": "https://example.invalid/bria/video-edit-erase/generated.mp4"
      },
      "status": "COMPLETED"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/bria/video-edit-erase/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/bria/video-edit-erase/code)

[Image](https://docs.comfy.org/es/development/comfy-router/models/bria/image/code)[Video Edit Green Screen](https://docs.comfy.org/es/development/comfy-router/models/bria/video-edit-green-screen/code)
