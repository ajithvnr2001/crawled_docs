---
url: https://docs.comfy.org/es/development/comfy-router/models/krea/krea-2-medium-turbo/code/
title: Usa Krea 2 Medium Turbo con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:09.331749+00:00
---

# Usa Krea 2 Medium Turbo con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/krea/krea-2-medium-turbo/code/

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



Krea

# Usa Krea 2 Medium Turbo con Comfy Router

Copiar páginaCopiar página

Llama a krea/krea-2-medium-turbo con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `krea/krea-2-medium-turbo`, servida por Comfy Router de Krea. **Entrada:** Texto · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `krea/krea-2-medium-turbo` **Endpoint:** `POST https://api.comfy.org/v2/models/krea/krea-2-medium-turbo`

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
            "krea/krea-2-medium-turbo",
            {
                "aspect_ratio": "1:1",
                "prompt": "a red circle",
                "resolution": "1K",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("krea/krea-2-medium-turbo", {
      aspect_ratio: "1:1",
      prompt: "a red circle",
      resolution: "1K",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/krea/krea-2-medium-turbo \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"1:1\", \"prompt\": \"a red circle\", \"resolution\": \"1K\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/krea/krea-2-medium-turbo/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "krea/krea-2-medium-turbo",
                {
                    "aspect_ratio": "1:1",
                    "prompt": "a red circle",
                    "resolution": "1K",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("krea/krea-2-medium-turbo", {
      aspect_ratio: "1:1",
      prompt: "a red circle",
      resolution: "1K",
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
    curl https://api.comfy.org/v2/models/krea/krea-2-medium-turbo/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"aspect_ratio\": \"1:1\", \"prompt\": \"a red circle\", \"resolution\": \"1K\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/krea/krea-2-medium-turbo/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/krea/krea-2-medium-turbo/requests/$REQUEST_ID \
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

requerido

Relación de aspecto. Una de: 1:1, 4:3, 3:2, 16:9, 2.35:1, 4:5, 2:3, 9:16.Valores posibles: `1:1`, `4:3`, `3:2`, `16:9`, `2.35:1`, `4:5`, `2:3`, `9:16`

​

creativity

string

predeterminado:"\"medium\""

Intensidad de interpretación del prompt: raw=0, low=10, medium=50, high=100.Valores posibles: `raw`, `low`, `medium`, `high`

​

image_style_references

object[]

Referencias de estilo que se usarán para la generación

​

image_style_references[].strength

number

requerido

Rango: `-2` a `2`Formato: `double`

​

image_style_references[].url

string (uri)

Formato: `uri`

​

moodboards

object[]

Moodboards que se usarán para la generación. Actualmente limitado a un moodboard.

​

moodboards[].id

string (uuid)

requerido

Formato: `uuid`

​

moodboards[].strength

number

predeterminado:"0.35"

Rango: `-0.5` a `1.5`Formato: `double`

​

prompt

string

requerido

​

resolution

string

requerido

Escala de resolución. Una de: 1K.Valores posibles: `1K`

​

seed

number

​

styles

object[]

Estilos (normalmente LoRAs) que se usarán para la generación

​

styles[].id

string

requerido

​

styles[].strength

number

requerido

Rango: `-2` a `2`Formato: `double`

Generado a partir del esquema que Router sirve en `GET /v2/models/krea/krea-2-medium-turbo/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

completed_at

string (date-time)

requerido

Formato: `date-time`

​

created_at

string (date-time)

requerido

Formato: `date-time`

​

job_id

string (uuid)

requerido

Formato: `uuid`

​

result

object

requerido

La generación finalizada. Aquí no admite null, a diferencia de en `KreaJob`: una tarea terminal cuyo `result` no lleva `urls` recibe como respuesta un error de Comfy Router, así que un `200` siempre lo incluye.

​

result.style_id

string

Lo establecen las tareas de loraTraining, no una generación; un `200` para estos modelos trae `urls`.

​

result.urls

string (uri)[]

requerido

Las imágenes generadas, como enlaces descargables. Al menos una, porque una tarea `completed` con `urls` vacío es `success_without_output` y nunca llega a este documento.

​

status

string

requerido

Siempre `completed` en este documento: es el único estado que Router reporta como éxito, y el vocabulario de Krea se compara tal cual, sin normalizar mayúsculas y minúsculas.Valores posibles: `completed`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "aspect_ratio": "1:1",
      "prompt": "a red circle",
      "resolution": "1K"
    }
    

### 

​

Salida
    
    
    {
      "completed_at": "2027-01-01T00:00:37Z",
      "created_at": "2027-01-01T00:00:00Z",
      "job_id": "7f1c2e84-5b90-4a37-8d61-2c0f9ab4e153",
      "result": {
        "urls": [
          "https://example.invalid/krea/krea-2/generated.png"
        ]
      },
      "status": "completed"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/krea/krea-2-medium-turbo/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/krea/krea-2-medium-turbo/code)

[Krea 2 Large](https://docs.comfy.org/es/development/comfy-router/models/krea/krea-2-large/code)[Krea 2 Medium](https://docs.comfy.org/es/development/comfy-router/models/krea/krea-2-medium/code)
