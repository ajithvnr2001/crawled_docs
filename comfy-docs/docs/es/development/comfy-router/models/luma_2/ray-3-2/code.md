---
url: https://docs.comfy.org/es/development/comfy-router/models/luma_2/ray-3-2/code/
title: Usa Ray 3.2 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:10.162117+00:00
---

# Usa Ray 3.2 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/luma_2/ray-3-2/code/

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



Luma 2

# Usa Ray 3.2 con Comfy Router

Copiar páginaCopiar página

Llama a luma_2/ray-3.2 con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `luma_2/ray-3.2`, servida por Comfy Router desde Luma 2. **Entrada:** Texto, Imagen, Video · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `luma_2/ray-3.2` **Endpoint:** `POST https://api.comfy.org/v2/models/luma_2/ray-3.2`

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
            "luma_2/ray-3.2",
            {
                "prompt": "a paper boat drifting across a plain white background",
                "type": "video",
                "video": {
                    "duration": "5s",
                    "resolution": "360p",
                },
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("luma_2/ray-3.2", {
      prompt: "a paper boat drifting across a plain white background",
      type: "video",
      video: {
        duration: "5s",
        resolution: "360p",
      },
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/luma_2/ray-3.2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a paper boat drifting across a plain white background\", \"type\": \"video\", \"video\": {\"duration\":\"5s\",\"resolution\":\"360p\"}}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/luma_2/ray-3.2/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # Cada llamada a submit() genera su propio Idempotency-Key y lo reutiliza para los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            handle = await client.models.submit(
                "luma_2/ray-3.2",
                {
                    "prompt": "a paper boat drifting across a plain white background",
                    "type": "video",
                    "video": {
                        "duration": "5s",
                        "resolution": "360p",
                    },
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
    // Cada llamada a submit() genera su propio Idempotency-Key y lo reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("luma_2/ray-3.2", {
      prompt: "a paper boat drifting across a plain white background",
      type: "video",
      video: {
        duration: "5s",
        resolution: "360p",
      },
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Enviar. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/luma_2/ray-3.2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"prompt\": \"a paper boat drifting across a plain white background\", \"type\": \"video\", \"video\": {\"duration\":\"5s\",\"resolution\":\"360p\"}}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/luma_2/ray-3.2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoger. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/luma_2/ray-3.2/requests/$REQUEST_ID \
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

Relación de aspecto de salida. Los modelos de video ray-3.2 admiten el subconjunto 9:16, 3:4, 1:1, 4:3, 16:9, 21:9.Posibles valores: `3:1`, `2:1`, `21:9`, `16:9`, `3:2`, `4:3`, `1:1`, `3:4`, `2:3`, `9:16`, `1:2`, `1:3`

​

image_ref

object[]

Imágenes de referencia para orientación de estilo/contenido. Hasta 9 para el tipo ‘image’, hasta 8 para el tipo ‘image_edit’.

​

image_ref[].data

string

Datos de imagen o video codificados en Base64

​

image_ref[].generation_id

string

UUID de una generación completada previa para reutilizarla como fuente. Lo usan ray-3.2 video_edit / video_reframe.

​

image_ref[].media_type

string

Tipo MIME. Requerido con data (y con url para fuentes de video, por ejemplo, video/mp4 en video_edit / video_reframe).

​

image_ref[].url

string

URL de imagen o video de acceso público

​

model

string

Modelo a usar. uni-1 / uni-1-max para generación de imágenes, ray-3.2 para generación, edición y reencuadre de video.

​

output_format

string

Formato de imagen de salidaPosibles valores: `png`, `jpeg`

​

prompt

string

requerido

Prompt de texto

​

source

object

Referencia a una imagen o un video. Se usa para orientación de estilo/contenido, generación guiada, fuentes de video-edit/video-reframe y keyframes de guía. Proporciona exactamente uno de generation_id, url o data.

​

source.data

string

Datos de imagen o video codificados en Base64

​

source.generation_id

string

UUID de una generación completada previa para reutilizarla como fuente. Lo usan ray-3.2 video_edit / video_reframe.

​

source.media_type

string

Tipo MIME. Requerido con data (y con url para fuentes de video, por ejemplo, video/mp4 en video_edit / video_reframe).

​

source.url

string

URL de imagen o video de acceso público

​

style

string

Preajuste de estiloPosibles valores: `auto`, `manga`

​

type

string

El tipo de generación a realizar. image/image_edit los generan los modelos uni-1 / uni-1-max; video/video_edit/video_reframe los genera el modelo ray-3.2.Posibles valores: `image`, `image_edit`, `video`, `video_edit`, `video_reframe`

​

video

object

Configuraciones de salida de video para ray-3.2. Aquí solo se modelan los campos que afectan la validación y la facturación; los campos adicionales (controles de edición, source_position) se reenvían a Luma sin modificar.

​

video.duration

string

Duración del clip para ray-3.2 video / video_edit. Por defecto 5s. La generación HDR (tipo video) está restringida a 5s.Posibles valores: `5s`, `10s`

​

video.end_frame

object

Referencia a una imagen o un video. Se usa para orientación de estilo/contenido, generación guiada, fuentes de video-edit/video-reframe y keyframes de guía. Proporciona exactamente uno de generation_id, url o data.

​

video.end_frame.data

string

Datos de imagen o video codificados en Base64

​

video.end_frame.generation_id

string

UUID de una generación completada previa para reutilizarla como fuente. Lo usan ray-3.2 video_edit / video_reframe.

​

video.end_frame.media_type

string

Tipo MIME. Requerido con data (y con url para fuentes de video, por ejemplo, video/mp4 en video_edit / video_reframe).

​

video.end_frame.url

string

URL de imagen o video de acceso público

​

video.exr_export

boolean

Aún no disponible: las solicitudes con exr_export=true se rechazan con 400 hasta que Luma habilite la entrega EXR. Exportará un archivo EXR junto al MP4 (requiere hdr true). Se rechaza para video_reframe.

​

video.hdr

boolean

Renderizar en HDR. Requiere 720p/1080p. Se rechaza para video_reframe.

​

video.keyframe_indexes

integer[]

Posiciones de fotograma de salida para `keyframes`, de la misma longitud; 0–120 para 5s, 0–240 para 10s. Se reenvían sin modificar.

​

video.keyframes

object[]

Imágenes de fotograma guía (1–64), mutuamente excluyentes con start_frame/end_frame. Se facturan según la duración solicitada; una solicitud con keyframes nunca es una extensión de un solo keyframe.

​

video.keyframes[].data

string

Datos de imagen o video codificados en Base64

​

video.keyframes[].generation_id

string

UUID de una generación completada previa para reutilizarla como fuente. Lo usan ray-3.2 video_edit / video_reframe.

​

video.keyframes[].media_type

string

Tipo MIME. Requerido con data (y con url para fuentes de video, por ejemplo, video/mp4 en video_edit / video_reframe).

​

video.keyframes[].url

string

URL de imagen o video de acceso público

​

video.loop

boolean

Repetir el clip generado. Solo para creación (tipo video).

​

video.resolution

string

Resolución de salida para ray-3.2 video. Por defecto 720p. 360p es el nivel de borrador. HDR requiere 720p o 1080p.Posibles valores: `360p`, `540p`, `720p`, `1080p`

​

video.start_frame

object

Referencia a una imagen o un video. Se usa para orientación de estilo/contenido, generación guiada, fuentes de video-edit/video-reframe y keyframes de guía. Proporciona exactamente uno de generation_id, url o data.

​

video.start_frame.data

string

Datos de imagen o video codificados en Base64

​

video.start_frame.generation_id

string

UUID de una generación completada previa para reutilizar como fuente. Usado por ray-3.2 video_edit / video_reframe.

​

video.start_frame.media_type

string

Tipo MIME. Requerido con data (y con url para fuentes de video, p. ej. video/mp4 en video_edit / video_reframe).

​

video.start_frame.url

string

URL de imagen o video de acceso público

​

web_search

boolean

Habilitar la fundamentación de búsqueda web

Generado a partir del esquema que Router sirve en `GET /v2/models/luma_2/ray-3.2/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

created_at

string

Marca de tiempo de creación

​

failure_code

string

Código de fallo legible por máquina para su manejo programáticoValores posibles: `content_moderated`, `generation_failed`, `budget_exhausted`, `output_not_found`

​

failure_reason

string

Descripción del fallo legible por humanos, presente solo en una generación FAILED. Es `null` en una generación exitosa.

​

id

string

Identificador de la generación

​

model

string

Modelo utilizado

​

output

object[]

Una entrada de salida generada

​

output[].type

string

Tipo de medio (por ejemplo, image)

​

output[].url

string

URL prefirmada (caduca en 1 hora)

​

state

string

Estado actual de la generaciónValores posibles: `queued`, `processing`, `completed`, `failed`

​

type

string

El tipo de generación que se realizará. image/image_edit se producen con los modelos uni-1 / uni-1-max; video/video_edit/video_reframe se producen con el modelo ray-3.2.Valores posibles: `image`, `image_edit`, `video`, `video_edit`, `video_reframe`

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "prompt": "a paper boat drifting across a plain white background",
      "type": "video",
      "video": {
        "duration": "5s",
        "resolution": "360p"
      }
    }
    

### 

​

Salida
    
    
    {
      "created_at": "2027-01-01T00:00:00Z",
      "failure_code": null,
      "failure_reason": null,
      "id": "gen-luma-agents-ray32-9c1f3a0e7d52",
      "model": "ray-3.2",
      "output": [
        {
          "type": "video",
          "url": "https://example.invalid/luma_2/ray-3.2/generated.mp4"
        }
      ],
      "state": "completed",
      "type": "video"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/luma_2/ray-3-2/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/luma_2/ray-3-2/code)

[Ray Flash 2](https://docs.comfy.org/es/development/comfy-router/models/luma/ray-flash-2/code)[Uni 1 Max](https://docs.comfy.org/es/development/comfy-router/models/luma_2/uni-1-max/code)
