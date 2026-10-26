---
url: https://docs.comfy.org/es/development/comfy-router/models/moonvalley/video-to-video/code/
title: Usa Video To Video con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:12.124360+00:00
---

# Usa Video To Video con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/moonvalley/video-to-video/code/

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

# Usa Video To Video con Comfy Router

Copiar páginaCopiar página

Llama a moonvalley/video-to-video mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `moonvalley/video-to-video`, servida por Comfy Router de Moonvalley. **Entrada:** Video, Texto · **Salida:** Video

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de código de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP directo. **ID del modelo:** `moonvalley/video-to-video` **Endpoint:** `POST https://api.comfy.org/v2/models/moonvalley/video-to-video`

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
            "moonvalley/video-to-video",
            {
                "control_type": "motion_control",
                "prompt_text": "Apply motion control to enhance this video",
                "video_url": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("moonvalley/video-to-video", {
      control_type: "motion_control",
      prompt_text: "Apply motion control to enhance this video",
      video_url: "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/moonvalley/video-to-video \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"control_type\": \"motion_control\", \"prompt_text\": \"Apply motion control to enhance this video\", \"video_url\": \"https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/moonvalley/video-to-video/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge en cuanto está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica paso a paso el estado, la cancelación y la recogida.

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
                "moonvalley/video-to-video",
                {
                    "control_type": "motion_control",
                    "prompt_text": "Apply motion control to enhance this video",
                    "video_url": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
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
    const handle = await comfy.models.submit("moonvalley/video-to-video", {
      control_type: "motion_control",
      prompt_text: "Apply motion control to enhance this video",
      video_url: "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/moonvalley/video-to-video/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"control_type\": \"motion_control\", \"prompt_text\": \"Apply motion control to enhance this video\", \"video_url\": \"https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/moonvalley/video-to-video/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/moonvalley/video-to-video/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

control_type

string

requerido

Tipos compatibles para el control de videoValores posibles: `motion_control`, `pose_control`

​

image_url

string

URL de la imagen de control

​

inference_params

object

​

inference_params.control_params

object

​

inference_params.control_params.motion_intensity

integer

predeterminado:"6"

Intensidad del control de movimientoFormato: `int32`

​

inference_params.guidance_scale

number

predeterminado:"10"

Escalar de orientación para el control de la generaciónFormato: `float`

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

Número de pasos de eliminación de ruido

​

inference_params.use_negative_prompts

boolean

predeterminado:"true"

Indica si se usan prompts negativos

​

prompt_text

string

requerido

Describe el video a generar

​

video_url

string

requerido

URL del video de control

​

webhook_url

string

URL de webhook opcional para notificaciones

Generados a partir del esquema que Router sirve en `GET /v2/models/moonvalley/video-to-video/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

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
      "control_type": "motion_control",
      "prompt_text": "Apply motion control to enhance this video",
      "video_url": "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/moonvalley/video-to-video/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/moonvalley/video-to-video/code)

[Texto a video](https://docs.comfy.org/es/development/comfy-router/models/moonvalley/text-to-video/code)[GPT 4.1 Mini](https://docs.comfy.org/es/development/comfy-router/models/openai/gpt-4-1-mini/code)
