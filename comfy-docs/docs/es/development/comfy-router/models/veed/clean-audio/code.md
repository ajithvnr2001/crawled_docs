---
url: https://docs.comfy.org/es/development/comfy-router/models/veed/clean-audio/code/
title: Usa Clean Audio con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:20.657306+00:00
---

# Usa Clean Audio con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/veed/clean-audio/code/

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



Veed

# Usa Clean Audio con Comfy Router

Copiar páginaCopiar página

Llama a veed/clean-audio a través de Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `veed/clean-audio`, servida por Comfy Router desde Veed. **Entrada:** Audio · **Salida:** Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `veed/clean-audio` **Endpoint:** `POST https://api.comfy.org/v2/models/veed/clean-audio`

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
            "veed/clean-audio",
            {
                "audio_url": "https://static-assets.veed.io/api-examples/clean-audio-input.m4a",
                "normalize_loudness": True,
                "output_format": "flac",
                "strength": 0.874,
                "target_lufs": -19,
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("veed/clean-audio", {
      audio_url: "https://static-assets.veed.io/api-examples/clean-audio-input.m4a",
      normalize_loudness: true,
      output_format: "flac",
      strength: 0.874,
      target_lufs: -19,
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/veed/clean-audio \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"https://static-assets.veed.io/api-examples/clean-audio-input.m4a\", \"normalize_loudness\": true, \"output_format\": \"flac\", \"strength\": 0.874, \"target_lufs\": -19}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/veed/clean-audio/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recopila cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recopilación.

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
                "veed/clean-audio",
                {
                    "audio_url": "https://static-assets.veed.io/api-examples/clean-audio-input.m4a",
                    "normalize_loudness": True,
                    "output_format": "flac",
                    "strength": 0.874,
                    "target_lufs": -19,
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
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("veed/clean-audio", {
      audio_url: "https://static-assets.veed.io/api-examples/clean-audio-input.m4a",
      normalize_loudness: true,
      output_format: "flac",
      strength: 0.874,
      target_lufs: -19,
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
    curl https://api.comfy.org/v2/models/veed/clean-audio/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_url\": \"https://static-assets.veed.io/api-examples/clean-audio-input.m4a\", \"normalize_loudness\": true, \"output_format\": \"flac\", \"strength\": 0.874, \"target_lufs\": -19}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/veed/clean-audio/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recopila. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras aún se está ejecutando.
    curl https://api.comfy.org/v2/models/veed/clean-audio/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

audio_url

string

requerido

URL http(s) pública de la grabación que se va a limpiar, de hasta 30 minutos.

​

normalize_loudness

boolean

predeterminado:"true"

Establece en false para conservar la sonoridad de la entrada.

​

output_format

string

predeterminado:"\"flac\""

Contenedor de salida: flac o wav.

​

strength

number

predeterminado:"0.874"

Cuánto ruido de fondo se elimina por debajo del habla.Rango: `0` a `1`

​

target_lufs

number

predeterminado:"-19"

Sonoridad de salida en LUFS. Se ignora cuando `normalize_loudness` es false.Rango: `-40` a `-8`

Generado a partir del esquema que Router sirve en `GET /v2/models/veed/clean-audio/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

data

object

​

data.credits_charged

integer

Créditos que VEED cobró por la tarea. Se incluye cuando la tarea está COMPLETED.

​

data.credits_estimated

integer

Créditos que VEED cotizó antes de ejecutar la tarea. Solo aparece en la respuesta del envío.

​

data.error

object

Información del fallo. Se incluye cuando la tarea ha fallado (FAILED).

​

data.error.code

string

Código de fallo legible por máquina.

​

data.error.details

object[]

​

data.error.message

string

Mensaje de fallo legible por personas.

​

data.job_id

string

ID de trabajo usado para consultar el estado.

​

data.result

object

El contenido multimedia producido. Se incluye cuando la tarea está COMPLETED. Las rutas de video responden `video`, Clean Audio responde `audio` y Video Background Removal responde `files`.

​

data.result.audio

object

​

data.result.audio.content_type

string

Tipo MIME del archivo.

​

data.result.audio.file_name

string

Nombre del archivo.

​

data.result.audio.file_size

integer

Tamaño del archivo en bytes.Formato: `int64`

​

data.result.audio.url

string

URL desde la que se puede descargar el archivo.

​

data.result.files

object[]

Salida de Video Background Removal. Un WebM con alfa para `vp9`, o el video RGB y una máscara alfa para `h264`.

​

data.result.files[].content_type

string

Tipo MIME del archivo.

​

data.result.files[].file_name

string

Nombre del archivo.

​

data.result.files[].file_size

integer

Tamaño del archivo en bytes.Formato: `int64`

​

data.result.files[].url

string

URL desde la que se puede descargar el archivo.

​

data.result.video

object

​

data.result.video.content_type

string

Tipo MIME del archivo.

​

data.result.video.file_name

string

Nombre del archivo.

​

data.result.video.file_size

integer

Tamaño del archivo en bytes.Formato: `int64`

​

data.result.video.url

string

URL desde la que se puede descargar el archivo.

​

data.status

string

Estado de la tarea: PROCESSING, COMPLETED, FAILED o CANCELLED.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "audio_url": "https://static-assets.veed.io/api-examples/clean-audio-input.m4a",
      "normalize_loudness": true,
      "output_format": "flac",
      "strength": 0.874,
      "target_lufs": -19
    }
    

### 

​

Salida
    
    
    {
      "data": {
        "credits_charged": 1,
        "job_id": "2e3f1c51-a71c-4dc2-9c8d-857c1920a64d",
        "result": {
          "audio": {
            "content_type": "audio/flac",
            "url": "https://example.invalid/veed/clean.flac"
          }
        },
        "status": "COMPLETED"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/veed/clean-audio/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/veed/clean-audio/code)

[Clean Audio Video](https://docs.comfy.org/es/development/comfy-router/models/veed/clean-audio-video/code)[Fabric 1.0](https://docs.comfy.org/es/development/comfy-router/models/veed/fabric-1-0/code)
