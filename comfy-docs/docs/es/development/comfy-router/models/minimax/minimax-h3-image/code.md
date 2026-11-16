---
url: https://docs.comfy.org/es/development/comfy-router/models/minimax/minimax-h3-image/code/
title: Usa MiniMax H3 Image con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:54.397227+00:00
---

# Usa MiniMax H3 Image con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/minimax/minimax-h3-image/code/

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



MiniMax

# Usa MiniMax H3 Image con Comfy Router

Copiar páginaCopiar página

Llama a minimax/minimax-h3-image con Comfy Router: endpoint, forma de la solicitud y respuesta del Router.

Copiar páginaCopiar página

Referencia de la API para `minimax/minimax-h3-image`, servida por Comfy Router de MiniMax. **Entrada:** Texto, Imagen · **Salida:** Imagen

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `minimax/minimax-h3-image` **Endpoint:** `POST https://api.comfy.org/v2/models/minimax/minimax-h3-image`

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
            "minimax/minimax-h3-image",
            {
                "area": "1K",
                "prompt": "A single red maple leaf resting on a plain white background.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("minimax/minimax-h3-image", {
      area: "1K",
      prompt: "A single red maple leaf resting on a plain white background.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/minimax/minimax-h3-image \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"area\": \"1K\", \"prompt\": \"A single red maple leaf resting on a plain white background.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/minimax/minimax-h3-image/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "minimax/minimax-h3-image",
                {
                    "area": "1K",
                    "prompt": "A single red maple leaf resting on a plain white background.",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("minimax/minimax-h3-image", {
      area: "1K",
      prompt: "A single red maple leaf resting on a plain white background.",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud fallida o cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/minimax/minimax-h3-image/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"area\": \"1K\", \"prompt\": \"A single red maple leaf resting on a plain white background.\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/minimax/minimax-h3-image/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/minimax/minimax-h3-image/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

area

string

Nivel de área de salida cuando `size` se omite o es `auto`. Uno de `1K`, `2K`, `4K` (predeterminado).

aspect_ratio

string

Relación de aspecto de salida cuando `size` se omite o es `auto`. `auto` (predeterminado) o `X:Y` entre 1:3 y 3:1, por ejemplo `16:9`.

disable_prompt_enhanced

boolean

predeterminado:"false"

Desactiva la mejora de prompt de MiniMax. Requiere un `size` fijo o un `aspect_ratio` con formato `X:Y`.

images

object[]

Imágenes de referencia opcionales. Cuando están presentes, la solicitud se ejecuta como una edición de imagen, exactamente igual que en la ruta de ediciones.

images[].image_url

string

requerido

Una URL http(s) pública o un URI `data:image/<format>;base64,`. JPEG, PNG, WEBP, HEIC o HEIF, cada lado de 128 a 8192 px, con el lado largo como máximo 4 veces el lado corto.

model

string

Nombre del modelo. `MiniMax-H3-Image` o `MiniMax-H3-Image-Highspeed`. Quienes llaman al Router pueden omitir este campo o enviar null; el Router completa el modelo seleccionado por la ruta de la solicitud.

n

integer

predeterminado:"1"

Número de imágenes. Los tokens de entrada se cobran una vez por imagen.Alcance: `1` a `10`

output_compression

integer

Calidad de compresión para `jpeg` y `webp`, predeterminado 95.Alcance: `0` a `100`

output_format

string

Formato de la imagen de salida. Uno de `png`, `jpeg`, `jpg` (predeterminado), `webp`.

prompt

string

requerido

Descripción de texto de la imagen. Con `images`, la descripción de la edición; las imágenes de referencia son imagen 1, imagen 2 y así sucesivamente, en el orden del arreglo.

size

string

Tamaño de salida, `auto` (predeterminado) o `WIDTHxHEIGHT`, por ejemplo `2720x1536`. Un tamaño fijo debe tener un área de 655,360 a 20,000,000 píxeles y una relación de aspecto entre 1:3 y 3:1, y no se puede combinar con `aspect_ratio` ni con `area`.

Generado a partir del esquema que el Router publica en `GET /v2/models/minimax/minimax-h3-image/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

created

integer

Formato: `int64`

data

object[]

data[].error

object

Presente solo cuando esta imagen falló o fue retenida.

data[].error.code

string

data[].error.message

string

data[].revised_prompt

string

El prompt que MiniMax usó para esta imagen.

data[].size

string

Tamaño real de la imagen como `WIDTHxHEIGHT`.

data[].url

string

URL de la imagen generada. Caduca, así que descarga la imagen.

output_format

string

request_id

string

usage

object

Uso de tokens de las imágenes exitosas. La facturación se basa en él.

usage.generated_images

integer

usage.input_tokens

integer

usage.input_tokens_details

object

usage.input_tokens_details.image_tokens

integer

usage.input_tokens_details.text_tokens

integer

usage.output_tokens

integer

usage.output_tokens_details

object

usage.output_tokens_details.image_tokens

integer

usage.total_tokens

integer

## Ejemplos

### Entrada
    
    
    {
      "area": "1K",
      "prompt": "A single red maple leaf resting on a plain white background."
    }
    

### Salida
    
    
    {
      "created": 1794300000,
      "data": [
        {
          "size": "1024x1024",
          "url": "https://example.invalid/minimax/minimax-h3-image/generated.jpg"
        }
      ],
      "output_format": "jpeg",
      "request_id": "06a1b2c3d4e5f60718293a4b5c6d7e8f",
      "usage": {
        "generated_images": 1,
        "input_tokens": 10,
        "input_tokens_details": {
          "image_tokens": 0,
          "text_tokens": 10
        },
        "output_tokens": 1024,
        "output_tokens_details": {
          "image_tokens": 1024
        },
        "total_tokens": 1034
      }
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/minimax/minimax-h3-image/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/minimax/minimax-h3-image/code)

[MiniMax H3 Image Highspeed](https://docs.comfy.org/es/development/comfy-router/models/minimax/minimax-h3-image-highspeed/code)[MiniMax H3](https://docs.comfy.org/es/development/comfy-router/models/minimax/minimax-h3/code)
