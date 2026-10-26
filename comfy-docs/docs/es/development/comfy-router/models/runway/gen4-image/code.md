---
url: https://docs.comfy.org/es/development/comfy-router/models/runway/gen4-image/code/
title: Usa Gen 4 Image con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:19.237498+00:00
---

# Usa Gen 4 Image con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/runway/gen4-image/code/

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



Runway

# Usa Gen 4 Image con Comfy Router

Copiar páginaCopiar página

Llama a runway/gen4_image a través de Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `runway/gen4_image`, que Comfy Router sirve desde Runway. **Entrada:** Texto, Imagen · **Salida:** Imagen

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `runway/gen4_image` **Endpoint:** `POST https://api.comfy.org/v2/models/runway/gen4_image`

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
            "runway/gen4_image",
            {
                "promptText": "a red circle",
                "ratio": "1024:1024",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("runway/gen4_image", {
      promptText: "a red circle",
      ratio: "1024:1024",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/runway/gen4_image \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"promptText\": \"a red circle\", \"ratio\": \"1024:1024\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/runway/gen4_image/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "runway/gen4_image",
                {
                    "promptText": "a red circle",
                    "ratio": "1024:1024",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("runway/gen4_image", {
      promptText: "a red circle",
      ratio: "1024:1024",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/runway/gen4_image/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"promptText\": \"a red circle\", \"ratio\": \"1024:1024\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/runway/gen4_image/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras aún se ejecuta.
    curl https://api.comfy.org/v2/models/runway/gen4_image/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

model

string

Modelo que se usará para la generación. En la ruta de Comfy Router `POST /v2/models/runway/{model}`, este campo se obtiene de la ruta y NO DEBE enviarse; en la ruta v1 `POST /proxy/runway/text_to_image`, es requerido y está restringido a `gen4_image`.

​

promptText

string

requerido

Prompt de texto para la generación de la imagen

​

ratio

string

requerido

Posibles valores: `1920:1080`, `1080:1920`, `1024:1024`, `1360:768`, `1080:1080`, `1168:880`, `1440:1080`, `1080:1440`, `1808:768`, `2112:912`

​

referenceImages

object[]

Arreglo de imágenes de referencia para guiar la generación

​

referenceImages[].uri

string

requerido

Una URL HTTPS o un URI de datos que contiene una imagen codificada

Generado a partir del esquema que Router expone en `GET /v2/models/runway/gen4_image/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

createdAt

string (date-time)

requerido

Marca de tiempo de creación de la tareaFormato: `date-time`

​

id

string

requerido

ID de la tarea

​

output

string[]

Las URL de los recursos de la generación finalizada: para `runway/gen4_image`, cada elemento es una URL de IMAGEN. Disponible una vez que la tarea termina correctamente; esta lista ES el resultado.

​

progress

number

Valor flotante entre 0 y 1 que representa el progreso de la tarea. Solo disponible si el estado es RUNNING.Rango: `0` a `1`Formato: `float`

​

status

string

requerido

Estados posibles de una tarea de Runway.Posibles valores: `SUCCEEDED`, `RUNNING`, `FAILED`, `PENDING`, `CANCELLED`, `THROTTLED`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "promptText": "a red circle",
      "ratio": "1024:1024"
    }
    

### 

​

Salida
    
    
    {
      "createdAt": "2027-01-01T00:00:00Z",
      "id": "5f7c1b28-9a03-4e61-8d2f-1b2c3d4e5f60",
      "output": [
        "https://example.invalid/runway/gen4_image/generated.png"
      ],
      "status": "SUCCEEDED"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/runway/gen4-image/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/runway/gen4-image/code)

[Aleph 2](https://docs.comfy.org/es/development/comfy-router/models/runway/aleph2/code)[Gen 4 Turbo](https://docs.comfy.org/es/development/comfy-router/models/runway/gen4-turbo/code)
