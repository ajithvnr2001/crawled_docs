---
url: https://docs.comfy.org/es/development/comfy-router/models/wavespeed/flashvsr/code/
title: Usa Flashvsr con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:25.190780+00:00
---

# Usa Flashvsr con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/wavespeed/flashvsr/code/

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



WaveSpeed

# Usa Flashvsr con Comfy Router

Copiar páginaCopiar página

Llama a wavespeed/flashvsr desde Comfy Router: endpoint, forma de la petición y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `wavespeed/flashvsr`, servida por Comfy Router desde WaveSpeed. **Entrada:** Video · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `wavespeed/flashvsr` **Endpoint:** `POST https://api.comfy.org/v2/models/wavespeed/flashvsr`

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
            "wavespeed/flashvsr",
            {
                "duration": 4,
                "target_resolution": "1080p",
                "video": "https://samplelib.com/mp4/sample-30s.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("wavespeed/flashvsr", {
      duration: 4,
      target_resolution: "1080p",
      video: "https://samplelib.com/mp4/sample-30s.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/wavespeed/flashvsr \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 4, \"target_resolution\": \"1080p\", \"video\": \"https://samplelib.com/mp4/sample-30s.mp4\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/wavespeed/flashvsr/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "wavespeed/flashvsr",
                {
                    "duration": 4,
                    "target_resolution": "1080p",
                    "video": "https://samplelib.com/mp4/sample-30s.mp4",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
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
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("wavespeed/flashvsr", {
      duration: 4,
      target_resolution: "1080p",
      video: "https://samplelib.com/mp4/sample-30s.mp4",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/wavespeed/flashvsr/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 4, \"target_resolution\": \"1080p\", \"video\": \"https://samplelib.com/mp4/sample-30s.mp4\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/wavespeed/flashvsr/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/wavespeed/flashvsr/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

duration

number

requerido

Duración del video en segundos

​

target_resolution

string

predeterminado:"\"1080p\""

Resolución objetivo a la que escalar.Valores posibles: `720p`, `1080p`, `2k`, `4k`

​

video

string

requerido

El video que se va a escalar. Puede ser una URL al archivo de video o un video codificado en base64.

Generado a partir del esquema que Router sirve en `GET /v2/models/wavespeed/flashvsr/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

code

integer

Código de estado de la envoltura propia de WavespeedAI, que refleja un estado HTTP (200 en el documento que describe este esquema). Wavespeed informa algunos fallos aquí en lugar de en el estado del transporte.

​

data

object

requerido

​

data.created_at

string

Marca de tiempo ISO-8601 de cuándo creó Wavespeed la predicción.

​

data.error

string

Motivo del fallo en texto libre de Wavespeed, una cadena vacía cuando no hay ninguno. Una predicción que realmente falló llega a quien llama a Router como un error de Comfy Router en lugar de como este documento.

​

data.id

string

Identificador de Wavespeed para la predicción que Router envió y consultó.

​

data.model

string

El id del modelo de Wavespeed con el que se ejecutó la predicción.

​

data.outputs

string[]

requerido

La generación finalizada. Presente y no vacía en el documento que devuelve Router; esta lista ES el resultado. Cada elemento es una URL al contenido generado (un MP4 para `wavespeed/flashvsr`, una imagen para los dos upscalers) o, para los dos ids de imagen cuando la solicitud estableció `enable_base64_output`, los propios bytes codificados en base64. Los enlaces son de Wavespeed y caducan.

​

data.status

string

requerido

El estado terminal de la predicción tal como lo escribió Wavespeed. Aquí no se restringe a un enum: Router reenvía el valor sin cambios y el clasificador de sondeo lo convierte a minúsculas antes de comparar, así que un éxito puede llegar legítimamente como `completed`, `succeeded`, `success` o `done`, en cualquier combinación de mayúsculas y minúsculas.

​

data.timings

object

Las propias mediciones de tiempos de Wavespeed.

​

data.timings.inference

integer

Tiempo de inferencia en milisegundos. Es la cifra de Wavespeed, no el cargo de Comfy.

​

data.urls

object

Los enlaces propios de Wavespeed para la predicción.

​

data.urls.get

string

La URL del resultado de la predicción que Router consultó.

​

message

string

Mensaje de estado de la envoltura, por ejemplo `success`.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "duration": 4,
      "target_resolution": "1080p",
      "video": "https://samplelib.com/mp4/sample-30s.mp4"
    }
    

### 

​

Salida
    
    
    {
      "code": 200,
      "data": {
        "created_at": "2027-01-01T00:00:00Z",
        "error": "",
        "id": "3f6c1a90-2b47-4d18-9a55-7c0e8b21d4f3",
        "outputs": [
          "https://example.invalid/wavespeed/flashvsr/upscaled.mp4"
        ],
        "status": "completed",
        "timings": {
          "inference": 128000
        }
      },
      "message": "success"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/wavespeed/flashvsr/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/wavespeed/flashvsr/code)

[Wan 3.0 Video](https://docs.comfy.org/es/development/comfy-router/models/wan/wan3-0-video/code)[Seedvr 2](https://docs.comfy.org/es/development/comfy-router/models/wavespeed/seedvr2/code)
