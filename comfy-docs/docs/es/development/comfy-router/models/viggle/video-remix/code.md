---
url: https://docs.comfy.org/es/development/comfy-router/models/viggle/video-remix/code/
title: Usar Video Remix con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:29.159544+00:00
---

# Usar Video Remix con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/viggle/video-remix/code/

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



Viggle

# Usar Video Remix con Comfy Router

Copiar páginaCopiar página

Llama a viggle/video-remix mediante Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `viggle/video-remix`, servida por Comfy Router desde Viggle. **Entrada:** Imagen, Video · **Salida:** Video

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `viggle/video-remix` **Endpoint:** `POST https://api.comfy.org/v2/models/viggle/video-remix`

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
            "viggle/video-remix",
            {
                "background_mode": "original",
                "image_url": "https://example.invalid/viggle/character.png",
                "motion_video_url": "https://example.invalid/viggle/dance.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("viggle/video-remix", {
      background_mode: "original",
      image_url: "https://example.invalid/viggle/character.png",
      motion_video_url: "https://example.invalid/viggle/dance.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/viggle/video-remix \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"background_mode\": \"original\", \"image_url\": \"https://example.invalid/viggle/character.png\", \"motion_video_url\": \"https://example.invalid/viggle/dance.mp4\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/viggle/video-remix/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y puedes recoger el resultado en cuanto esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "viggle/video-remix",
                {
                    "background_mode": "original",
                    "image_url": "https://example.invalid/viggle/character.png",
                    "motion_video_url": "https://example.invalid/viggle/dance.mp4",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
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
    const handle = await comfy.models.submit("viggle/video-remix", {
      background_mode: "original",
      image_url: "https://example.invalid/viggle/character.png",
      motion_video_url: "https://example.invalid/viggle/dance.mp4",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/viggle/video-remix/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"background_mode\": \"original\", \"image_url\": \"https://example.invalid/viggle/character.png\", \"motion_video_url\": \"https://example.invalid/viggle/dance.mp4\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/viggle/video-remix/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/viggle/video-remix/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

background_mode

string

original (el valor predeterminado), solid o transparent. `transparent` añade un video de máscara alfa, `alpha_url`.

bg_color

string

Color de fondo sólido como `R,G,B`. Solo con `background_mode=solid`.

image_url

string

requerido

URL http(s) pública de la imagen del personaje.

model

string

Modelo de render opcional: V3 o V4.

motion_video_url

string

requerido

URL http(s) pública del video guía, de hasta 100 MiB.

Generado a partir del esquema que Router sirve en `GET /v2/models/viggle/video-remix/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

alpha_url

string

El video de máscara alfa de un render transparente, una vez que está listo.

completed_at

string

created_at

string

credits_used

number

Créditos de Viggle que se cobran por la tarea, fijados cuando está lista.Formato: `double`

duration_seconds

number

Duración en segundos en la que se basa el cobro, fijada cuando la tarea está lista.Formato: `double`

error

object

Objeto de error de Viggle, establecido cuando la tarea falló.

error.code

string

error.message

string

error.request_id

string

error.retryable

boolean

id

string

Id del render (prefijo `render_`). Consúltalo en la ruta de videos.

progress

integer

Progreso de 0 a 100, cuando se conoce.

stage

string

Etapa de progreso aproximada mientras se ejecuta el render.

status

string

Estado: queued, processing, ready, failed o cancelled.

video_url

string

El video finalizado, una vez que está listo. La URL dura una hora.

## Ejemplos

### Entrada
    
    
    {
      "background_mode": "original",
      "image_url": "https://example.invalid/viggle/character.png",
      "motion_video_url": "https://example.invalid/viggle/dance.mp4"
    }
    

### Salida
    
    
    {
      "alpha_url": null,
      "credits_used": 5.04,
      "duration_seconds": 5.04,
      "error": null,
      "id": "render_job_38d67fcfb717e8d4",
      "progress": 100,
      "status": "ready",
      "video_url": "https://example.invalid/viggle/output.mp4"
    }
    

## Antes de lanzar

Los SDK crean una `Idempotency-Key` y la reutilizan para los reintentos automáticos. Para los reintentos manuales, reutiliza la clave original. Router puede mantener la conexión abierta hasta 10 minutos. Cuando una solicitud falla, Router envía un encabezado de respuesta `X-Comfy-Error-Type` que explica el motivo. Un `422` significa que Router rechazó la entrada antes de llamar al proveedor, y un `413` significa que el cuerpo de la solicitud era más grande de lo que Router acepta. Descarga los recursos generados de inmediato, porque [las URL de resultados pueden caducar](https://docs.comfy.org/es/development/comfy-router/reference#recursos-del-resultado). Cualquier límite de tamaño mencionado en la descripción de un campo más arriba es el límite propio del proveedor para ese campo, citado de la especificación del proveedor. Router aplica un tope aparte al cuerpo completo de la solicitud, con el que cuentan los medios codificados en base64: consulta [tamaño del cuerpo de la solicitud](https://docs.comfy.org/es/development/comfy-router/limitations#los-cuerpos-de-las-solicitudes-tienen-un-l%C3%ADmite). Esta página documenta un modelo socio al que se llama a través de Comfy Router. El mismo paquete `comfy-sdk` / `@comfyorg/sdk` también incluye un segundo cliente, para ejecutar todo un gráfico de flujo de trabajo de ComfyUI en Comfy Cloud: `Comfy(api_key=...)` / `new Comfy({ apiKey })`, con `client.workflows`, `client.assets` y `client.jobs`. Consulta [SDK de Comfy](https://docs.comfy.org/es/development/api-development/sdks).

## Encabezados

Autenticación, idempotencia, IDs de solicitud, agrupaciones de errores, ritmo de reintentos y límites de gasto.

## Uso de la API de Router

Descubrimiento de modelos, errores de validación, reintentos y facturación.

## Limitaciones

Lo que Router no hace hoy y qué usar en su lugar.

¿Esta página le ayudó?

SíNo

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/viggle/video-remix/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/viggle/video-remix/code)

[Text To Motion](https://docs.comfy.org/es/development/comfy-router/models/viggle/text-to-motion/code)[HappyHorse 1.0 I2V](https://docs.comfy.org/es/development/comfy-router/models/wan/happyhorse-1-0-i2v/code)
