---
url: https://docs.comfy.org/es/development/comfy-router/models/stability/sdxl-1-0-masking/code/
title: Usa Sdxl 1.0 Masking con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:57.449560+00:00
---

# Usa Sdxl 1.0 Masking con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/stability/sdxl-1-0-masking/code/

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

# Usa Sdxl 1.0 Masking con Comfy Router

Copiar páginaCopiar página

Llama a stability/sdxl-1.0-masking desde Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API de `stability/sdxl-1.0-masking`, servido por Comfy Router de Stability. **Entrada:** Texto, Imagen · **Salida:** Imagen

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL realiza la misma llamada mediante HTTP sin procesar. **ID del modelo:** `stability/sdxl-1.0-masking` **Endpoint:** `POST https://api.comfy.org/v2/models/stability/sdxl-1.0-masking`

  * Esperar el resultado

  * Poner en cola y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY desde el entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "stability/sdxl-1.0-masking",
            {
                "init_image": "https://storage.googleapis.com/example-bucket/source.png",
                "mask_image": "https://storage.googleapis.com/example-bucket/mask.png",
                "mask_source": "MASK_IMAGE_WHITE",
                "seed": 12345,
                "text_prompts": [
                    {
                        "text": "a lighthouse on a cliff at sunset, oil painting",
                    },
                ],
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY desde el entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("stability/sdxl-1.0-masking", {
      init_image: "https://storage.googleapis.com/example-bucket/source.png",
      mask_image: "https://storage.googleapis.com/example-bucket/mask.png",
      mask_source: "MASK_IMAGE_WHITE",
      seed: 12345,
      text_prompts: [
        {
          text: "a lighthouse on a cliff at sunset, oil painting",
        },
      ],
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/stability/sdxl-1.0-masking \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"init_image\": \"https://storage.googleapis.com/example-bucket/source.png\", \"mask_image\": \"https://storage.googleapis.com/example-bucket/mask.png\", \"mask_source\": \"MASK_IMAGE_WHITE\", \"seed\": 12345, \"text_prompts\": [{\"text\":\"a lighthouse on a cliff at sunset, oil painting\"}]}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/stability/sdxl-1.0-masking/requests`. El Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "stability/sdxl-1.0-masking",
                {
                    "init_image": "https://storage.googleapis.com/example-bucket/source.png",
                    "mask_image": "https://storage.googleapis.com/example-bucket/mask.png",
                    "mask_source": "MASK_IMAGE_WHITE",
                    "seed": 12345,
                    "text_prompts": [
                        {
                            "text": "a lighthouse on a cliff at sunset, oil painting",
                        },
                    ],
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado del Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("stability/sdxl-1.0-masking", {
      init_image: "https://storage.googleapis.com/example-bucket/source.png",
      mask_image: "https://storage.googleapis.com/example-bucket/mask.png",
      mask_source: "MASK_IMAGE_WHITE",
      seed: 12345,
      text_prompts: [
        {
          text: "a lighthouse on a cliff at sunset, oil painting",
        },
      ],
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. El Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/stability/sdxl-1.0-masking/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"init_image\": \"https://storage.googleapis.com/example-bucket/source.png\", \"mask_image\": \"https://storage.googleapis.com/example-bucket/mask.png\", \"mask_source\": \"MASK_IMAGE_WHITE\", \"seed\": 12345, \"text_prompts\": [{\"text\":\"a lighthouse on a cliff at sunset, oil painting\"}]}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/stability/sdxl-1.0-masking/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/stability/sdxl-1.0-masking/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

cfg_scale

number

Qué tan estrictamente sigue la imagen al prompt. Valor predeterminado: 7.Alcance: `0` a `35`

clip_guidance_preset

string

El preset de orientación CLIP de Stability, por ejemplo `NONE`.

extras

object

Se acepta por compatibilidad y se ignora.

init_image

string (uri)

requerido

Una URL de recurso firmada por Comfy de la imagen de origen.Formato: `uri`

mask_image

string (uri)

Una URL de recurso firmada por Comfy de la máscara. Requerida con MASK_IMAGE_WHITE y MASK_IMAGE_BLACK, rechazada con INIT_IMAGE_ALPHA.Formato: `uri`

mask_source

string

requerido

De dónde proviene la máscara. MASK_IMAGE_WHITE y MASK_IMAGE_BLACK leen `mask_image` y repintan sus píxeles blancos o negros; INIT_IMAGE_ALPHA lee el canal alfa de `init_image`.Valores posibles: `MASK_IMAGE_WHITE`, `MASK_IMAGE_BLACK`, `INIT_IMAGE_ALPHA`

sampler

string

El nombre del sampler de Stability, por ejemplo `K_DPMPP_2M`.

samples

integer

Cantidad de imágenes a generar. Valor predeterminado: 1. Cada imagen devuelta se factura.Alcance: `1` a `10`

seed

integer

Semilla para todo el lote. 0 u omitida elige una semilla aleatoria.Alcance: `0` a `…`

steps

integer

Pasos de diffusion. Valor predeterminado: 30.Alcance: `10` a `30`

style_preset

string

Preset de estilo de Stability, por ejemplo `photographic`.

text_prompts

object[]

requerido

Prompts, cada uno con un peso opcional. Un peso negativo lo convierte en prompt negativo.

text_prompts[].text

string

requerido

text_prompts[].weight

number

Generado a partir del esquema que Router sirve en `GET /v2/models/stability/sdxl-1.0-masking/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

finish_reason

string

requerido

Siempre SUCCESS en un 200.

image

string (uri)

requerido

URL firmada por Comfy de la imagen PNG (la primera), válida hasta 24 horas.Formato: `uri`

images

string (uri)[]

Solo SDXL, cuando se devolvió más de una imagen. Todas las URL de imagen firmadas por Comfy, en el orden de salida, cada una válida hasta 24 horas.

seed

integer

requerido

La semilla con la que se generó la imagen.

## Ejemplos

### Entrada
    
    
    {
      "init_image": "https://storage.googleapis.com/example-bucket/source.png",
      "mask_image": "https://storage.googleapis.com/example-bucket/mask.png",
      "mask_source": "MASK_IMAGE_WHITE",
      "seed": 12345,
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/stability/sdxl-1-0-masking/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/stability/sdxl-1-0-masking/code)

[Sdxl 1.0 Imagen a imagen](https://docs.comfy.org/es/development/comfy-router/models/stability/sdxl-1-0-image-to-image/code)[Sdxl 1.0 Text To Image](https://docs.comfy.org/es/development/comfy-router/models/stability/sdxl-1-0-text-to-image/code)
