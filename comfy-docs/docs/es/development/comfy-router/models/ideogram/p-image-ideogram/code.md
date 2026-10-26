---
url: https://docs.comfy.org/es/development/comfy-router/models/ideogram/p-image-ideogram/code/
title: Usa P Image Ideogram con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:07.280122+00:00
---

# Usa P Image Ideogram con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/ideogram/p-image-ideogram/code/

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



Ideogram

# Usa P Image Ideogram con Comfy Router

Copiar páginaCopiar página

Llama a ideogram/p-image-ideogram desde Comfy Router: endpoint, forma de la solicitud y respuesta del Router.

Copiar páginaCopiar página

Referencia de API para `ideogram/p-image-ideogram`, servida por Comfy Router desde Ideogram. **Entrada:** Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `ideogram/p-image-ideogram` **Endpoint:** `POST https://api.comfy.org/v2/models/ideogram/p-image-ideogram`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Reads COMFY_API_KEY from the environment.
    # The SDK automatically creates an idempotency key and reuses it for automatic retries.
    with Comfy() as client:
        result = client.models.run(
            "ideogram/p-image-ideogram",
            {
                "prompt": "A beautiful mountain landscape",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // The SDK automatically creates an idempotency key and reuses it for automatic retries.
    const { data } = await comfy.models.run("ideogram/p-image-ideogram", {
      prompt: "A beautiful mountain landscape",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/ideogram/p-image-ideogram \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A beautiful mountain landscape\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/ideogram/p-image-ideogram/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Reads COMFY_API_KEY from the environment.
    # Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "ideogram/p-image-ideogram",
                {
                    "prompt": "A beautiful mountain landscape",
                },
            )
            print("request_id:", handle.request_id)  # with the model ID, all another process needs
    
            # Poll until the request completes, waiting the Retry-After the server names.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # The provider's own payload, the same value models.run() returns.
            # A request that failed or was cancelled raises the typed Router error here.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Reads COMFY_API_KEY from the environment.
    // Each submit() call mints its own Idempotency-Key and reuses it for automatic retries.
    const handle = await comfy.models.submit("ideogram/p-image-ideogram", {
      prompt: "A beautiful mountain landscape",
    });
    console.log("requestId:", handle.requestId); // with the model ID, all another process needs
    
    // Poll until the request completes, waiting the Retry-After the server names.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // The same result models.run() returns. A request that failed or was cancelled rejects here.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Submit. Router answers 201 with request_id, status_url, response_url and cancel_url.
    curl https://api.comfy.org/v2/models/ideogram/p-image-ideogram/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"A beautiful mountain landscape\"}"
    
    # 2. Poll until status is COMPLETED, waiting the Retry-After seconds each response names.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/ideogram/p-image-ideogram/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Collect. 200 with the model's native output, 202 with the status body while it is still running.
    curl https://api.comfy.org/v2/models/ideogram/p-image-ideogram/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

aspect_ratio

string

Relación de aspecto en formato WxH. Valores admitidos: 1x3, 3x1, 1x2, 2x1, 9x16, 16x9, 10x16, 16x10, 2x3, 3x2, 3x4, 4x3, 4x5, 5x4, 1x1. El valor predeterminado es 1x1.

​

enable_copyright_detection

boolean

Activa la detección de derechos de autor posterior a la generación (comprobaciones de parecido y logotipos de Hive).

​

prompt

string

requerido

El prompt para la generación de imágenes, ya sea en lenguaje natural o un prompt estructurado en JSON de Ideogram 4.0.

​

prompt_upsampling

string

Modo de sobremuestreo del prompt. Los valores admitidos son AUTO, ON y OFF. El valor predeterminado es AUTO.

​

quality

string

Nivel de calidad de la generación. Los valores admitidos son VERY_LOW, LOW, MEDIUM y HIGH. El valor predeterminado es MEDIUM.

​

resolution

string

Resolución de salida. Los valores admitidos son 1K y 2K. El valor predeterminado es 1K.

​

seed

integer

Valor de semilla para una generación reproducible

Generado a partir del esquema que Router expone en `GET /v2/models/ideogram/p-image-ideogram/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

created

string (date-time)

Marca de tiempo de cuándo se creó la generación.Formato: `date-time`

​

data

object[]

Arreglo con la información de las imágenes generadas.

​

data[].is_image_safe

boolean

Indica si la imagen se considera segura.

​

data[].prompt

string

El prompt usado para generar esta imagen.

​

data[].resolution

string

La resolución de la imagen generada (por ejemplo, ‘1024x1024’).

​

data[].seed

integer

El valor de semilla usado para esta generación.

​

data[].style_type

string

El tipo de estilo usado para la generación (por ejemplo, ‘REALISTIC’, ‘ANIME’).

​

data[].url

string

URL de la imagen generada.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "prompt": "A beautiful mountain landscape"
    }
    

### 

​

Salida
    
    
    {
      "created": "2026-01-01T00:00:00Z",
      "data": [
        {
          "is_image_safe": true,
          "prompt": "A poster for a jazz festival, bold typography, warm colours",
          "resolution": "1024x1024",
          "seed": 918273645,
          "style_type": "REALISTIC",
          "url": "https://example.invalid/ideogram/p-image-ideogram/generated.png"
        }
      ]
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/ideogram/p-image-ideogram/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/ideogram/p-image-ideogram/code)

[Ideogram 4.0](https://docs.comfy.org/es/development/comfy-router/models/ideogram/ideogram-v4/code)[Kling 3.0 Turbo](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-3-0-turbo/code)
