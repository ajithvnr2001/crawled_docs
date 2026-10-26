---
url: https://docs.comfy.org/es/development/comfy-router/models/kling/videos-lip-sync/code/
title: Usa Videos Lip Sync con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:09.225156+00:00
---

# Usa Videos Lip Sync con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/kling/videos-lip-sync/code/

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



Kling

# Usa Videos Lip Sync con Comfy Router

Copiar páginaCopiar página

Llama a kling/videos-lip-sync desde Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `kling/videos-lip-sync`, servida por Comfy Router desde Kling. **Entrada:** Video, Audio · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `kling/videos-lip-sync` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/videos-lip-sync`

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
            "kling/videos-lip-sync",
            {
                "input": {
                    "mode": "text2video",
                    "text": "Welcome to Comfy Cloud.",
                    "video_id": "kling-video-6f5e4d3c2b1a",
                    "voice_id": "genshin_vindi2",
                    "voice_language": "en",
                    "voice_speed": 1,
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("kling/videos-lip-sync", {
      input: {
        mode: "text2video",
        text: "Welcome to Comfy Cloud.",
        video_id: "kling-video-6f5e4d3c2b1a",
        voice_id: "genshin_vindi2",
        voice_language: "en",
        voice_speed: 1,
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/videos-lip-sync \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"mode\":\"text2video\",\"text\":\"Welcome to Comfy Cloud.\",\"video_id\":\"kling-video-6f5e4d3c2b1a\",\"voice_id\":\"genshin_vindi2\",\"voice_language\":\"en\",\"voice_speed\":1}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/kling/videos-lip-sync/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "kling/videos-lip-sync",
                {
                    "input": {
                        "mode": "text2video",
                        "text": "Welcome to Comfy Cloud.",
                        "video_id": "kling-video-6f5e4d3c2b1a",
                        "voice_id": "genshin_vindi2",
                        "voice_language": "en",
                        "voice_speed": 1,
                    },
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("kling/videos-lip-sync", {
      input: {
        mode: "text2video",
        text: "Welcome to Comfy Cloud.",
        video_id: "kling-video-6f5e4d3c2b1a",
        voice_id: "genshin_vindi2",
        voice_language: "en",
        voice_speed: 1,
      },
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/kling/videos-lip-sync/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"input\": {\"mode\":\"text2video\",\"text\":\"Welcome to Comfy Cloud.\",\"video_id\":\"kling-video-6f5e4d3c2b1a\",\"voice_id\":\"genshin_vindi2\",\"voice_language\":\"en\",\"voice_speed\":1}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/videos-lip-sync/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/kling/videos-lip-sync/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

callback_url

string (uri)

La dirección de notificación de callback. El servidor enviará una notificación cuando cambie el estado de la tarea.Formato: `uri`

​

input

object

requerido

​

input.audio_file

string

Ruta local del archivo de audio. Formatos admitidos: .mp3/.wav/.m4a/.aac, tamaño máximo de archivo de 5MB. Código Base64.

​

input.audio_type

string

Método de transmisión de archivos de audio para lip-sync. Requerido cuando el modo es audio2video.Valores posibles: `file`, `url`

​

input.audio_url

string

URL de descarga del archivo de audio. Formatos admitidos: .mp3/.wav/.m4a/.aac, tamaño máximo de archivo de 5MB.

​

input.mode

string

requerido

Modo de generación de video. text2video: modo de generación de texto a video; audio2video: modo de generación de audio a videoValores posibles: `text2video`, `audio2video`

​

input.text

string

Contenido de texto para la generación de video con lip-sync. Requerido cuando el modo es text2video. La longitud máxima es de 120 caracteres.

​

input.video_id

string

El ID del video generado por Kling AI. Solo admite videos de 5 y 10 segundos generados en los últimos 30 días.

​

input.video_url

string

Enlace para obtener el video subido. Los archivos de video admiten .mp4/.mov, el tamaño del archivo no debe superar los 100MB y la duración del video debe estar entre 2 y 10 s.

​

input.voice_id

string

ID de voz. Requerido cuando el modo es text2video. El sistema ofrece una variedad de opciones de voz para elegir.

​

input.voice_language

string

predeterminado:"\"en\""

El idioma de la voz corresponde al ID de voz.Valores posibles: `zh`, `en`

​

input.voice_speed

number

predeterminado:"1"

Velocidad del habla. Rango válido: 0.8~2.0, con precisión de un decimal.Rango: `0.8` a `2`

Generado a partir del esquema que Router sirve en `GET /v2/models/kling/videos-lip-sync/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

code

integer

Código de error

​

data

object

​

data.created_at

integer

Hora de creación de la tarea

​

data.final_unit_deduction

string

Las unidades de deducción de la tarea

​

data.task_id

string

ID de la tarea

​

data.task_info

object

​

data.task_info.external_task_id

string

​

data.task_result

object

​

data.task_result.videos

object[]

​

data.task_result.videos[].duration

string

Duración total del video en segundos

​

data.task_result.videos[].id

string

ID del video generado

​

data.task_result.videos[].url

string (uri)

URL del video generadoFormato: `uri`

​

data.task_result.videos[].watermark_url

string (uri)

URL del video generado con marca de agua, en formato de protección contra hotlinkingFormato: `uri`

​

data.task_status

string

Estado de la tareaValores posibles: `submitted`, `processing`, `succeed`, `failed`

​

data.updated_at

integer

Hora de actualización de la tarea

​

message

string

Mensaje de error

​

request_id

string

ID de la solicitud

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "input": {
        "mode": "text2video",
        "text": "Welcome to Comfy Cloud.",
        "video_id": "kling-video-6f5e4d3c2b1a",
        "voice_id": "genshin_vindi2",
        "voice_language": "en",
        "voice_speed": 1
      }
    }
    

### 

​

Salida
    
    
    {
      "code": 0,
      "data": {
        "created_at": 1798761600000,
        "final_unit_deduction": "1.00",
        "task_id": "kling-lip-sync-task-4f3e2d1c0b9a",
        "task_result": {
          "videos": [
            {
              "duration": "8",
              "id": "kling-video-9a8b7c6d5e4f",
              "url": "https://example.invalid/kling/videos-lip-sync/generated.mp4"
            }
          ]
        },
        "task_status": "succeed",
        "updated_at": 1798761780000
      },
      "message": "SUCCEED",
      "request_id": "5e0a9b17-6d3c-42f8-91b4-7a2c8d6e0f35"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/kling/videos-lip-sync/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/kling/videos-lip-sync/code)

[Videos Avatar Image 2video](https://docs.comfy.org/es/development/comfy-router/models/kling/videos-avatar-image2video/code)[Videos Video Extend](https://docs.comfy.org/es/development/comfy-router/models/kling/videos-video-extend/code)
