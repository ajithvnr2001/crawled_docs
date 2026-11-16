---
url: https://docs.comfy.org/es/development/comfy-router/models/stability/sdxl-1-0-image-to-image/code/
title: Usar Sdxl 1.0 Imagen a imagen con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:57.038170+00:00
---

# Usar Sdxl 1.0 Imagen a imagen con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/stability/sdxl-1-0-image-to-image/code/

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



Stability

# Usar Sdxl 1.0 Imagen a imagen con Comfy Router

Copiar páginaCopiar página

Llama a stability/sdxl-1.0-image-to-image con Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `stability/sdxl-1.0-image-to-image`, servido por Comfy Router de Stability. **Entrada:** Texto, Imagen · **Salida:** Imagen

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `stability/sdxl-1.0-image-to-image` **Endpoint:** `POST https://api.comfy.org/v2/models/stability/sdxl-1.0-image-to-image`

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
            "stability/sdxl-1.0-image-to-image",
            {
                "samples": 1,
                "seed": 12345,
                "steps": 30,
                "text_prompts": [
                    {
                        "text": "a lighthouse on a cliff at sunset, oil painting",
                    },
                ],
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("stability/sdxl-1.0-image-to-image", {
      samples: 1,
      seed: 12345,
      steps: 30,
      text_prompts: [
        {
          text: "a lighthouse on a cliff at sunset, oil painting",
        },
      ],
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/stability/sdxl-1.0-image-to-image \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"samples\": 1, \"seed\": 12345, \"steps\": 30, \"text_prompts\": [{\"text\":\"a lighthouse on a cliff at sunset, oil painting\"}]}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/stability/sdxl-1.0-image-to-image/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y recoges el resultado cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "stability/sdxl-1.0-image-to-image",
                {
                    "samples": 1,
                    "seed": 12345,
                    "steps": 30,
                    "text_prompts": [
                        {
                            "text": "a lighthouse on a cliff at sunset, oil painting",
                        },
                    ],
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
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
    const handle = await comfy.models.submit("stability/sdxl-1.0-image-to-image", {
      samples: 1,
      seed: 12345,
      steps: 30,
      text_prompts: [
        {
          text: "a lighthouse on a cliff at sunset, oil painting",
        },
      ],
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
    curl https://api.comfy.org/v2/models/stability/sdxl-1.0-image-to-image/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"samples\": 1, \"seed\": 12345, \"steps\": 30, \"text_prompts\": [{\"text\":\"a lighthouse on a cliff at sunset, oil painting\"}]}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/stability/sdxl-1.0-image-to-image/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/stability/sdxl-1.0-image-to-image/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

cfg_scale

number

Qué tan estrictamente sigue la imagen al prompt. Predeterminado 7.Alcance: `0` a `35`

clip_guidance_preset

string

Preajuste de orientación CLIP de Stability, por ejemplo `NONE`.

extras

object

Se acepta por compatibilidad y se ignora.

height

integer

Solo texto a imagen. Alto de salida; debe formar uno de los tamaños compatibles de SDXL 1.0 junto con `width`. Predeterminado 1024.

image_strength

number

Solo imagen a imagen. Cuánto de la imagen fuente se conserva.Alcance: `0` a `1`

init_image

string (uri)

Solo imagen a imagen, requerido en ese caso. Una URL de recurso firmada por Comfy de la imagen fuente.Formato: `uri`

init_image_mode

string

Solo imagen a imagen. Si `image_strength` o el programa de pasos controla cuánto de la imagen fuente se conserva. Predeterminado IMAGE_STRENGTH.Valores posibles: `IMAGE_STRENGTH`, `STEP_SCHEDULE`

sampler

string

Nombre del sampler de Stability, por ejemplo `K_DPMPP_2M`.

samples

integer

Cantidad de imágenes a generar. Predeterminado 1. Cada imagen devuelta se factura.Alcance: `1` a `10`

seed

integer

Semilla para todo el lote. 0 u omitida elige una semilla aleatoria.Alcance: `0` a `…`

step_schedule_end

number

Solo imagen a imagen, con `init_image_mode` STEP_SCHEDULE.Alcance: `0` a `1`

step_schedule_start

number

Solo imagen a imagen, con `init_image_mode` STEP_SCHEDULE.Alcance: `0` a `1`

steps

integer

Pasos de difusión. Predeterminado 30.Alcance: `10` a `30`

style_preset

string

Preajuste de estilo de Stability, por ejemplo `photographic`.

text_prompts

object[]

requerido

Prompts, cada uno con un peso opcional. Un peso negativo lo convierte en un prompt negativo.

text_prompts[].text

string

requerido

text_prompts[].weight

number

width

integer

Solo texto a imagen. Ancho de salida; debe formar uno de los tamaños compatibles de SDXL 1.0 junto con `height`. Predeterminado 1024.

Generado a partir del esquema que Router sirve en `GET /v2/models/stability/sdxl-1.0-image-to-image/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

finish_reason

string

requerido

Siempre SUCCESS en una respuesta 200.

image

string (uri)

requerido

URL firmada por Comfy de la imagen PNG (la primera), válida por hasta 24 horas.Formato: `uri`

images

string (uri)[]

Solo SDXL, cuando se devolvió más de una imagen. Todas las URL de imagen firmadas por Comfy, en el orden de salida, cada una válida por hasta 24 horas.

seed

integer

requerido

La semilla con la que se generó la imagen.

## Ejemplos

### Entrada
    
    
    {
      "samples": 1,
      "seed": 12345,
      "steps": 30,
      "text_prompts": [
        {
          "text": "a lighthouse on a cliff at sunset, oil painting"
        }
      ]
    }
    

### Salida
    
    
    {
      "finish_reason": "SUCCESS",
      "image": "https://example.invalid/stability/image.png",
      "seed": 12345
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/stability/sdxl-1-0-image-to-image/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/stability/sdxl-1-0-image-to-image/code)

[Sd3.5 Medium](https://docs.comfy.org/es/development/comfy-router/models/stability/sd3-5-medium/code)[Sdxl 1.0 Masking](https://docs.comfy.org/es/development/comfy-router/models/stability/sdxl-1-0-masking/code)
