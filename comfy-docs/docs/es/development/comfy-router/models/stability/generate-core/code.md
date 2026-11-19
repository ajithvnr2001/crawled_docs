---
url: https://docs.comfy.org/es/development/comfy-router/models/stability/generate-core/code/
title: Usar Generate Core con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-19T16:26:09.215548+00:00
---

# Usar Generate Core con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/stability/generate-core/code/

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

# Usar Generate Core con Comfy Router

Copiar páginaCopiar página

Llama a stability/generate-core mediante Comfy Router: el endpoint, la forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `stability/generate-core`, servido por Comfy Router desde Stability. **Entrada:** Texto · **Salida:** Imagen

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada con HTTP sin procesar. **ID del modelo:** `stability/generate-core` **Endpoint:** `POST https://api.comfy.org/v2/models/stability/generate-core`

  * Esperar el resultado

  * Enviar a la cola y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY desde el entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "stability/generate-core",
            {
                "aspect_ratio": "16:9",
                "prompt": "a lighthouse on a cliff at sunset, oil painting",
                "seed": 12345,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY desde el entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("stability/generate-core", {
      aspect_ratio: "16:9",
      prompt: "a lighthouse on a cliff at sunset, oil painting",
      seed: 12345,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/stability/generate-core \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"prompt\": \"a lighthouse on a cliff at sunset, oil painting\", \"seed\": 12345}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/stability/generate-core/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY desde el entorno.
    # Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "stability/generate-core",
                {
                    "aspect_ratio": "16:9",
                    "prompt": "a lighthouse on a cliff at sunset, oil painting",
                    "seed": 12345,
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY desde el entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("stability/generate-core", {
      aspect_ratio: "16:9",
      prompt: "a lighthouse on a cliff at sunset, oil painting",
      seed: 12345,
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud fallida o cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/stability/generate-core/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"16:9\", \"prompt\": \"a lighthouse on a cliff at sunset, oil painting\", \"seed\": 12345}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/stability/generate-core/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/stability/generate-core/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

aspect_ratio

string

Solo texto a imagen. Relación de aspecto de salida. Por defecto 1:1.Valores posibles: `1:1`, `16:9`, `9:16`, `21:9`, `9:21`, `3:2`, `2:3`, `5:4`, `4:5`

image

string (uri)

Solo para `stability/generate-ultra`. Una URL de recurso firmada por Comfy de una imagen de origen; enviarla cambia a imagen a imagen y requiere `strength`. Se rechaza con un error 400 en `stability/generate-core`.Formato: `uri`

negative_prompt

string

Lo que quieres mantener fuera de la imagen.

output_format

string

Solo se devuelve `png`.Valores posibles: `png`

prompt

string

requerido

Lo que quieres generar.

seed

integer

0 u omitido elige una semilla aleatoria.Alcance: `0` a `4294967294`

strength

number

Solo para imagen a imagen de `stability/generate-ultra`. Cuánto mover desde la imagen de origen; 1 la ignora. Se rechaza con un error 400 en `stability/generate-core`.Alcance: `0` a `1`

style_preset

string

Preajuste de estilo de Stability, por ejemplo `photographic`.

Generado a partir del esquema que Router sirve en `GET /v2/models/stability/generate-core/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

finish_reason

string

requerido

Siempre SUCCESS en una respuesta 200.

image

string (uri)

requerido

URL firmada por Comfy de la (primera) imagen PNG, válida hasta por 24 horas.Formato: `uri`

images

string (uri)[]

Solo SDXL, cuando se devolvió más de una imagen. Todas las URL de imagen firmadas por Comfy, en el orden de salida, cada una válida hasta por 24 horas.

seed

integer

requerido

La semilla con la que se generó la imagen.

## Ejemplos

### Entrada
    
    
    {
      "aspect_ratio": "16:9",
      "prompt": "a lighthouse on a cliff at sunset, oil painting",
      "seed": 12345
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/stability/generate-core/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/stability/generate-core/code)

[Edit Search And Replace](https://docs.comfy.org/es/development/comfy-router/models/stability/edit-search-and-replace/code)[Generate Ultra](https://docs.comfy.org/es/development/comfy-router/models/stability/generate-ultra/code)
