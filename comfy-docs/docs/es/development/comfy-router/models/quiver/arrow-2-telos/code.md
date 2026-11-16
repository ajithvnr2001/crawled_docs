---
url: https://docs.comfy.org/es/development/comfy-router/models/quiver/arrow-2-telos/code/
title: Usar Arrow 2 Telos con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:55.204472+00:00
---

# Usar Arrow 2 Telos con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/quiver/arrow-2-telos/code/

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



Quiver

# Usar Arrow 2 Telos con Comfy Router

Copiar páginaCopiar página

Llama a quiver/arrow-2-telos con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `quiver/arrow-2-telos`, servido por Comfy Router desde Quiver. **Entrada:** Texto, Imagen · **Salida:** Imagen

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP sin procesar. **ID del modelo:** `quiver/arrow-2-telos` **Endpoint:** `POST https://api.comfy.org/v2/models/quiver/arrow-2-telos`

  * Esperar el resultado

  * Poner en cola y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "quiver/arrow-2-telos",
            {
                "n": 1,
                "prompt": "A single red maple leaf on a plain white background.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("quiver/arrow-2-telos", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/quiver/arrow-2-telos \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/quiver/arrow-2-telos/requests`. Router responde `201` con un `request_id` en cuanto admite la ejecución, y recoges el resultado cuando esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) detalla el estado, la cancelación y la recogida.

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
                "quiver/arrow-2-telos",
                {
                    "n": 1,
                    "prompt": "A single red maple leaf on a plain white background.",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
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
    const handle = await comfy.models.submit("quiver/arrow-2-telos", {
      n: 1,
      prompt: "A single red maple leaf on a plain white background.",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló provoca un rechazo aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/quiver/arrow-2-telos/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"n\": 1, \"prompt\": \"A single red maple leaf on a plain white background.\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/quiver/arrow-2-telos/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/quiver/arrow-2-telos/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

instructions

string

Orientación adicional sobre estilo o formato

max_output_tokens

integer

Número máximo de tokens de salidaRango: `1` a `131072`

model

string

Identificador del modelo para la generación de SVG

n

integer

predeterminado:"1"

Cantidad de SVG a generarRango: `1` a `16`

presence_penalty

number

predeterminado:"0"

Penalización para los tokens ya presentes en la salida previa. `arrow-2-telos` la ignora, ya que no acepta parámetros de muestreo; el campo se elimina de la solicitud antes de reenviarla, sin generar un error.Rango: `-2` a `2`

prompt

string

requerido

Descripción de texto del SVG de salida deseado

references

object | string (uri)[]

Imágenes de referencia opcionales para orientar el estilo y la composición. Acepta un objeto URL, un objeto base64 o la forma abreviada de cadena URL. Los límites en tiempo de ejecución dependen de cada modelo.

temperature

number

predeterminado:"1"

Temperatura de muestreo. `arrow-2-telos` la ignora, ya que no acepta parámetros de muestreo; el campo se elimina de la solicitud antes de reenviarla, sin generar un error.Rango: `0` a `2`

top_p

number

predeterminado:"1"

Probabilidad de muestreo por núcleo. `arrow-2-telos` la ignora, ya que no acepta parámetros de muestreo; el campo se elimina de la solicitud antes de reenviarla, sin generar un error.Rango: `0` a `1`

Generado a partir del esquema que Router sirve en `GET /v2/models/quiver/arrow-2-telos/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

created

integer

requerido

Marca de tiempo Unix de creación

credits

integer

Costo en créditos para los modelos de créditos fijos como arrow-1.1. Se omite en los modelos con precio por token como arrow-2, que reportan los totales de tokens medidos en usage.Rango: `0` a `…`

data

object[]

requerido

data[].mime_type

string

requerido

Tipo MIME de la salidaValores posibles: `image/svg+xml`

data[].svg

string

requerido

Marcado SVG sin procesar

id

string

requerido

Identificador único de la generación

usage

object

Totales de tokens para los modelos con precio por token como arrow-2. Los modelos de créditos fijos pueden reportar ceros aquí.

usage.input_tokens

integer

Cantidad de tokens de entrada para los modelos con precio por token.Rango: `0` a `…`

usage.output_tokens

integer

Cantidad de tokens de salida para los modelos con precio por token.Rango: `0` a `…`

usage.total_tokens

integer

Cantidad total de tokens para los modelos con precio por token.Rango: `0` a `…`

## Ejemplos

### Entrada
    
    
    {
      "n": 1,
      "prompt": "A single red maple leaf on a plain white background."
    }
    

### Salida
    
    
    {
      "created": 1767225600,
      "data": [
        {
          "mime_type": "image/svg+xml",
          "svg": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 64 64\"><path d=\"M32 4 44 28 60 30 48 42 52 60 32 50 12 60 16 42 4 30 20 28Z\"/></svg>"
        }
      ],
      "id": "svg_018f2c7a4b1e7c3d9a056e2f8b41d0c9",
      "usage": {
        "input_tokens": 180,
        "output_tokens": 240,
        "total_tokens": 420
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/quiver/arrow-2-telos/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/quiver/arrow-2-telos/code)

[P Video 2](https://docs.comfy.org/es/development/comfy-router/models/pruna/p-video-2/code)[Arrow 2](https://docs.comfy.org/es/development/comfy-router/models/quiver/arrow-2/code)
