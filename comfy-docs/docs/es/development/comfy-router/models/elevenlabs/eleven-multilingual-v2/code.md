---
url: https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code/
title: Usa Eleven Multilingual V2 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:02.572807+00:00
---

# Usa Eleven Multilingual V2 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code/

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



Elevenlabs

# Usa Eleven Multilingual V2 con Comfy Router

Copiar páginaCopiar página

Llama a elevenlabs/eleven_multilingual_v2 mediante Comfy Router: endpoint, forma de la solicitud y la respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de la API para `elevenlabs/eleven_multilingual_v2`, servida por Comfy Router desde Elevenlabs. **Entrada:** Texto · **Salida:** Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada sobre HTTP sin procesar. **ID del modelo:** `elevenlabs/eleven_multilingual_v2` **Endpoint:** `POST https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2`

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
            "elevenlabs/eleven_multilingual_v2",
            {
                "text": "Hello from Comfy Router.",
                "voice_id": "21m00Tcm4TlvDq8ikWAM",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("elevenlabs/eleven_multilingual_v2", {
      text: "Hello from Comfy Router.",
      voice_id: "21m00Tcm4TlvDq8ikWAM",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text\": \"Hello from Comfy Router.\", \"voice_id\": \"21m00Tcm4TlvDq8ikWAM\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida del resultado.

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
                "elevenlabs/eleven_multilingual_v2",
                {
                    "text": "Hello from Comfy Router.",
                    "voice_id": "21m00Tcm4TlvDq8ikWAM",
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
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("elevenlabs/eleven_multilingual_v2", {
      text: "Hello from Comfy Router.",
      voice_id: "21m00Tcm4TlvDq8ikWAM",
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
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"text\": \"Hello from Comfy Router.\", \"voice_id\": \"21m00Tcm4TlvDq8ikWAM\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_multilingual_v2/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

apply_language_text_normalization

boolean

predeterminado:"false"

Controla la normalización de texto específica del idioma. Puede aumentar considerablemente la latencia. Actualmente solo es compatible con japonés.

​

apply_text_normalization

string

predeterminado:"\"auto\""

Controla la normalización de texto. ‘auto’ deja que el sistema decida, ‘on’ siempre aplica la normalización, ‘off’ omite la normalización.Valores posibles: `auto`, `on`, `off`

​

language_code

string

Código de idioma (ISO 639-1) que se debe aplicar al modelo. Si no es compatible, se devuelve un error.

​

model_id

string

predeterminado:"\"eleven_multilingual_v2\""

Identificador del modelo que se va a usar. Consulta /v1/models para ver la lista de modelos disponibles.

​

next_request_ids

string[]

IDs de solicitud de las generaciones siguientes para mantener la continuidad. Máximo 3.

​

next_text

string

Texto que viene después de esta solicitud, usado para mejorar la continuidad del habla.

​

previous_request_ids

string[]

IDs de solicitud de las generaciones anteriores para mantener la continuidad. Máximo 3.

​

previous_text

string

Texto que venía antes de esta solicitud, usado para mejorar la continuidad del habla.

​

pronunciation_dictionary_locators

object[]

Lista de localizadores de diccionarios de pronunciación (id, version_id). Máximo 3 por solicitud.

​

pronunciation_dictionary_locators[].pronunciation_dictionary_id

string

requerido

El ID del diccionario de pronunciación

​

pronunciation_dictionary_locators[].version_id

string

requerido

El ID de versión del diccionario de pronunciación

​

seed

integer

Semilla para una generación determinista. Debe estar entre 0 y 4294967295.Rango: `0` a `4294967295`

​

text

string

requerido

El texto que se convertirá en voz.

​

use_pvc_as_ivc

boolean

predeterminado:"false"

Obsoleto. Si es verdadero, usa la versión IVC de la voz en lugar de PVC.

​

voice_settings

object

Configuraciones de voz

​

voice_settings.similarity_boost

number

predeterminado:"0.75"

Qué tan fielmente se adhiere la IA a la voz original al replicarla.Rango: `0` a `1`Formato: `double`

​

voice_settings.speed

number

predeterminado:"1"

Ajuste de velocidad. 1.0 es el valor predeterminado, los valores por debajo reducen la velocidad y los valores por encima la aumentan.Rango: `0.7` a `1.2`Formato: `double`

​

voice_settings.stability

number

predeterminado:"0.5"

Estabilidad de la voz. Los valores más bajos introducen un rango emocional más amplio.Rango: `0` a `1`Formato: `double`

​

voice_settings.style

number

predeterminado:"0"

Exageración del estilo. Amplifica el estilo del hablante original.Rango: `0` a `1`Formato: `double`

​

voice_settings.use_speaker_boost

boolean

predeterminado:"true"

Aumenta la similitud con el hablante original. Requiere una mayor carga computacional.

​

voice_id

string

requerido

ID de la voz que se va a usar, solo letras y dígitos. Router lo coloca en la ruta de la solicitud a ElevenLabs.

Generado a partir del esquema que Router publica en `GET /v2/models/elevenlabs/eleven_multilingual_v2/openapi.json`, el mismo documento con el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

*/*

string (binary)

Bytes de audio sin procesar. El Content-Type y la codificación siguen el output_format solicitado y se reenvían desde ElevenLabs. El ejemplo es un marcador de posición para el cuerpo binario, no JSON ni base64.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "text": "Hello from Comfy Router.",
      "voice_id": "21m00Tcm4TlvDq8ikWAM"
    }
    

### 

​

Salida

Cuerpo binario: bytes sin procesar en lugar de un documento JSON, devueltos como `*/*`, así que no hay un ejemplo JSON que mostrar. El `Content-Type` y la codificación de la respuesta dependen de la solicitud, como describe el esquema de Salida anterior.

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/elevenlabs/eleven-multilingual-v2/code)

[Seedream 5.0 Pro 260628](https://docs.comfy.org/es/development/comfy-router/models/byteplus/seedream-5-0-pro-260628/code)[Eleven Sfx V2](https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-sfx-v2/code)
