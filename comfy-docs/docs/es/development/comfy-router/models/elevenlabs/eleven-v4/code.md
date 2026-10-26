---
url: https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-v4/code/
title: Usa Eleven V4 con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:03.428054+00:00
---

# Usa Eleven V4 con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-v4/code/

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

# Usa Eleven V4 con Comfy Router

Copiar páginaCopiar página

Llama a elevenlabs/eleven_v4 con Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `elevenlabs/eleven_v4`, servida por Comfy Router de Elevenlabs. **Entrada:** Texto · **Salida:** Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada mediante HTTP sin procesar. **ID del modelo:** `elevenlabs/eleven_v4` **Endpoint:** `POST https://api.comfy.org/v2/models/elevenlabs/eleven_v4`

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
            "elevenlabs/eleven_v4",
            {
                "inputs": [
                    {
                        "text": "Hello from Comfy Router.",
                        "voice_id": "21m00Tcm4TlvDq8ikWAM",
                    },
                ],
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza para los reintentos automáticos.
    const { data } = await comfy.models.run("elevenlabs/eleven_v4", {
      inputs: [
        {
          text: "Hello from Comfy Router.",
          voice_id: "21m00Tcm4TlvDq8ikWAM",
        },
      ],
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_v4 \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"inputs\": [{\"text\":\"Hello from Comfy Router.\",\"voice_id\":\"21m00Tcm4TlvDq8ikWAM\"}]}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/elevenlabs/eleven_v4/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y el resultado se recoge cuando está listo, desde este proceso u otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "elevenlabs/eleven_v4",
                {
                    "inputs": [
                        {
                            "text": "Hello from Comfy Router.",
                            "voice_id": "21m00Tcm4TlvDq8ikWAM",
                        },
                    ],
                },
            )
            print("request_id:", handle.request_id)  # junto con el ID del modelo, es todo lo que necesita otro proceso
    
            # Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
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
    const handle = await comfy.models.submit("elevenlabs/eleven_v4", {
      inputs: [
        {
          text: "Hello from Comfy Router.",
          voice_id: "21m00Tcm4TlvDq8ikWAM",
        },
      ],
    });
    console.log("requestId:", handle.requestId); // junto con el ID del modelo, es todo lo que necesita otro proceso
    
    // Sondea hasta que la solicitud se complete, esperando el Retry-After que indica el servidor.
    for await (const update of handle.events()) {
      console.log(update.status, update.queuePosition);
    }
    
    // El mismo resultado que devuelve models.run(). Una solicitud que falló o se canceló se rechaza aquí.
    const result = await handle.get();
    
    console.log(result.data);
    
    
    
    # 1. Envía. Router responde 201 con request_id, status_url, response_url y cancel_url.
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_v4/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"inputs\": [{\"text\":\"Hello from Comfy Router.\",\"voice_id\":\"21m00Tcm4TlvDq8ikWAM\"}]}"
    
    # 2. Sondea hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/elevenlabs/eleven_v4/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo del estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/elevenlabs/eleven_v4/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

apply_text_normalization

string

predeterminado:"\"auto\""

Controla la normalización de texto con tres modos: ‘auto’: el sistema decide automáticamente si aplicar la normalización de texto ‘on’: la normalización de texto siempre se aplicará ‘off’: se omitirá la normalización de textoValores posibles: `auto`, `on`, `off`

​

inputs

object[]

requerido

Una lista de entradas de diálogo, cada una con texto y un ID de voz que se convertirá en habla. El número máximo de IDs de voz únicos es 10.

​

inputs[].text

string

requerido

El texto que se convertirá en habla.

​

inputs[].voice_id

string

requerido

El ID de la voz que se usará para la generación.

​

language_code

string

Código de idioma (ISO 639-1) usado para imponer un idioma al modelo y a la normalización de texto. Si el modelo no admite el código de idioma proporcionado, se devolverá un error.

​

model_id

string

Identificador del modelo que se usará. Esta ruta admite ‘eleven_v3’, ‘eleven_v4’ y ‘eleven_v4_turbo’ y nada más; cualquier otro valor se rechaza con 400 antes de que la solicitud llegue a ElevenLabs. La recomendación upstream de ElevenLabs de consultar GET /v1/models para conocer el conjunto disponible NO describe esta ruta, que solo sirve estos modelos. NO está en la lista `required` de este esquema porque Comfy Router lo rellena desde el segmento de ruta `{model}` de /v2/models/elevenlabs/{model}, así que quien llama al Router lo omite.

​

pronunciation_dictionary_locators

object[]

Una lista de localizadores del diccionario de pronunciación (id, version_id) que se aplicarán al texto. Se aplicarán en orden. Puedes tener hasta 3 localizadores por solicitud.

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

Si se especifica, nuestro sistema hará su mejor esfuerzo para muestrear de forma determinista. Las solicitudes repetidas con la misma semilla y los mismos parámetros deberían devolver el mismo resultado. Debe ser un número entero entre 0 y 4294967295.Rango: `0` a `4294967295`

​

settings

object

Configuraciones que controlan la generación del diálogo

​

settings.stability

number

predeterminado:"0.5"

Determina qué tan estable es la voz y la aleatoriedad entre cada generación. Los valores más bajos introducen un rango emocional más amplio para la voz. Los valores más altos pueden dar como resultado una voz monótona con emoción limitada.Formato: `double`

Generado a partir del esquema que sirve Router en `GET /v2/models/elevenlabs/eleven_v4/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

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
      "inputs": [
        {
          "text": "Hello from Comfy Router.",
          "voice_id": "21m00Tcm4TlvDq8ikWAM"
        }
      ]
    }
    

### 

​

Salida

Cuerpo binario: bytes sin procesar en lugar de un documento JSON, devueltos como `*/*`, por lo que no hay un ejemplo JSON que mostrar. El `Content-Type` y la codificación de la respuesta siguen a la solicitud, tal como describe el esquema de Salida anterior.

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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/elevenlabs/eleven-v4/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/elevenlabs/eleven-v4/code)

[Eleven V4 Turbo](https://docs.comfy.org/es/development/comfy-router/models/elevenlabs/eleven-v4-turbo/code)[Crystal Upscaler](https://docs.comfy.org/es/development/comfy-router/models/fal/crystal-upscaler/code)
