---
url: https://docs.comfy.org/es/development/comfy-router/models/stability/stable-fast-3d/code/
title: Usa Stable Fast 3D con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:51:57.837677+00:00
---

# Usa Stable Fast 3D con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/stability/stable-fast-3d/code/

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

# Usa Stable Fast 3D con Comfy Router

Copiar páginaCopiar página

Llama a stability/stable-fast-3d mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `stability/stable-fast-3d`, servido por Comfy Router de Stability. **Entrada:** Imagen · **Salida:** 3D

## Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **Model ID:** `stability/stable-fast-3d` **Endpoint:** `POST https://api.comfy.org/v2/models/stability/stable-fast-3d`

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
            "stability/stable-fast-3d",
            {
                "foreground_ratio": 0.85,
                "image": "https://storage.googleapis.com/example-bucket/source.png",
                "remesh": "none",
                "texture_resolution": 1024,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("stability/stable-fast-3d", {
      foreground_ratio: 0.85,
      image: "https://storage.googleapis.com/example-bucket/source.png",
      remesh: "none",
      texture_resolution: 1024,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/stability/stable-fast-3d \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"foreground_ratio\": 0.85, \"image\": \"https://storage.googleapis.com/example-bucket/source.png\", \"remesh\": \"none\", \"texture_resolution\": 1024}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/stability/stable-fast-3d/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "stability/stable-fast-3d",
                {
                    "foreground_ratio": 0.85,
                    "image": "https://storage.googleapis.com/example-bucket/source.png",
                    "remesh": "none",
                    "texture_resolution": 1024,
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
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
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("stability/stable-fast-3d", {
      foreground_ratio: 0.85,
      image: "https://storage.googleapis.com/example-bucket/source.png",
      remesh: "none",
      texture_resolution: 1024,
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Aquí se rechaza una solicitud que falló o se canceló.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/stability/stable-fast-3d/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"foreground_ratio\": 0.85, \"image\": \"https://storage.googleapis.com/example-bucket/source.png\", \"remesh\": \"none\", \"texture_resolution\": 1024}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/stability/stable-fast-3d/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/stability/stable-fast-3d/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## Esquema

### Entrada

foreground_ratio

number

Qué proporción del encuadre ocupa el sujeto. Predeterminado 0.85.Rango: `0.1` a `1`

image

string (uri)

requerido

Una URL de recurso firmada por Comfy de la imagen de origen.Formato: `uri`

remesh

string

Modo de remallado. Predeterminado `none`.Valores posibles: `none`, `triangle`, `quad`

texture_resolution

integer

Tamaño de textura. Predeterminado 1024.Valores posibles: `512`, `1024`, `2048`

vertex_count

integer

Recuento de vértices objetivo. -1 deja el recuento propio del gráfico. Predeterminado -1.Rango: `-1` a `20000`

Generado a partir del esquema que Router sirve en `GET /v2/models/stability/stable-fast-3d/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### Salida

finish_reason

string

requerido

Siempre SUCCESS en un 200.

model

string (uri)

requerido

URL firmada por Comfy del GLB, válida por hasta 24 horas.Formato: `uri`

## Ejemplos

### Entrada
    
    
    {
      "foreground_ratio": 0.85,
      "image": "https://storage.googleapis.com/example-bucket/source.png",
      "remesh": "none",
      "texture_resolution": 1024
    }
    

### Salida
    
    
    {
      "finish_reason": "SUCCESS",
      "model": "https://example.invalid/stability/model.glb"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/stability/stable-fast-3d/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/stability/stable-fast-3d/code)

[Sdxl 1.0 Text To Image](https://docs.comfy.org/es/development/comfy-router/models/stability/sdxl-1-0-text-to-image/code)[Stable Point Aware 3D](https://docs.comfy.org/es/development/comfy-router/models/stability/stable-point-aware-3d/code)
