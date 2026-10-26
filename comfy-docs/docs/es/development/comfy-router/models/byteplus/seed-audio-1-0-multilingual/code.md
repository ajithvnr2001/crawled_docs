---
url: https://docs.comfy.org/es/development/comfy-router/models/byteplus/seed-audio-1-0-multilingual/code/
title: Usa Seed Audio 1.0 Multilingual con Comfy Router - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:03:01.103865+00:00
---

# Usa Seed Audio 1.0 Multilingual con Comfy Router - ComfyUI

> Source: https://docs.comfy.org/es/development/comfy-router/models/byteplus/seed-audio-1-0-multilingual/code/

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



BytePlus

# Usa Seed Audio 1.0 Multilingual con Comfy Router

Copiar páginaCopiar página

Llama a byteplus/seed-audio-1.0-multilingual desde Comfy Router: endpoint, forma de la solicitud y respuesta que devuelve Router.

Copiar páginaCopiar página

Referencia de API para `byteplus/seed-audio-1.0-multilingual`, servida por Comfy Router desde BytePlus. **Entrada:** Texto · **Salida:** Audio

## 

​

Inicio rápido

Crea una clave en [tu espacio de trabajo de Comfy](https://platform.comfy.org/profile/api-keys?onboarding=router) y expórtala como `COMFY_API_KEY`. Los fragmentos de Python y TypeScript usan los SDK de Comfy (`pip install comfy-sdk` y `npm install @comfyorg/sdk`); el fragmento de cURL es la misma llamada por HTTP directo. **ID del modelo:** `byteplus/seed-audio-1.0-multilingual` **Endpoint:** `POST https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual`

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
            "byteplus/seed-audio-1.0-multilingual",
            {
                "audio_config": {
                    "format": "wav",
                    "sample_rate": 24000,
                },
                "text_prompt": "Hello from Comfy Router.",
            },
        )
    
    print(result)
    
    
    
    import { comfy } from "@comfyorg/sdk";
    
    // Lee COMFY_API_KEY del entorno.
    // El SDK crea automáticamente una clave de idempotencia y la reutiliza en los reintentos automáticos.
    const { data } = await comfy.models.run("byteplus/seed-audio-1.0-multilingual", {
      audio_config: {
        format: "wav",
        sample_rate: 24000,
      },
      text_prompt: "Hello from Comfy Router.",
    });
    
    console.log(data);
    
    
    
    curl https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_config\": {\"format\":\"wav\",\"sample_rate\":24000}, \"text_prompt\": \"Hello from Comfy Router.\"}"
    

