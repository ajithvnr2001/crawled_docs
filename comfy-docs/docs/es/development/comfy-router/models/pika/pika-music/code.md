---
url: https://docs.comfy.org/es/development/comfy-router/models/pika/pika-music/code/
title: Usar Pika Music con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:41.025078+00:00
---

# Usar Pika Music con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/pika/pika-music/code/

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



Pika

# Usar Pika Music con Comfy Router

Copiar páginaCopiar página

Llama a pika/pika-music con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve el Router.

Copiar páginaCopiar página

Referencia de API de `pika/pika-music`, servida por Comfy Router desde Pika. **Entrada:** Texto, Audio · **Salida:** Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `pika/pika-music` **Endpoint:** `POST https://api.comfy.org/v2/models/pika/pika-music`

  * Esperar el resultado

  * Encolar y recopilar más tarde




Python

TypeScript

cURL
    
    
    from comfy_sdk import Comfy
    
    # Lee COMFY_API_KEY del entorno.
    # El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    with Comfy() as client:
        result = client.models.run(
            "pika/pika-music",
            {
                "duration": 30,
                "mode": "text_to_music",
                "prompt": "warm lo-fi hip hop with soft piano and vinyl crackle",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("pika/pika-music", {
      duration: 30,
      mode: "text_to_music",
      prompt: "warm lo-fi hip hop with soft piano and vinyl crackle",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/pika/pika-music \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 30, \"mode\": \"text_to_music\", \"prompt\": \"warm lo-fi hip hop with soft piano and vinyl crackle\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/pika/pika-music/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recopila cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recopilación.

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
                "pika/pika-music",
                {
                    "duration": 30,
                    "mode": "text_to_music",
                    "prompt": "warm lo-fi hip hop with soft piano and vinyl crackle",
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que otro proceso necesita
    
            # Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga propia del proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló genera aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("pika/pika-music", {
      duration: 30,
      mode: "text_to_music",
      prompt: "warm lo-fi hip hop with soft piano and vinyl crackle",
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que otro proceso necesita
    
    // Consulta hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/pika/pika-music/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"duration\": 30, \"mode\": \"text_to_music\", \"prompt\": \"warm lo-fi hip hop with soft piano and vinyl crackle\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/pika/pika-music/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recopila. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/pika/pika-music/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

clean_reference_audio

boolean

predeterminado:"false"

Limpia el audio de referencia antes de usarlo.

​

duration

number

predeterminado:"30"

Duración de la música en segundos, de 10 a 360.Rango: `10` a `360`

​

lyrics

string

Letra para cantar.

​

mode

string

predeterminado:"\"text_to_music\""

Modo de generación: text_to_music, voice_conditioned_text_to_music o music_cover.Valores posibles: `text_to_music`, `voice_conditioned_text_to_music`, `music_cover`

​

prompt

string

requerido

Descripción de la música.

​

reference_audio

string

URL de una referencia de voz. Requiere que `voice_consent_attested` esté establecido en true.

​

rewrite_prompt

boolean

predeterminado:"false"

Expande un prompt corto con un modelo antes de la generación.

​

seed

integer

predeterminado:"-1"

Semilla para una salida reproducible, de -1 a 2147483647. -1 elige una semilla aleatoria.Rango: `-1` a `2147483647`

​

source_audio

string

URL de la canción fuente para `music_cover`.

​

voice_consent_attested

boolean

predeterminado:"false"

Confirma que quien llama tiene los derechos para clonar la voz en `reference_audio`.

Generado a partir del esquema que Router sirve en `GET /v2/models/pika/pika-music/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

error

object

Se establece en una tarea `failed`.

​

error.code

string

Código de fallo legible por máquina, como invalid_input, content_moderation o provider_error.

​

error.message

string

Texto de diagnóstico.

​

id

string

ID de trabajo usado para consultar el estado.

​

model_id

string

La entrada del catálogo de Pika que ejecutó la tarea.

​

output

object

Los archivos multimedia de la tarea finalizada, establecidos cuando `status` es `completed`.

​

output.audio

object

Un archivo multimedia generado.

​

output.audio.content_type

string

Tipo MIME del archivo.

​

output.audio.url

string

URL de descarga del archivo generado.

​

output.media_type

string

Qué campo contiene el archivo: video o audio.

​

output.video

object

Un archivo multimedia generado.

​

output.video.content_type

string

Tipo MIME del archivo.

​

output.video.url

string

URL de descarga del archivo generado.

​

status

string

Estado de la tarea: queued, running, completed o failed.

​

usage

object

Unidades que Pika reportó para la tarea.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "duration": 30,
      "mode": "text_to_music",
      "prompt": "warm lo-fi hip hop with soft piano and vinyl crackle"
    }
    

### 

​

Salida
    
    
    {
      "id": "media_2d8e4b71-9c05-4f3a-b6d2-81e7a5c09f44",
      "output": {
        "audio": {
          "content_type": "audio/mpeg",
          "url": "https://example.invalid/pika/audio.mp3"
        },
        "media_type": "audio"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/pika/pika-music/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/pika/pika-music/code)

[Pika 2.5 Text To Video](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-2-5-text-to-video/code)[Pika Sfx](https://docs.comfy.org/es/development/comfy-router/models/pika/pika-sfx/code)
