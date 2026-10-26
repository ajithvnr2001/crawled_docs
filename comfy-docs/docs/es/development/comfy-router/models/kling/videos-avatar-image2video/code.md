---
url: https://docs.comfy.org/es/development/comfy-router/models/kling/videos-avatar-image2video/code/
title: Usa Videos Avatar Image 2video con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:09.106631+00:00
---

# Usa Videos Avatar Image 2video con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/kling/videos-avatar-image2video/code/

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

# Usa Videos Avatar Image 2video con Comfy Router

Copiar páginaCopiar página

Llama a kling/videos-avatar-image2video con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `kling/videos-avatar-image2video`, servida por Comfy Router desde Kling. **Entrada:** Imagen, Audio · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP directo. **ID del modelo:** `kling/videos-avatar-image2video` **Endpoint:** `POST https://api.comfy.org/v2/models/kling/videos-avatar-image2video`

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
            "kling/videos-avatar-image2video",
            {
                "image": "https://example.invalid/kling/avatar.png",
                "mode": "std",
                "prompt": "The presenter smiles and gestures towards the camera.",
                "sound_file": "https://example.invalid/kling/voice.mp3",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("kling/videos-avatar-image2video", {
      image: "https://example.invalid/kling/avatar.png",
      mode: "std",
      prompt: "The presenter smiles and gestures towards the camera.",
      sound_file: "https://example.invalid/kling/voice.mp3",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/kling/videos-avatar-image2video \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://example.invalid/kling/avatar.png\", \"mode\": \"std\", \"prompt\": \"The presenter smiles and gestures towards the camera.\", \"sound_file\": \"https://example.invalid/kling/voice.mp3\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/kling/videos-avatar-image2video/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "kling/videos-avatar-image2video",
                {
                    "image": "https://example.invalid/kling/avatar.png",
                    "mode": "std",
                    "prompt": "The presenter smiles and gestures towards the camera.",
                    "sound_file": "https://example.invalid/kling/voice.mp3",
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
    const handle = await comfy.models.submit("kling/videos-avatar-image2video", {
      image: "https://example.invalid/kling/avatar.png",
      mode: "std",
      prompt: "The presenter smiles and gestures towards the camera.",
      sound_file: "https://example.invalid/kling/voice.mp3",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/kling/videos-avatar-image2video/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"image\": \"https://example.invalid/kling/avatar.png\", \"mode\": \"std\", \"prompt\": \"The presenter smiles and gestures towards the camera.\", \"sound_file\": \"https://example.invalid/kling/voice.mp3\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/kling/videos-avatar-image2video/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/kling/videos-avatar-image2video/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

audio_id

string

ID de audio generado mediante la API de TTS. Solo admite audio de 2 a 300 segundos generado en los últimos 30 días. Debes proporcionar `audio_id` o `sound_file` (son mutuamente excluyentes).

​

callback_url

string (uri)

La dirección de notificación de callback para el resultado de esta tarea.Formato: `uri`

​

external_task_id

string

ID de tarea personalizado. Debe ser único dentro de una misma cuenta de usuario.

​

image

string

requerido

Imagen de referencia del avatar. Admite codificación Base64 o URL de la imagen. Formatos admitidos: .jpg/.jpeg/.png. Máx 10MB, mín 300px de ancho/alto, relación de aspecto entre 1:2.5 y 2.5:1.

​

mode

string

predeterminado:"\"std\""

Modo de generación de video. std: Modo estándar (rentable), pro: Modo profesional (mayor duración, mayor calidad).Valores posibles: `std`, `pro`

​

prompt

string

Prompt de texto positivo. Puede definir las acciones, las emociones y los movimientos de cámara del avatar.

​

sound_file

string

Archivo de sonido. Admite audio codificado en Base64 o una URL de audio accesible. Formatos aceptados: .mp3/.wav/.m4a/.aac (máx 5MB), de 2 a 300 segundos. Debes proporcionar `audio_id` o `sound_file` (son mutuamente excluyentes).

​

watermark_info

object

​

watermark_info.enabled

boolean

Indica si se generan resultados con marca de agua al mismo tiempo.

Generado a partir del esquema que Router sirve en `GET /v2/models/kling/videos-avatar-image2video/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

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

Hora de creación de la tarea, marca de tiempo Unix en milisegundos

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

URL del video generado con marca de agua, formato con protección de hotlinkFormato: `uri`

​

data.task_status

string

Estado de la tareaValores posibles: `submitted`, `processing`, `succeed`, `failed`

​

data.task_status_msg

string

Información del estado de la tarea; muestra el motivo del fallo cuando la tarea falla

​

data.updated_at

integer

Hora de actualización de la tarea, marca de tiempo Unix en milisegundos

​

data.watermark_info

object

​

data.watermark_info.enabled

boolean

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
      "image": "https://example.invalid/kling/avatar.png",
      "mode": "std",
      "prompt": "The presenter smiles and gestures towards the camera.",
      "sound_file": "https://example.invalid/kling/voice.mp3"
    }
    

### 

​

Salida
    
    
    {
      "code": 0,
      "data": {
        "created_at": 1798761600000,
        "task_id": "kling-avatar-task-8b7a6c5d4e3f",
        "task_result": {
          "videos": [
            {
              "duration": "10",
              "id": "kling-video-1c2d3e4f5a6b",
              "url": "https://example.invalid/kling/videos-avatar-image2video/generated.mp4"
            }
          ]
        },
        "task_status": "succeed",
        "task_status_msg": "",
        "updated_at": 1798761900000
      },
      "message": "SUCCEED",
      "request_id": "b41d7c58-9e26-4f03-a7d1-5c8e0b3f2a69"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/kling/videos-avatar-image2video/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/kling/videos-avatar-image2video/code)

[Kling Video O1](https://docs.comfy.org/es/development/comfy-router/models/kling/kling-video-o1/code)[Videos Lip Sync](https://docs.comfy.org/es/development/comfy-router/models/kling/videos-lip-sync/code)
