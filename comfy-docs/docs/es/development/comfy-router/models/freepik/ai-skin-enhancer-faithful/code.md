---
url: https://docs.comfy.org/es/development/comfy-router/models/freepik/ai-skin-enhancer-faithful/code/
title: Usa AI Skin Enhancer Faithful con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:04.160539+00:00
---

# Usa AI Skin Enhancer Faithful con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/freepik/ai-skin-enhancer-faithful/code/

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



Freepik

# Usa AI Skin Enhancer Faithful con Comfy Router

Copiar páginaCopiar página

Llama a freepik/ai-skin-enhancer-faithful desde Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API de `freepik/ai-skin-enhancer-faithful`, servida por Comfy Router desde Freepik. **Entrada:** Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los snippets de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el snippet de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `freepik/ai-skin-enhancer-faithful` **Endpoint:** `POST https://api.comfy.org/v2/models/freepik/ai-skin-enhancer-faithful`

  * Esperar el resultado

  * Encolar y recoger más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "freepik/ai-skin-enhancer-faithful",
            {
                "image": "https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("freepik/ai-skin-enhancer-faithful", {
      image: "https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/freepik/ai-skin-enhancer-faithful \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/freepik/ai-skin-enhancer-faithful/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge una vez que está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "freepik/ai-skin-enhancer-faithful",
                {
                    "image": "https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # El payload propio del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud fallida o cancelada lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("freepik/ai-skin-enhancer-faithful", {
      image: "https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80",
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
    curl https://api.comfy.org/v2/models/freepik/ai-skin-enhancer-faithful/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/freepik/ai-skin-enhancer-faithful/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el body de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/freepik/ai-skin-enhancer-faithful/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

image

string

requerido

Imagen de entrada. Admite codificación Base64 o URL HTTPS (debe ser accesible públicamente).

​

sharpen

integer

predeterminado:"0"

Intensidad del enfoqueRango: `0` a `100`

​

skin_detail

integer

predeterminado:"80"

Nivel de mejora del detalle de la pielRango: `0` a `100`

​

smart_grain

integer

predeterminado:"2"

Intensidad del grano inteligenteRango: `0` a `100`

​

webhook_url

string (uri)

URL de callback opcional para notificaciones asíncronas.Formato: `uri`

Generado a partir del esquema que Router publica en `GET /v2/models/freepik/ai-skin-enhancer-faithful/openapi.json`, el mismo documento con el que valida cada llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

data

object

requerido

​

data.generated

string (uri)[]

requerido

Las URL de imagen de la generación finalizada. Presentes y no vacías en el documento que devuelve Router; esta lista ES el resultado. Los enlaces son de Freepik y caducan.

​

data.status

string

requerido

Valores posibles: `COMPLETED`

​

data.task_id

string (uuid)

Formato: `uuid`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "image": "https://img.magnific.com/free-photo/portrait-woman_395237-33.jpg?w=740&q=80"
    }
    

### 

​

Salida
    
    
    {
      "data": {
        "generated": [
          "https://example.invalid/freepik/ai-skin-enhancer-faithful/enhanced.png"
        ],
        "status": "COMPLETED",
        "task_id": "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
      }
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/freepik/ai-skin-enhancer-faithful/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/freepik/ai-skin-enhancer-faithful/code)

[AI Skin Enhancer Creative](https://docs.comfy.org/es/development/comfy-router/models/freepik/ai-skin-enhancer-creative/code)[AI Skin Enhancer Flexible](https://docs.comfy.org/es/development/comfy-router/models/freepik/ai-skin-enhancer-flexible/code)
