---
url: https://docs.comfy.org/es/development/comfy-router/models/fal/crystal-video-upscaler/code/
title: Usa Crystal Video Upscaler con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:03.068102+00:00
---

# Usa Crystal Video Upscaler con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/fal/crystal-video-upscaler/code/

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



fal

# Usa Crystal Video Upscaler con Comfy Router

Copiar páginaCopiar página

Llama a fal/crystal-video-upscaler mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `fal/crystal-video-upscaler`, que Comfy Router ofrece desde fal. **Entrada:** Video · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `fal/crystal-video-upscaler` **Endpoint:** `POST https://api.comfy.org/v2/models/fal/crystal-video-upscaler`

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
            "fal/crystal-video-upscaler",
            {
                "scale_factor": 2,
                "video_url": "https://storage.googleapis.com/falserverless/example_inputs/crystal_upscaler/video_upscaling/video_in.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("fal/crystal-video-upscaler", {
      scale_factor: 2,
      video_url: "https://storage.googleapis.com/falserverless/example_inputs/crystal_upscaler/video_upscaling/video_in.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/fal/crystal-video-upscaler \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"scale_factor\": 2, \"video_url\": \"https://storage.googleapis.com/falserverless/example_inputs/crystal_upscaler/video_upscaling/video_in.mp4\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/fal/crystal-video-upscaler/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "fal/crystal-video-upscaler",
                {
                    "scale_factor": 2,
                    "video_url": "https://storage.googleapis.com/falserverless/example_inputs/crystal_upscaler/video_upscaling/video_in.mp4",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta el estado hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
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
    const handle = await comfy.models.submit("fal/crystal-video-upscaler", {
      scale_factor: 2,
      video_url: "https://storage.googleapis.com/falserverless/example_inputs/crystal_upscaler/video_upscaling/video_in.mp4",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta el estado hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/fal/crystal-video-upscaler/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"scale_factor\": 2, \"video_url\": \"https://storage.googleapis.com/falserverless/example_inputs/crystal_upscaler/video_upscaling/video_in.mp4\"}"
    
    # 2. Consulta el estado hasta que sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/fal/crystal-video-upscaler/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/fal/crystal-video-upscaler/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

scale_factor

number

predeterminado:"2"

Factor que se aplica a cada lado del video de entrada. El video ampliado no debe superar los 5K. fal cobra por megapíxel de salida por segundo, así que el precio crece con el cuadrado de este valor.Rango: `1` a `200`

​

video_url

string

requerido

URL del video de entrada (MP4, MOV, WebM, M4V o GIF).

Generado a partir del esquema que Router sirve en `GET /v2/models/fal/crystal-video-upscaler/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

video

object

requerido

El archivo de video ampliado.

​

video.content_type

string

Tipo MIME del archivo de video.

​

video.duration

number

Duración del video en segundos.

​

video.file_name

string

Nombre del archivo de video.

​

video.file_size

integer

Tamaño del archivo de video en bytes.

​

video.fps

number

Frecuencia de cuadros del video.

​

video.height

integer

Alto del video en píxeles.

​

video.num_frames

integer

Número de fotogramas del video.

​

video.url

string

requerido

URL del video ampliado.

​

video.width

integer

Ancho del video en píxeles.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "scale_factor": 2,
      "video_url": "https://storage.googleapis.com/falserverless/example_inputs/crystal_upscaler/video_upscaling/video_in.mp4"
    }
    

### 

​

Salida
    
    
    {
      "video": {
        "content_type": "video/mp4",
        "duration": 10,
        "file_name": "upscaled.mp4",
        "file_size": 3950551,
        "fps": 30,
        "height": 720,
        "num_frames": 300,
        "url": "https://example.invalid/fal/crystal-video-upscaler/upscaled.mp4",
        "width": 1280
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/fal/crystal-video-upscaler/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/fal/crystal-video-upscaler/code)

[Crystal Upscaler](https://docs.comfy.org/es/development/comfy-router/models/fal/crystal-upscaler/code)[FLUX 3 Max](https://docs.comfy.org/es/development/comfy-router/models/fal/flux-3-max/code)
