---
url: https://docs.comfy.org/es/development/comfy-router/models/heygen/starfish/code/
title: Usa Starfish con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:05.594271+00:00
---

# Usa Starfish con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/heygen/starfish/code/

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



HeyGen

# Usa Starfish con Comfy Router

Copiar páginaCopiar página

Llama a heygen/starfish desde Comfy Router: endpoint, cuerpo de la solicitud y respuesta devuelta.

Copiar páginaCopiar página

Referencia de API de `heygen/starfish`, que Comfy Router sirve desde HeyGen. **Entrada:** Texto · **Salida:** Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `heygen/starfish` **Endpoint:** `POST https://api.comfy.org/v2/models/heygen/starfish`

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
            "heygen/starfish",
            {
                "text": "Hello from Comfy. This voice is generated with the HeyGen Starfish engine.",
                "voice_id": "d2f4f24783d04e22ab49ee8fdc3715e0",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("heygen/starfish", {
      text: "Hello from Comfy. This voice is generated with the HeyGen Starfish engine.",
      voice_id: "d2f4f24783d04e22ab49ee8fdc3715e0",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/heygen/starfish \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text\": \"Hello from Comfy. This voice is generated with the HeyGen Starfish engine.\", \"voice_id\": \"d2f4f24783d04e22ab49ee8fdc3715e0\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/heygen/starfish/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge una vez que está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) recorre el estado, la cancelación y la recogida.

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
                "heygen/starfish",
                {
                    "text": "Hello from Comfy. This voice is generated with the HeyGen Starfish engine.",
                    "voice_id": "d2f4f24783d04e22ab49ee8fdc3715e0",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que otro proceso necesita
    
            # Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
            async for update in handle.iter_events():
                print(update.status, update.queue_position)
    
            # La carga útil del propio proveedor, el mismo valor que devuelve models.run().
            # Una solicitud que falló o se canceló lanza aquí el error tipado de Router.
            result = await handle.get()
    
        print(result)
    
    asyncio.run(main())
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza para los reintentos automáticos.
    const handle = await comfy.models.submit("heygen/starfish", {
      text: "Hello from Comfy. This voice is generated with the HeyGen Starfish engine.",
      voice_id: "d2f4f24783d04e22ab49ee8fdc3715e0",
    });
    console.log("requestId:", handle.requestId); // con el ID del modelo, todo lo que otro proceso necesita
    
    // Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló provoca aquí un rechazo.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/heygen/starfish/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text\": \"Hello from Comfy. This voice is generated with the HeyGen Starfish engine.\", \"voice_id\": \"d2f4f24783d04e22ab49ee8fdc3715e0\"}"
    
    # 2. Sondea hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/heygen/starfish/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/heygen/starfish/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

input_type

string

Tipo de entrada: ‘text’ para texto sin formato, ‘ssml’ para marcado SSML. El valor predeterminado es ‘text’

​

language

string

Código de idioma base (por ejemplo, ‘en’). Se detecta automáticamente a partir del texto cuando se omite

​

locale

string

Etiqueta de localización BCP-47 (por ejemplo, ‘en-US’). Cuando se define, el idioma se infiere de la localización

​

speed

number

Multiplicador de velocidad (0.5-2.0)Rango: `0.5` a `2`Formato: `double`

​

text

string

requerido

Texto que se va a sintetizar (1-5000 caracteres)

​

voice_id

string

requerido

ID de la voz que se va a usar. La voz debe tener soporte para el motor starfish

Generado a partir del esquema que Router publica en `GET /v2/models/heygen/starfish/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

data

object

requerido

Payload de una respuesta correcta de texto a voz de HeyGen

​

data.audio_url

string

requerido

URL del archivo de audio generado

​

data.duration

number

Duración del audio en segundosFormato: `double`

​

data.request_id

string

Identificador único de esta solicitud de generación

​

data.word_timestamps

object[]

Datos de tiempo a nivel de palabra

​

data.word_timestamps[].end

number

Hora de finalización en segundosFormato: `double`

​

data.word_timestamps[].start

number

Hora de inicio en segundosFormato: `double`

​

data.word_timestamps[].word

string

La palabra

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "text": "Hello from Comfy. This voice is generated with the HeyGen Starfish engine.",
      "voice_id": "d2f4f24783d04e22ab49ee8fdc3715e0"
    }
    

### 

​

Salida
    
    
    {
      "data": {
        "audio_url": "https://example.invalid/heygen/starfish/speech.mp3",
        "duration": 12.5,
        "request_id": "018f2c7a-4b1e-7c3d-9a05-6e2f8b41d0c9"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/heygen/starfish/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/heygen/starfish/code)

[Nano Banana Pro](https://docs.comfy.org/es/development/comfy-router/models/google/nano-banana-pro/code)[Higgsfield Genjutsu Motion Transfer V1.0](https://docs.comfy.org/es/development/comfy-router/models/higgsfield/higgsfield-genjutsu-motion-transfer-v1-0/code)
