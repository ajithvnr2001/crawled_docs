---
url: https://docs.comfy.org/es/development/comfy-router/models/xai/grok-imagine-video/code/
title: Usa Grok Imagine Video con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:26.370062+00:00
---

# Usa Grok Imagine Video con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/xai/grok-imagine-video/code/

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



xAI

# Usa Grok Imagine Video con Comfy Router

Copiar páginaCopiar página

Llama a xai/grok-imagine-video mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `xai/grok-imagine-video`, servida por Comfy Router desde xAI. **Entrada:** Texto, Imagen · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los snippets de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el snippet de cURL es la misma llamada por HTTP directo. **ID del modelo:** `xai/grok-imagine-video` **Endpoint:** `POST https://api.comfy.org/v2/models/xai/grok-imagine-video`

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
            "xai/grok-imagine-video",
            {
                "duration": 4,
                "prompt": "a single red maple leaf falling onto still water, slow motion",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("xai/grok-imagine-video", {
      duration: 4,
      prompt: "a single red maple leaf falling onto still water, slow motion",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/xai/grok-imagine-video \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 4, \"prompt\": \"a single red maple leaf falling onto still water, slow motion\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/xai/grok-imagine-video/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "xai/grok-imagine-video",
                {
                    "duration": 4,
                    "prompt": "a single red maple leaf falling onto still water, slow motion",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o fue cancelada lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("xai/grok-imagine-video", {
      duration: 4,
      prompt: "a single red maple leaf falling onto still water, slow motion",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indique el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o fue cancelada se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/xai/grok-imagine-video/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 4, \"prompt\": \"a single red maple leaf falling onto still water, slow motion\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indique cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/xai/grok-imagine-video/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/xai/grok-imagine-video/requests/$REQUEST_ID \
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

predeterminado:"\"16:9\""

Relación de aspecto del video generadoValores posibles: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`

​

duration

integer

predeterminado:"8"

Duración del video en segundos. Rango [1, 15]. Valor predeterminado 8.Rango: `1` a `15`

​

image

object

Objeto de imagen de entrada para los endpoints de xAI

​

image.type

string

Tipo de la entrada de imagenValores posibles: `image_url`

​

image.url

string

requerido

URL de la imagen de entrada (URL pública o URI de datos codificado en base64)

​

model

string

Modelo que se va a usar. Compatibles: grok-imagine-video (predeterminado), grok-imagine-video-1.5-preview, grok-imagine-video-1.5, grok-imagine-video-1.5-lite. El id obsoleto grok-imagine-video-beta es un alias de grok-imagine-video.

​

output

object

Destino de salida opcional para el video generado

​

prompt

string

requerido

Prompt para generar el video. Máximo 4.096 caracteres.

​

reference_images

object[]

Una o más imágenes de referencia para guiar la generación del video (modo referencia a video). Es mutuamente excluyente con image. Router reenvía solo application/json y ni este objeto ni XAIImageObject aceptan un file_id, así que las entradas de imagen respaldadas por archivo no son compatibles en esta ruta.

​

reference_images[].url

string

requerido

URL de la imagen de referencia. Admite URL HTTPS (públicas) o URL de datos codificados en base64 (por ejemplo, data:image/jpeg;base64,…).

​

resolution

string

Resolución del video de salida

​

size

string

Tamaño del video de salida

​

user

string

Un identificador único que representa a tu usuario final

Generado a partir del esquema que Router sirve en `GET /v2/models/xai/grok-imagine-video/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

block_reason

string

Nunca lleva un motivo en este documento: un motivo de bloqueo no vacío es una denegación por moderación de entrada, que Router responde como un error de Comfy Router en lugar de con este cuerpo. Ausente, null o vacío aquí.

​

model

string

El modelo usado para generar el video

​

status

string

Ausente o `done` en este documento. `pending` es el cuerpo de un sondeo que Router no ha terminado y nunca se devuelve como un `200`; Router acepta un status faltante cuando `video.url` está poblado, así que quien llama no debe exigirlo.Valores posibles: `done`

​

usage

object

Información de uso de la solicitud de generación de video

​

usage.cost_in_usd_ticks

integer

El costo de esta solicitud expresado en ticks de USD. Un centavo de USD equivale a 100.000.000 ticks, así que un dólar estadounidense equivale a 10.000.000.000 ticks.

​

video

object

requerido

La generación finalizada. Es requerido aquí, a diferencia del documento de sondeo: un resultado terminal sin `video.url` se responde como un error de Comfy Router, así que un `200` siempre lo incluye.

​

video.duration

integer

Duración del video generado en segundos

​

video.respect_moderation

boolean

Indica si el video generado por el modelo respeta las reglas de moderación

​

video.url

string

requerido

No vacío en este documento. Router informa éxito solo cuando este campo está poblado; es la URL re-alojada y firmada por Comfy descrita arriba, o la propia URL de corta duración de xAI cuando no se pudo realizar el re-alojamiento.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "duration": 4,
      "prompt": "a single red maple leaf falling onto still water, slow motion"
    }
    

### 

​

Salida
    
    
    {
      "model": "grok-imagine-video",
      "status": "done",
      "usage": {
        "cost_in_usd_ticks": 3500000000
      },
      "video": {
        "duration": 4,
        "respect_moderation": true,
        "url": "https://example.invalid/xai/grok-imagine-video/generated.mp4"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/xai/grok-imagine-video/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/xai/grok-imagine-video/code)

[Grok Imagine Video 1.5](https://docs.comfy.org/es/development/comfy-router/models/xai/grok-imagine-video-1-5/code)
