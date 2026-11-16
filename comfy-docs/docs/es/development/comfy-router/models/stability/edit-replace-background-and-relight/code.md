---
url: https://docs.comfy.org/es/development/comfy-router/models/stability/edit-replace-background-and-relight/code/
title: Usar Edit Replace Background And Relight con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:56.138048+00:00
---

# Usar Edit Replace Background And Relight con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/stability/edit-replace-background-and-relight/code/

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

# Usar Edit Replace Background And Relight con Comfy Router

Copiar páginaCopiar página

Llama a stability/edit-replace-background-and-relight con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `stability/edit-replace-background-and-relight`, servida por Comfy Router desde Stability. **Entrada:** Texto, Imagen · **Salida:** Imagen

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `stability/edit-replace-background-and-relight` **Endpoint:** `POST https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight`

  * Esperar el resultado

  * Enviar a la cola y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "stability/edit-replace-background-and-relight",
            {
                "background_prompt": "a sunlit beach at golden hour",
                "light_source_direction": "above",
                "light_source_strength": 0.5,
                "seed": 12345,
                "subject_image": "https://storage.googleapis.com/example-bucket/subject.png",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("stability/edit-replace-background-and-relight", {
      background_prompt: "a sunlit beach at golden hour",
      light_source_direction: "above",
      light_source_strength: 0.5,
      seed: 12345,
      subject_image: "https://storage.googleapis.com/example-bucket/subject.png",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"background_prompt\": \"a sunlit beach at golden hour\", \"light_source_direction\": \"above\", \"light_source_strength\": 0.5, \"seed\": 12345, \"subject_image\": \"https://storage.googleapis.com/example-bucket/subject.png\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "stability/edit-replace-background-and-relight",
                {
                    "background_prompt": "a sunlit beach at golden hour",
                    "light_source_direction": "above",
                    "light_source_strength": 0.5,
                    "seed": 12345,
                    "subject_image": "https://storage.googleapis.com/example-bucket/subject.png",
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
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("stability/edit-replace-background-and-relight", {
      background_prompt: "a sunlit beach at golden hour",
      light_source_direction: "above",
      light_source_strength: 0.5,
      seed: 12345,
      subject_image: "https://storage.googleapis.com/example-bucket/subject.png",
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
    curl https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"background_prompt\": \"a sunlit beach at golden hour\", \"light_source_direction\": \"above\", \"light_source_strength\": 0.5, \"seed\": 12345, \"subject_image\": \"https://storage.googleapis.com/example-bucket/subject.png\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/stability/edit-replace-background-and-relight/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

background_prompt

string

El nuevo fondo. Requerido cuando se omite `background_reference`.

background_reference

string (uri)

URL de un recurso firmado por Comfy de una imagen que sirve de referencia para el nuevo fondo.Formato: `uri`

foreground_prompt

string

Qué es el sujeto.

keep_original_background

string

`true` conserva elementos del fondo original. Predeterminado `false`. Es una cadena, como en los campos de formulario de Stability.Valores posibles: `true`, `false`

light_reference

string (uri)

URL de un recurso firmado por Comfy de una imagen que sirve de referencia para la iluminación.Formato: `uri`

light_source_direction

string

De dónde viene la luz. `left` no está disponible.Valores posibles: `right`, `below`, `above`

light_source_strength

number

Qué tan intensa es la luz. Requiere `light_reference` o `light_source_direction`.Rango: `0` a `1`

negative_prompt

string

Lo que quieres mantener fuera de la imagen.

original_background_depth

number

Qué tan fielmente el nuevo fondo coincide con la profundidad del sujeto. Predeterminado 0.5.Rango: `0` a `1`

output_format

string

Solo se devuelve `png`.Valores posibles: `png`

preserve_original_subject

number

Qué tan exactamente se conserva el sujeto original. Predeterminado 0.6.Rango: `0` a `1`

seed

integer

`0` o si se omite, se elige una semilla al azar.Rango: `0` a `4294967294`

subject_image

string (uri)

requerido

URL de un recurso firmado por Comfy de la imagen cuyo sujeto se conserva.Formato: `uri`

Generado a partir del esquema que Router sirve en `GET /v2/models/stability/edit-replace-background-and-relight/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

finish_reason

string

requerido

Siempre SUCCESS en una respuesta 200.

image

string (uri)

requerido

URL firmada por Comfy de la (primera) imagen PNG, válida por hasta 24 horas.Formato: `uri`

images

string (uri)[]

Solo SDXL, cuando se devolvió más de una imagen. Cada URL de imagen firmada por Comfy, en el orden de salida, válida por hasta 24 horas.

seed

integer

requerido

La semilla con la que se generó la imagen.

## Ejemplos

### Entrada
    
    
    {
      "background_prompt": "a sunlit beach at golden hour",
      "light_source_direction": "above",
      "light_source_strength": 0.5,
      "seed": 12345,
      "subject_image": "https://storage.googleapis.com/example-bucket/subject.png"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/stability/edit-replace-background-and-relight/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/stability/edit-replace-background-and-relight/code)

[Edit Remove Background](https://docs.comfy.org/es/development/comfy-router/models/stability/edit-remove-background/code)[Edit Search And Recolor](https://docs.comfy.org/es/development/comfy-router/models/stability/edit-search-and-recolor/code)
