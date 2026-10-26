---
url: https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2/code/
title: Usa P Video 2 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:16.449987+00:00
---

# Usa P Video 2 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2/code/

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



Pruna

# Usa P Video 2 con Comfy Router

Copiar páginaCopiar página

Llama a pruna/p-video-2 mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API de `pruna/p-video-2`, que Comfy Router sirve desde Pruna. **Entrada:** Texto, Imagen, Audio · **Salida:** Video + Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `pruna/p-video-2` **Endpoint:** `POST https://api.comfy.org/v2/models/pruna/p-video-2`

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
            "pruna/p-video-2",
            {
                "input": {
                    "aspect_ratio": "16:9",
                    "draft": False,
                    "duration": 2,
                    "fps": 24,
                    "prompt": "A single red maple leaf resting on a plain white background.",
                    "resolution": "720p",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("pruna/p-video-2", {
      input: {
        aspect_ratio: "16:9",
        draft: false,
        duration: 2,
        fps: 24,
        prompt: "A single red maple leaf resting on a plain white background.",
        resolution: "720p",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pruna/p-video-2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"aspect_ratio\":\"16:9\",\"draft\":false,\"duration\":2,\"fps\":24,\"prompt\":\"A single red maple leaf resting on a plain white background.\",\"resolution\":\"720p\"}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/pruna/p-video-2/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recopila cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recopilación.

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
                "pruna/p-video-2",
                {
                    "input": {
                        "aspect_ratio": "16:9",
                        "draft": False,
                        "duration": 2,
                        "fps": 24,
                        "prompt": "A single red maple leaf resting on a plain white background.",
                        "resolution": "720p",
                    },
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
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
    const handle = await comfy.models.submit("pruna/p-video-2", {
      input: {
        aspect_ratio: "16:9",
        draft: false,
        duration: 2,
        fps: 24,
        prompt: "A single red maple leaf resting on a plain white background.",
        resolution: "720p",
      },
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
    curl https://api.comfy.org/v2/models/pruna/p-video-2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"aspect_ratio\":\"16:9\",\"draft\":false,\"duration\":2,\"fps\":24,\"prompt\":\"A single red maple leaf resting on a plain white background.\",\"resolution\":\"720p\"}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pruna/p-video-2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recopila. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/pruna/p-video-2/requests/$REQUEST_ID \
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

Parámetros de generación de P-Video-2. La generación se factura por segundo del video finalizado, medido desde el archivo devuelto, a una tarifa definida por `resolution` y `draft`. El filtro de seguridad siempre está activo; un valor `disable_safety_filter` en la solicitud se ignora.

​

input.aspect_ratio

string

predeterminado:"\"16:9\""

Relación de aspecto: 16:9, 9:16, 4:3, 3:4, 3:2, 2:3 o 1:1. Se ignora cuando `image` está definido.

​

input.audio

string

URI de audio de entrada para condicionar la generación (flac, mp3 o wav). La duración de salida sigue al audio.

​

input.draft

boolean

predeterminado:"false"

Vista previa más rápida y de menor calidad, facturada a la tarifa de borrador.

​

input.duration

integer

Duración del video generado en segundos (1-20). Cuando se omite, el modelo elige la longitud a partir del prompt, hasta 20 segundos. Se ignora cuando `audio` está definido.Rango: `1` a `20`

​

input.fps

integer

predeterminado:"24"

Frecuencia de cuadros: 24 o 48.

​

input.image

string

URI de imagen de entrada para imagen a video (jpg, jpeg, png o webp).

​

input.last_frame_image

string

URI de imagen de referencia para el último cuadro.

​

input.prompt

string

requerido

Prompt de texto para la generación de video.

​

input.prompt_upsampling

boolean

predeterminado:"true"

Reescribir el prompt antes de la generación. Desactívalo cuando un `seed` deba reproducir un resultado.

​

input.resolution

string

predeterminado:"\"720p\""

Resolución de salida: 720p o 1080p.

​

input.save_audio

boolean

predeterminado:"true"

Guardar el video con audio.

​

input.seed

integer

Semilla aleatoria para una generación reproducible. Aleatoria cuando se omite.

Generado a partir del esquema que Router sirve en `GET /v2/models/pruna/p-video-2/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

error

string

Mensaje de error. Presente cuando el estado es failed.

​

generation_url

string

URL del video finalizado. Presente cuando el estado es succeeded.

​

message

string

Mensaje de progreso legible para las personas.

​

status

string

Estado de la predicción: starting, processing, succeeded, failed o canceled.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "input": {
        "aspect_ratio": "16:9",
        "draft": false,
        "duration": 2,
        "fps": 24,
        "prompt": "A single red maple leaf resting on a plain white background.",
        "resolution": "720p"
      }
    }
    

### 

​

Salida
    
    
    {
      "generation_url": "https://example.invalid/pruna/p-video-2/output.mp4",
      "status": "succeeded"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/pruna/p-video-2/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/pruna/p-video-2/code)

[Pika 2.5 Text To Video](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-2-5-text-to-video/code)[Qwen Image 3.0 Pro](https://docs.comfy.org/es/development/comfy-router/models/qwen/qwen-image-3-0-pro/code)
