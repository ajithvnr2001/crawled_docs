---
url: https://docs.comfy.org/es/development/comfy-router/models/moonvalley/image-to-video/code/
title: Usa Image To Video con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:11.525540+00:00
---

# Usa Image To Video con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/moonvalley/image-to-video/code/

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



Moonvalley

# Usa Image To Video con Comfy Router

Copiar páginaCopiar página

Llama a moonvalley/image-to-video con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `moonvalley/image-to-video`, servida por Comfy Router desde Moonvalley. **Entrada:** Imagen, Texto · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `moonvalley/image-to-video` **Endpoint:** `POST https://api.comfy.org/v2/models/moonvalley/image-to-video`

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
            "moonvalley/image-to-video",
            {
                "image_url": "https://yavuzceliker.github.io/sample-images/image-1021.jpg",
                "prompt_text": "a single red maple leaf falling onto still water",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("moonvalley/image-to-video", {
      image_url: "https://yavuzceliker.github.io/sample-images/image-1021.jpg",
      prompt_text: "a single red maple leaf falling onto still water",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/moonvalley/image-to-video \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://yavuzceliker.github.io/sample-images/image-1021.jpg\", \"prompt_text\": \"a single red maple leaf falling onto still water\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/moonvalley/image-to-video/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "moonvalley/image-to-video",
                {
                    "image_url": "https://yavuzceliker.github.io/sample-images/image-1021.jpg",
                    "prompt_text": "a single red maple leaf falling onto still water",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o fue cancelada lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("moonvalley/image-to-video", {
      image_url: "https://yavuzceliker.github.io/sample-images/image-1021.jpg",
      prompt_text: "a single red maple leaf falling onto still water",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o fue cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/moonvalley/image-to-video/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image_url\": \"https://yavuzceliker.github.io/sample-images/image-1021.jpg\", \"prompt_text\": \"a single red maple leaf falling onto still water\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/moonvalley/image-to-video/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge el resultado. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/moonvalley/image-to-video/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

image_url

string

​

inference_params

object

​

inference_params.guidance_scale

number

predeterminado:"10"

Escala de orientación para el control de la generaciónFormato: `float`

​

inference_params.height

integer

predeterminado:"1080"

Alto del video generado en píxeles

​

inference_params.negative_prompt

string

Texto del prompt negativo

​

inference_params.seed

integer

predeterminado:"9"

Semilla aleatoria para la generación (predeterminada: aleatoria)

​

inference_params.steps

integer

predeterminado:"80"

Cantidad de pasos de eliminación de ruido

​

inference_params.use_negative_prompts

boolean

predeterminado:"true"

Indica si se usan prompts negativos

​

inference_params.width

integer

predeterminado:"1920"

Ancho del video generado en píxeles

​

prompt_text

string

​

webhook_url

string

​

keyframes

object

Generado a partir del esquema que Router publica en `GET /v2/models/moonvalley/image-to-video/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

error

object

​

frame_conditioning

object

​

id

string

​

inference_params

object

​

meta

object

​

model_params

object

​

output_url

string

requerido

​

prompt_text

string

​

status

string

requerido

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "image_url": "https://yavuzceliker.github.io/sample-images/image-1021.jpg",
      "prompt_text": "a single red maple leaf falling onto still water"
    }
    

### 

​

Salida
    
    
    {
      "id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9",
      "output_url": "https://example.invalid/moonvalley/prompts/output.mp4",
      "prompt_text": "a single red maple leaf falling onto still water",
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/moonvalley/image-to-video/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/moonvalley/image-to-video/code)

[MiniMax H3](https://docs.comfy.org/es/development/comfy-router/models/minimax/minimax-h3/code)[Texto a video](https://docs.comfy.org/es/development/comfy-router/models/moonvalley/text-to-video/code)
