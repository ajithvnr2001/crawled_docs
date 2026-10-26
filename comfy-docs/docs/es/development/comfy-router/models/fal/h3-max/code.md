---
url: https://docs.comfy.org/es/development/comfy-router/models/fal/h3-max/code/
title: Usa H3 Max con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:03.793893+00:00
---

# Usa H3 Max con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/fal/h3-max/code/

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



fal

# Usa H3 Max con Comfy Router

Copiar páginaCopiar página

Llama a fal/h3-max mediante Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `fal/h3-max`, servida por Comfy Router desde fal. **Entrada:** Texto, Imagen, Video, Audio · **Salida:** Video + Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP sin procesar. **ID del modelo:** `fal/h3-max` **Endpoint:** `POST https://api.comfy.org/v2/models/fal/h3-max`

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
            "fal/h3-max",
            {
                "duration": 5,
                "prompt": "a red fox running through a snowy forest",
                "prompt_expansion_mode": "balanced",
                "resolution": "480P",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("fal/h3-max", {
      duration: 5,
      prompt: "a red fox running through a snowy forest",
      prompt_expansion_mode: "balanced",
      resolution: "480P",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/fal/h3-max \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"a red fox running through a snowy forest\", \"prompt_expansion_mode\": \"balanced\", \"resolution\": \"480P\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/fal/h3-max/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "fal/h3-max",
                {
                    "duration": 5,
                    "prompt": "a red fox running through a snowy forest",
                    "prompt_expansion_mode": "balanced",
                    "resolution": "480P",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
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
    const handle = await comfy.models.submit("fal/h3-max", {
      duration: 5,
      prompt: "a red fox running through a snowy forest",
      prompt_expansion_mode: "balanced",
      resolution: "480P",
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
    curl https://api.comfy.org/v2/models/fal/h3-max/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"a red fox running through a snowy forest\", \"prompt_expansion_mode\": \"balanced\", \"resolution\": \"480P\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/fal/h3-max/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/fal/h3-max/requests/$REQUEST_ID \
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

Relación de aspecto: 21:9, 16:9, 4:3, 1:1, 3:4 o 9:16.

​

duration

integer

predeterminado:"5"

Duración del video generado en segundos.

​

enable_safety_checker

boolean

predeterminado:"true"

Habilita el verificador de seguridad.

​

prompt

string

requerido

Prompt de texto para la generación del video.

​

prompt_expansion_mode

string

requerido

Cuánto esfuerzo dedicar a reescribir el prompt antes de la generación: balanced o quality.

​

resolution

string

predeterminado:"\"768P\""

Resolución del video generado: 480P o 768P.

​

seed

integer

Semilla aleatoria. Si se omite, se selecciona una semilla aleatoria.

​

sync_mode

boolean

Devuelve el video generado como base64 en lugar de una URL de CDN.

Generado a partir del esquema que Router sirve en `GET /v2/models/fal/h3-max/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

expanded_prompt

string

El prompt después de la expansión, tal como se envió al modelo.

​

timings

object

Desglose de los tiempos de extremo a extremo (segundos).

​

video

object

requerido

El archivo de video generado.

​

video.content_type

string

Tipo MIME del archivo de video.

​

video.file_name

string

Nombre del archivo de video.

​

video.file_size

integer

Tamaño del archivo de video en bytes.

​

video.url

string

URL del video generado.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "duration": 5,
      "prompt": "a red fox running through a snowy forest",
      "prompt_expansion_mode": "balanced",
      "resolution": "480P"
    }
    

### 

​

Salida
    
    
    {
      "expanded_prompt": "a single red maple leaf falling onto still water, cinematic, 4k",
      "timings": {
        "inference": 42.5
      },
      "video": {
        "content_type": "video/mp4",
        "file_name": "output.mp4",
        "file_size": 4194304,
        "url": "https://example.invalid/fal/minimax/h3-max/output.mp4"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/fal/h3-max/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/fal/h3-max/code)

[H3 Max Turbo](https://docs.comfy.org/es/development/comfy-router/models/fal/h3-max-turbo/code)[Patina](https://docs.comfy.org/es/development/comfy-router/models/fal/patina/code)
