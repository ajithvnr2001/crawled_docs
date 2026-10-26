---
url: https://docs.comfy.org/es/development/comfy-router/models/ltx/ltx-2-5-fast/code/
title: Usa LTX 2.5 Fast con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:09.815952+00:00
---

# Usa LTX 2.5 Fast con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/ltx/ltx-2-5-fast/code/

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



LTX

# Usa LTX 2.5 Fast con Comfy Router

Copiar páginaCopiar página

Llama a ltx/ltx-2-5-fast con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `ltx/ltx-2-5-fast`, servida por Comfy Router desde LTX. **Entrada:** Texto · **Salida:** Video + Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP puro. **ID del modelo:** `ltx/ltx-2-5-fast` **Endpoint:** `POST https://api.comfy.org/v2/models/ltx/ltx-2-5-fast`

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
            "ltx/ltx-2-5-fast",
            {
                "duration": 2,
                "fps": 24,
                "generate_audio": False,
                "prompt": "A single red maple leaf resting on a plain white background.",
                "resolution": "1280x720",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("ltx/ltx-2-5-fast", {
      duration: 2,
      fps: 24,
      generate_audio: false,
      prompt: "A single red maple leaf resting on a plain white background.",
      resolution: "1280x720",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/ltx/ltx-2-5-fast \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 2, \"fps\": 24, \"generate_audio\": false, \"prompt\": \"A single red maple leaf resting on a plain white background.\", \"resolution\": \"1280x720\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/ltx/ltx-2-5-fast/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "ltx/ltx-2-5-fast",
                {
                    "duration": 2,
                    "fps": 24,
                    "generate_audio": False,
                    "prompt": "A single red maple leaf resting on a plain white background.",
                    "resolution": "1280x720",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, es todo lo que necesita otro proceso
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil del propio proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("ltx/ltx-2-5-fast", {
      duration: 2,
      fps: 24,
      generate_audio: false,
      prompt: "A single red maple leaf resting on a plain white background.",
      resolution: "1280x720",
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
    curl https://api.comfy.org/v2/models/ltx/ltx-2-5-fast/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 2, \"fps\": 24, \"generate_audio\": false, \"prompt\": \"A single red maple leaf resting on a plain white background.\", \"resolution\": \"1280x720\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/ltx/ltx-2-5-fast/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/ltx/ltx-2-5-fast/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

duration

integer

requerido

Duración del video en segundos (el máximo depende de la resolución y la frecuencia de cuadros)Valores posibles: `2`, `3`, `4`, `5`, `6`, `8`, `10`, `12`, `14`, `16`, `18`, `20`

​

fps

integer

predeterminado:"25"

Frecuencia de cuadros por segundoValores posibles: `24`, `25`, `48`, `50`

​

generate_audio

boolean

predeterminado:"true"

Generar audio para el video

​

model

string

Modelo que se usará para la generación. En la ruta `POST /v2/models/ltx/{model}` de Comfy Router, este campo se suministra desde la ruta y puede omitirse. Las grafías que LTX sirve en esta operación, el conjunto que Comfy Router direcciona como `ltx/<model>`, son ltx-2-5-fast y ltx-2-5-pro; se escriben aquí en lugar de restringirse a un enum por la razón que da el comentario anterior. Qué resoluciones admite cada uno es la matriz `x-comfy-model-resolutions` de la propiedad `resolution` que aparece a continuación.

​

prompt

string

requerido

Prompt de texto que describe el contenido de video deseado

​

resolution

string

requerido

Resolución del video de salida. El enum es la unión de todos los modelos; el conjunto admitido depende de cada modelo. Pares admitidos: ltx-2-5-fast: 1280x720, 720x1280, 1920x1080, 1080x1920, 2560x1440, 1440x2560, 3840x2160, 2160x3840; ltx-2-5-pro: 1280x720, 720x1280, 1920x1080, 1080x1920. Otros pares (modelo, resolución) no son compatibles; las rutas v2 los rechazan con 400. La misma matriz se publica de forma legible por máquina en la extensión x-comfy-model-resolutions de esta propiedad.Valores posibles: `1280x720`, `720x1280`, `1920x1080`, `1080x1920`, `2560x1440`, `1440x2560`, `3840x2160`, `2160x3840`

Generado a partir del esquema que Router sirve en `GET /v2/models/ltx/ltx-2-5-fast/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

completed_at

string

Marca de tiempo de finalización de la tarea (ISO 8601)

​

created_at

string

Marca de tiempo de creación de la tarea (ISO 8601)

​

error

object

Presente cuando el estado es failed

​

error.message

string

​

error.type

string

​

id

string

Identificador único de la tarea

​

result

object

Presente cuando el estado es completed; las URL de salida vencen 24 horas después de la finalización

​

result.video_url

string

URL del video generado

​

status

string

Estado de la tarea (pending, processing, completed, failed)

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "duration": 2,
      "fps": 24,
      "generate_audio": false,
      "prompt": "A single red maple leaf resting on a plain white background.",
      "resolution": "1280x720"
    }
    

### 

​

Salida
    
    
    {
      "completed_at": "2026-01-01T00:02:10Z",
      "created_at": "2026-01-01T00:00:00Z",
      "id": "3f7a1b28-5c0d-4e91-8a6f-1b2c3d4e5f60",
      "result": {
        "video_url": "https://example.invalid/ltx/generated.mp4"
      },
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/ltx/ltx-2-5-fast/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/ltx/ltx-2-5-fast/code)

[Krea 3](https://docs.comfy.org/es/development/comfy-router/models/krea/krea-3/code)[LTX 2.5 Pro](https://docs.comfy.org/es/development/comfy-router/models/ltx/ltx-2-5-pro/code)
