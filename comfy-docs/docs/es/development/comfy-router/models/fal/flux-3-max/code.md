---
url: https://docs.comfy.org/es/development/comfy-router/models/fal/flux-3-max/code/
title: Usa FLUX 3 Max con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:03.691027+00:00
---

# Usa FLUX 3 Max con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/fal/flux-3-max/code/

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

# Usa FLUX 3 Max con Comfy Router

Copiar páginaCopiar página

Llama a fal/flux-3-max mediante Comfy Router: endpoint, forma de la petición y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `fal/flux-3-max`, servida por Comfy Router desde fal. **Entrada:** Texto, Imagen · **Salida:** Video + Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `fal/flux-3-max` **Endpoint:** `POST https://api.comfy.org/v2/models/fal/flux-3-max`

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
            "fal/flux-3-max",
            {
                "duration": 5,
                "prompt": "A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.",
                "resolution": "720p",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("fal/flux-3-max", {
      duration: 5,
      prompt: "A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.",
      resolution: "720p",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/fal/flux-3-max \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.\", \"resolution\": \"720p\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/fal/flux-3-max/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "fal/flux-3-max",
                {
                    "duration": 5,
                    "prompt": "A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.",
                    "resolution": "720p",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que otro proceso necesita
    
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
    const handle = await comfy.models.submit("fal/flux-3-max", {
      duration: 5,
      prompt: "A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.",
      resolution: "720p",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/fal/flux-3-max/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 5, \"prompt\": \"A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.\", \"resolution\": \"720p\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/fal/flux-3-max/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras todavía se ejecuta.
    curl https://api.comfy.org/v2/models/fal/flux-3-max/requests/$REQUEST_ID \
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

predeterminado:"\"auto\""

Relación de aspecto del video generado. El valor auto es 16:9 para un prompt de texto y, en caso contrario, sigue la primera imagen.Valores posibles: `auto`, `21:9`, `2:1`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`

​

duration

integer

predeterminado:"5"

Duración del video generado en segundos, de 5 a 20. fal factura por segundo de este valor.Rango: `5` a `20`

​

generate_audio

boolean

predeterminado:"true"

Genera audio sincronizado. El precio no cambia.

​

prompt

string

requerido

Prompt de texto que describe el video y su sonido.

​

reasoning_level

string

predeterminado:"\"high\""

Cuánto razona y expande el modelo el prompt antes de la generación. El valor high es más lento. El precio no cambia.Valores posibles: `low`, `high`

​

resolution

string

predeterminado:"\"720p\""

Resolución del video generado. 1080p cuesta más por segundo que 720p.Valores posibles: `720p`, `1080p`

​

seed

integer

Semilla aleatoria. Si se omite, se elige una semilla al azar.

Generado a partir del esquema que Router expone en `GET /v2/models/fal/flux-3-max/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

seed

integer

La semilla utilizada para la generación.

​

timings

object

Desglose de tiempos en segundos.

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

video.duration

number

Duración del video en segundos.

​

video.file_name

string

Nombre del archivo de video.

​

video.file_size

integer

Tamaño del archivo de video en bytes.

​

video.fps

number

Frecuencia de cuadros del video.

​

video.height

integer

Alto del video en píxeles.

​

video.num_frames

integer

Número de fotogramas del video.

​

video.url

string

requerido

URL del video generado.

​

video.width

integer

Ancho del video en píxeles.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "duration": 5,
      "prompt": "A red panda walks along a mossy log in a sunlit forest. Ambient birdsong.",
      "resolution": "720p"
    }
    

### 

​

Salida
    
    
    {
      "seed": 42,
      "video": {
        "content_type": "video/mp4",
        "duration": 5.041666666666667,
        "file_name": "video.mp4",
        "file_size": 4404019,
        "fps": 24,
        "height": 704,
        "num_frames": 121,
        "url": "https://example.invalid/fal/flux-3-max/video.mp4",
        "width": 1280
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/fal/flux-3-max/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/fal/flux-3-max/code)

[Crystal Video Upscaler](https://docs.comfy.org/es/development/comfy-router/models/fal/crystal-video-upscaler/code)[H3 Max Turbo](https://docs.comfy.org/es/development/comfy-router/models/fal/h3-max-turbo/code)
