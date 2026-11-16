---
url: https://docs.comfy.org/es/development/comfy-router/models/stability/control-style-transfer/code/
title: Usa Control Style Transfer con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:55.553261+00:00
---

# Usa Control Style Transfer con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/stability/control-style-transfer/code/

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

# Usa Control Style Transfer con Comfy Router

Copiar páginaCopiar página

Llama a stability/control-style-transfer mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `stability/control-style-transfer`, servida por Comfy Router desde Stability. **Entrada:** Texto, Imagen · **Salida:** Imagen

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `stability/control-style-transfer` **Endpoint:** `POST https://api.comfy.org/v2/models/stability/control-style-transfer`

  * Esperar el resultado

  * Enviar a la cola y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "stability/control-style-transfer",
            {
                "init_image": "https://storage.googleapis.com/example-bucket/photo.png",
                "seed": 12345,
                "style_image": "https://storage.googleapis.com/example-bucket/style.png",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("stability/control-style-transfer", {
      init_image: "https://storage.googleapis.com/example-bucket/photo.png",
      seed: 12345,
      style_image: "https://storage.googleapis.com/example-bucket/style.png",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/stability/control-style-transfer \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"init_image\": \"https://storage.googleapis.com/example-bucket/photo.png\", \"seed\": 12345, \"style_image\": \"https://storage.googleapis.com/example-bucket/style.png\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/stability/control-style-transfer/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "stability/control-style-transfer",
                {
                    "init_image": "https://storage.googleapis.com/example-bucket/photo.png",
                    "seed": 12345,
                    "style_image": "https://storage.googleapis.com/example-bucket/style.png",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("stability/control-style-transfer", {
      init_image: "https://storage.googleapis.com/example-bucket/photo.png",
      seed: 12345,
      style_image: "https://storage.googleapis.com/example-bucket/style.png",
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
    curl https://api.comfy.org/v2/models/stability/control-style-transfer/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"init_image\": \"https://storage.googleapis.com/example-bucket/photo.png\", \"seed\": 12345, \"style_image\": \"https://storage.googleapis.com/example-bucket/style.png\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/stability/control-style-transfer/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/stability/control-style-transfer/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

change_strength

number

Cuánto puede alejarse el resultado de `init_image`. Valor predeterminado: 0.9.Rango: `0.1` a `1`

composition_fidelity

number

Qué tan fielmente se conserva la composición de `init_image`. Valor predeterminado: 0.9.Rango: `0` a `1`

init_image

string (uri)

requerido

Una URL de recurso firmada por Comfy de la imagen a la que se le cambiará el estilo.Formato: `uri`

negative_prompt

string

Qué excluir de la imagen.

output_format

string

Solo devuelve `png`.Valores posibles: `png`

prompt

string

Sugerencia opcional para el resultado.

seed

integer

0 o si se omite, se elige una semilla aleatoria.Rango: `0` a `4294967294`

style_image

string (uri)

requerido

Una URL de recurso firmada por Comfy de la fuente de estilo.Formato: `uri`

style_preset

string

Se acepta pero no se aplica.

style_strength

number

Qué tan intensamente se aplica el estilo. Valor predeterminado: 1.Rango: `0` a `1`

Generado a partir del esquema que Router publica en `GET /v2/models/stability/control-style-transfer/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

finish_reason

string

requerido

Siempre SUCCESS con un 200.

image

string (uri)

requerido

URL firmada por Comfy de la imagen PNG (la primera), válida durante un máximo de 24 horas.Formato: `uri`

images

string (uri)[]

Solo SDXL, cuando se devolvió más de una imagen. Todas las URL de imagen firmadas por Comfy, en el orden de salida, cada una válida durante un máximo de 24 horas.

seed

integer

requerido

La semilla con la que se generó la imagen.

## Ejemplos

### Entrada
    
    
    {
      "init_image": "https://storage.googleapis.com/example-bucket/photo.png",
      "seed": 12345,
      "style_image": "https://storage.googleapis.com/example-bucket/style.png"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/stability/control-style-transfer/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/stability/control-style-transfer/code)

[Control Structure](https://docs.comfy.org/es/development/comfy-router/models/stability/control-structure/code)[Control Style](https://docs.comfy.org/es/development/comfy-router/models/stability/control-style/code)
