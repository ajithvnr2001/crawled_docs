---
url: https://docs.comfy.org/es/development/comfy-router/models/minimax/minimax-h3/code/
title: Usa MiniMax H3 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:11.761395+00:00
---

# Usa MiniMax H3 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/minimax/minimax-h3/code/

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



MiniMax

# Usa MiniMax H3 con Comfy Router

Copiar páginaCopiar página

Llama a minimax/minimax-h3 desde Comfy Router: endpoint, forma de la solicitud y el MP4 con audio estéreo nativo que devuelve Router

Copiar páginaCopiar página

Referencia de API para MiniMax H3. MiniMax H3 (Hailuo 03) es un modelo de video omnimodal. Genera la imagen y su pista de audio juntas en una sola pasada, así que un clip finalizado ya incluye diálogo, efectos de sonido y música. **Entrada:** Texto, Imagen · **Salida:** Video + Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP directo. **ID del modelo:** `minimax/minimax-h3` **Endpoint:** `POST https://api.comfy.org/v2/models/minimax/minimax-h3`

  * Esperar el resultado

  * Enviar y recoger más tarde




Python

TypeScript

cURL
    
    
    import asyncio
    from comfy_sdk import AsyncComfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    async def main():
        async with AsyncComfy() as client:
            result = await client.models.run(
                "minimax/minimax-h3",
                {
                    "content": [
                        {
                            "text": "A single red maple leaf resting on a plain white background.",
                            "type": "text",
                        },
                    ],
                    "duration": 5,
                    "ratio": "16:9",
                    "resolution": "768P",
                },
            )
    
        print("video:", result["task"]["content"]["url"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    type Result = { task: { content: { url: string } } };
    const result = await comfy.models.run<Result>("minimax/minimax-h3", {
      content: [
        {
          text: "A single red maple leaf resting on a plain white background.",
          type: "text",
        },
      ],
      duration: 5,
      ratio: "16:9",
      resolution: "768P",
    });
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("video:", result.data.task.content.url);
    
    
    
    curl https://api.comfy.org/v2/models/minimax/minimax-h3 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"content\": [{\"text\":\"A single red maple leaf resting on a plain white background.\",\"type\":\"text\"}], \"duration\": 5, \"ratio\": \"16:9\", \"resolution\": \"768P\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/minimax/minimax-h3/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida del resultado.

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
                "minimax/minimax-h3",
                {
                    "content": [
                        {
                            "text": "A single red maple leaf resting on a plain white background.",
                            "type": "text",
                        },
                    ],
                    "duration": 5,
                    "ratio": "16:9",
                    "resolution": "768P",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta el estado hasta que la solicitud se completa, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló genera aquí el error tipado de Router.
            result = await handle.get()
    
        print("video:", result["task"]["content"]["url"])
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    type Result = { task: { content: { url: string } } };
    const handle = await comfy.models.submit<Result>("minimax/minimax-h3", {
      content: [
        {
          text: "A single red maple leaf resting on a plain white background.",
          type: "text",
        },
      ],
      duration: 5,
      ratio: "16:9",
      resolution: "768P",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta el estado hasta que la solicitud se completa, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    if (result.kind !== "json") throw new Error("expected a JSON result");
    
    console.log("video:", result.data.task.content.url);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/minimax/minimax-h3/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"content\": [{\"text\":\"A single red maple leaf resting on a plain white background.\",\"type\":\"text\"}], \"duration\": 5, \"ratio\": \"16:9\", \"resolution\": \"768P\"}"
    
    # 2. Consulta el estado hasta que sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/minimax/minimax-h3/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge el resultado. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/minimax/minimax-h3/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

aigc_watermark

boolean

Indica si se debe agregar una marca de agua AIGC a la salida. El valor predeterminado es false.

​

callback_url

string

Opcional. URL que recibe los cambios de estado de la tarea después de la verificación del desafío.

​

content

object[]

requerido

Elementos de contenido que impulsan la generación. Debe contener un elemento de texto no vacío; de forma opcional, agrega imágenes first_frame/last_frame o medios reference_*.

​

content[].audio_url

object

Fuente de audio. Requerido para los elementos audio_url.

​

content[].audio_url.url

string

Una URL accesible públicamente, una referencia mm_file://{file_id} o un data URI.

​

content[].image_url

object

Fuente de imagen. Requerido para los elementos image_url.

​

content[].image_url.url

string

Una URL accesible públicamente, una referencia mm_file://{file_id} o un data URI.

​

content[].role

string

Rol de un elemento multimedia. Opciones: first_frame, last_frame, reference_image, reference_video, reference_audio, base_video. Los roles de fotograma clave y los roles reference_* son mutuamente excluyentes dentro de una solicitud; base_video marca el video de origen de una solicitud de regeneración de video.

​

content[].text

string

El texto del prompt. Se requiere exactamente un elemento de texto no vacío por solicitud.

​

content[].type

string

requerido

Tipo de elemento de contenido. Opciones: text, image_url, video_url, audio_url.

​

content[].video_url

object

Fuente de video. Requerido para los elementos video_url.

​

content[].video_url.url

string

Una URL accesible públicamente, una referencia mm_file://{file_id} o un data URI.

​

duration

integer

requerido

Duración del video en segundos. Comfy Router acepta de 4 a 15 y rechaza cualquier valor fuera de ese rango antes de llamar al proveedor. La documentación propia de MiniMax para este modelo indica de 5 a 15; los nodos ComfyUI MiniMax H3 ofrecen de 4 a 15 y se ha observado que una generación de 4 segundos se completa correctamente, por lo que aquí se acepta 4.Rango: de `4` a `15`

​

model

string

ID del modelo. Opciones: MiniMax-H3. Quienes llaman al Router pueden omitir este campo o enviar null; el Router inyecta el modelo seleccionado por la ruta de la solicitud antes del despacho al proveedor.

​

ratio

string

Relación de aspecto. Opciones: adaptive (predeterminada), 21:9, 16:9, 4:3, 1:1, 3:4, 9:16. Es requerida y no debe ser adaptive para texto a video; se ignora (se trata como adaptive) en la generación con primer fotograma o último fotograma.

​

resolution

string

requerido

Resolución del video. Opciones: 2K, 768P. El valor se compara sin distinguir mayúsculas y minúsculas y se normaliza antes del despacho, así que `2k` y `768p` se aceptan y se envían como `2K` y `768P`.Valores posibles: `2K`, `2k`, `768P`, `768p`

​

seed

integer

Semilla aleatoria en [-1, 2^32 - 1]; si se omite o es -1, es aleatoria.Formato: `int64`

Generado a partir del esquema que el Router sirve en `GET /v2/models/minimax/minimax-h3/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

task

object

Una tarea de generación de video de Minimax V2.

​

task.content

object

Salida generada; está presente cuando el estado es succeeded.

​

task.content.prompt

string

El prompt de video mejorado que produce una tarea h3_context_ir completada correctamente.

​

task.content.url

string

URL con tiempo limitado del MP4 generado. Consulta de nuevo para obtener una URL renovada.

​

task.duration

number

La duración del video generado en segundos.

​

task.error

object

Detalles del error cuando el estado es failed; incluye code y message.

​

task.id

string

El ID de la tarea.

​

task.model

string

El modelo usado para la tarea.

​

task.ratio

string

La relación de aspecto real del video generado.

​

task.resolution

string

La resolución del video generado.

​

task.status

string

Estado de la tarea. Opciones: queued, running, succeeded, failed, cancelled, expired.

​

task.task_type

string

El tipo de la tarea.

​

task.usage

object

El uso registrado para la tarea.

​

task.usage.completion_tokens

integer

​

task.usage.input_image_count

integer

​

task.usage.input_seconds

number

​

task.usage.output_seconds

number

​

task.usage.prompt_tokens

integer

​

task.usage.total_seconds

number

​

task.usage.total_tokens

integer

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "content": [
        {
          "text": "A single red maple leaf resting on a plain white background.",
          "type": "text"
        }
      ],
      "duration": 5,
      "ratio": "16:9",
      "resolution": "768P"
    }
    

### 

​

Salida
    
    
    {
      "task": {
        "content": {
          "url": "https://example.invalid/minimax/minimax-h3/generated.mp4"
        },
        "duration": 6,
        "id": "3f7a1b28-5c0d-4e91-8a6f-1b2c3d4e5f60",
        "model": "MiniMax-H3",
        "ratio": "16:9",
        "resolution": "768P",
        "status": "succeeded",
        "usage": {
          "output_seconds": 6,
          "total_seconds": 6
        }
      }
    }
    

**El MP4 incluye una pista de audio generada.** H3 es omnimodal: la voz, los efectos de sonido y la música se sintetizan junto con la imagen en una sola pasada hacia adelante, no se añaden después, y el resultado es un único MP4 con audio estéreo nativo. Nada en el cuerpo de la solicitud anterior desactiva eso: los campos documentados son el contenido del prompt, `duration`, `ratio`, `resolution`, `seed`, `aigc_watermark` y `callback_url`, y ninguno de ellos selecciona una renderización silenciosa. Por eso, un pipeline que pretenda superponer su propia voz en off sobre el clip tiene que silenciar o quitar primero la pista devuelta, o hará el mux sobre un clip que ya está hablando. El prompt es lo que guía el audio: describe el diálogo, los efectos de sonido y la música en el mismo bloque de prompt que la toma. Consulta la [guía de prompts de MiniMax H3](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3-prompt-guide) para saber cómo estructurar uno, y la [descripción general de MiniMax H3](https://docs.comfy.org/es/tutorials/video/minimax/minimax-h3) para saber qué hace el modelo en ComfyUI. La URL del video caduca. Router vuelve a alojar el MP4 y responde con una URL firmada por Comfy válida durante 12 horas, y recurre al enlace propio de MiniMax, de vida más corta, cuando el re-alojamiento falla. La descripción de `task.content.url` en el esquema de respuesta anterior te indica que consultes de nuevo para obtener una URL actualizada: esa es la redacción propia de MiniMax para su API, trasladada sin cambios, y Router no expone la ruta de consulta de tareas de MiniMax. Volver a leer la ruta de resultados de una solicitud en cola devuelve el documento de resultado almacenado mientras la solicitud se [conserva durante 24 horas después de completarse](https://docs.comfy.org/es/development/comfy-router/queue#idempotencia-y-facturaci%C3%B3n), pero nada documenta que esa lectura genere una URL recién firmada. Descarga el MP4 cuanto antes en lugar de guardar el enlace.

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/minimax/minimax-h3/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/minimax/minimax-h3/code)

[Rigging](https://docs.comfy.org/es/development/comfy-router/models/meshy/rigging/code)[Image To Video](https://docs.comfy.org/es/development/comfy-router/models/moonvalley/image-to-video/code)