El mismo cuerpo, enviado a `POST https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual/requests`. Router responde `201` con un `request_id` en cuanto se admite la ejecución, y puedes recoger el resultado cuando esté listo, desde este proceso o desde otro. [Entrega en cola](https://docs.comfy.org/es/development/comfy-router/queue) explica el estado, la cancelación y la recogida.

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
                "byteplus/seed-audio-1.0-multilingual",
                {
                    "audio_config": {
                        "format": "wav",
                        "sample_rate": 24000,
                    },
                    "text_prompt": "Hello from Comfy Router.",
                },
            )
            print("request_id:", handle.request_id)  # con el ID del modelo, todo lo que necesita otro proceso
    
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
    // Cada llamada a submit() genera su propia Idempotency-Key y la reutiliza en los reintentos automáticos.
    const handle = await comfy.models.submit("byteplus/seed-audio-1.0-multilingual", {
      audio_config: {
        format: "wav",
        sample_rate: 24000,
      },
      text_prompt: "Hello from Comfy Router.",
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
    curl https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual/requests \
      -H "X-API-Key: $COMFY_API_KEY" \
      -H "Idempotency-Key: $(uuidgen)" \
      -H "Content-Type: application/json" \
      -d "{\"audio_config\": {\"format\":\"wav\",\"sample_rate\":24000}, \"text_prompt\": \"Hello from Comfy Router.\"}"
    
    # 2. Consulta hasta que el estado sea COMPLETED, esperando los segundos de Retry-After que indica cada respuesta.
    REQUEST_ID="<request_id from the 201 body>"
    curl -i https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual/requests/$REQUEST_ID/status \
      -H "X-API-Key: $COMFY_API_KEY"
    
    # 3. Recoge. 200 con la salida nativa del modelo, 202 con el cuerpo de estado mientras sigue en ejecución.
    curl https://api.comfy.org/v2/models/byteplus/seed-audio-1.0-multilingual/requests/$REQUEST_ID \
      -H "X-API-Key: $COMFY_API_KEY"
    

## 

​

Esquema

### 

​

Entrada

​

audio_config

object

Configuración del audio de salida.

​

audio_config.enable_subtitle

boolean

Indica si se habilita el servicio de subtítulos. Cuando se habilita, la respuesta incluye marcas de tiempo a nivel de enunciado y de palabra (predeterminado: false).

​

audio_config.format

string

Formato del audio de salida: wav (predeterminado), mp3, pcm u ogg_opus.Valores posibles: `wav`, `mp3`, `pcm`, `ogg_opus`

​

audio_config.loudness_rate

integer

De -50 a 100; 100 significa volumen de 2.0x, -50 significa volumen de 0.5x (predeterminado: 0).Rango: de `-50` a `100`

​

audio_config.pitch_rate

integer

De -12 a 12 (predeterminado: 0).Rango: de `-12` a `12`

​

audio_config.sample_rate

integer

Frecuencia de muestreo de salida: 8000, 16000, 24000 (predeterminado), 32000, 44100 o 48000.Valores posibles: `8000`, `16000`, `24000`, `32000`, `44100`, `48000`

​

audio_config.speech_rate

integer

De -50 a 100; 100 significa velocidad de 2.0x, -50 significa velocidad de 0.5x (predeterminado: 0).Rango: de `-50` a `100`

​

model

string

Identificador del modelo. Modelos compatibles: seed-audio-1.0 y seed-audio-1.0-multilingual. Una llamada directa v1 a POST /proxy/byteplus/api/v3/tts/create DEBE proporcionarlo: el proxy rechaza con un 400 cualquier otro valor, y también su omisión. NO está en la lista `required` de este esquema porque Comfy Router lo rellena desde el segmento de ruta `{model}` de /v2/models/byteplus/{model}, así que quien llama a Router lo omite.

​

references

object[]

Recursos de referencia. Omítelas para la generación solo de texto. Hasta 3 referencias de audio (cada una de hasta 30 segundos y 10 MB decodificados; wav, mp3, pcm u ogg_opus) o exactamente 1 referencia de imagen (hasta 10 MB decodificados; jpeg, png o webp). Las referencias de imagen no se pueden mezclar con las referencias de audio. Esos topes son de BytePlus y se expresan en bytes DECODIFICADOS: base64 infla un recurso aproximadamente 4/3, y una llamada a Comfy Router tiene un tope de 100 MiB para todo el documento JSON, así que una referencia `audio_data`/`image_data` en línea enviada a /v2/models/byteplus/{model} puede llevar aproximadamente 75 MB decodificados antes de que el límite del transporte la rechace. Por lo tanto, el tope propio de BytePlus de 10 MB por referencia es el que se aplica primero para cualquier referencia individual en línea, y tres referencias de audio en ese tope ahora caben en un solo cuerpo; usa `audio_url`/`image_url` para mantener los recursos grandes fuera de la solicitud por completo.

​

references[].audio_data

string

Audio de referencia codificado en Base64.

​

references[].audio_url

string

URL de un archivo de audio de referencia remoto.

​

references[].image_data

string

Imagen de referencia codificada en Base64.

​

references[].image_url

string

URL de una imagen de referencia remota.

​

references[].speaker

string

ID de voz. Puede ser una voz de Doubao TTS compatible o un ID de voz clonada.

​

text_prompt

string

requerido

Prompt o texto a sintetizar (de 1 a 3,000 caracteres; una cadena vacía se rechaza). Cuando proporciones referencias de audio, haz referencia a ellas por orden usando @Audio1, @Audio2 y @Audio3.

​

watermark

object

Objeto de configuración de la marca de agua. Se acepta un objeto vacío.

​

watermark.aigc_metadata

object

Marca de agua implícita. Agrega metadatos a la cabecera del audio sintetizado.

​

watermark.aigc_metadata.content_producer

string

Nombre o código del proveedor del servicio de síntesis.

​

watermark.aigc_metadata.content_propagator

string

Nombre o código del proveedor del servicio de distribución de contenido.

​

watermark.aigc_metadata.enable

boolean

Indica si se habilita la marca de agua implícita (predeterminado: false).

​

watermark.aigc_metadata.produce_id

string

ID de producción de contenido.

​

watermark.aigc_metadata.propagate_id

string

ID de distribución de contenido.

​

watermark.aigc_watermark

boolean

Interruptor de marca de agua explícita. Agrega un marcador de ritmo de audio al final del audio sintetizado (predeterminado: false).

Generado a partir del esquema que Router sirve en `GET /v2/models/byteplus/seed-audio-1.0-multilingual/openapi.json`, el mismo documento contra el que valida una llamada antes de que la solicitud llegue al proveedor.

### 

​

Salida

​

audio

string

Datos de audio generados, codificados en Base64.

​

code

integer

Código de estado. Consulta el documento oficial de códigos de error para obtener más detalles.

​

duration

number

Duración después de aplicar la velocidad o el posprocesamiento, en segundos.Formato: `double`

​

message

string

Detalles del estado.

​

original_duration

number

Duración original de la salida del modelo, en segundos. Se usa para el cobro y se limita a 120 segundos.Formato: `double`

​

subtitle

object

Información de subtítulos del audio. Solo está presente cuando audio_config.enable_subtitle se establece en true en la solicitud.

​

subtitle.sentences

object[]

Información de subtítulos por enunciado.

​

subtitle.sentences[].end_time

integer

Hora de fin del segmento, en milisegundos desde el inicio del audio.

​

subtitle.sentences[].start_time

integer

Hora de inicio del segmento, en milisegundos desde el inicio del audio.

​

subtitle.sentences[].text

string

El texto completo del segmento.

​

subtitle.text

string

Texto de los subtítulos correspondiente al audio.

​

subtitle.words

object[]

Información de subtítulos por palabra.

​

subtitle.words[].end_time

integer

Hora de fin del segmento, en milisegundos desde el inicio del audio.

​

subtitle.words[].start_time

integer

Hora de inicio del segmento, en milisegundos desde el inicio del audio.

​

subtitle.words[].text

string

El texto completo del segmento.

​

url

string

URL temporal del audio, válida durante 2 horas.

## 

​

Ejemplos

### 

​

Entrada
    
    
    {
      "audio_config": {
        "format": "wav",
        "sample_rate": 24000
      },
      "text_prompt": "Hello from Comfy Router."
    }
    

### 

​

Salida
    
    
    {
      "audio": "PGJhc2U2ND4=",
      "duration": 1.2,
      "original_duration": 1.2,
      "url": "https://example.invalid/byteplus/seed-audio/generated.wav"
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

[Sugerir cambios](https://github.com/comfy-org/docs/edit/main/es/development/comfy-router/models/byteplus/seed-audio-1-0-multilingual/code.mdx)[Reportar problema](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/es/development/comfy-router/models/byteplus/seed-audio-1-0-multilingual/code)

[Seed 2.0 Pro 260328](https://docs.comfy.org/es/development/comfy-router/models/byteplus/seed-2-0-pro-260328/code)[Seed Audio 1.0](https://docs.comfy.org/es/development/comfy-router/models/byteplus/seed-audio-1-0/code)
